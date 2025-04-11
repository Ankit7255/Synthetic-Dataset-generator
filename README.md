
# 🧪 Synthetic Dataset Generator

This project is a **Streamlit-based app** that generates synthetic datasets with both **categorical** and **numerical** features. It's designed to help developers, data scientists, and machine learning enthusiasts quickly create mock data for experiments, testing, and model training.

---

## 📁 Example Input

You can start with a base dataset (like the included `synthetic_employee_data.csv`) that contains:
- **Numerical features**: age, salary, experience_years
- **Categorical features**: department, education_level
- **Target**: left_company (binary classification)

---

## 🚀 Features

- Upload a base dataset or start from scratch
- Add new synthetic rows based on statistical properties
- Control balance of categorical values
- Choose random noise or consistent patterns
- Download the final dataset as CSV

---

## 🛠️ How to Run

1. Install Streamlit (if not already):

    ```bash
    pip install streamlit
    ```

2. Run the app:

    ```bash
    streamlit run app.py
    ```

3. Upload a CSV or use default generation parameters to create new data.

---

## 💡 Use Cases

- Rapid prototyping of ML models
- Stress testing pipelines
- Teaching data science without real data
- Mock data for presentations or demos

---

## 📦 Included Files

- `app.py` - The main Streamlit app
- `synthetic_employee_data.csv` - Starter dataset
- `README.md` - This file

---

## 🧠 Pro Tip

If your synthetic data starts predicting your real life… close the app. It's become self-aware. 😈

---

## 📬 Contact

Made with caffeine, chaos, and code. Reach out if you want to add new generation modes, automated outlier injection, or deep fake HR data generators.
