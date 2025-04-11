# Heart Disease Classification Model

*Predicting Heart Disease with Precision and Simplicity*

## 🌟 Overview
This project implements a **logistic regression model** to classify heart disease using a dataset (`heart-disease.csv`). Built with **scikit-learn**, the model is trained, pre-tuned with optimal hyperparameters, and saved using **pickle** for future use. The script includes data preprocessing, train-test splitting, and model training—making it a complete pipeline for heart disease prediction.

### ✨ Key Features
- **📊 Data Loading**: Imports `heart-disease.csv` with ease.
- **✂️ Data Splitting**: Separates features (X) and target (y), then splits into training and testing sets.
- **🧠 Model Training**: Uses logistic regression with pre-tuned hyperparameters.
- **💾 Model Saving**: Exports the trained model to `_model.pkl` for reuse.
- **⚙️ Pre-Tuned**: Hardcoded hyperparameters for optimal performance.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Dataset](#-dataset)
- [Usage](#-usage)
- [Code Explanation](#-code-explanation)
- [File Structure](#-file-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## ⚙️ Requirements
- **🐍 Python 3.x**
- **Required Libraries**:
  - `pandas`: Data manipulation and loading.
  - `scikit-learn`: Machine learning model training and splitting.
  - `pickle`: Model serialization (included in Python standard library).

---

## 🏁 Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/felekekinfe/Heart-Disease-Prediction
   cd Heart-Disease-Prediction
   ```

2. **Install Dependencies**:
   ```bash
   pip install pandas scikit-learn
   ```
   *Note: `pickle` is built into Python, so no additional installation is needed.*

3. **Add the Dataset**:
   - Place `heart-disease.csv` in the `dataset/` folder (create this folder if it doesn’t exist).

---

## 📊 Dataset
The model uses **`heart-disease.csv`**, a dataset containing features related to heart disease and a binary target column (`target`). It should be located in the `dataset/` directory.

### Example Structure
```
age  sex  cp  trestbps  chol  ...  target
63   1    3   145       233   ...  1
37   1    2   130       250   ...  1
```
- **Features**: All columns except `target` (e.g., `age`, `sex`, `chol`).
- **Target**: `target` column (0 = no heart disease, 1 = heart disease).

*Source*: Available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease) or use your own dataset with a similar structure.

---

## 🎬 Usage
1. **Ensure Setup**:
   - Dependencies installed.
   - `heart-disease.csv` in `dataset/`.

2. **Run the Script**:
   ```bash
   python heart_disease_model.py
   ```
   - Loads the dataset.
   - Trains the model.
   - Saves it as `_model.pkl`.

3. **Reuse the Model**:
   Load `_model.pkl` in another script for predictions:
   ```python
   import pickle
   with open('_model.pkl', 'rb') as file:
       model = pickle.load(file)
   # Use model.predict(X) for predictions
   ```

---

## 🧠 Code Explanation
The script performs these steps:
1. **Loads Data**: Reads `heart-disease.csv` using `pandas`.
2. **Prepares Data**:
   - Features (`X`): All columns except `target`.
   - Target (`y`): `target` column.
3. **Splits Data**: Uses `train_test_split` from `scikit-learn` for training and testing sets.
4. **Trains Model**: Logistic regression with:
   - `C=0.23357214690901212`
   - `solver='liblinear'`
   *(Pre-tuned, via `RandomizedSearchCV` or `GridSearchCV`.)*
5. **Saves Model**: Exports to `_model.pkl` using `pickle`.

---

## 📁 File Structure
```
├── dataset/                  # Dataset storage
│   └── heart-disease.csv     # Heart disease dataset
├── heart_disease_model.py    # Main script
├── _model.pkl                # Saved model (generated after running)
├── README.md                 # This file
└── .gitignore                # Git ignore file
```

*Note*: Create `dataset/` manually if it’s not in the repo.

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

Feel free to suggest improvements or report issues!

---

## 📜 License
This project is licensed under the [MIT License](LICENSE)

---

*Built with 💻 and ❤️ by [felekekinfe](https://github.com/felekekinfe).*  
Let’s predict heart disease and save lives.🚀

---


Let me know if you’d like to add a banner, tweak anything, or need help with specific sections!
