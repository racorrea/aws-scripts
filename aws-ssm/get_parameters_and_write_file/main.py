# Permite recuperar todas las variables ssm de una cuenta por path y escribir un archivo
import boto3
import os
import time
import json
from dotenv import load_dotenv
from progress.bar import Bar

load_dotenv()

session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN')
)

client = session.client('ssm', region_name=os.getenv('AWS_REGION_CODE'))

paginator = client.get_paginator('get_parameters_by_path')

response_iterator = paginator.paginate(
    Path=os.getenv('SSM_PATH_PARAMETERS')
)

parameters=[]

with Bar('Processing...', fill='#', suffix='%(percent)d%%') as bar:
    for page in response_iterator:
        for entry in page['Parameters']:
            parameters.append(entry)
            time.sleep(0.02)
            bar.next()  
        
json_object = json.dumps(parameters, indent=4, default=str)

with open(os.getenv('FILE_NAME') + ".json", "w") as outfile:
    outfile.write(json_object)
    
time.sleep(0.5)

print('Finish processing ...')




