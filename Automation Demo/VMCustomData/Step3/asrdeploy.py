import winrm

ps_script = """wget http://aka.ms/unifiedinstaller_eus -OutFile "C:\WindowsAzure\MicrosoftAzureSiteRecoveryUnifiedSetup.exe" """
s = winrm.Session('{asrpublicip}', auth=('alihhussain', 'asrdemo@teamcim123'))

r = s.run_ps(ps_script)

print("The standard error is: %s" %r.std_err)