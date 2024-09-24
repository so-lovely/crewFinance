"""
    CodeDocsSearchTool
    GitHubSearchTool
    SerperDevTool
    PDFSearchTool
    Langchain.utilites
    Langchain.tools
    Good - 
    AskNews
"""
from dotenv import load_dotenv
import os
import http.client
import json
import time

# Search tool for crewAI 
def Serper_Search(query:str):
  load_dotenv()
  conn = http.client.HTTPSConnection("google.serper.dev")
  payload = json.dumps({
    "q": query
  })
  headers = {
    'X-API-KEY': os.environ.get('SERPER_API_KEY'),
    'Content-Type': 'application/json'
  }
  conn.request("POST", "/search", payload, headers)
  res = conn.getresponse()
  if res.status == 200:
    data = res.read()
    data = data.decode()
    return data
  else:
    return "Not Found"
  

def Serper_news_Search(query:str):
  load_dotenv()
  conn = http.client.HTTPSConnection("google.serper.dev")
  payload = json.dumps({
    "q": query
  })
  headers = {
    'X-API-KEY': os.environ.get('SERPER_API_KEY'),
    'Content-Type': 'application/json'
  }
  conn.request("POST", "/news", payload, headers)
  res = conn.getresponse()
  if res.status == 200:
    data = res.read()
    return data.decode()
  else:
    return "Not Found"
  

def Serper_Scholar_Search(query:str):
  load_dotenv()
  conn = http.client.HTTPSConnection("google.serper.dev")
  payload = json.dumps({
    "q": "apple inc"
  })
  headers = {
    'X-API-KEY': os.environ.get('SERPER_API_KEY'),
    'Content-Type': 'application/json'
  }
  conn.request("POST", "/scholar", payload, headers)
  res = conn.getresponse()
  if res.status == 200:
    data = res.read()
    return data.decode()
  else:
    return "Not Found"
  

    
        