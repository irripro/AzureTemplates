#Login to Azure Subscription (CSP)
$UserName = "e9bd41cb-da37-4ed1-a978-5871d04e742b"
$Password = "2#Adam26185"
$SecurePassword = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $UserName, $SecurePassword
$tenant = "772a2751-8bb4-4823-957f-4e6bd5d70f45"
Login-AzureRmAccount -Credential $Cred -ServicePrincipal -TenantId $tenant
Get-AzureRmResourceProvider -ListAvailable > C:\Users\alhussai\Documents\Microsoft\AvailableList\CSPList.txt
 
#Login to Azure Subscription (EA)
$UserName = "a289cbdd-4fca-4a7d-88c4-6a02892223d4"
$Password = "2#Adam26185"
$SecurePassword = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $UserName, $SecurePassword
$tenant = "72f988bf-86f1-41af-91ab-2d7cd011db47"
Login-AzureRmAccount -Credential $Cred -ServicePrincipal -TenantId $tenant
#Get-AzureRmResourceProvider -ListAvailable > C:\Users\alhussai\Documents\Microsoft\AvailableList\EAList.txt

$vault = Get-AzureRmRecoveryServicesVault -Name asrvault -ResourceGroupName ExampleGroup
$VaultSet = Set-AzureRmSiteRecoveryVaultSettings -ARSVault $Vault
Get-AzureRmSiteRecoveryPolicy -Name testing
Get-AzureRmSiteRecoveryFabric

$ResourceGroup = "Group"
$StorageAccountName = "asrstorageexample9"
$StorageAccountGeo  = "eastus"

$asrstorageobject = New-AzureRmStorageAccount -Location $StorageAccountGeo -Name $StorageAccountName -ResourceGroupName $ResourceGroup -SkuName "Standard_LRS"
Write-Host ($asrstorageobject | Format-List | Out-String)
Write-Host ($asrstorageobject.Sku | Format-List | Out-String)

$ProfileResult = New-AzureSiteRecoveryProtectionProfileObject -RecoveryAzureStorageAccount $StorageAccountName -RecoveryAzureSubscription "e729c299-db43-40ce-991a-7e4572a69d50" -ReplicationFrequencyInSeconds 300 -ReplicationProvider HyperVReplica -AllowReplicaDeletion -Force -RecoveryPoints 2

$clientSecret = 's0WML8mfs9GmDzSzC/k0R9huau2AOIqNu8w/0ZqFe7E='
$clientSecretSecure = $clientSecret | ConvertTo-SecureString -AsPlainText -Force

# Add-PCAuthentication -cspappID '74d333f7-1349-4423-8ef5-27643bc4bf28' -cspDomain 'testtestcsp1twwp1.onmicrosoft.com' -cspClientSecret $clientSecretSecure
Add-PCAuthentication -cspappID '5518c52c-d005-4a5b-aaf9-f4420bf9717b' -cspDomain 'testtestcsp1twwp1.onmicrosoft.com' -cspClientSecret $clientSecretSecure