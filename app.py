import streamlit as st
import pandas as pd
from ctgan import CTGAN
from io import BytesIO

# Inject custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stButton > button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #ff1c1c;
    }
    .stDownloadButton > button {
        background-color: #00c853;
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("## 🧪 Synthetic Dataset Generator")
st.markdown("Create Synthetic datasets for your machine learning fantasies. 🤖✨")

# Upload CSV
uploaded_file = st.file_uploader("📤 Upload a CSV (Categorical + Numerical)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Column Analysis
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    tab1, tab2 = st.tabs(["📊 Preview", "📁 Column Types"])
    with tab1:
        st.subheader("👁️ Original Data Preview")
        st.dataframe(df.head())

    with tab2:
        st.subheader("🧬 Column Breakdown")
        st.write(f"**Categorical Columns:** {', '.join(categorical_columns)}")
        st.write(f"**Numerical Columns:** {', '.join(numerical_columns)}")

    # Number input
    num_samples = st.number_input("🔢 Number of synthetic samples to generate", min_value=1, value=100)

    # Generate synthetic data
    if st.button("🔥 Generate Synthetic Data"):
        st.info("Training CTGAN model... sip your coffee while I do the black magic ☕🧙")

        # Train model
        model = CTGAN()
        model.fit(df, categorical_columns)

        # Generate synthetic data
        synthetic_data = model.sample(num_samples)

        st.success("🎉 Synthetic Data Generated Successfully!")
        st.write(synthetic_data.head())

        # Download button
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="💾 Download Synthetic CSV",
            data=convert_df(synthetic_data),
            file_name='synthetic_data.csv',
            mime='text/csv'
        )
