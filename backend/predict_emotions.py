import transformers
from preprocess import clean_text

classifier = None


def get_classifier():
    global classifier
    if classifier is None:
        classifier = transformers.pipeline(
            "text-classification",
            model="bhadresh-savani/distilbert-base-uncased-emotion"
        )
    return classifier


def predict_emotion(text):
    tokens = clean_text(text)
    cleaned_text = " ".join(tokens)

    classifier = get_classifier()
    result = classifier(cleaned_text)

    label = result[0]["label"]
    score = result[0]["score"]

    return label, score




