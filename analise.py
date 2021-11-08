
import pandas as pd
import streamlit as st
import s3fs


# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False)

# Retrieve file contents.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600000)

bucket = "teste-streamlit"
key = "analise_s3.csv"

df = pd.read_csv(fs.open('{}/{}'.format(bucket, key), mode='rb'), delimiter=';')

kpi1, kpi2, kpi3, kpi4 = st.beta_columns(4)
with kpi1:
    st.markdown('**Tempo Produção**')
    number1 = df.iloc[1,1]
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with kpi2:
    st.markdown('**Tempo M3M**')
    number2 = df.iloc[2,1]
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True) 
    
with kpi3:
    st.markdown('**Tempo M4M**')
    number3 = df.iloc[3,1]
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True) 

with kpi4:
    st.markdown('**Tempo Outros**')
    number4 = df.iloc[4,1]
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number4}</h1>", unsafe_allow_html=True)