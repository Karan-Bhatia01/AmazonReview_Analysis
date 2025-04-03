from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained Model and Vectorizer
with open(r"models/sentiment_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open(r"models/tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('predict.html', review="", sentiment="")  # Load UI

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review'].strip()  # Get user input
        if not review:
            return render_template('predict.html', review=review, sentiment="⚠️ Please enter a review!")

        transformed_review = vectorizer.transform([review])  # Transform input using TF-IDF
        prediction = model.predict(transformed_review)  # Predict sentiment
        
        sentiment = "🟢 Positive 😊" if prediction[0] == 1 else "🔴 Negative 😡"
        
        return render_template('predict.html', review=review, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
