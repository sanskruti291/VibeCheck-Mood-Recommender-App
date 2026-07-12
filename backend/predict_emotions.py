import transformers
from transformers import pipeline
from preprocess import clean_text
classifier = transformers.pipeline(
    "text-classification",model="bhadresh-savani/distilbert-base-uncased-emotion")
 
def predict_emotion(text):

    tokens = clean_text(text)

    cleaned_text = " ".join(tokens)

    result = classifier(cleaned_text)

    label = result[0]["label"]
    score = result[0]["score"]

    return label, score




