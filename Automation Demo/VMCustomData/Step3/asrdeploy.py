import winrm
#C:\WindowsAzure\MicrosoftAzureSiteRecoveryUnifiedSetup.exe /q /x:C:\WindowsAzure\Extracted
ps_script = """wget http://aka.ms/unifiedinstaller_eus -OutFile "C:\WindowsAzure\MicrosoftAzureSiteRecoveryUnifiedSetup.exe" 
"""
s = winrm.Session('{asrpublicip}', auth=('alihhussain', 'asrdemo@teamcim123'))
r = s.run_ps(ps_script)

ps_scripttwo = """Get-Module PowerShellGet -list | Select-Object Name,Version,Path
Install-PackageProvider -Name NuGet -Force
Install-Module AzureRM -Force
Import-Module AzureRM
"""
r = s.run_ps(ps_scripttwo)
print("The standard output is: %s" %r.std_out)

ps_scriptthree = """wget https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/Automation%20Demo/VMCustomData/Step3/asr_cred_dl.ps1 -OutFile "C:\WindowsAzure\asr_cred_dl.ps1"
"""

r = s.run_ps(ps_scriptthree)
print("The standard output is: %s" %r.std_out)
print("The standard error is: %s" %r.std_err)