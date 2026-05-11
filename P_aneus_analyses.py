MULTIVARIATE MORPHOMETRIC ANALYSES OF Pennahia aneus (Acanthuriformes: Scieanidae)

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
# from cartopy.mpl.ticker import (LongitudeFormatter, LatitudeFormatter,
# LatitudeLocator, LongitudeLocator)
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.colors as mcolors
from matplotlib import rc
import matplotlib
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = r'\boldmath'
# matplotlib.rcParams['axes.linewidth'] = 4.0
plt.rcParams.update({'axes.linewidth': 4}) # Adjust thickness as needed
matplotlib.rcParams['xtick.major.size'] = 4
matplotlib.rcParams['xtick.major.width'] = 0.5
matplotlib.rcParams['xtick.minor.size'] = 4
matplotlib.rcParams['xtick.minor.width'] = 0.5
matplotlib.rcParams['ytick.major.size'] = 4
matplotlib.rcParams['ytick.major.width'] = 0.5
matplotlib.rcParams['ytick.minor.size'] = 4
matplotlib.rcParams['ytick.minor.width'] = 0.5
plt.style.use('classic')
plt.rcParams.update()
from google.colab import files
uploaded = files.upload()
# Replace with your actual CSV file
df =
pd.read_excel('Transformed_P_anea_Morphometrics_Peninsular_Malaysia_Borneo.xlsx',
engine='openpyxl')
# df.head()
# select columns having _adj
df.columns
# select only these columns'Region Name', 'Marine Region ID','TL_adj', 'SnL_adj',
'HL_adj', 'ED_adj', 'BD_adj', 'CPD_adj', 'DD_adj', 'Dpec_adj', 'Dpel_adj',
'DA_adj']
selected_columns = ['Region Name', 'Marine Region ID','TL_adj', 'SnL_adj',
'HL_adj', 'ED_adj', 'BD_adj', 'CPD_adj', 'DD_adj', 'Dpec_adj', 'Dpel_adj','DA_adj']
df_selected = df[selected_columns]
df_selected.head()
dfad = df_selected.copy()
X=dfad[['TL_adj', 'SnL_adj', 'HL_adj', 'ED_adj', 'BD_adj', 'CPD_adj', 'DD_adj',
'Dpec_adj', 'Dpel_adj', 'DA_adj']]
y=dfad['Region Name']

# X=df.drop(columns=['Collector', 'Sample ID', 'Species', 'Location',
'Geographical Region',
# 'Marine Region', 'Region Code'])
# y = df['Marine Region']

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Ensure necessary libraries are installed
# !pip install scikit-learn matplotlib seaborn
# !pip install factor_analyzer
# Import additional libraries

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 1. PRINCIPAL COMPONENT ANALYSIS (PCA)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)
# Create DataFrame for plotting
pca_df = pd.DataFrame({
'PC1': X_pca[:, 0],
'PC2': X_pca[:, 1],
'Marine Region': y
})
color_palette = [
"#E69F00", # orange
"#56B4E9", # sky blue
"grey", # bluish green
"#D55E00" # vermilion
]
unique_labels = pca_df['Marine Region'].unique()
palette = color_palette
color_map = dict(zip(unique_labels, palette))

# Plot
fig, ax = plt.subplots(1, 1, figsize=(8, 5), facecolor='white', dpi=300)
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Marine Region',
palette=color_map, ax=ax)
ax.axvline(x=0, color='black', linestyle='--')
ax.axhline(y=0, color='black', linestyle='--')

# ax.set_title('PCA of Morphometric Data')
ax.set_xlabel(f'PC 1 ({pca.explained_variance_ratio_[0]*100:.2f}%)')
ax.set_ylabel(f'PC 2 ({pca.explained_variance_ratio_[1]*100:.2f}%)')
ax.minorticks_on()
ax.tick_params(which='major', direction='out', length=6, width=1,labelsize=18)#,
grid_alpha=0.5)
ax.tick_params(which='minor', direction='out', length=3, width=1)
ax.tick_params(which='both',top=False, right=False)

# Fix legend
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), title='Marine Region',fontsize = 10)
plt.tight_layout()

# plt.savefig(save_topath + 'PCA_of_Morphometric_Adj_Data_adj.png',
dpi=600,pad_inches=0.2,)
plt.show()

# Plot individual and cumulative explained variance
fig, axp = plt.subplots(figsize=(6, 4), facecolor='white', dpi=300)

# Bar plot: Individual explained variance
axp.bar(
range(1, pca.n_components_ + 1),
pca.explained_variance_ratio_,
alpha=0.6,
color="#56B4E9",
label='Individual Explained Variance'
)

# Line plot: Cumulative explained variance
axp.plot(
range(1, pca.n_components_ + 1),
np.cumsum(pca.explained_variance_ratio_),
color="#D55E00",
marker='o',
label='Cumulative Explained Variance'
)
# Labels and title
axp.set_xlabel('Number of Components')
axp.set_ylabel('Explained Variance Ratio')
# axp.set_title('Explained Variance by PCA Components')
axp.set_xticks(np.arange(1, pca.n_components_+1,2 ))
axp.set_ylim(0, 1.1)
# Enable minor ticks
axp.minorticks_on()
# Hide all x-axis ticks
axp.tick_params(axis='x', which='minor',direction='out',bottom=False, top=False,
labelbottom=True)
axp.tick_params(axis='x', which='both',direction='out', top=False, width=1)
# Hide y-axis major ticks, show only minor ticks
axp.tick_params(axis='y', which='major', length=6,width=1,
direction='out',right=False)
axp.tick_params(axis='y', which='minor', direction='out', length=3,
width=0.5,right=False)
# Add legend
axp.legend(loc='lower right', fontsize=10, frameon=False)
plt.tight_layout()
plt.savefig(save_topath + 'Explained_Variance_by_PCA_Components_adj.png',
dpi=600,pad_inches=0.2,)
plt.show()
#use X_pca data to make a table for the following information: PCs, eigenvalues,
and percentage variances
import pandas as pd
# Create a table of PCA results
pca_results = pd.DataFrame({
'PC': range(1, pca.n_components_ + 1),
'Eigenvalue': pca.explained_variance_,
'Percentage Variance': pca.explained_variance_ratio_ * 100
})
# Display the table
pca_results
pca_df[:11]
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
from matplotlib.path import Path
from matplotlib.patches import PathPatch

# PCA LOADINGS
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
# 1. Isolate the variables
Xp = dfad[morphometric_columns]
# 2. Standardize (Crucial for morphometrics to handle scale differences)
X_scaled = StandardScaler().fit_transform(Xp)
# 3. Run PCA
pca = PCA(n_components=10)
pca.fit(X_scaled)
# 4. Create the loadings table
loadings = pd.DataFrame(
pca.components_.T,
columns=['PC1', 'PC2','PC3','PC4','PC5','PC6','PC7','PC8','PC9','PC10',],
index=morphometric_columns
)
print(loadings)

# Add convex hull to the scatter plot
for region in unique_labels:
points = pca_df[pca_df['Marine Region'] == region][['PC1', 'PC2']].values
if len(points) > 2: # Need at least 3 points for a convex hull
hull = ConvexHull(points)
hull_points = points[hull.vertices]

# Close the loop
hull_points = np.append(hull_points, [hull_points[0]], axis=0)

# Create a Path from the hull points
path = Path(hull_points)
patch = PathPatch(path, facecolor=color_map[region],
edgecolor=color_map[region], lw=2, alpha=0.1)
ax.add_patch(patch)
ax.axvline(x=0, color='black', linestyle='--')
ax.axhline(y=0, color='black', linestyle='--')

# ax.set_title('(b) PCA of Morphometric Data',fontsize=10, loc='left')
# ax.set_title('(b)',fontsize=10, loc='left')

ax.set_xlabel(f'PC 1 ({pca.explained_variance_ratio_[0]*100:.2f}%)',fontsize=10)
ax.set_ylabel(f'PC 2 ({pca.explained_variance_ratio_[1]*100:.2f}%)',fontsize=10)
ax.minorticks_on()
ax.tick_params(which='major', direction='out', length=6, width=1,labelsize=10)#,
grid_alpha=0.5)
ax.tick_params(which='minor', direction='out', length=3, width=1)
ax.tick_params(which='both',top=False, right=False)

# Fix legend
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), title='Region',fontsize = 8)

# Bar plot: Individual explained variance
# axp.bar(
# range(1, pca.n_components_ + 1),
# pca.explained_variance_ratio_,
# alpha=0.6,
# color="#56B4E9",
# label='Individual Explained Variance'
# )
# # Line plot: Cumulative explained variance
# axp.plot(
# range(1, pca.n_components_ + 1),
# np.cumsum(pca.explained_variance_ratio_),
# color="#D55E00",
# marker='o',
# label='Cumulative Explained Variance'
# )
# Labels and title
# axp.set_xlabel('Number of Components',fontsize=10)
# axp.set_ylabel('Explained Variance Ratio',fontsize=10)
# # axp.set_title('(a) Explained Variance by PCA
Components',fontsize=10,loc='left')
# axp.set_title('(a)', fontsize=10,loc='left')
# axp.set_xticks(range(1, pca.n_components_ + 1))
# axp.set_ylim(0, 1.1)
# # Enable minor ticks
# axp.minorticks_on()
# Hide all x-axis ticks
# axp.tick_params(axis='x', which='minor',direction='out',bottom=False, top=False,
labelbottom=True)
# axp.tick_params(axis='x', which='both',direction='out', top=False, width=1)
# # Hide y-axis major ticks, show only minor ticks
# axp.tick_params(axis='y', which='major', length=6,width=1,
direction='out',right=False)
# axp.tick_params(axis='y', which='minor', direction='out', length=3,
width=0.5,right=False)
# # Add legend
# axp.legend(loc='lower right', fontsize=10, frameon=False)
# plt.tight_layout()
# plt.savefig(save_topath +
'convex_hull_combined_figure_pca_of_morphometric_data_and_explained_variance_by_pca_no_title_adj.dpi=600,pad_inches=0.2,)
plt.show()

# 2. HIERARCHICAL CLUSTER ANALYSIS 

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import mahalanobis
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.linalg import inv

# Calculate Mahalanobis distances
# You need the covariance matrix for each population or a pooled covariance matrix.
# Let's assume you calculate the covariance matrix for the *entire* dataset for
simplicity here.
# For a proper Mahalanobis distance between group means, you would need group
means and covariance.
# Calculate the inverse covariance matrix of the entire dataset X_scaled
try:
cov_matrix = np.cov(X_scaled.T)
inv_cov_matrix = inv(cov_matrix)

# Calculate the means for each population
population_means = {}
for region in unique_labels:
population_means[region] = X_scaled[y == region].mean(axis=0)

# Calculate the Mahalanobis distance matrix between population means
num_populations = len(unique_labels)
mahalanobis_dist_matrix = np.zeros((num_populations, num_populations))
population_names = list(unique_labels)
for i in range(num_populations):
for j in range(num_populations):
mean_i = population_means[population_names[i]]
mean_j = population_means[population_names[j]]
mahalanobis_dist_matrix[i, j] = mahalanobis(mean_i, mean_j,
inv_cov_matrix)
# Perform hierarchical clustering using the Mahalanobis distance matrix
# Use the upper triangle of the distance matrix for linkage
condensed_dist_matrix =
mahalanobis_dist_matrix[np.triu_indices_from(mahalanobis_dist_matrix, k=1)]
linked = linkage(condensed_dist_matrix, 'average') # 'average' linkage is
common
# Plot the dendrogram
fig, axd = plt.subplots(figsize=(8, 4), facecolor='white', dpi=300)
dendrogram(linked,
orientation='top',
labels=population_names,
distance_sort='descending',
show_leaf_counts=True,
ax=axd)
for icoord in axd.collections:
icoord.set_linewidth(2)

# axd.set_title('Cluster Analysis Dendrogram based on Mahalanobis
Distance',fontsize=10)
axd.set_xlabel('Population',fontsize=10)
axd.set_ylabel('Mahalanobis Distance',fontsize=10)
axd.minorticks_on()
# # Hide all x-axis ticks
axd.tick_params(axis='x', which='minor',direction='out',width=0, bottom=False,
top=False)#, labelbottom=True)
# axd.tick_params(axis='x', which='major',direction='out',width=1)
# Hide y-axis major ticks, show only minor ticks
axd.tick_params(axis='y', which='major', length=6,width=1,
direction='out',right=False)
axd.tick_params(axis='y', which='minor', direction='out', length=3,
width=0.5,right=False)
axd.set_ylim(0,2)
plt.tight_layout()
# plt.savefig(save_topath + 'mahalanobis_dendrogram_cluster_analysis_adj.png',
dpi=600, pad_inches=0.2)
plt.show()

# 1. Conduct Random Forest (RF) on the data 'df' to Capture non-linear relationships.
# 2. Also, Provide variable importance rankings (e.g., body depth might be more
informative than standard length)


import pandas as pd
import matplotlib.pyplot as plt
# !pip install scikit-learn umap-learn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.inspection import permutation_importance
import umap.umap_ as umap

# Assuming X and y are defined from dataset loading
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42)

# 3. RANDOM FOREST ANALYSIS
# Initialize and train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=1000, random_state=42)
rf_model.fit(X_train, y_train)
# Predict on the test set
y_pred_rf = rf_model.predict(X_test)
# Evaluate the model
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f'Random Forest Accuracy: {accuracy_rf:.2f}')
# Variable Importance Rankings
# Get feature importances from the trained model
feature_importances = rf_model.feature_importances_
# Create a DataFrame to visualize feature importance
# Assuming your feature names are in X.columns
if isinstance(X, pd.DataFrame):
feature_names = X.columns
else:
# If X is a numpy array, create generic names
feature_names = [f'Feature {i}' for i in range(X.shape[1])]
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance':
feature_importances})
# Sort by importance
importance_df = importance_df.sort_values(by='Importance', ascending=False)
print("\nRandom Forest Feature Importance Rankings:")
print(importance_df)
# You can also use permutation importance for a potentially more reliable estimate
result = permutation_importance(rf_model, X_test, y_test, n_repeats=10,
random_state=42, n_jobs=-1)
perm_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance_mean':
result.importances_mean, 'Importance_std': result.importances_std})
perm_importance_df = perm_importance_df.sort_values(by='Importance_mean',
ascending=False)
print("\nRandom Forest Permutation Importance Rankings:")
print(perm_importance_df)
# Create the DataFrame using the requested column names
importance_table = pd.DataFrame({
'Feature': perm_importance_df['Feature'],
'Importance mean': perm_importance_df['Importance_mean'],
'Importance sd': perm_importance_df['Importance_std']
})
# Name the existing index 'Rank'
importance_table.index.name = 'Rank'
# Reset the index to turn 'Rank' into a column and rename columns to your specific
request
importance_table = importance_table.reset_index()
print(importance_table)
# save the data to csv
importance_table.to_csv(save_topath+"Random_Forest_Feature_Importance_using
permutation_table_with_1000_estimators.csv", index=False)
# ------------------ hard‑code the numbers ------------------ #
rf_feat_importance = pd.DataFrame(
{
"Feature": [
"ED_adj", "SnL_adj", "CPD_adj", "TL_adj", "DA_adj",
"Dpec_adj", "HL_adj", "Dpel_adj", "DD_adj", "BD_adj"
],
"RF_FeatureImportance": [
0.236378, 0.155892, 0.107350, 0.090071, 0.083938,
0.080811, 0.074118, 0.063340, 0.058988, 0.049114
],
}
)
rf_perm_importance = pd.DataFrame(
{
"Feature": [
"ED_adj", "SnL_adj", "DA_adj", "CPD_adj", "TL_adj",
"HL_adj", "Dpel_adj", "Dpec_adj", "DD_adj", "BD_adj"
],
"RF_PermImportance_mean": [
0.264567, 0.074016, 0.043307, 0.033858, 0.033071,
0.030709, 0.028346, 0.020472, 0.014173, 0.003937
],
"RF_PermImportance_std": [
0.026399, 0.016214, 0.011274, 0.011706, 0.007715,
0.008943, 0.010681, 0.012300, 0.010446, 0.003937
],
}
)
# ------------------ merge the two tables ------------------ #
df = rf_feat_importance.merge(rf_perm_importance, on="Feature")
# ------------------ drop “_adj” from Feature names -------- #
df["Feature"] = df["Feature"].str.replace("_adj", "", regex=False)
# or: df["Feature"] = df["Feature"].str.removesuffix("_adj") # pandas ≥2.0
# ------------------ view / save --------------------------- #
print(df)
# df.to_csv(save_topath+"rf_feature_and_perm_importance_adj.csv", index=False)
# dfr = pd.DataFrame(data)
# # Save as CSV
# csv_path = "random_forest_feature_importance_summary_adj.csv"
# df.to_csv(save_topath+csv_path, index=False)

import matplotlib
import seaborn as sns
import matplotlib.colors as mcolors
# import matplotlib.colormaps as cmaps # Correct usage in Matplotlib ≥ 3.7 -
Commented out
# Get 12 evenly spaced colors from the reversed 'Blues' colormap
# Use plt.cm to access colormaps in older Matplotlib versions
cmap = plt.get_cmap('Blues_r')
cmap2 = [mcolors.rgb2hex(cmap(i / 11)) for i in range(12)] # Normalize from 0 to 1
# Select top 12 features and create color mapping
top_features = df.sort_values('RF_FeatureImportance',
ascending=False).head(12).copy()
top_features['Color'] = top_features['Feature'] # Dummy hue column for Seaborn
col_map = dict(zip(top_features['Color'], cmap2))
# Plot
fig, axb = plt.subplots(figsize=(10, 6), facecolor='White',dpi=300)
sns.barplot(
x='RF_FeatureImportance',
y='Feature',
data=top_features,
hue='Color', # Set hue to apply palette correctly
palette=col_map,
legend=False,
ax=axb
)
plt.grid(False)
axb.minorticks_on()
# # Hide all x-axis ticks
axb.tick_params(axis='y', which='minor',direction='out',width=0, right=False,
top=False)#, labelbottom=True)
axb.tick_params(axis='y',
which='major',direction='out',width=2,right=False,labelsize=15)
# Hide y-axis major ticks, show only minor ticks
axb.tick_params(axis='x', which='major', length=6,width=2,
direction='out',top=False,labelsize=15)
axb.tick_params(axis='x', which='minor', direction='out', length=3,
width=0.5,top=False)
# axb.set_title('Random Forest Feature Importance', fontsize=15)
axb.set_xlabel('Importance', fontsize=15)
axb.set_ylabel('Feature', fontsize=15)
plt.tight_layout()
# plt.savefig(save_topath + 'Random_Forest_Feature_Importance_adj.png',
dpi=600,pad_inches=0.2,)
plt.show()

# 4. UMAP ANALYSIS
#Perform UMAP for Dimensionality Reduction and Visualization

import pandas as pd
import matplotlib.pyplot as plt
# !pip install umap-learn
import umap

# Perform UMAP analysis
reducer = umap.UMAP(random_state=42,
n_neighbors=15,
min_dist=0.1,
metric='euclidean',
)
X_umap = reducer.fit_transform(X_scaled)
# Create DataFrame for plotting
umap_df = pd.DataFrame({
'UMAP 1': X_umap[:, 0],
'UMAP 2': X_umap[:, 1],
'Marine Region': y
})
# Plot UMAP results
fig, ax = plt.subplots(figsize=(8, 5), dpi=300, facecolor='white')
sns.scatterplot(data=umap_df, x='UMAP 1', y='UMAP 2', hue='Marine Region',
palette=color_map, ax=ax)
# ax.set_title('UMAP of Morphometric Data')
ax.set_xlabel('UMAP 1')
ax.set_ylabel('UMAP 2')
ax.minorticks_on()
ax.tick_params(which='major', direction='out', length=6, width=1,labelsize=18)
ax.tick_params(which='minor', direction='out', length=3, width=1)
ax.tick_params(which='both',top=False, right=False)
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), title='Region',fontsize =
8,loc='upper right', frameon=False)
ax.axvline(x=0, color='grey', linestyle='--')
ax.axhline(y=0, color='grey', linestyle='--')
plt.tight_layout()
# plt.savefig(save_topath + 'UMAP_of_Morphometric_Data_adj.png',
dpi=600,pad_inches=0.2,)
plt.show()

# 5. LINEAR DISCRIMINANT ANALYSIS(LDA)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

if len(y.unique()) <= X_scaled.shape[1]:
lda = LDA()
X_lda = lda.fit_transform(X_scaled, y)
# Create DataFrame for plotting
lda_df = pd.DataFrame(X_lda, columns=[f'LD{i+1}' for i in
range(X_lda.shape[1])])
lda_df['Marine Region'] = y.reset_index(drop=True)
fig,axc = plt.subplots(1,1,figsize=(8, 4),dpi=300,facecolor='white')
if lda_df.shape[1] >= 2:
scatter = sns.scatterplot(
x='LD1', y='LD2',
hue='Marine Region',
palette=color_map,
data=lda_df,
legend=True
)
for region in lda_df['Marine Region'].unique():
region_data = lda_df[lda_df['Marine Region'] == region]
mean_ld1 = region_data['LD1'].mean()
mean_ld2 = region_data['LD2'].mean()
# Covariance matrix and ellipse orientation
cov = np.cov(region_data[['LD1', 'LD2']].values.T)
lambda_, v = np.linalg.eig(cov)
lambda_ = np.sqrt(lambda_)
# Ellipse
ellipse = Ellipse(
xy=(mean_ld1, mean_ld2),
width=2 * lambda_[0],
height=2 * lambda_[1],
angle=np.rad2deg(np.arccos(v[0, 0])),
edgecolor=color_map[region],
facecolor='none',
linestyle='solid',
linewidth=1.5
)
scatter.axes.add_patch(ellipse)
# Star marker for centroid (unfilled)
scatter.plot(
mean_ld1,
mean_ld2,
marker='*',
markersize=16,
markerfacecolor='white',
markeredgecolor=color_map[region],
markeredgewidth=1
)
# plt.title('FDA of Morphometric Data with Group Ellipses and Centroids',
fontsize=14)
plt.xlabel(f'Function 1 ({lda.explained_variance_ratio_[0]*100:.2f}%)')
plt.ylabel(f'Function 2 ({lda.explained_variance_ratio_[1]*100:.2f}%)')
# Legend
handles, labels = scatter.axes.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
scatter.axes.legend(by_label.values(), by_label.keys(),
title='Region',fontsize=8, loc='lower right')
elif lda_df.shape[1] == 1:
sns.histplot(
x='LD1',
hue='Marine Region',
kde=True,
palette=color_map,
multiple="stack",
data=lda_df, ax=axc
)
# plt.title('DFA of Morphometric Data (1 Component)')
plt.xlabel('Linear Discriminant 1')
for region in lda_df['Marine Region'].unique():
region_data = lda_df[lda_df['Marine Region'] == region]
mean_ld1 = region_data['LD1'].mean()
color = color_map[region]
plt.axvline(mean_ld1, color=color, linestyle='--', linewidth=2,
label=f'{region} Mean')
plt.legend(title='Region', fontsize=8)
axc.axvline(x=0, color='black', linestyle='--')
axc.axhline(y=0, color='black', linestyle='--')
axc.minorticks_on()
axc.tick_params(which='major', direction='out', length=6, width=1,labelsize=16)
axc.tick_params(which='minor', direction='out', length=3, width=1)
axc.tick_params(which='both',top=False, right=False)
plt.tight_layout()
# plt.savefig(save_topath +
'FDA_of_Morphometric_Data_with_Group_Ellipses_and_Centroids_adj.png',
dpi=600,pad_inches=0.2)
plt.show()

lda.explained_variance_ratio_
#compute the DFA and show a table for a percentage of accurate classification of
the four populations considered the cell above
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# Split the data into training and testing sets for classification evaluation
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3,
random_state=42, stratify=y) # stratify to maintain class distribution

# Perform LDA for classification
lda_clf = LDA()
lda_clf.fit(X_train, y_train)
# Predict on the test set
y_pred = lda_clf.predict(X_test)
# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of LDA Classification: {accuracy:.2f}")
# Generate a classification report
report = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(report)
# Generate a confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(conf_matrix)
# Create a DataFrame for the classification accuracy table
classification_results = pd.DataFrame({
'Metric': ['Accuracy'],
'Value': [accuracy]
})
# Add metrics from the classification report to the table
report_dict = classification_report(y_test, y_pred, output_dict=True)
# Extract precision, recall, f1-score for each class and the overall average
metrics_list = []
for label in report_dict.keys():
if isinstance(report_dict[label], dict):
metrics_list.append({'Region': label, 'Precision': report_dict[label]
['precision'], 'Recall': report_dict[label]['recall'], 'F1-Score':
report_dict[label]['f1-score'], 'Support': report_dict[label]['support']})
elif label in ['accuracy', 'macro avg', 'weighted avg']:
if label == 'accuracy':
classification_results = pd.concat([classification_results,
pd.DataFrame({'Metric': [label], 'Value': [report_dict[label]]})],
ignore_index=True)
else:
classification_results = pd.concat([classification_results,
pd.DataFrame({'Metric': [f'{label} Precision', f'{label} Recall', f'{label} F1-
Score', f'{label} Support'],
'Value': [report_dict[label]['precision'], report_dict[label]['recall'],
report_dict[label]['f1-score'], report_dict[label]['support']]})],
ignore_index=True)
metrics_df = pd.DataFrame(metrics_list)
print("\nDetailed Classification Metrics per Region:")
print(metrics_df.to_string(index=False))
print("\nOverall Classification Summary:")
print(classification_results.to_string(index=False))
y[10:200]

# Length of samples range per region
dfad
length_summary = dfad.groupby('Region Name')['TL_adj'].agg(
Sample_Size='count',
Min_Length='min',
Max_Length='max',
Mean_Length='mean',
SD_Length='std'
)
print(length_summary)
length_summary.round(2).to_csv(save_topath+"Length_range_table.csv")

# Run ANOVA on Morphometrics Across Regions
from scipy.stats import f_oneway
morphometric_columns = ['TL_adj', 'SnL_adj', 'HL_adj', 'ED_adj',
'BD_adj', 'CPD_adj', 'DD_adj', 'Dpec_adj',
'Dpel_adj', 'DA_adj']
for col in morphometric_columns:
groups = [group[col].values for name, group in dfad.groupby('Region Name')]
stat, p = f_oneway(*groups)
print(col, "p =", p)
import pandas as pd
from scipy.stats import f_oneway
# Initialize an empty list to collect results
anova_results = []
for col in morphometric_columns:
# Group the data and run the ANOVA
groups = [group[col].values for name, group in dfad.groupby('Region Name')]
stat, p = f_oneway(*groups)
# Store the results in a dictionary
anova_results.append({
'Morphometris': col,
'F_statistic': stat,
'p_value': p
})
# Convert the list of results into a pandas DataFrame
results_anova = pd.DataFrame(anova_results)
# Display the final table
print(results_anova)
import numpy as np
# Create a boolean column (True if p < 0.05)
# results_df['Significant'] = results_df['p_value'] < 0.05
# Add notation: ** for p < 0.01, * for p < 0.05, and 'ns' (non-significant)
otherwise
results_anova['p<0.01:* & p<0.05:**'] = np.where(results_anova['p_value'] < 0.01,
'**',
np.where(results_anova['p_value'] < 0.05, '*',
'ns'))
print(results_anova)
#Shows significant morphological variation among sites

# Validation of Multivariate Assumptions
# 1. Multicollinearity (VIF)
from statsmodels.stats.outliers_influence import variance_inflation_factor
Xad = dfad[morphometric_columns]
vif = pd.DataFrame()
vif["feature"] = Xad.columns
vif["VIF"] = [variance_inflation_factor(Xad.values, i)
for i in range(len(Xad.columns))]
print(vif)

# 2. Homoscedasticity (Box M Test)
!pip install bioinfokit
import numpy as np
from statsmodels.stats.multivariate import test_cov_oneway
# Create a list of data arrays for each region
group_dat = [group[morphometric_columns].values for name, group in
dfad.groupby('Region Name')]
# Get the sample sizes (n) for each group
n_obs = [len(group) for group in group_dat]
# Calculate the covariance matrix for each group
cov_matrices = [np.cov(group, rowvar=False) for group in group_dat]
# Run the homogeneity of covariance test (Box's M equivalent)
res = test_cov_oneway(cov_matrices, n_obs)
print("Box's M Test Equivalent (statsmodels):")
print(f"Chi-square statistic: {res.statistic:.4f}")
# print(f"p-value: {res.pvalue:.4f}")
print(f"Degrees of freedom: {res}")

#MANOVA Tests Statistic
from statsmodels.multivariate.manova import MANOVA
# Wrap the variable with spaces in Q()
formula = ' + '.join(morphometric_columns) + ' ~ Q("Region Name")'
maov = MANOVA.from_formula(formula, data=dfad)
print(maov.mv_test())