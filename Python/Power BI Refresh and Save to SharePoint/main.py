import requests
from requests.auth import HTTPBasicAuth
import shutil
import os

# Power BI API details
power_bi_api_url = "https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/refreshes"
power_bi_access_token = "your_power_bi_access_token"

# SharePoint API details
sharepoint_url = "https://your-sharepoint-site.sharepoint.com/sites/your-site"
sharepoint_folder_path = "/Shared Documents/YourFolder"
sharepoint_username = "your_sharepoint_username"
sharepoint_password = "your_sharepoint_password"

# Local Power BI file path
local_power_bi_file_path = "path/to/your/PowerBIFile.pbix"

def refresh_power_bi():
    # Trigger Power BI refresh
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {power_bi_access_token}"
    }
    response = requests.post(power_bi_api_url, headers=headers)
    
    if response.status_code == 202:
        print("Power BI refresh triggered successfully.")
    else:
        print(f"Failed to trigger Power BI refresh. Status code: {response.status_code}")
        print(response.text)

def upload_to_sharepoint(file_path):
    # SharePoint API upload URL
    upload_url = f"{sharepoint_url}/_api/web/getfolderbyserverrelativeurl('{sharepoint_folder_path}')/files/add(url='{os.path.basename(file_path)}',overwrite=true)"

    # SharePoint authentication
    auth = HTTPBasicAuth(sharepoint_username, sharepoint_password)

    # Upload file to SharePoint
    with open(file_path, 'rb') as file:
        response = requests.post(upload_url, auth=auth, files={'file': file})
    
    if response.status_code == 200:
        print("File uploaded to SharePoint successfully.")
    else:
        print(f"Failed to upload file to SharePoint. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Step 1: Refresh Power BI
    refresh_power_bi()

    # Step 2: Upload the refreshed Power BI file to SharePoint
    upload_to_sharepoint(local_power_bi_file_path)