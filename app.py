from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from fuzzywuzzy import fuzz
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Flask-Login
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login page if not logged in

# User model for SQLAlchemy
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Create the database and table if it doesn't exist
with app.app_context():
    db.create_all()

# FAQ dataset
faqs = [
    {'Question': 'What is the launch date of Product X?', 'Answer': 'The launch date is January 15, 2024.'},
    {'Question': 'How do I reset my password?', 'Answer': 'You can reset your password by clicking on "Forgot Password" at the login page.'},
    {'Question': 'What are your hours?', 'Answer': 'We are open from 9 AM to 5 PM.'},
    {'Question': 'How can I contact support?', 'Answer': 'You can reach us at support@example.com.'},
    {'Question': 'Where are you located?', 'Answer': 'We are located at 123 Main St, Anytown, USA.'},
    {'Question': 'Do you offer refunds?', 'Answer': 'Yes, we offer refunds within 30 days of purchase.'},
    {'Question': 'What payment methods do you accept?', 'Answer': 'We accept credit cards and PayPal.'},
]

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def get_weather(city):
    """Fetch weather data from WeatherAPI."""
    url = f"http://api.weatherapi.com/v1/current.json?key=1d1dde36058a4d5fbc945340240810&q={city}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        country = data['location']['country']
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"The current weather in {location}, {country} is {temperature}°C with {condition}."
    else:
        return "Sorry, I couldn't retrieve the weather information."

def get_response(user_input):
    user_input_normalized = user_input.lower()
    best_match = None
    highest_score = 0

    # Weather query handling
    if "weather" in user_input_normalized:
        city = user_input_normalized.split("weather in")[-1].strip()
        if city:
            return get_weather(city)
        return "Please specify a city for the weather."

    # Check FAQs
    for faq in faqs:
        question = faq['Question'].lower()
        if user_input_normalized == question:
            response = faq['Answer']
            return response

        score = fuzz.ratio(user_input_normalized, question)
        if score > highest_score:
            highest_score = score
            best_match = faq['Answer']

    if highest_score > 60:
        best_faq_question = faqs[next(i for i, faq in enumerate(faqs) if faq['Answer'] == best_match)]['Question']
        return best_match

    return "I'm sorry, I don't have an answer for that."

# Home page with login required
@app.route('/')
@login_required
def home():
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html', chat_history=session['chat_history'])

# Chatbot response handling
@app.route('/get_response', methods=['POST'])
@login_required
def respond():
    user_input = request.form.get('user_input', '').strip()
    if user_input == '':  # Prevent empty input
        response = "Please ask a valid question."
    else:
        response = get_response(user_input)

    # Update chat history
    session['chat_history'].append({'type': 'user', 'message': user_input})
    session['chat_history'].append({'type': 'bot', 'message': response})

    return render_template('index.html', chat_history=session['chat_history'])

# Search FAQs
@app.route('/search', methods=['POST'])
@login_required
def search():
    search_input = request.form.get('search_input', '').strip()
    search_results = [faq for faq in faqs if search_input.lower() in faq['Question'].lower()]

    return render_template('index.html',
                           chat_history=session.get('chat_history', []),
                           search_results=search_results)

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another one.')
            return redirect(url_for('register'))

        # Add new user to the database
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and password is correct
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('home'))
        
        flash('Invalid credentials. Please try again.')
        return redirect(url_for('login'))
    
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

