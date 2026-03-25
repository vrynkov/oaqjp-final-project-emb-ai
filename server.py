'''
server.py

Calls utility for getting predominant mood from the user input.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__, template_folder='templates')

@app.route("/")
def render_index_page():
    ''' present user with the index.html where user provides their input '''
    return render_template('index.html')


@app.route('/emotionDetector')
def detect_emotion():
    ''' extract user input and uses it to determine users emotion '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return response


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
