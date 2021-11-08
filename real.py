import streamlit as st
import time
import boto3
import ast


id = st.text_input("AWS_ACCESS_KEY_ID", 0)
key = st.text_input("AWS_SECRET_ACCESS_KEY", 0)

kpi1, kpi2 = st.beta_columns(2) 



if (id!=0 and key!=0):
    kinesis_client = boto3.client('kinesis', aws_access_key_id=id, aws_secret_access_key=key, region_name='us-east-1')
    my_stream_name = 'ExampleInputStream'

    response = kinesis_client.describe_stream(StreamName=my_stream_name)
    my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

    shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name, ShardId=my_shard_id, ShardIteratorType='LATEST')

    my_shard_iterator = shard_iterator['ShardIterator']
    record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,Limit=100)

    while 'NextShardIterator' in record_response:
        record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],Limit=1)

        if(record_response['Records']):
            #file_content = obj.get()['Body'].read()
            #df = pd.read_json(file_content, lines=True)
            a = record_response['Records'][0]['Data']
            dict_str = a.decode("UTF-8")
            mydata = ast.literal_eval(dict_str)
            x = mydata.get('x')
            y = mydata.get('y')
            with kpi1:
                st.markdown('**X**')
                number1 = x
                st.markdown(f"<h1 style='text-align: center; color: red;'>{x}</h1>", unsafe_allow_html=True)

            with kpi2:
                st.markdown('**Y**')
                number2 = y
                st.markdown(f"<h1 style='text-align: center; color: red;'>{y}</h1>", unsafe_allow_html=True)


    
        time.sleep(1)

 

 
