import streamlit as st
import boto3
import pandas as pd

s3 = boto3.resource('s3')


obj = s3.Object('teste-streamlit', 'chave/KDS-S3-4bfyf-1-2021-11-03-18-10-17-3bb2ea69-7eff-3913-94ad-971ed72fec91')

    
file_content = obj.get()['Body'].read()
df = pd.read_json(file_content, lines=True)
#df.head()
st.line_chart(data=df['x'], width=0, height=0, use_container_width=True)