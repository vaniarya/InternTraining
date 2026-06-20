# AI Sales Training Simulator

An AI-powered sales training platform that simulates realistic customer interactions and provides instant feedback on communication, persuasion, confidence, and sales effectiveness.

The project aims to provide a safe and realistic environment for trainees to practice sales conversations with AI-generated customers before engaging with real clients.

---

## Overview

AI Sales Training Simulator is an intelligent conversational training system that combines Large Language Models (LLMs), Speech-to-Text (STT), and Text-to-Speech (TTS) technologies to create realistic sales practice scenarios.

Users can communicate with an AI-powered customer using voice or text, receive dynamic responses, and get performance evaluations based on their sales approach and communication skills.

The current version serves as the foundation for a future VR-based immersive training platform.

---

## Features

### AI Customer Simulation

* Dynamic AI-generated customer responses
* Context-aware conversations
* Realistic sales interaction flow
* Adaptive customer behavior

### Conversation Evaluation

* Automated sales performance scoring
* Communication skill assessment
* Real-time feedback generation
* Conversation quality analysis

### Voice-Based Interaction

* Speech-to-Text using Faster Whisper
* Text-to-Speech using Edge TTS
* Natural voice conversations
* Audio response generation

### Real-Time Communication

* FastAPI backend services
* Low-latency interactions
* Scalable API architecture

### Interactive Dashboard

* Streamlit-based interface
* Real-time chat experience
* Voice input support
* Instant AI responses

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI

### Artificial Intelligence

* Large Language Models (LLMs)
* Faster Whisper
* Edge TTS

### Programming Language

* Python

---

## Project Structure

```text
InternTraining/
│
└── ai_backend/
    │
    ├── ai/
    │   ├── llm.py
    │   ├── scorer.py
    │   ├── stt.py
    │   └── tts.py
    │
    ├── venv/
    │
    ├── .env
    ├── .gitignore
    ├── main.py
    ├── npc_response.mp3
    ├── README.md
    ├── requirements.txt
    └── streamlit_chat.py
```

### File Description

| File                | Description                         |
| ------------------- | ----------------------------------- |
| `main.py`           | FastAPI backend entry point         |
| `streamlit_chat.py` | Streamlit frontend application      |
| `ai/llm.py`         | AI customer response generation     |
| `ai/scorer.py`      | Sales conversation evaluation logic |
| `ai/stt.py`         | Speech-to-Text processing           |
| `ai/tts.py`         | Text-to-Speech generation           |
| `.env`              | Environment variables               |
| `requirements.txt`  | Project dependencies                |
| `npc_response.mp3`  | Generated AI voice response         |

---

## Screenshots

### Main Dashboard

Add a screenshot of your Streamlit interface here.

```markdown
![Dashboard](screenshots/dashboard.png)
```

### Voice Interaction

Add a screenshot showing voice input and AI response generation.

```markdown
![Voice Interaction](screenshots/voice_interaction.png)
```

### Conversation Evaluation

Add a screenshot of the scoring and feedback section.

```markdown
![Evaluation](screenshots/evaluation.png)
```

> Create a folder named `screenshots` in the repository root and place your images there.

---

## Current Development Status

### Completed

* FastAPI backend setup
* AI customer response generation
* Conversation scoring engine
* Streamlit dashboard
* Speech-to-Text integration
* Text-to-Speech integration
* Voice-enabled conversation flow

### In Progress

* Session management
* Database integration
* Conversation history storage
* Analytics dashboard
* Enhanced evaluation metrics

---

## Future Vision: VR Sales Training Platform

The current Streamlit application is the first prototype of a larger AI-powered training ecosystem.

The long-term vision is to build a fully immersive Virtual Reality sales training environment where trainees can practice customer interactions in realistic retail scenarios.

### Planned VR Features

* AI-powered virtual customers
* Real-time voice conversations
* Interactive retail environments
* Customer objection handling
* Negotiation simulations
* Dynamic customer personalities
* Real-time performance assessment

---

## Intelligent Evaluation System

Future versions will evaluate:

* Communication Skills
* Product Knowledge
* Persuasion Ability
* Confidence
* Objection Handling
* Customer Engagement
* Active Listening
* Sales Effectiveness

---

## Upcoming Versions

### Version 2

* User Authentication
* Session Management
* Persistent Storage
* Conversation History

### Version 3

* Multiple Customer Personas
* Industry-Specific Training Scenarios
* Personalized AI Coaching
* Performance Trend Tracking

### Version 4

* Avatar-Based Interactions
* Emotion-Aware AI Customers
* Advanced Behavioral Simulation

### Version 5

* Full VR Integration
* Immersive Retail Environments
* Real-Time Voice Conversations
* Enterprise Deployment

---

## Potential Applications

The platform can be adapted for:

* Sales Training
* Customer Service Training
* Interview Preparation
* Retail Staff Training
* Corporate Communication Training
* Negotiation Practice
* Public Speaking Training
* Soft Skills Development

---

## Installation

### Clone Repository

```bash
git clone https://github.com/vaniarya/InternTraining.git
cd InternTraining/ai_backend
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Backend

```bash
uvicorn main:app --reload
```

### Run Streamlit Application

```bash
streamlit run streamlit_chat.py
```

---

## Roadmap

* AI Customer Simulation
* Voice-Based Training
* Database Integration
* Analytics Dashboard
* Multi-Persona Scenarios
* Emotion-Aware AI Agents
* VR Training Environment
* Enterprise Management Dashboard

---

## Author

### Vani Arya

B.Tech Computer Science Engineering

Interested in Artificial Intelligence, Machine Learning, Conversational AI, XR Technologies, and Immersive Training Systems.

---

⭐ If you find this project interesting, consider giving the repository a star.
