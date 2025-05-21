This repo is for the practice project which is to be based on Embedded AI libraries. 

# Python Flask Sentiment Analyzer

This project is a simple web application built with Flask in Python that interacts with an IBM Watson Natural Language Processing (NLP) Sentiment Analysis service to determine the sentiment of a given text. It was developed as part of an IBM Skills Network course to practice integrating embedded AI services and building APIs with Flask.

## Features

Upon completion of this project, the following skills and functionalities have been achieved:

* **AI-Powered Sentiment Analysis Application:** Developed using Flask and the integrated Watson NLP libraries provided within the IBM Skills Network Labs environment.
* **Output Formatting:** The application formats the JSON output received from the Watson NLP library function, effectively extracting relevant information such as the sentiment `label` and its `score`.
* **Modularization and Packaging:** The sentiment analysis logic is encapsulated into an importable function, making the application modular and easy to integrate into other Python codebases.
* **Unit Testing:** Unit tests have been implemented for the sentiment analysis function (`test_sentiment_analysis.py`), verifying the validity of its outputs for different inputs (positive, negative, neutral).
* **Flask Deployment:** The application is configured to be deployed and run on `localhost:5000` using the Flask framework.
* **Error Handling:** Error handling capabilities have been incorporated into the application. It provides a specific error message for blank text inputs and a generic message for other analysis failures (such as a 500 response code from the external API).
* **Static Code Analysis:** Static code analysis using Pylint has been performed on the code files to confirm adherence to PEP8 guidelines and maintain code quality.

## Important Limitation: Watson API Access

The core sentiment analysis functionality in this project (`sentiment_analyzer` in `SentimentAnalysis/sentiment_analysis.py`) relies on a specific external API endpoint: `https://sn-watson-sentiment-bert.labs.skills.network`.

**This endpoint is part of the IBM Skills Network Labs environment and is NOT publicly accessible from outside that environment.**

Therefore:

* Attempting to run the application locally on your machine (outside the IBM Cloud IDE) **will result in a `ConnectTimeoutError`** when trying to connect to the Watson API.
* The application **functions correctly when executed within the IBM Cloud IDE** provided by the course, as that environment has privileged and direct access to the "Embeddable AI" services.

To demonstrate the full functionality outside the IBM Labs environment, you would need to integrate with a publicly accessible sentiment analysis API (e.g., an IBM Watson NLU instance provisioned by yourself on IBM Cloud, Google Cloud Natural Language, Azure Text Analytics, etc.) or implement a mock function for local testing.

### Prerequisites

* Python 3.x
* Flask
* Request
* `pip` (Python package installer)
* Access to the IBM Skills Network Cloud IDE for full functionality.

### Running the Application

From the `practice_project` directory:

```bash
python server.py