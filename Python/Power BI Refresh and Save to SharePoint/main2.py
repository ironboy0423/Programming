import subprocess
import shutil
import os
import time

# Local Power BI file path
local_power_bi_file_path = "path/to/your/PowerBIFile.pbix"

# SharePoint folder path
sharepoint_folder_path = "path/to/your/SharePoint/Folder"

def refresh_power_bi(local_file_path):
    # Replace with the path to your Power BI Desktop executable
    power_bi_desktop_executable = r"C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe"

    # Build the command to refresh Power BI
    command = [power_bi_desktop_executable, "--noSplash", "--no-lab", "--refresh", local_file_path]

    # Run the Power BI Desktop executable with the refresh command
    subprocess.run(command, check=True)

def upload_to_sharepoint(local_file_path, sharepoint_folder):
    # Copy the refreshed Power BI file to SharePoint folder
    file_name = os.path.basename(local_file_path)
    destination_path = os.path.join(sharepoint_folder, file_name)
    shutil.copyfile(local_file_path, destination_path)
    print(f"File copied to SharePoint: {destination_path}")

if __name__ == "__main__":
    # Step 1: Refresh Power BI locally
    refresh_power_bi(local_power_bi_file_path)

    # Allow some time for the refresh to complete before copying the file
    time.sleep(10)  # Adjust the sleep duration based on your dataset's refresh time

    # Step 2: Upload the refreshed Power BI file to SharePoint
    upload_to_sharepoint(local_power_bi_file_path, sharepoint_folder_path)
