#!/bin/bash 

export AWS_PROFILE=architecture

ENVIRONMENT="qa"
USRV_NAME="usrv-payment-credentials"

export AWS_REGION="us-east-1"
echo $AWS_REGION

aws ssm put-parameter --name "/GL/CONSOLE_DOMAIN" \
                      --type "String" \
                      --value "console.kushkipagos.com" \
                      --tier "Standard" \
                      --overwrite
aws ssm put-parameter --name "/GL/ACCOUNT_DETAILS" \
                      --type "String" \
                      --value "{\"accountid\":\"453027466500\",\"accountname\":\"dev\",\"region\":\"us-east-1\",\"accountdomain\":\"com\",\"dynamoParameters\":\"arn:aws:dynamodb:us-east-1:412465614222:table/usrv-parameters-manager-qa-parameters\"}" \
                      --tier "Standard" \
                      --overwrite
aws ssm put-parameter --name "/GL/ACCOUNT_NAME" \
                      --type "String" \
                      --value "dev" \
                      --tier "Standard" \
                      --overwrite
                      
