Introduction

This project is about building a Chat GPT chatbot that can be trained on custom data. This chatbot can be integrated with Google Sheets to automatically update the chatbot with the latest information. The following instructions provide an overview of how to set up the project and use it.

Installation
This project requires the following libraries to be installed:

google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
llama-index
langchain
To install these libraries, run the following command in your command prompt or terminal:
!pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client llama-index langchain

Instructions
Set up Google Sheets Integration
In order to use Google Sheets to update the chatbot data, you need to follow the below steps:
Authenticate user to access Google Drive:

javascript

from google.colab import auth

auth.authenticate_user()

from google.colab import drive

drive.mount('/content/drive')

Set up the Google Sheet to be accessed by the chatbot
Get the file ID of the Google Sheet and replace the file_id variable in the code with it.
Run the code to access the Google Sheet and save it as a text file.


Train the Chatbot

Create two text files containing the training data. You can either use the text files generated from the Google Sheet or create them manually.

Create a new Python file and copy the code from my_module.py and training.py

Replace the directory_path parameter with the path to the directory containing the text files.

Run the construct_index() function to train the chatbot and save it to disk.
Use the Chatbot
Load the chatbot from disk using the following code:
java

from llama_index import GPTSimpleVectorIndex

index = GPTSimpleVectorIndex.load_from_disk('index.json')

Use the index object to generate responses to user queries.

Conclusion
This project provides an easy way to build a Chat GPT chatbot that can be trained on custom data and integrated with Google Sheets. By following the above instructions, you can build your own chatbot and customize it to suit your needs.
