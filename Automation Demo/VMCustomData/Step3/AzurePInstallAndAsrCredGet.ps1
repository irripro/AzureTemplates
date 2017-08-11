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

mkdir "C:\ASR\"
mkdir "C:\ASR\asrcredfolder\"
pushd "C:\ASR\"

#Get the vault creds
$Vault01 = Get-AzureRmRecoveryServicesVault -Name "asrvault"
$CredsPath = "C:\ASR\asrcredfolder\"
$Credsfilename = Get-AzureRmRecoveryServicesVaultSettingsFile -SiteRecovery -Vault $Vault01 -Path $CredsPath

wget http://aka.ms/unifiedinstaller_eus -OutFile "C:\ASR\MicrosoftAzureSiteRecoveryUnifiedSetup.exe" 
wget https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/Automation%20Demo/VMCustomData/Step3/sql.cred -OutFile "C:\ASR\sql.cred" 
C:\ASR\MicrosoftAzureSiteRecoveryUnifiedSetup.exe /x:. /q
mkdir "C:\ASR\Installation"
cd "C:\ASR\Installation"
wget https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/Automation%20Demo/VMCustomData/Step3/passphrase.txt -OutFile "C:\ASR\Installation\passphrase.txt"