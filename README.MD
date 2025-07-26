# Gemini Powered Voice Assistant
A Python-based voice assistant that uses the Google Gemini API to understand natural language and execute local commands on a computer.

This project to designed to be an extension of my previous python voice assistant project. This projecct works dynamically without any fixed key words to use functionalities . It separates the AI's natural language understanding from the local system's action execution, allowing for a robust and modular design.

# Features
Natural Language Understanding: Uses the Gemini's Capabilities in converting the complex commands to simpler ones.

Direct Answers: Can answer general knowledge questions and updates directly from the Gemini model.

Local Command Execution:

System Control: Increase/decrease/mute system volume, shut down the computer.

Weather: Fetches the weather forecast from weather api's for a given location

File Navigation: Open specific folders by name.

Web Integration: plays YouTube videos, and open websites.

Modular approach: The system is designed with a functionalities pattern(dictionary of functions), making it easy to add new commands and functions.

# How It Works
The user provides a command (e.g., "open my downloads folder").

A Detailed prompt is prepared that includes a JSON schema of all available commands and their parameters.

This prompt is sent to the Gemini API.

Gemini analyzes the request and returns a structured JSON object containing either a direct answer or a specific code and parameters for a local command.

A Python object  receives this JSON, maps the code to the correct Python function, and executes it with the provided parameters.

# Setup and Installation
Follow the below steps to get the assistant running on your local system.

1. Prerequisites
Python 3.10+

Git

2. Clone the Repository
Open your terminal and clone this repository:

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

3. Install Dependencies
It's recommended to use a virtual environment.

 Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

 Install the required Python libraries
pip install -r requirements.txt

You will need to create a requirements.txt file with the following content:


4. Configuration

🔐 API Keys Required
This project uses external APIs:

1. OpenWeatherMap
Sign up at openweathermap.org
Get your API key
Add it as an environment variable:
$env:OPEN_WEATHER="your_api_key_here"

2. NewsAPI
Sign up at newsapi.org
Replace the placeholder in main.py:
newsapi = "your_news_api_key_here"


3.GeminiAPI
You need to provide your Gemini API key.

Create a file named .env in the root of the project folder.

Add your API key to this file:

GEMINI_API_KEY="your_api_key_here"

⚠️ Important: nircmd.exe
To enable volume control (up/down/mute) and shutdown functionality:

Download nircmd.exe
Place it in the same directory as your Python files 
Without this file, volume and shutdown features will not work.


Make sure that you  have a rules.json file in the project directory that consists of assistant's capabilities, as we designed.

Usage
Run the main script from your terminal:

python main.py

This will start the assistant, which will then listen for or prompt you for a command.
but for now i just have added the text based inputs as it will be easy for testing.

