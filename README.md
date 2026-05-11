# README.md

## Morphometric Analysis of *Pennahia aneus*

### Reproducible Python Workflow for Multivariate Morphometric Analysis


## Project Overview

This repository contains the reproducible Python workflow used for the morphometric analyses of *Pennahia aneus* populations sampled from multiple Malaysian marine regions. The analyses were conducted to investigate morphometric variation, population structure, and stock differentiation using multivariate statistical and machine-learning approaches.

The workflow was developed for the manuscript submitted to *Scientific Reports* and includes all scripts necessary to reproduce the statistical analyses, dimensionality reduction procedures, machine-learning classification, and graphical outputs presented in the study.


## Analyses Included

The workflow includes the following analyses:

* Principal Component Analysis (PCA)
* PCA loading analysis
* Hierarchical Cluster Analysis
* Mahalanobis distance analysis
* Linear Discriminant Analysis (LDA/DFA)
* Random Forest classification and feature importance
* Uniform Manifold Approximation and Projection (UMAP)
* Analysis of Variance (ANOVA)
* Multicollinearity Assessment using Variance Inflation Factor (VIF) analysis
* Multivariate Analysis of Variance (MANOVA)
* Homogeneity of covariance assessment


## Morphometric Variables Used

The analyses were performed using size-adjusted morphometric variables:

* TL_adj
* SnL_adj
* HL_adj
* ED_adj
* BD_adj
* CPD_adj
* DD_adj
* Dpec_adj
* Dpel_adj
* DA_adj


## Repository Structure

morphometric_analysis_p_aneus/
│
├── data/
│   └── morphometric_data.xlsx
│
├── results/
│   ├── figures/
│   └── tables/
│
├── morphometric_analysis.py
├── requirements.txt
└── README.md


## Software Requirements

The workflow was originally developed and executed in Google Colab using Python.  

The analyses used the following Python libraries:


-numpy
-pandas
-matplotlib
-seaborn
-scikit-learn
-scipy
-statsmodels
-umap-learn
-openpyxl
-bioinfokit


Install all dependencies using:
```bash

pip install -r requirements.txt

## Input Data

The script requires an Excel file containing morphometric measurements and sampling-region information.

Expected input file:

data/morphometric_data.xlsx

The dataset should include:

* Sampling region information
* All adjusted morphometric variables used in the analyses


## Running the Workflow

Run the complete analysis pipeline using:

python morphometric_analysis.py

The script automatically:

1. Loads the dataset
2. Standardizes morphometric variables
3. Performs all statistical analyses
4. Generates figures and plots
5. Exports tables and summary statistics

---

## Output Files

### Figures Generated

* PCA ordination plots
* PCA explained variance plots
* PCA convex hull plots
* Hierarchical clustering dendrograms
* Random Forest importance plots
* UMAP ordination plots
* LDA/DFA plots

### Tables Generated

* PCA eigenvalue tables
* PCA loading matrices
* Random Forest importance rankings
* Classification accuracy summaries
* ANOVA tables
* VIF tables
* Morphometric summary tables

## Reproducibility Notes

To ensure reproducibility:

* Morphometric variables were standardized using `StandardScaler` prior to multivariate analyses.
* Randomized analyses used a fixed random seed (`random_state = 42`).
* UMAP analyses were conducted using:

  * `n_neighbors = 15`
  * `min_dist = 0.1`
  * `metric = 'euclidean'`


## Code Availability

All analyses were conducted in Python using standard scientific libraries. The full reproducible code used to generate the results and figures in this study is publicly available at: [Insert GitHub Repository or Zenodo DOI Here].


## Citation

If you use this workflow or code, please cite the associated manuscript:

> [Manuscript currently under review]

## Author Information

Jolly Babangida Kachi
[Universiti Sains Malaysia]
[Kachijb@student.usm.my]
