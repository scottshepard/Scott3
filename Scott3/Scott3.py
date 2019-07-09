import boto3
import json
import os
import pandas as pd
import yaml

class Scott3:

    def __init__(self, config_file = '../config.yml'):
        self.credentials = self.load_credentials(config_file)
        self.bucket = self.credentials['aws']['bucket']
        self.client = boto3.client(
            's3', 
            aws_access_key_id = self.credentials['aws']['access_key'],
            aws_secret_access_key = self.credentials['aws']['secret'])

    def load_credentials(self, config_file):
        # Read YAML file
        with open(config_file, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        return data_loaded

    def read_csv(self, s3_filename, bucket_name=None):
        if bucket_name is None:
            bucket_name=self.bucket
        self.client.download_file(bucket_name, s3_filename, 'df.csv')
        return pd.read_csv('df.csv')

    def read_json(self, s3_filename, bucket_name=None):
        if bucket_name is None:
            bucket_name=self.bucket
        self.client.download_file(bucket_name, s3_filename, 'dict.json')
        with open('dict.json', 'r') as f:
            output_dict = json.load(f)
        return output_dict

    def write_csv(self, df, s3_filename, bucket_name=None):
        if bucket_name is None:
            bucket_name=self.bucket
        df.to_csv('df.csv', index=False)
        self.client.upload_file('df.csv', bucket_name, s3_filename)

    def write_json(self, dictionary, s3_filename, bucket_name=None):
        if bucket_name is None:
            bucket_name=self.bucket
        json_output = json.dumps(dictionary)
        with open('dict.json', 'w') as f:
            f.write(json_output)
        self.client.upload_file('dict.json', bucket_name, s3_filename)
