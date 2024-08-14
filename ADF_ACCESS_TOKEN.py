import requests
# Replace these variables with your actual values
tenant_id = ""
client_id = ""
client_secret = ""
scope = "https://management.azure.com/.default" # This is the scope 
for Azure Management API
# Azure AD Token endpoint for OAuth2
token_url = 
f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
# Prepare the data for the token request
data = {
 'grant_type': 'client_credentials',
 'client_id': client_id,
 'client_secret': client_secret,
 'scope': scope
}
# Make the request to get the token
response = requests.post(token_url, data=data)
# Parse the JSON response to extract the access token
token = response.json().get('access_token')
if token:
 print(f"ADF_ACCESS_TOKEN: {token}")
else:
 print("Failed to obtain access token.")
 print(response.json())
