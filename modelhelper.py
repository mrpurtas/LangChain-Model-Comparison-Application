import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI

def ask_gpt(prompt, temperature, max_tokens):
    llm = ChatOpenAI(api_key=my_key_openai, temperature=temperature, max_tokens=max_tokens, model="gpt-4-1106-preview")
    
    AI_Response = llm.invoke(prompt)
    
    return AI_Response.content



my_key_google = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

def ask_gemini(prompt, temperature):
    llm = ChatGoogleGenerativeAI(google_api_key=my_key_google, temperature=temperature, model="gemini-pro")
    
    AI_Response = llm.invoke(prompt)
    
    return AI_Response.content




my_key_anthropic = os.getenv("anthropic_apikey")

from langchain_community.chat_models import ChatAnthropic

def ask_claude(prompt, temperature, max_tokens):
    llm = ChatAnthropic(anthropic_api_key=my_key_anthropic, temperature=temperature, max_tokens=max_tokens, model_name="claude-2.1")
    
    AI_Response = llm.invoke(prompt)
    
    return AI_Response.content


my_key_cohere = os.getenv("COHERE_API_KEY")

from langchain_community.chat_models import ChatCohere

def ask_command(prompt, temperature, max_tokens):
    llm = ChatCohere(cohere_api_key=my_key_cohere, temperature=temperature, max_tokens=max_tokens, model="command")
    
    AI_Response = llm.invoke(prompt)
    
    return AI_Response.content



