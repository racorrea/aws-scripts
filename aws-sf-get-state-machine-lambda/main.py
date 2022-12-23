
from symtable import Function
import boto3
import json
import logging
import csv


print ('Init script ...')
print ('Processing, wait a moment ....')
session = boto3.Session(profile_name='produccion')
logger = logging.getLogger(__name__)

client = session.client('stepfunctions', region_name='us-east-1')
client_lambda = session.client('lambda', region_name='us-east-1')
path_file = '/Users/roddy.correa/Desktop/'
file_name = 'step-functions-details.csv'

response = client.list_state_machines()
state_machines = response['stateMachines']

fieldnames = ['NAME', 'TYPE', 'RESOURCE', 'FUNCTION_NAME', 'RUNTIME', 'MEMORY_SIZE', 'ARCHITECTURE']
row = list()
line = []
line_details=[]
counter = 0
for state_machine in state_machines:
    sm_name = state_machine['name']
    state_machine_describe = client.describe_state_machine(
        stateMachineArn = state_machine['stateMachineArn']
    )
    sm_name = state_machine_describe['name']
    definition = json.loads(state_machine_describe['definition'])
    states = definition['States']
    if (sm_name == "monitorFranchises" or sm_name == "stateExportsLogsS3" or sm_name == "test"):
        print('Not valid step: ' + sm_name)
    else:
        for item in states.items():
            step = item[1]
            sm_type = step['Type']
            
            if sm_type == "Task":
                if step['Resource'] == "arn:aws:states:::lambda:invoke":
                    for step_parameter in step.items():
                        parameter = item[1]
                        sm_resource = parameter['Parameters']['FunctionName']
                else:
                    sm_resource = step['Resource']
            else:
                sm_resource = ''

            if sm_resource != "":
                try:
                    function = client_lambda.get_function(
                        FunctionName=sm_resource
                    )
                    sm_function_name = function['Configuration']['FunctionName']
                    sm_runtime = function['Configuration']['Runtime']
                    sm_memory_size = function['Configuration']['MemorySize']
                    sm_architecture = function['Configuration']['Architectures'][0]
                except:
                    print ('Error en la función: ' + sm_resource)
            else:
                sm_function_name = ''
                sm_runtime = ''
                sm_memory_size = ''
                sm_architecture = ''

            line_details = [sm_name, sm_type, sm_resource, sm_function_name, sm_runtime, sm_memory_size, sm_architecture]
            row.append(line_details)
        
with open(path_file + file_name, 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row)

print ('End script ...')



