import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQMatcher:
    def __init__(self, faq_file):
        with open(faq_file, 'r') as f:
            data = json.load(f)
        self.questions = [item["question"] for item in data]
        self.answers = [item["answer"] for item in data]

        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.questions)

    def get_answer(self, user_input):
        user_vec = self.vectorizer.transform([user_input])
        similarity = cosine_similarity(user_vec, self.X)
        best_match = similarity.argmax()
        confidence = similarity[0, best_match]

        if confidence < 0.3:
            return "🤖 Sorry, I couldn't understand your question. Please try again."
        return self.answers[best_match]
