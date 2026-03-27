# 🚀 Code Review Assistant (OpenEnv)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenEnv](https://img.shields.io/badge/OpenEnv-Compatible-green)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

> 🧠 AI-powered code review environment built using OpenEnv — simulating real-world software engineering workflows.


# 🚀 Code Review Assistant (OpenEnv)

## 📌 Overview

This project implements a **real-world OpenEnv environment** where an AI agent performs automated code reviews.

The agent analyzes code, identifies critical issues, assigns severity, and suggests fixes — simulating how real engineers review code in production systems.

---

## 🎯 Motivation

Code review is a critical part of software development but is:

* Time-consuming
* Error-prone
* Hard to scale

This environment enables training and evaluation of AI agents that can assist or automate code review workflows.

---

## 🧠 Environment Design

The environment follows the **OpenEnv standard**:

* `reset()` → provides a new code review task
* `step(action)` → evaluates agent output
* `state()` → returns current environment state

---

## 📥 Observation Space

```json
{
  "code": "string",
  "task_id": "easy | medium | hard"
}
```

---

## 📤 Action Space

```json
{
  "issues": ["list of detected issues"],
  "severity": "low | medium | high",
  "suggestion": "fix recommendation",
  "reasoning": "why this is an issue"
}
```

---

## 🏆 Reward Design

The reward function evaluates:

* ✅ Correct issue detection
* ✅ Severity classification
* ✅ Quality of suggestion
* ✅ Reasoning relevance

Score range: **0.0 → 1.0**

Includes:

* Partial rewards for incomplete answers
* Penalties for hallucinations or irrelevant issues

---

## 🧪 Tasks

### 🟢 Easy

* Detect runtime bug (division by zero)

### 🟡 Medium

* Detect security vulnerability (SQL injection)

### 🔴 Hard

* Identify performance & code quality issues

---

## 🤖 Baseline Agent

A baseline agent using an LLM (Anthropic Claude) is provided.

Features:

* Structured JSON output
* Controlled issue selection
* Robust parsing for real-world LLM behavior

---

## 📊 Baseline Results

| Task   | Score |
| ------ | ----- |
| Easy   | 0.8   |
| Medium | 0.8   |
| Hard   | 1.0   |

**Final Score: ~0.86**

---

## ⚙️ Setup Instructions

```bash
# Clone repo
git clone <your-repo>

# Install dependencies
pip install -e .

# Set API key
setx ANTHROPIC_API_KEY "your_key"

# Run baseline agent
python -m baseline.run_agent
```

---

## 🐳 Docker Support

```bash
docker build -t code-review-env .
docker run code-review-env
```

---

## 📦 OpenEnv Compliance

* ✔ Full OpenEnv API (step/reset/state)
* ✔ Typed Pydantic models
* ✔ openenv.yaml included
* ✔ Validated with `openenv validate`

---

## 🚀 Deployment

This environment is fully containerized and ready for deployment on:

* Hugging Face Spaces
* Docker-based platforms

---

## 🧠 Key Highlights

* Real-world task (code review)
* Robust LLM integration
* Fault-tolerant parsing
* Smart grading system
* Production-ready design

---

## 👤 Author

**Besita Augustin**

---

## 🏁 Conclusion

This project demonstrates how AI agents can be evaluated in structured environments for real-world engineering tasks, bridging the gap between LLM capabilities and practical applications.


## 🎥 Demo

### Example Output

```json
{
  "issues": ["SQL injection vulnerability"],
  "severity": "high",
  "suggestion": "Use parameterized queries",
  "reasoning": "Prevents malicious query injection"
}
```

---

### 🔥 Key Capability

* Detects runtime bugs
* Identifies security issues
* Suggests production-ready fixes
