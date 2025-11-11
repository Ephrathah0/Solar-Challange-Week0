import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Solar Data Explorer')
col1, col2, col3 = st.columns([1, 1, 1]) 


with col1:
    uploaded_file1 = st.file_uploader("Upload Benin's data", type="csv", key='file1')
    if uploaded_file1 is not None:
        try:
            df_benin = pd.read_csv(uploaded_file1)
            st.success("Uploaded")
            st.write(df_benin.head())
        except Exception as e:
            st.error(f"Error: {e}")

with col2:
    uploaded_file2 = st.file_uploader("Upload Togo's data", type="csv", key='file2')
    if uploaded_file2 is not None:
        try:
            df_togo = pd.read_csv(uploaded_file2)
            st.success("Uploaded")
            st.write(df_togo.head())
        except Exception as e:
            st.error(f"Error: {e}")

with col3:
    uploaded_file3 = st.file_uploader("Upload Sierraleone's data", type="csv", key='file3')
    if uploaded_file3 is not None:
        try:
            df_sierra = pd.read_csv(uploaded_file3)
            st.success("Uploaded!")
            st.write(df_sierra.head())
        except Exception as e:
            st.error(f"Error: {e}")


dfs=[]
if uploaded_file1 is not None:
    try:
        df_benin["Country"] = "Benin"
        dfs.append(df_benin)
    except: pass

if uploaded_file2 is not None:
    try:
        df_togo["Country"] = "Togo"
        dfs.append(df_togo)
    except: pass

if uploaded_file3 is not None:
    try:
        df_sierra["Country"] = "Sierra Leone"
        dfs.append(df_sierra)
    except: pass
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    st.subheader("Combined Dataset Preview")
    st.write(combined_df.head())
if dfs:
    st.subheader("GHI Comparison Across Countries")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=combined_df, x="Country", y="GHI", palette="viridis", ax=ax)
    st.pyplot(fig)
if dfs:
    st.subheader("📊 Summary Statistics")
    summary = combined_df.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"]).round(2)
    st.dataframe(summary)
metric = st.sidebar.selectbox(
    "Select metric to visualize",
    ["GHI", "DNI", "DHI", "Tamb", "RH", "WS"]  
)

if dfs: 
    st.subheader(f"📦 {metric} Comparison Across Countries")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=combined_df, x="Country", y=metric, palette="viridis", ax=ax)
    st.pyplot(fig)

