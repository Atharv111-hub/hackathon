from flask import request
import app
@app.route('/detect_news', methods=['POST'])
def detect_news():
    text = request.form['news_text']
    # Run your model here
    return "News detection done"

@app.route('/detect_deepfake', methods=['POST'])
def detect_deepfake():
    file = request.files['media_file']
    # Run deepfake check here
    return "Deepfake detection done"
