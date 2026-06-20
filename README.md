# AI Sales Training Simulator

An AI-powered sales training platform that simulates realistic customer interactions and provides instant feedback on communication, persuasion, and sales effectiveness.

---

## Overview

This project is an intelligent sales training system designed to help trainees practice conversations with AI-powered customers in realistic business scenarios.

The current version includes a Streamlit-based conversational interface with Speech-to-Text (STT) and Text-to-Speech (TTS) capabilities, allowing users to interact naturally through voice.

---

## Current Features

### AI Customer Simulation

* Dynamic AI-generated customer/shopkeeper responses
* Context-aware conversations
* Realistic sales interaction flow

### Performance Evaluation

* Automated conversation scoring
* Real-time feedback generation
* Sales communication assessment

### Voice Interaction

* Speech-to-Text using Faster Whisper
* Text-to-Speech using Edge TTS
* Hands-free conversational experience

### Real-Time Communication

* FastAPI backend
* WebSocket-based communication
* Low-latency interactions

### Interactive Dashboard

* Streamlit user interface
* Chat-based conversation experience
* Real-time score display

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* WebSockets

### AI & NLP

* LLM Integration
* Faster Whisper
* Edge TTS

### Language

* Python

---

## Project Structure

```text
ai_backend/
│
├── main.py
├── requirements.txt
├── config.py
│
├── ai/
│   ├── stt.py
│   ├── tts.py
│   ├── llm.py
│   ├── scorer.py
│   └── npc_generator.py
│
├── db/
│   ├── models.py
│   ├── crud.py
│   └── database.py
│
├── routers/
│   ├── sessions.py
│   └── interns.py
│
├── prompts/
│   ├── npc_base.txt
│   └── scorer_judge.txt
│
└── dashboard/
    └── app.py
```

---

## Current Development Status

### Completed

* FastAPI backend setup
* WebSocket communication
* AI conversation generation
* Conversation scoring engine
* Streamlit dashboard
* Speech-to-Text integration
* Text-to-Speech integration

### In Progress

* Session management
* Database integration
* Analytics dashboard
* Enhanced evaluation metrics

---

## Future Vision: VR Sales Training Platform

The Streamlit application is the first prototype of a larger AI-powered training ecosystem.

The long-term goal is to build an immersive Virtual Reality (VR) sales training platform where trainees can practice customer interactions in realistic environments and receive detailed AI-driven feedback.

### Planned VR Experience

Users will enter a virtual retail environment and interact with AI-controlled customers.

The AI customer will be capable of:

* Asking product-related questions
* Raising objections
* Negotiating prices
* Demonstrating different personalities
* Reacting dynamically to trainee behavior

Voice communication will occur naturally while the AI continuously evaluates performance.

---

## Intelligent Evaluation System

The platform will assess:

* Communication Skills
* Product Knowledge
* Persuasion Ability
* Confidence
* Objection Handling
* Customer Engagement
* Active Listening
* Sales Effectiveness

---

## Management Dashboard

Future versions will provide trainer and manager dashboards for:

* Progress Tracking
* Session Review
* Performance Comparison
* Automated Reports
* Long-Term Skill Analysis

---

## Upcoming Versions

### Version 2

* User Authentication
* Persistent Session Storage
* Conversation History
* Enhanced Analytics

### Version 3

* Multiple Customer Personas
* Industry-Specific Scenarios
* AI Coaching Recommendations
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

Although currently focused on sales training, the platform can be extended for:

* Customer Service Training
* Interview Preparation
* Retail Staff Training
* Corporate Communication Training
* Negotiation Practice
* Soft Skills Development
* Public Speaking Simulation

---

## Installation

### Clone Repository

```bash
git clone https://github.com/vaniarya/InternTraining.git
cd InternTraining
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

### Start Backend

```bash
uvicorn main:app --reload
```

### Start Streamlit Application

```bash
streamlit run streamlit_chat.py
```

---

## Roadmap

* AI-powered customer simulation
* Voice-first training experience
* Performance analytics dashboard
* Multi-persona customer interactions
* Emotion-aware AI agents
* VR-based immersive training
* Enterprise-scale deployment

---

## Author

**Vani Arya**

B.Tech Computer Science Engineering

Interested in Artificial Intelligence, Machine Learning, Conversational AI, and Immersive Training Technologies.
