import winrm

def getasrinstaller():
    #C:\WindowsAzure\MicrosoftAzureSiteRecoveryUnifiedSetup.exe /q /x:C:\WindowsAzure\Extracted
    ps_script = """wget http://aka.ms/unifiedinstaller_eus -OutFile "C:\WindowsAzure\MicrosoftAzureSiteRecoveryUnifiedSetup.exe" 
    """
    s = winrm.Session('{asrpublicip}', auth=('alihhussain', 'asrdemo@teamcim123'))
    r = s.run_ps(ps_script)

def setupnewpowershell():
    ps_scripttwo = """Get-Module PowerShellGet -list | Select-Object Name,Version,Path
    Install-PackageProvider -Name NuGet -Force
    Install-Module AzureRM -Force
    Import-Module AzureRM
    """
    s = winrm.Session('{asrpublicip}', auth=('alihhussain', 'asrdemo@teamcim123'))
    r = s.run_ps(ps_scripttwo)
    print("The standard output is: %s" %r.std_out)

def get_asr_cred():
    ps_scriptthree = """
    """
    s = winrm.Session('{asrpublicip}', auth=('alihhussain', 'asrdemo@teamcim123'))
    r = s.run_ps(ps_scriptthree)
    print("The standard output is: %s" %r.std_out)
    print("The standard error is: %s" %r.std_err)

getasrinstaller()
setupnewpowershell()