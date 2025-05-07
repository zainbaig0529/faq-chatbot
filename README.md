# FAQ Chatbot 🤖

A simple FAQ chatbot built using Flask, with integration of external APIs for enhanced functionality. Users can interact with the bot to get answers to common questions and real-time data such as weather updates.

---

## 🚀 Features

- **Natural Language Processing:** Understands user queries and provides relevant responses.
- **Real-Time Info:** Pulls data from external APIs (e.g., weather, news).
- **User Interaction History:** Maintains a simple session-based history.
- **Single Page Application:** Smooth interactions without page refresh.

---

## 🛠 Tech Stack

- Python
- Flask
- HTML/CSS/JavaScript
- External APIs (e.g., OpenWeather)

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/zainbaig0529/faq-chatbot.git
cd faq-chatbot
2. Set up a virtual environment
bash
Copy
Edit
python -m venv chatbot-env
source chatbot-env/bin/activate  # On Windows: chatbot-env\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set environment variables
On macOS/Linux:
bash
Copy
Edit
export SECRET_KEY='your_secret_key'
export WEATHER_API_KEY='your_weather_api_key'
On Windows (CMD):
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
Visit http://127.0.0.1:5000 in your browser.

🌐 Live Demo
Check out the live version:
🔗 https://faq-chatbot-czyy.onrender.com

📦 Deployment
This app is deployed on Render. Just push changes to GitHub, and Render will auto-deploy your updates.

🤝 Contributing
Pull requests are welcome!
For major changes, open an issue first to discuss what you'd like to change.

📄 License
This project is licensed under the MIT License.