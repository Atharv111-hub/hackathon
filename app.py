from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user storage
users = {'admin@example.com': 'admin123'}

# Home/Login/Signup Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', message='Invalid credentials')
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']
    if email in users:
        return render_template('login.html', message='User already exists')
    users[email] = password
    return redirect(url_for('dashboard'))


# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Upload Page
@app.route('/upload')
def upload():
    return render_template('upload.html')

# Analyze Explanation Page
@app.route('/analyze-info')
def analyze_info():
    return render_template('analyze-info.html')

# Result Explanation Page
@app.route('/result-info')
def result_info():
    return render_template('result-info.html')

# Feedback Page
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        feedback_text = request.form['feedback']
        print(f"Feedback from {name}: {feedback_text}")  # Optionally save to DB or file
        return f"Thank you for your feedback, {name}!"
    return render_template('feedback.html')
@app.route('/about')
def about():
    return render_template('about.html')
# === AI Model Result Routes ===

@app.route('/predict_news', methods=['POST'])
def predict_news():
    news_text = request.form['news_text']
    region = request.form.get('region')

    # Dummy AI logic (replace with BERT)
    prediction = "Fake"
    confidence = 91.6
    explanation = "Detected known misinformation pattern."

    return render_template("result.html", prediction=prediction, confidence=confidence, explanation=explanation, source='news')

@app.route('/predict_deepfake', methods=['POST'])
def predict_deepfake():
    media = request.files['media']

    # Dummy AI logic (replace with XceptionNet)
    prediction = "Real"
    confidence = 88.4
    explanation = "No manipulation detected in face region."

    return render_template("result.html", prediction=prediction, confidence=confidence, explanation=explanation, source='deepfake')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
