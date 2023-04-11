#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
# Authenticate user to access Google Drive
from google.colab import auth                  # Imports the auth module from google.colab library
auth.authenticate_user()                       # Authenticates the user to access Google APIs
from google.colab import drive                 # Imports the drive module from google.colab library
drive.mount('/content/drive')                  # Mounts the Google Drive to the current runtime environment


from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import io

file_id = '1UnA5RjwMlYqyxn_n6rGpABbuzGCKxLUvYbOmZwFRryI'   #https://docs.google.com/document/d/1UnA5RjwMlYqyxn_n6rGpABbuzGCKxLUvYbOmZwFRryI/edit?usp=sharing

# Authenticate and construct the service object
drive_service = build('drive', 'v3')
doc = drive_service.files().get(fileId=file_id).execute()
doc_content = drive_service.files().export(fileId=file_id, mimeType='text/plain').execute()
content = doc_content.decode('utf-8')


# Create a new text file and write the content to it
with open('text1.txt', 'w') as f:
    f.write(content)




file_id = '1C3dGzGTmv3urH918GRQ0Nyw2ADWKOlxnHFqtOSN3wzk'   #https://docs.google.com/document/d/1C3dGzGTmv3urH918GRQ0Nyw2ADWKOlxnHFqtOSN3wzk/edit?usp=share_link

# Authenticate and construct the service object
drive_service = build('drive', 'v3')
doc = drive_service.files().get(fileId=file_id).execute()
doc_content = drive_service.files().export(fileId=file_id, mimeType='text/plain').execute()
content = doc_content.decode('utf-8')


# Create a new text file and write the content to it
with open('text2.txt', 'w') as f:
    f.write(content)

