from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetection")

@app.route('emotionDetector')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)