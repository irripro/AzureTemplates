import winrm

ps_script = """wget http://aka.ms/unifiedinstaller_eus -OutFile "C:\WindowsAzure\MicrosoftAzureSiteRecoveryUnifiedSetup.exe" 
C:\WindowsAzure\MicrosoftAzureSiteRecoveryUnifiedSetup.exe /q /x:C:\WindowsAzure\Extracted
"""
s = winrm.Session('{asrpublicip}', auth=('alihhussain', 'asrdemo@teamcim123'))
r = s.run_ps(ps_script)

ps_scripttwo = """Get-Module PowerShellGet -list | Select-Object Name,Version,Path
Install-PackageProvider -Name NuGet -Force
Install-Module AzureRM -Force
Import-Module AzureRM
"""
r = s.run_ps(ps_scripttwo)
print("The standard error is: %s" %r.std_out)

ps_scriptthree = """
#Login to Azure Subscription
$UserName = "{appid}"
$Password = "{passwd}"
$SecurePassword = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $UserName, $SecurePassword
$tenant = "{tenant}"
Login-AzureRmAccount -Credential $Cred -ServicePrincipal -TenantId $tenant

#Get the vault creds
$Vault01 = Get-AzureRmRecoveryServicesVault -Name "asrvault"
$CredsPath = "C:\WindowsAzure\"
$Credsfilename = Get-AzureRmRecoveryServicesVaultSettingsFile -Backup -Vault $Vault01 -Path $CredsPath
"""