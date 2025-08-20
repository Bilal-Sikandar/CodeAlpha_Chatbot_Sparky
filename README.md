# 🤖 FAQ Chatbot

This is a simple **FAQ Chatbot** built using **Python, Streamlit, and Scikit-learn** as part of the **CodeAlpha AI Internship**.

## 📌 Features
- Matches user questions to the closest FAQ using **TF-IDF + Cosine Similarity**
- Interactive **Streamlit interface**
- Easy to extend by editing `faqs.json`

## 🚀 Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CodeAlpha_Chatbot.git
   cd CodeAlpha_Chatbot
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the chatbot:

   ```bash
   streamlit run app.py
   ```

## 🗂 Project Structure

```
CodeAlpha_Chatbot/
│── faqs.json          # FAQ dataset
│── matcher.py         # Matching logic (TF-IDF + cosine similarity)
│── app.py             # Streamlit app (UI)
│── requirements.txt   # Required Python libraries
│── README.md          # Project documentation
```

## 🌐 Deployment

You can deploy the chatbot for free using **Streamlit Cloud**:

1. Push your project to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo and deploy.

## 🎯 Example FAQs

* *What is Artificial Intelligence?*
* *Who created Python?*
* *What is Streamlit?*

---

✨ Built with ❤️ for the **CodeAlpha AI Internship**

```
```
