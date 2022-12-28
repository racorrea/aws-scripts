import csv
import math
import boto3



INIT_TIME = 1672232400 #2022-10-28 0h 0m 0s
END_TIME = 1672239080 #2022-12-28 0h 0m 0s

lambdas = ['usrv-billing-primary-verifyFinishStep',
'usrv-reports-primary-buildBatchFile',
'usrv-reports-primary-buildFile',
'usrv-payouts-transfer-primary-processTransactionDavivienda',
'usrv-transfer-subscriptions-primary-sqsCharges',
'usrv-reseller-core-primary-verifyMassiveCertificate',
'usrv-reseller-core-primary-refundMassiveCertificate',
'usrv-reseller-core-primary-sendMailMassiveCertificate',
'usrv-reseller-core-primary-massiveDataRaw',
'usrv-cash-processor-primary-updatePayvalidaStatus',
'usrv-payouts-transfer-primary-processTransaction',
'usrv-subscriptions-primary-enqueueDailySubs',
'usrv-subscriptions-primary-enqueueWeeklySubs',
'usrv-subscriptions-primary-enqueueBiweeklySubs',
'usrv-subscriptions-primary-enqueueThreeFortnightsSubs',
'usrv-subscriptions-primary-enqueueYearlySubs',
'usrv-subscriptions-primary-enqueueMQHSubs',
'usrv-subscriptions-primary-enqueueRetries',
'usrv-transfer-subscriptions-primary-processBiweeklySubsFile',
'usrv-transfer-subscriptions-primary-processMQHSubsFile',
'usrv-transfer-subscriptions-primary-processWeeklySubsFile',
'usrv-transfer-subscriptions-primary-processYearlySubsFile',
'usrv-card-reports-primary-notifyJobError',
'usrv-card-reports-primary-validateBounceStep',
'usrv-itierra-primary-commit',
'usrv-itierra-primary-checkCertificateStatus',
'usrv-itierra-primary-getRawData',
'usrv-itierra-primary-updateChanges',
'usrv-billing-reports-primary-getTransactionFromLedger',
'usrv-billing-reports-primary-downloadFileLedgerDetail',
'usrv-compliance-payouts-primary-getMerchantData',
'usrv-compliance-payouts-primary-convertCurrency',
'usrv-compliance-payouts-primary-getTransactionsRisk',
'usrv-compliance-payouts-primary-generateBeneficiarySum',
'usrv-compliance-payouts-primary-validateRefinitiv',
'usrv-compliance-payouts-primary-validateRefinitivResolution',
'usrv-compliance-payouts-primary-saveTransactionsPayoutCl',
'usrv-payouts-transfer-primary-splitTransactionFileBancoChile',
'usrv-payouts-transfer-primary-finalizeDispersionProcess',
'usrv-reseller-core-primary-stepStartDocumentAnalysis',
'usrv-reseller-core-primary-stepGetJobStatus',
'usrv-reseller-core-primary-stepFetchBlocks',
'usrv-reseller-core-primary-stepMergeBlocks',
'usrv-reseller-core-primary-stepSortData',
'usrv-reseller-core-primary-stepFailedDataSort',
'usrv-reseller-core-primary-stepSuccededDataSort',
'usrv-reseller-core-primary-stepFailedJob',
'usrv-payouts-transfer-banco-chile-primary-splitValidationFile',
'usrv-payouts-transfer-banco-chile-primary-notifyFileVnProcess',
'usrv-acq-bins-primary-launchRangesJob',
'usrv-acq-bins-primary-checkRangesJobStatus',
'usrv-acq-bins-primary-handleRangesJobFail',
'usrv-acq-regulatory-primary-launchMCRegulatory',
'usrv-acq-regulatory-primary-checkMCJobStatus',
'usrv-acq-regulatory-primary-buildMCRegulatory',
'usrv-acq-regulatory-primary-handleMcJobFail',
'usrv-acq-regulatory-primary-launchVisaRegulatory',
'usrv-acq-regulatory-primary-checkVisaJobStatus',
'usrv-acq-regulatory-primary-buildVisaRegulatory',
'usrv-acq-regulatory-primary-handleJobFail',
'usrv-billing-merchant-reseller-primary-activeMerchantsByFrequecy',
'usrv-billing-merchant-reseller-primary-saveBillingRecords',
'usrv-billing-merchant-reseller-primary-processInvoice',
'usrv-reseller-batch-primary-processFailedTransaction',
'usrv-reseller-batch-primary-generateFailedFile',
'usrv-reseller-batch-primary-processSuccessfulTransaction',
'usrv-reseller-batch-primary-processSuccessfulCalculate',
'usrv-reseller-batch-primary-refundMassiveCertificate',
'usrv-reseller-batch-primary-sendMailMassiveCertificate',
'usrv-kushki-ci-primary-runIntegrationTests',
'usrv-plugins-primary-triggerShopifyRetry',
'usrv-plugins-primary-saveData',
'usrv-retentions-primary-downloadRetentionReceiptCo',
'usrv-retentions-primary-saveRetentionReceiptCo',
'usrv-subscriptions-primary-migrateAllSubscriptions',
'usrv-transaction-rates-primary-discountsStep',
'usrv-transaction-rates-primary-minComisionalStep',
'usrv-transaction-rates-primary-updateHierarchyConfigDiscountStep',
'usrv-transaction-rates-primary-discountsCallbackStep',
'usrv-transaction-rates-primary-undoHierarchyConfigDiscountStep',
'usrv-transaction-rates-primary-configRatesStep',
'usrv-transaction-rates-primary-updateHierarchyConfigStep',
'usrv-transaction-rates-primary-undoHierarchyConfigStep',
'usrv-transaction-rates-primary-ratesCallbackStep',
'dynamo-mongo-sync-getTables']

list = []
mesagge=''
memory_size = ''
max_memory_used=''
path_file = '/Users/roddy.correa/Desktop/'
file_name = 'logs-details.csv'

session = boto3.Session(profile_name='produccion')
client = session.client('logs', region_name='us-east-1')

query = f"fields @timestamp, @message, @memorySize, @maxMemoryUsed" \
        f"| sort @timestamp desc" \
        f"| filter @message like \"REPORT RequestId\"" \
        f"| limit 1"

def get_query(query, client, init_time, end_time, log_group):
    start_query_response = client.start_query(
        logGroupName=log_group,
        startTime=math.trunc(init_time * 1000),
        endTime=math.trunc(end_time * 1000),
        queryString=query
    )
    query_id = start_query_response['queryId']
    response = None
    #print(
    #    f'query from {math.trunc(init_time * 1000)} to {math.trunc(end_time * 1000)}')

    while response is None or response['status'] == 'Running':
        #print('Consultando')
        response = client.get_query_results(
            queryId=query_id
        )
    return response

def main():
    for lambda_item in lambdas:
        print ("Consultando para " + lambda_item)
        log_group = f"/aws/lambda/{lambda_item}"
        print ('LOG GROUP: ' + log_group)
        response = get_query(query, client, INIT_TIME, END_TIME, log_group)
        #print (' ### Tamaño de la lista: ' + str(len(response['results'])))
        if(len(response['results']) > 0):
            for result in response['results']:

                for data in result:
                    #print ('*************\n')
                    if(data['field'] == '@message') : 
                        #print ('DATA:' + data['field'] + ' => ' + data['value'])
                        message = data['value']  
                        x = message.split()
                        memory_size = (x[10] + x[11] + x[12] + x[13])
                        max_memory_used = (x[14] + x[15] + x[16] + x[17] + x[18])
                item = [lambda_item + '; ' + message.rstrip() + '; ' + memory_size+ '; ' + max_memory_used]
                print (lambda_item + ' | ' + message.rstrip() + '\n')
                memory_size = ''
                max_memory_used = ''
                list.append(item)
                
        else:
            print('*** LOG GROUP: ' + log_group + ' No contain results ***')
        
        print ('------------------------\n')
    #print(list)

    with open(path_file + file_name, 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(list)


main()








    
