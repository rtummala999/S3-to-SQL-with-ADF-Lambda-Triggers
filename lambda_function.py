import json
import urllib3
import os
import requests
def lambda_handler(event, context):
 object_key = event['Records'][0]['s3']['object']['key']
 tenant_id = ""
 client_id = ""
 client_secret = ""
 resource_group = ""
 adf_factory_name = ""
 adf_pipeline_name = ""
 adf_url = (
 f"https://management.azure.com/subscriptions/<sub-id>/"
 f"resourceGroups/{resource_group}/"
 
f"providers/Microsoft.DataFactory/factories/{adf_factory_name}/"
 f"pipelines/{adf_pipeline_name}/createRun?api-version=2018-
06-01"
 )
 data = {"sourceFileName": object_key}
 headers = {
 'Content-Type': 'application/json',
 'Authorization': f'Bearer {os.getenv("ADF_ACCESS_TOKEN")}'
 }
 try:
 # Enable SSL verification (default behavior)
 response = requests.post(adf_url, json=data, headers=headers)
 if response.status_code == 200:
 print(f"Successfully triggered ADF pipeline: 
{response.text}")
 else:
 print(f"Failed to trigger ADF pipeline: 
{response.status_code}")
 except Exception as e:
 print(f"Error triggering ADF pipeline: {str(e)}")
