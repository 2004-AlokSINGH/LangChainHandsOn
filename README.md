# LangChain & AI Agents (Hands-On)
This repository contains hands-on implementations of **AI agents** built using **LangChain** and **LangGraph**, leveraging **open-source LLMs** for reasoning, tool execution, and retrieval-augmented generation (RAG).

## Project

# 🛠️ AI Ops Debug Copilot (LangChain + Groq)

An AI-powered debugging copilot that analyzes backend logs, identifies root causes, suggests fixes, and conditionally creates Jira tickets — built using **LangChain’s modern Runnable API** and **Groq LLMs** with structured outputs.

---

## 🚀 What This Project Does

Given raw application or API logs, the system:

- Classifies the **error type** (e.g. Authorization, Network, Timeout)
- Identifies the **root cause**
- Suggests **concrete fixes**
- Decides whether a **Jira ticket is required**
- Automatically **creates a Jira ticket** when needed
- Returns a **clean, typed, structured response** (Pydantic)

Example output:

```json
{
  "error_type": "Authorization Error",
  "root_cause": "Insufficient permissions to create issues in the project",
  "suggested_fix": "Verify user permissions and ensure the user has the necessary roles",
  "jira_ticket_required": false,
  "jira_ticket_id": null
}

or


{'error_type': 'Deployment Error', 'root_cause': "Insufficient permissions for service account 'system:serviceaccount:ci:github-runner' to create deployments in 'production' namespace", 'suggested_fix': "Update the RoleBinding or ClusterRoleBinding to grant the 'system:serviceaccount:ci:github-runner' service account the necessary permissions to create deployments in the 'production' namespace", 'jira_ticket_required': True, 'jira_ticket_id': 'TEST-4'}

````
**Now in case if jira required it will create jira and send it to you**
and in json you can see details 
```
 'jira_ticket_required': True,
 'jira_ticket_id': 'TEST-4'
```

<img width="1251" height="749" alt="image" src="https://github.com/user-attachments/assets/7439d479-07d2-485d-a271-ff6baf923bea" />


## 🚀 Features
- Multi-step **AI agent workflows** using LangChain and LangGraph
- **State-based agent orchestration** and control flow with LangGraph
- Integration with **open-source LLMs** (e.g., LLaMA, Mistral via Hugging Face)
- **Tool calling** for API, utility, and data source interaction
- **Retrieval-Augmented Generation (RAG)** using vector embeddings
- **Conversational memory** and context management
- Logging and error handling for agent execution tracking

## 🧠 Use Cases
- Autonomous AI agents
- Question answering over documents
- Multi-tool reasoning pipelines
- LLM experimentation with open-source models

## 🛠️ Tech Stack
- Python  
- LangChain  
- LangGraph  
- Hugging Face Transformers  
- Open-source LLMs  

## 📌 Purpose
This project is intended for **learning and experimentation** with modern **GenAI agent architectures**, focusing on practical, production-inspired patterns.

---

⭐ Feel free to explore, fork, and extend the agents!
