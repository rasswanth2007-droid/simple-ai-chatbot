# 🤖 Simple AI Chatbot

A lightweight, keyword-based AI chatbot built with **Python** and **Flask**, featuring a clean dark-themed web interface.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange?logo=html5&logoColor=white)

---

## ✨ Features

- 💬 **Chat Interface** — Clean, dark-themed responsive UI (single HTML file)
- ⚡ **Keyword Matching** — Pattern-based responses from a JSON knowledge base
- 📱 **Mobile Friendly** — Accessible from any device on the same network
- 🎨 **Smooth Animations** — Typing indicators, message bubbles with transitions
- 📚 **70+ Topics** — Covers AI, ML, Python, Data Structures, SQL, Web Dev, and more

## 📂 Project Structure

```
simple-ai-chatbot/
├── main.py            # Flask backend with /chat API endpoint
├── index.html         # Single-file chat frontend (HTML + CSS + JS)
├── responses.json     # Knowledge base with conditions & responses
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Flask (`pip install flask`)

### Run Locally

```bash
# Clone the repository
git clone https://github.com/rasswanth2007-droid/simple-ai-chatbot.git
cd simple-ai-chatbot

# Install dependencies
pip install flask

# Start the server
python main.py
```

Open **http://localhost:5000** in your browser.

### Access from Mobile

The server runs on `0.0.0.0:5000`, so any device on the same Wi-Fi can access it.  
Find your PC's local IP and open it on your phone:

```
http://<YOUR-PC-IP>:5000
```

## 💡 Topics Covered

| Category | Topics |
|----------|--------|
| **AI & ML** | Artificial Intelligence, Machine Learning, Deep Learning, Neural Networks, NLP, Computer Vision, Generative AI |
| **ML Concepts** | Supervised/Unsupervised/Reinforcement Learning, Classification, Regression, Clustering, Overfitting, Underfitting |
| **Programming** | Python, C, Java, JavaScript, HTML, CSS, Git, Debugging |
| **Data Structures** | Arrays, Stacks, Queues, Trees, Graphs, BFS, DFS, Sorting, Searching |
| **Databases** | SQL, DBMS, Normalization, Primary/Foreign Keys, SELECT, INSERT, JOIN |
| **Statistics** | Mean, Median, Probability, Accuracy, Precision, Recall, F1 Score |
| **General** | Computers, Internet, Cybersecurity, Cloud Computing, APIs, Web Development |

## 🛠️ How It Works

1. User sends a message from the frontend
2. The message is sent as a `POST` request to `/chat`
3. The backend matches keywords in the message against `responses.json`
4. A random response from the matched category is returned
5. If no match is found, a default response is sent

```
User: "What is machine learning?"
 ↓ matches "machine_learning" conditions
Bot: "Machine Learning is a subset of AI that learns from data."
```

## 📝 Customization

Add your own topics by editing `responses.json`:

```json
{
    "your_topic": {
        "conditions": [
            "keyword1",
            "keyword2",
            "tell me about keyword1"
        ],
        "responses": [
            "Response 1 for this topic.",
            "Response 2 for this topic."
        ]
    }
}
```

Restart the server after making changes.

## 📄 License

This project is open source and available for educational purposes.
