# wine-quality-elastic-net
Machine learning project predicting wine quality using Elastic Net regression with Python and Scikit-learn.


## ⚙️ Data Validation Workflow

The data validation process follows a structured pipeline to ensure the dataset is correct before moving to the next ML stage.

```text
Read YAML Files (config.yaml + schema.yaml)
            ↓
Load and parse configurations
            ↓
Assign values to Config Entity (DataValidationConfig)
            ↓
Run data validation checks on dataset
            ↓
Generate validation status (True / False) 

```
## 📄 schema.yaml – Data Validation Contract

The `schema.yaml` file acts as a data contract for this project. It defines the expected structure, data types, and validation rules that the dataset must follow before entering the ML pipeline.

---

## 🔍 What does schema.yaml define?

- **Schema (COLUMNS)** → Expected columns with their data types  
- **Target Column (TARGET_COLUMN)** → Label used for model training  
- **Feature Groups** → Numerical and categorical columns  
- **Structure Rules** → Expected column order and total column count  
- **Required Columns** → Columns that must exist in the dataset  
- **Validation Rules** → Value constraints such as min/max rules  

---
## 🧠 Key Idea

> **"Garbage in → Garbage out"**

This schema prevents bad data from entering the system.

## ✅ Validation Checks Performed

### 📦 Structure Validation
- Column existence (`REQUIRED_COLUMNS`)  
- Schema match (`COLUMNS`)  
- Numerical column existence (`NUMERICAL_COLUMNS`)  
- Categorical column existence (`CATEGORICAL_COLUMNS`)  
- Column count (`COLUMN_COUNT`)  
- Column order (`COLUMN_ORDER`)  

### 🔤 Data Type Validation
- Data type check using `COLUMNS`  

### 📏 Value Validation
- Range checks using `DATA_VALIDATION_RULES`  

### 🎯 ML-Specific Validation
- Target column existence (`TARGET_COLUMN`)  

---

## 🚀 Why This Matters

This validation step is important because it:

- Ensures clean and consistent data  
- Prevents pipeline failures early  
- Improves model reliability  
- Makes the system more production-ready  

## 🧠 Key Idea

`schema.yaml` + `config.yaml` → Config Entity → Validation Logic → Clean Data