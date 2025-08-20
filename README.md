
---

# ⚡ Sparky – AI FAQ Chatbot

Sparky is an interactive FAQ chatbot powered by **Artificial Intelligence**.
It is designed to answer common questions about AI concepts, applications, and trends in a friendly chat-style interface.

The chatbot uses:

* **TF-IDF + Cosine Similarity** for matching user questions with stored FAQs.
* A curated dataset (`faqs.json`) with 60+ AI-related FAQs.
* **Streamlit** for a clean, modern user interface.

This project was developed as part of the **CodeAlpha AI Internship**, showcasing practical use of NLP and information retrieval.
It can be run locally or deployed easily on **Streamlit Cloud** for free.

---

## 📌 Features

* AI-powered FAQ matching system.
* Beautiful **chat-style UI** with distinct colors for user and bot.
* Expandable dataset — just add more Q\&A to `faqs.json`.
* Deployable on Streamlit Cloud.

---

## 🗂 Project Structure

```
CodeAlpha_Chatbot_Sparky/
│── chatbot_app.py       # Main Streamlit app
│── matcher.py           # FAQ matching logic (TF-IDF + cosine similarity)
│── faqs.json            # Dataset of FAQs about AI
│── requirements.txt     # Required dependencies
│── README.md            # Project documentation
```

---

## 🚀 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/CodeAlpha_Chatbot_Sparky.git
   cd CodeAlpha_Chatbot_Sparky
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run chatbot_app.py
   ```

---

## 🌐 Deployment

You can deploy the chatbot on **Streamlit Cloud**:

1. Push your project to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo and deploy the `chatbot_app.py`.

---

## 🎯 Example Questions

* What is Artificial Intelligence?
* What is Machine Learning?
* Who is the father of AI?
* What is ChatGPT?

---

✨ Built with ⚡ by Bilal Sikandar for the **CodeAlpha AI Internship**

---

```
```

