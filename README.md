🌟 AI-Based Automated Content Marketing Optimizer
AI-Based Automated Content Marketing Optimizer is an open-source tool that leverages the X (Twitter) API and Gemini API to help brands like Microsoft generate and compare highly engaging, brand-authentic tweets—using real engagement data and state-of-the-art AI.

🚀 Features
Generate tweets using few-shot learning, guided by your brand’s top-performing tweet examples.

Compare tweets from different AI models, with AI-predicted engagement and detailed explanations.

Sentiment & engagement analysis tailoring results to your audience.

Modern, responsive UX: Built with Flask, JS, and dynamic CSS.

Modular, extensible code for research or production use.

🌱 Getting Started
1. Clone the Repository
Bash

git clone https://github.com/Sarthak-csai/Infosys_Intern_LLM
cd Infosys_Intern_LLM
2. Environment Configuration
This project requires credentials for the X (Twitter) API and the Gemini API. Create a file named .env in the project root directory with the following:

Code snippet

# ==== X (Twitter) API credentials ====
API_KEY=your_twitter_api_key
API_SECRET_KEY=your_twitter_api_secret_key
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
BEARER_TOKEN=your_twitter_bearer_token

# ==== Gemini API ====
GEMINI_API_KEY=your_gemini_api_key
⚠️ Important: Never commit your real .env file or secrets to GitHub. See .env.example for a template.

3. Install Dependencies
All Python dependencies are included in requirements.txt:

Bash

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
4. Run the Web App
Bash

python app.py
Go to http://localhost:5000 in your browser.

🌐 Deployed Application
You can access the live version of the application here:

https://infosys-intern-llm.onrender.com

💻 Usage
Use the Generate Tweet tab to create highly engaging, on-brand tweets.

Use the Compare Tweets tab to see two model outputs side-by-side, with AI-powered analysis and prediction of the winner.

🧠 How It Works
Collects tweets and engagement data for your brand using the X API.

Analyzes tweets with the Gemini API for sentiment, keywords, and engagement insights.

Selects your brand’s top-performing tweets as few-shot examples.

Uses these examples to guide the Gemini model to generate and compare tweets specifically tuned for your brand voice and audience.

👨‍💻 Contributing
Fork the repository.

Make a branch (git checkout -b feature/my-feature).

Commit your changes.

Push and open a Pull Request!

📄 License
This project is licensed under the MIT License.

📫 Questions?
Feel free to open an issue or submit a pull request.

Inspired by the growing need for AI-driven brand engagement optimization
