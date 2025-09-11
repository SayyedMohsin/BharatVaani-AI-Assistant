# BharatVaani AI Assistant
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

## Overview
BharatVaani is a multilingual AI assistant designed to provide instant answers to user queries in multiple Indian languages. It leverages the power of Google Gemini AI and FastAPI for backend services, combined with a React frontend for a seamless user experience.

## Features
- **Multilingual Support**: Supports 22 Indian languages.
- **AI-Powered Responses**: Generates context-aware responses using Google Gemini.
- **User Profiles**: Stores user preferences and settings.
- **Responsive Design**: Tailwind CSS for a clean and responsive UI.

## Technologies Used
- **Frontend**: React.js, Tailwind CSS
- **Backend**: FastAPI, Google Gemini AI
- **Database**: In-memory (can be extended to PostgreSQL or Firebase)
- **Deployment**: Docker (optional)

## Project Structure

BharatVaani/
├── backend/
│   ├── .env
│   ├── requirements.txt
│   └── main.py
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── tailwind.css
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── vite.config.js
├── .gitignore
└── README.md

## Getting Started

### Prerequisites
- Node.js (for frontend)
- Python (for backend)
- Google Gemini API Key

### Backend Setup
1. **Install Python and FastAPI**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r backend/requirements.txt
   
### Set Environment Variables:
Create a .env file in the backend directory and add your Google Gemini API Key:
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

### Run the Backend:
uvicorn main:app --reload --port 8000

### Frontend Setup
Install Node.js and Dependencies:
bash
cd frontend
npm install

### Run the Frontend:
bash
npm run dev

### Accessing the Application
### Backend: http://localhost:8000/docs
### Frontend: http://localhost:5173

### Usage
**Home Page** : Ask questions in multiple languages and get instant AI responses.

**Services Page**: Explore different categories like UPI, Government Schemes, Weather, etc.

**Settings Page**: Customize your profile, language preferences, and enable/disable voice commands.

### Contact
For any queries or support, contact **smohsin32@yahoo.in**

This project is maintained by **Sayyed Mohsin Ali**
