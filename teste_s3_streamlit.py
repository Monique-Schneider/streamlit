import streamlit as st
import boto3
import pandas as pd

aws_id = st.text_input("AWS_ACCESS_KEY_ID", 0)
aws_key = st.text_input("AWS_SECRET_ACCESS_KEY", 0)

if (aws_id!=0 and aws_key!=0):
    s3 = boto3.resource('s3', aws_access_key_id=aws_id, aws_secret_access_key=aws_key)
    obj = s3.Object('teste-streamlit', 'chave/KDS-S3-4bfyf-1-2021-11-03-18-10-17-3bb2ea69-7eff-3913-94ad-971ed72fec91')
    file_content = obj.get()['Body'].read()
    df = pd.read_json(file_content, lines=True)
    #df.head()
    st.line_chart(data=df['x'], width=0, height=0, use_container_width=True)
