Sentiment Analysis Web App
📌 Overview
This project is a Flask-based web application that predicts the sentiment (positive or negative) of a given text review. It utilizes Machine Learning (Random Forest Classifier) and TF-IDF vectorization to analyze text input and determine its sentiment.

🏗️ Features
✔️ User-friendly web interface for sentiment prediction
✔️ Pre-trained Random Forest Classifier for high accuracy
✔️ TF-IDF vectorization for text preprocessing
✔️ Supports real-time predictions on new user inputs

🚀 How to Run
1️⃣ Install Dependencies
Ensure you have Python installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
2️⃣ Start the Flask App
Run the following command:

bash
Copy
Edit
python app.py
This will start a local web server, usually at http://127.0.0.1:5000/.

3️⃣ Use the Web App
Open your browser and go to http://127.0.0.1:5000/
Enter a text review in the input box
Click "Predict" to get the sentiment classification
🛠️ Project Structure
bash
Copy
Edit
📂 sentiment_analysis_project
│── 📂 models
│   ├── sentiment_model.pkl  # Trained Random Forest model
│   ├── tfidf_vectorizer.pkl # TF-IDF vectorizer
│── 📂 templates
│   ├── predict.html         # HTML for user input & results
│── 📜 app.py                # Flask backend
│── 📜 requirements.txt       # Required Python libraries
│── 📜 README.txt             # Project documentation (this file)
📊 Machine Learning Model
Vectorization: TF-IDF (max_features=6000)
Model Used: Random Forest Classifier
Performance Metrics: Accuracy, F1-score, Precision, Recall
📝 Example Test Case
Input:
"I expected this product to be amazing, but while it has some great features, it also has frustrating issues that make me wonder if it was worth the money."

Predicted Sentiment: (Try it yourself!)