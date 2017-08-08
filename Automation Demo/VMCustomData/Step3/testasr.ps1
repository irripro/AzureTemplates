#Install the Azure Module
Get-Module PowerShellGet -list | Select-Object Name,Version,Path
Install-PackageProvider -Name NuGet -Force
Install-Module AzureRM -Force
Import-Module AzureRM

#Login to Azure Subscription
$UserName = "a289cbdd-4fca-4a7d-88c4-6a02892223d4"
$Password = "2#Adam26185"
$SecurePassword = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $UserName, $SecurePassword
$tenant = "72f988bf-86f1-41af-91ab-2d7cd011db47"
Login-AzureRmAccount -Credential $Cred -ServicePrincipal -TenantId $tenant

#Get the vault creds
$Vault01 = Get-AzureRmRecoveryServicesVault -Name "asrvault"
$CredsPath = "C:\WindowsAzure\"
$Credsfilename = Get-AzureRmRecoveryServicesVaultSettingsFile -Backup -Vault $Vault01 -Path $CredsPath