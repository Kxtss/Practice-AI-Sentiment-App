''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    '''
        This code receives the text from the HTML interface and
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "No text provided for analysis. Please enter a sentence."
    response = sentiment_analyzer(text_to_analyze)
    label = response["label"]
    score = response["score"]
    if label is None:
        return "Invalid entry! Try again."
    formatted_label = label.split("_")[1]
    return f"The given text has been identified as {formatted_label} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host='0.0.0.0', port=5000)
