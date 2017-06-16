<# Custom Script for Windows to install a file from Azure Storage using the staging folder created by the deployment script #>
param (
    [string]$artifactsLocation,
    [string]$artifactsLocationSasToken,
    [string]$folderName,
    [string]$fileToInstall
)

$source = $artifactsLocation + "\$folderName\$fileToInstall" + $artifactsLocationSasToken
$dest = "C:\WindowsAzure\$folderName"

wget http://aka.ms/unifiedinstaller_eus -OutFile "$dest\MicrosoftAzureSiteRecoveryUnifiedSetup.exe"

New-Item -Path $dest -ItemType directory
Invoke-WebRequest $source -OutFile "$dest\$fileToInstall"