Heart Disease Classification Model

This project implements a logistic regression model to classify heart disease based on a dataset. The model is trained using the scikit-learn library, and the trained model is saved using pickle for later use. Hyperparameters are pre-tuned, and the code includes data preprocessing and train-test splitting.
Table of Contents

    Overview
    Requirements
    Installation
    Dataset
    Usage
    Code Explanation
    File Structure
    Contributing
    License

Overview

The script performs the following tasks:

    Loads a heart disease dataset (heart-disease.csv).
    Splits the data into features (X) and target (y).
    Splits the dataset into training and testing sets.
    Trains a logistic regression model with pre-tuned hyperparameters.
    Saves the trained model to a file (_model.pkl) using pickle.

The hyperparameters for the logistic regression model (C=0.23357214690901212, solver='liblinear') are hardcoded, presumably obtained from prior tuning (e.g., using RandomizedSearchCV or GridSearchCV).
Requirements

    Python 3.x
    Required Python libraries:
        pandas
        scikit-learn
        pickle (comes with Python standard library)

Installation

    Clone the repository or download the script:
    bash

git clone https://github.com/felekekinfe/Heart-Disease-Prediction
cd Heart-Disease-Prediction
Install the required dependencies:
bash

    pip install pandas scikit-learn
    (Note: pickle is included in Python by default.)
    Ensure the dataset (heart-disease.csv) is placed in the dataset/ folder.

Dataset

The dataset used is heart-disease.csv, which should be located in the dataset/ directory. It is assumed to contain features related to heart disease and a target column (target) indicating the presence (1) or absence (0) of heart disease.

Example structure of the dataset:
age	sex	cp	trestbps	chol	...	target
63	1	3	145	233	...	1
37	1	2	130	250	...	1

    Features: All columns except target.
    Target: target column (binary: 0 or 1).

You can download this dataset from sources like UCI Machine Learning Repository or replace it with your own dataset with a similar structure.
