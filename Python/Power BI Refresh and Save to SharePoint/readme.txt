To use the Power BI API, you need to register your application in the Azure portal and obtain the necessary credentials. Here are the general steps to get the Power BI API URL and access token:

Step 1: Register your application in Azure portal
Go to the Azure portal.
Navigate to the "Azure Active Directory" service.
Select "App registrations" and click on "New registration."
Fill in the required information, such as the name and supported account types.
After registration, note down the "Application (client) ID" and "Directory (tenant) ID" from the application overview page.
Step 2: Configure API permissions
In the application overview page, go to the "API permissions" tab.
Click on "Add a permission" and select "APIs my organization uses."
Search for "Power BI Service" and select it.
Choose the required permissions, such as Dataset - Dataset (workspace) or others based on your needs.
Click on "Add permissions."
Step 3: Generate client secret
In the application overview page, go to the "Certificates & Secrets" tab.
In the "Client secrets" section, click on "New client secret."
Note down the generated secret value. This secret will only be displayed once, so make sure to save it securely.
Step 4: Get Power BI API URL
Step 5: Obtain Access Token