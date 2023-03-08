# Permite recuperar todas las variables ssm de una cuenta por path y llevarlas a otra cuenta
# get-parameters-by-path
# put_parameters


import boto3


print ('Init script ...')
print ('Processing, wait a moment ....')
session = boto3.Session(profile_name='uat')
client = session.client('ssm', region_name='us-east-1')

paginator = client.get_paginator('get_parameters_by_path')

response_iterator = paginator.paginate(
    Path='/qa/usrv-card/'
)

parameters=[]

for page in response_iterator:
    for entry in page['Parameters']:
        parameters.append(entry)

print ('Login architecture profile ...')
print ('Processing, wait a moment ....')


session_architecture = boto3.Session(profile_name='architecture')
client_architecture = session_architecture.client('ssm', region_name='us-east-1')

for parameter in parameters:
    print('NAME: ' + parameter['Name'])
    print('VALUE: ' + parameter['Value'])
    print('TYPE: ' + parameter['Type'])
    response = client_architecture.put_parameter(
        Name=parameter['Name'],
        Value=parameter['Value'],
        Type=parameter['Type'],
        Overwrite=True,
        Tier='Standard',
    )
    print("-----------------")


