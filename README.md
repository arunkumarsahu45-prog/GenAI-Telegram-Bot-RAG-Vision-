# 🤖 GenAI Telegram Bot (RAG + Image Captioning)

## 📌 Overview

This project is a lightweight **Generative AI Telegram Bot** that supports:

* 🧠 **RAG (Retrieval-Augmented Generation)** for answering questions from documents
* 🖼️ **Image Captioning** using a vision model
* 💬 Interactive Telegram interface

The bot can respond to user queries and describe uploaded images in real time.

---

## 🚀 Features

### 🔹 Text Query (/ask)

* Retrieves relevant information from local documents
* Uses embeddings + FAISS for similarity search
* Generates answers using an LLM (Ollama - Mistral)

### 🔹 Image Captioning

* Accepts image uploads
* Generates:
  * Caption
  * Tags (keywords)

### 🔹 Help Command

* `/help` shows usage instructions

---

## 🏗️ System Architecture

User → Telegram Bot → Router
→ RAG Pipeline (Embeddings + FAISS + LLM)
→ Vision Model (BLIP)
→ Response to User

---

## ⚙️ Tech Stack

| Component    | Technology            |
| ------------ | --------------------- |
| Bot          | python-telegram-bot   |
| Embeddings   | sentence-transformers |
| Vector DB    | FAISS                 |
| LLM          | Ollama (Mistral)      |
| Vision Model | BLIP (Hugging Face)   |

---

## 📂 Project Structure

```
genai-bot/
│
├── app.py
├── handlers.py
├── rag.py
├── vision.py
│
├── memory/
│   └── chat_memory.py
│
├── data/
│   ├── docs/
│   └── db.sqlite
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd genai-bot
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Install Ollama (for LLM)

Download: [https://ollama.com](https://ollama.com/)

Run model:

```
ollama run mistral
```

---

### 4️⃣ Configure Bot Token

Edit `app.py`:

```
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

---

### 5️⃣ Run the application

```
python app.py
```

---

## 🧪 Usage

### Ask a question:

```
/ask What is machine learning?
```

### Upload an image:

* Send image directly → bot returns caption + tags

### Help:

```
/help
```

---

## 📊 Example Output

**User:**

```
/ask What is AI?
```

**Bot:**

```
AI is a field of computer science focused on building intelligent systems...
Sources: ai_notes.md
```

---

## ⭐ Optional Enhancements Implemented

* ✅ Chat memory (last 3 interactions)
* ✅ Source snippets in responses
* ✅ Modular architecture

---

## 📈 Future Improvements

* Add caching for embeddings
* Deploy using Docker
* Add web UI (Streamlit/Gradio)
* Use advanced LLMs (LLaMA 3, Phi-3)

---

## 🎯 Conclusion

This project demonstrates:

* Practical use of **RAG architecture**
* Integration of **vision + NLP models**
* Clean and scalable **system design**

---

## 👨‍💻 Author

Arun Kumar Sahu
