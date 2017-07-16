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
$Credsfilename = Get-AzureRmRecoveryServicesVaultSettingsFile -Backup -Vault $Vault01 -Path $CredsPath