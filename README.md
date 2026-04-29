# 🚀 AI Code Documentation Generator

An AI-powered web application that automatically generates **meaningful code comments and algorithm explanations** from source code.

It acts as a **Code Documentation Generator**, helping developers understand complex code instantly using an NLP-inspired approach.

---

## ✨ Features

- 🧠 Auto algorithm detection (BFS, DFS, DP, Binary Search, Graph, etc.)
- 💬 Generates short and detailed code explanations
- 🌐 Supports multiple languages:
  - C++
  - Python
  - Java
- ⚡ Real-time backend API (Flask)
- 📝 AI-style code documentation generation
- 🔗 Full frontend + backend integration
- ☁️ Deployed on:
  - Render (Backend)
  - Netlify (Frontend)

---

## 🧠 Core Concept (NLP-Inspired Engine)

The **AI Code Documentation Generator** uses a custom NLP-inspired system instead of external AI APIs.

It includes:

- 🔍 Pattern recognition (regex-based parsing)
- 📊 Feature extraction from code structure
- ⚖️ Rule + scoring-based algorithm detection
- 🧠 Context-aware documentation generation

This makes it:
- ⚡ Fast
- 🌐 Fully offline logic-based
- 💰 No API cost
- 🔧 Fully customizable

---

## 🏗️ Tech Stack

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python (Flask)
- Flask-CORS
- NLP-inspired rule-based engine

Deployment:
- Render (Backend Hosting)
- Netlify (Frontend Hosting)
- GitHub (Version Control)

---

## 📁 Project Structure

code-comment-generator/
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│
└── README.md

---

## ⚙️ How It Works

1. User enters code in the frontend
2. Frontend sends code to backend API
3. Backend:
   - Detects programming language
   - Identifies algorithm type
   - Generates meaningful documentation/comments
4. Response is displayed as:
   - Clean annotated code
   - AI-generated explanation

---

## 🚀 API Endpoint

POST /generate

Request:
{
  "code": "your code here",
  "language": "",
  "mode": "detailed"
}

Response:
{
  "comment": "documented code output",
  "language": "C++",
  "algorithm": "BFS / DFS / DP etc."
}

---

## 🧪 Example

Input:
int binarySearch(vector<int>& nums, int target) {
    int low = 0, high = nums.size() - 1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (nums[mid] == target)
            return mid;
    }

    return -1;
}

Output:
- Language: C++
- Algorithm: Binary Search
- Documentation:
  - Search space reduction logic
  - Mid-point calculation
  - Condition-based narrowing
  - Return index if found

---

## 🌐 Live Demo

Frontend: https://lovely-treacle-470d36.netlify.app  
Backend: https://code-comment-backend-cjah.onrender.com  

---

## 📌 Key Highlights

- AI Code Documentation Generator (project name)
- Real-time NLP-inspired code understanding engine
- No external AI/LLM APIs used
- Fully custom-built logic system
- Lightweight, fast, and scalable
- Beginner + recruiter friendly

---

## 🚀 Future Improvements

- OpenAI integration for advanced explanations
- Syntax highlighting editor UI
- User login + history tracking
- Downloadable documentation file
- GitHub integration for repo analysis

---

## 👨‍💻 Author

Shivanshi Sharma

---

## 📄 License

This project is open-source and free to use for learning and development.
