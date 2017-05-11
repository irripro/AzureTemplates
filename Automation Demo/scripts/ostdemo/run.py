from __future__ import absolute_import, division, print_function, with_statement
import datetime, os, shutil
from azure.storage.blob import BlockBlobService
from azure.storage.file import FileService
from azure.storage.file import ContentSettings

#Create A TimeStamp for the directory
timestamp='{:%Y_%m_%d_%H_%M_%S}'.format(datetime.datetime.now())

#Current Working Directory
cwd = os.getcwd()

#Create Directory where blobs are going to be copied into
try:
    directorytocreate="%s\%s" %(cwd,timestamp)
    os.makedirs(directorytocreate)
    print("Directory '%s' has been created." %directorytocreate)
except:
    pass

#Storage Account info where the Blob is stored
BAccountName="function5b835eceb6db"
BAccountKey="fYwHa9NYaB9aQgcDOcPMYoA92i++5Ik/92oRmXleC4bZUOmnadRIaE/mwpCRPj1UWpw73opHjMpMo+Dgw5R8uw=="
mycontainer="osttest"

#Storage Account About the FileShare
FSAccountName="functionc134d59b8177"
FSAccountKey="74BVR5wyXbEZ7tpi10Rh36kytGbvXePtf/F2BR3SXM+9Pz/vlYuyD7HOVEChjuOFCsF3GpCrnnLRBzAQe9NiYQ=="
myshare="privateuploadedblobs"

#Create a FileShare Object to manipulate in this script
file_service = FileService(account_name=FSAccountName, account_key=FSAccountKey)

#Download and Delete the Blobs Uploaded
block_blob_service = BlockBlobService(account_name=BAccountName, account_key=BAccountKey)
generator = block_blob_service.list_blobs(mycontainer)
for blob in generator:
    try:
        block_blob_service.get_blob_to_path(mycontainer, blob.name,str("%s\%s" %(directorytocreate,blob.name)))
        block_blob_service.delete_blob(mycontainer, blob.name)
        file_service.create_file_from_path(
            myshare,
            None,
            str("%s_%s" %(timestamp,blob.name)),
            str("%s\%s" %(directorytocreate,blob.name)),
            content_settings=ContentSettings(content_type='image'))
    except: 
        continue

#Deletge Directory where blobs where copied
try:
    shutil.rmtree(directorytocreate)
except:
    pass
