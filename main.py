import gradio as gr
from unstract.llmwhisperer import LLMWhispererClientV2
import os
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import Document
from langchain import hub
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Load environment variables
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("openai_api_key")
UNSTRACT_API_KEY = os.getenv("unstract_api_key")
BASE_URL = os.getenv("BASE_URL")

client = LLMWhispererClientV2(api_key=UNSTRACT_API_KEY)

# Global variable to store the current document's vector store
current_vectorstore = None

def process_pdf(pdf_path):
    try:
        # Process PDF with LLM Whisperer
        whisper = client.whisper(
            file_path=pdf_path.name,
            wait_for_completion=True,
            wait_timeout=200
        )
        
        extracted_text = whisper['extraction']['result_text']
        
        # Create document for vector store
        documents = [
            Document(
                page_content=extracted_text,
                metadata={"source": pdf_path.name}
            )
        ]
        
        # Create vector store and store it globally
        global current_vectorstore
        embeddings = OpenAIEmbeddings()
        current_vectorstore = FAISS.from_documents(documents, embeddings)
        
        return extracted_text, "Document processed successfully. You can now ask questions."
    except Exception as e:
        return "", f"Error processing document: {str(e)}"

def answer_question(question):
    try:
        if current_vectorstore is None:
            return "Please upload a document first."
        
        # Set up QA chain
        retriever = current_vectorstore.as_retriever()
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
        combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
        retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
        
        # Get answer
        response = retrieval_chain.invoke({"input": question})
        return response['answer']
    except Exception as e:
        return f"Error answering question: {str(e)}"

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Document Q&A with LLM Whisperer")
    gr.Markdown("Upload a PDF document and ask questions about its content.")
    
    with gr.Row():
        pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
    
    with gr.Row():
        extracted_text = gr.Textbox(label="Extracted Text", interactive=False, lines=10)
        status_output = gr.Textbox(label="Status", interactive=False)
    
    with gr.Row():
        question_input = gr.Textbox(label="Your Question", placeholder="Ask a question about the document...")
        answer_output = gr.Textbox(label="Answer", interactive=False)
    
    # Handle PDF upload
    pdf_input.upload(
        fn=process_pdf,
        inputs=[pdf_input],
        outputs=[extracted_text, status_output]
    )
    
    # Handle question submission
    question_btn = gr.Button("Get Answer")
    question_btn.click(
        fn=answer_question,
        inputs=[question_input],
        outputs=[answer_output]
    )

# Launch the app
demo.launch(server_name="127.0.0.1",
            server_port=7860,
            share=True)