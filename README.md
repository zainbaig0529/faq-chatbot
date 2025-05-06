FAQ Chatbot 🤖
A simple FAQ chatbot built using Flask, with integration of external APIs for enhanced functionality. Users can interact with the bot to get answers to common questions and real-time data such as weather updates.

🚀 Features
Natural Language Processing: Understands user queries and provides relevant responses.

Real-Time Info: Pulls data from external APIs (e.g., weather, news).

User Interaction History: Maintains a simple session-based history.

Single Page Application: Smooth interactions without page refresh.

🛠 Tech Stack
Python

Flask

HTML/CSS/JavaScript

External APIs (e.g., OpenWeather)

🔧 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/zainbaig0529/faq-chatbot.git
cd faq-chatbot
Set up a virtual environment:

bash
Copy
Edit
python -m venv chatbot-env
source chatbot-env/bin/activate  # On Windows use chatbot-env\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set environment variables (Linux/macOS):

bash
Copy
Edit
export SECRET_KEY='your_secret_key'
export WEATHER_API_KEY='your_weather_api_key'
On Windows (Command Prompt):

cmd
Copy
Edit
set SECRET_KEY=your_secret_key
set WEATHER_API_KEY=your_weather_api_key
▶️ Running Locally
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000

🌐 Live Demo
Check out the live version here:
🔗 https://faq-chatbot-czyy.onrender.com

📦 Deployment
This app is currently deployed on Render. Simply push changes to GitHub and Render will auto-deploy.

🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

📄 License
This project is licensed under the MIT License.
