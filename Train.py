#!/usr/bin/env python
# coding: utf-8

# In[ ]:




os.environ["OPENAI_API_KEY"] = input("Paste your OpenAI key here and hit enter:") # This makes the API key available to the OpenAI class from the langchain library, which is used to initialize the GPT-3 language model.
#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

# Create a SimpleDirectoryReader object and load data from the 'data' directory
documents = SimpleDirectoryReader('data').load_data()

# Read the text content of 'text1.txt' and 'text2.txt'
with open('text1.txt', 'r') as f:
    text1 = f.read()

with open('text2.txt', 'r') as f:
    text2 = f.read()

# Create a list of text documents from the read texts
text_list = [text1, text2]
documents = [Document(t) for t in text_list]

# Create a SimpleNodeParser object
parser = SimpleNodeParser()

# Get nodes from the specified documents using the SimpleNodeParser object
nodes = parser.get_nodes_from_documents(documents)

# Create two new nodes with  text and IDs
node1 = Node(text="<text_chunk>", doc_id="<node_id>")
node2 = Node(text="<text_chunk>", doc_id="<node_id>")

# Set relationships between the two nodes
node1.relationships[DocumentRelationship.NEXT] = node2.get_doc_id()
node2.relationships[DocumentRelationship.PREVIOUS] = node1.get_doc_id()

# Create a new GPTSimpleVectorIndex object from the specified documents
index = GPTSimpleVectorIndex.from_documents(documents)

# Create a new GPTSimpleVectorIndex object from the specified nodes
index = GPTSimpleVectorIndex(nodes)

# Create a new empty GPTSimpleVectorIndex object
index = GPTSimpleVectorIndex([])

# Insert each document in the 'documents' list into the empty index
for doc in documents:
    index.insert(doc)


# create directory to hold all data
if not os.path.exists('construct_data'):
    os.makedirs('construct_data')

# create directory to hold text files
if not os.path.exists('construct_data/data'):
    os.makedirs('construct_data/data')


# Move text1.txt to /content/construct_data/data/
shutil.move('text1.txt', '/content/construct_data/data/text1.txt')

# Move text2.txt to /content/construct_data/data/
shutil.move('text2.txt', '/content/construct_data/data/text2.txt')
construct_index("context_data/data") #creates an index of documents located in the "context_data/data" directory using a GPT-based vector index.



ask_ai() #The function then enters a loop where it prompts the user to enter a query using the input() function

