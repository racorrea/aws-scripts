#!/bin/bash 

export AWS_PROFILE=architecture

ENVIRONMENT="qa"
USRV_NAME="usrv-payment-credentials"

export AWS_REGION="us-east-1"
echo $AWS_REGION

##########################################################
######                                              ######
######              GLOBAL VARIABLES                ######
######                                              ######
##########################################################


# aws ssm put-parameter --name "/GL/CONSOLE_DOMAIN" \
#                       --type "String" \
#                       --value "console.kushkipagos.com" \
#                       --tier "Standard" \
#                       --overwrite
# aws ssm put-parameter --name "/GL/ACCOUNT_DETAILS" \
#                       --type "String" \
#                       --value "{\"accountid\":\"453027466500\",\"accountname\":\"dev\",\"region\":\"us-east-1\",\"accountdomain\":\"com\",\"dynamoParameters\":\"arn:aws:dynamodb:us-east-1:412465614222:table/usrv-parameters-manager-qa-parameters\"}" \
#                       --tier "Standard" \
#                       --overwrite
# aws ssm put-parameter --name "/GL/ACCOUNT_NAME" \
#                       --type "String" \
#                       --value "dev" \
#                       --tier "Standard" \
#                       --overwrite
                      



aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/BASE_PATH" \
                      --type "String" \
                      --value "payment-credentials" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/BASIC_AUTH_PASS" \
                      --type "String" \
                      --value "YCN3gyz7bhy4zrp.gpy" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/BASIC_AUTH_USER" \
                      --type "String" \
                      --value "microservices" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/BUILD_VARIABLES" \
                      --type "String" \
                      --value "{\"rollbarToken\":\"468f829fbd84481281c28464ac44d182\",\"runscopeSuiteTest\":\"6d2d6b2b-6ef7-45f4-9bac-44a6d0f70531\",\"runscopeEnv\":\"39d07e1c-000d-4cae-9b2b-b63c72b896e7\",\"distributionArray\":\"\",\"ecrUri\":\"\",\"multiRegion\":\"\"}" \
                      --tier "Standard" \
                      --overwrite

# aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/MERCHANT_ARN" \
#                       --type "String" \
#                       --value "arn:aws:dynamodb:us-east-1:412465614222:table/qa-kushki-usrv-merchant-merchants/stream/2020-02-28T21:35:19.597" \
#                       --tier "Standard" \
#                       --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/MERCHANT_DELETE_EVENT_BUS_ARN" \
                      --type "String" \
                      --value "arn:aws:events:us-east-1:412465614222:event-bus/qa-merchants" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/RUNSCOPE_ENV" \
                      --type "String" \
                      --value "39d07e1c-000d-4cae-9b2b-b63c72b896e7" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/RUNSCOPE_SUITE_TEST" \
                      --type "String" \
                      --value "6d2d6b2b-6ef7-45f4-9bac-44a6d0f70531" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/SLS_BUILD" \
                      --type "String" \
                      --value "kushkipagos.com,usrv-authorizer-qa-authorizerAdmin,us-east-1_9FDXFZaVS,usrv-payment-credentials-qa-privateMasterCredential,usrv-payment-credentials-qa-privateCredential," \
                      --tier "Standard" \
                      --overwrite


aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/VPC_SG" \
                      --type "String" \
                      --value "vpc-07bc8ba7649236b65" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/VPC_SUBNET1" \
                      --type "String" \
                      --value "subnet-0458f44b2f82fbb8e" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/VPC_SUBNET2" \
                      --type "String" \
                      --value "subnet-0ef42cf7b94709f18" \
                      --tier "Standard" \
                      --overwrite


aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/ROLLBAR_TOKEN" \
                      --type "String" \
                      --value "468f829fbd84481281c28464ac44d182" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/DOMAIN" \
                      --type "String" \
                      --value "api-qa.arquitectura.click" \
                      --tier "Standard" \
                      --overwrite

aws ssm put-parameter --name "/$ENVIRONMENT/$USRV_NAME/ELASTIC_HOST" \
                      --type "String" \
                      --value "https://search-leonardo-srucwxil2tmzf4ga7jmjx6okbe.us-east-1.es.amazonaws.com" \
                      --tier "Standard" \
                      --overwrite






