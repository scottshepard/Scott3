import boto3
import json
import os
import pandas as pd
import yaml

class Scott3:

    def __init__(self, aws_access_key_id, aws_secret_access_key, default_bucket):

        self.bucket = default_bucket
        self.client = boto3.client(
            's3', 
            aws_access_key_id = aws_access_key_id,
            aws_secret_access_key = aws_secret_access_key)

    def read_csv(self, s3_filename, bucket_name=None):
        if bucket_name is None:
            bucket_name=self.bucket
        self.client.download_file(bucket_name, s3_filename, 'df.csv')
        df = pd.read_csv('df.csv')
        os.remove('df.csv')
        return df

    def read_json(self, s3_filename, bucket_name=None):
        if bucket_name is None:
            bucket_name=self.bucket
        self.client.download_file(bucket_name, s3_filename, 'dict.json')
        with open('dict.json', 'r') as f:
            output_dict = json.load(f)
        os.remove('dict.json')
        return output_dict

    def write_csv(self, df, s3_filename, bucket_name=None):
        if bucket_name is None:
            bucket_name=self.bucket
        df.to_csv('df.csv', index=False)
        self.client.upload_file('df.csv', bucket_name, s3_filename)
        os.remove('df.csv')

    def write_json(self, dictionary, s3_filename, bucket_name=None):
        if bucket_name is None:
            bucket_name=self.bucket
        json_output = json.dumps(dictionary)
        with open('dict.json', 'w') as f:
            f.write(json_output)
        self.client.upload_file('dict.json', bucket_name, s3_filename)
        os.remove('dict.json')
