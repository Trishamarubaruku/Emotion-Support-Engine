import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# 1. Load your Kaggle dataset
# Ensure your CSV has columns named 'text' and 'emotion'
df = pd.read_csv('data/train/your_dataset.csv') 

# 2. Create a pipeline (Vectorization + Classifier)
model = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())

# 3. Train
model.fit(df['text'], df['emotion'])

# 4. Save the model
joblib.dump(model, 'emotion_model.pkl')
print("Model trained and saved as emotion_model.pkl")