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