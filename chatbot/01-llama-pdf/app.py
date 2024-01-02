import os
import sys
import pinecone
from langchain.llms import Replicate
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain

# Replicate API token
os.environ['REPLICATE_API_TOKEN'] = "r8_63gKphsNWphgor1k007lhviNphn8Pp12sqIoV"

# Initialize Pinecone
pinecone.init(api_key='da356a2a-acff-4aab-af60-37ad1b7eff6d', environment='gcp-starter')

print("<<<<<<<<<<<<<<<<<<<<<<< Pinecone Initialized >>>>>>>>>>>>>>>>>>>>>>")

# Load and preprocess the PDF document
loader = PyPDFLoader('sample.pdf')
documents = loader.load()

print("<<<<<<<<<<<<<<<<<<<<<<< Doc loaded >>>>>>>>>>>>>>>>>>>>>>")

# Split the documents into smaller chunks for processing
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

print("<<<<<<<<<<<<<<<<<<<<<<< Doc Splitted >>>>>>>>>>>>>>>>>>>>>>")


# Use HuggingFace embeddings for transforming text into numerical vectors
embeddings = HuggingFaceEmbeddings()

print("<<<<<<<<<<<<<<<<<<<<<<< Huggingface thing done >>>>>>>>>>>>>>>>>>>>>>")


# Set up the Pinecone vector database
index_name = "test-index"
index = pinecone.Index(index_name)
vectordb = Pinecone.from_documents(texts, embeddings, index_name=index_name)

print("<<<<<<<<<<<<<<<<<<<<<<< vector DB thing done >>>>>>>>>>>>>>>>>>>>>>")


# Initialize Replicate Llama2 Model
llm = Replicate(
    model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
    input={"temperature": 0.75, "max_length": 3000}
)

print("<<<<<<<<<<<<<<<<<<<<<<< replicate initialized >>>>>>>>>>>>>>>>>>>>>>")

# Set up the Conversational Retrieval Chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm,
    vectordb.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True
)

print("<<<<<<<<<<<<<<<<<<<<<<< retrieval chain thing done >>>>>>>>>>>>>>>>>>>>>>")

# Start chatting with the chatbot
chat_history = []
while True:
    query = input('Prompt: ')
    if query.lower() in ["exit", "quit", "q"]:
        print('Exiting')
        sys.exit()
    result = qa_chain({'question': query, 'chat_history': chat_history})
    print('Answer: ' + result['answer'] + '\n')
    chat_history.append((query, result['answer']))