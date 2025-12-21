
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


---

## 🧠 Why This Is NOT a “Generic GPT Agent”

| Generic GPT Agent      | This Project                      |
| ---------------------- | --------------------------------- |
| Free-form text output  | Strict **Pydantic-typed output**  |
| Prompt + LLM only      | **Prompt → LLM → Parser → Tools** |
| Hard to automate       | **Automation-ready JSON**         |
| No guardrails          | Enforced schema & validation      |
| Manual ticket creation | **Conditional Jira automation**   |

This project is designed for **real backend / SRE / DevOps workflows**, not demos.

---

## 🏗️ Architecture Overview

```
Log Input
   ↓
PromptTemplate
   ↓
Groq LLM (Llama-3.3-70B)
   ↓
PydanticOutputParser
   ↓
Typed DebugResult
   ↓
Conditional Jira Tool
```

---

## 📁 Project Structure

```
app/
├── chains/
│   └── debug_chain.py        # Runnable chain definition
├── llm/
│   └── groq_client.py        # Groq LLM setup
├── prompts/
│   └── debug_prompt.py      # Structured prompt
├── schemas/
│   └── debug_schema.py      # Pydantic output schema
├── tools/
    |-issue-classifier.py  # Error classification tool
│   └── jiracreator.py       # Jira API tool
├── main.py                  # Entry point
```

---

## 🔧 Tech Stack

* **LangChain (Runnable API)**
* **Groq LLM (Llama-3.3-70B)**
* **Pydantic v2**
* **Python 3.10+**
* **Jira REST API**

---

## 🧪 Key LangChain Concepts Used

* `ChatPromptTemplate`
* `RunnableSequence (| operator)`
* `PydanticOutputParser`
* `RunnableLambda` (post-processing)
* Tool invocation outside the LLM
* Structured output enforcement

---

## ⚠️ Known Limitations (Planned Improvements)

* No **Human-in-the-Loop (HITL)** yet
* No retry / branching logic
* Jira decision is single-step

➡️ These will be addressed in the **next LangGraph-based version**.

---

## 🧭 What’s Next

* Rebuild this using **LangGraph**
* Add **HITL approval** before Jira creation
* Add multi-step reasoning + retries
* Add Slack / PagerDuty integrations

---

## 🙌 Acknowledgements

* **Groq** for providing extremely fast, free access to large open models
* **LangChain team** for the Runnable + Core architecture

---


