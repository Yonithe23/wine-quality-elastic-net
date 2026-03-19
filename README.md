# wine-quality-elastic-net
Machine learning project predicting wine quality using Elastic Net regression with Python and Scikit-learn.

⚙️ Data Ingestion Workflow  
The data ingestion process follows a structured pipeline to collect and prepare the dataset before moving to the next ML stage.
```text
Read YAML File (config.yaml)
            ↓
Load and parse ingestion configurations
            ↓
Assign values to Config Entity (DataIngestionConfig)
            ↓
Download / access dataset from source
            ↓
Extract and store dataset into local artifacts folder
            ↓
Generate ingestion status / output dataset path
```
## 📄 config.yaml – Data Ingestion Contract

The `config.yaml` file acts as a **configuration contract** for the data ingestion stage.  
It defines how the dataset is collected, where it is stored, and how it is prepared before entering the ML pipeline.

---

### 🔍 What does `config.yaml` define?

- **Data Source (SOURCE_URL)** → Location of dataset (URL / API / local)
- **Download Path** → Where raw data is downloaded
- **Extraction Path** → Where compressed data is extracted
- **Raw Data Path** → Final usable dataset location
- **Artifacts Directory** → Organized storage for pipeline outputs
- **File Handling Rules** → Format (CSV, ZIP, etc.) and extraction behavior

---

### 🧠 Key Idea

"Wrong data source → Wrong results"

This configuration ensures the correct data is collected before processing.

---

## ⚙️ Data Ingestion Tasks Performed

- Download dataset from source  
- Handle compressed files (ZIP extraction)  
- Store data in artifacts directory  
- Organize raw dataset for next stage  
- Ensure file availability for pipeline  

---

## 🚀 Why This Matters

This ingestion step is important because it:

- Ensures **reproducible data collection**
- Maintains **consistent data storage structure**
- Prevents **missing or incorrect data issues**
- Makes the pipeline **modular and scalable**
- Enables **production-ready data flow**

---

### 🧠 Key Idea

config.yaml → Config Entity → Ingestion Logic → Raw Data

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