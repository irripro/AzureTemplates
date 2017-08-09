#Install the Azure Module
Get-Module PowerShellGet -list | Select-Object Name,Version,Path
Install-PackageProvider -Name NuGet -Force
Install-Module AzureRM -Force
Import-Module AzureRM

#Login to Azure Subscription
$UserName = "{appid}"
$Password = "2#Adam26185"
$SecurePassword = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $UserName, $SecurePassword
$tenant = "{tenant}"
Login-AzureRmAccount -Credential $Cred -ServicePrincipal -TenantId $tenant

#Get the vault creds
$Vault01 = Get-AzureRmRecoveryServicesVault -Name "asrvault"
$CredsPath = "C:\WindowsAzure\"
$Credsfilename = Get-AzureRmRecoveryServicesVaultSettingsFile -SiteRecovery -Vault $Vault01 -Path $CredsPath
wget http://aka.ms/unifiedinstaller_eus -OutFile "C:\WindowsAzure\MicrosoftAzureSiteRecoveryUnifiedSetup.exe" 