from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity  # from -1 to 1
    subjectivity = sentiment.subjectivity  # from 0 to 1
    
    if polarity > 0:
        category = "Positive"
    elif polarity < 0:
        category = "Negative"
    else:
        category = "Neutral"

    return category, polarity, subjectivity


@app.route('/', methods=['GET','POST'])
def index():
    sentiment = None
    polarity = None
    subjectivity = None

    if request.method == "POST":
        text = request.form['text']
        sentiment, polarity, subjectivity = analyze(text)


    return render_template('index.html', sentiment=sentiment, polarity=polarity, subjectivity=subjectivity)


if __name__ == '__main__':
    app.run(debug=True)
