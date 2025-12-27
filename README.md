# JARVIS - Voice-Activated Personal Assistant

A Python-based voice-activated personal assistant inspired by the AI from Iron Man. JARVIS is designed to help you with various tasks through natural language voice commands.

## Features

- **Voice Recognition**: Listen to and understand voice commands using Google's speech recognition API
- **Text-to-Speech**: Natural voice responses using Windows SAPI5 text-to-speech engine
- **Greeting System**: Time-aware greetings (Good Morning/Afternoon/Evening)
- **Alarm Management**: Set and manage alarms with voice commands
- **News Updates**: Get the latest news from various categories (Business, Entertainment, Health, Science, Sports)
- **Calculations**: Advanced mathematical queries using WolframAlpha API
- **Web Search**: Search the internet, Wikipedia, and YouTube through voice commands
- **Keyboard Control**: Automated keyboard interactions for various tasks
- **Memory System**: Remember and retrieve important information

## Project Structure

```
JARVIS/
├── Jarvis_main.py          # Main entry point for the application
├── greetME.py              # Greeting module with time-aware responses
├── alarm.py                # Alarm management system
├── news.py                 # News fetching module
├── Calculatenumbers.py     # Mathematical calculations using WolframAlpha
├── SearchNow.py            # Web search and information retrieval
├── keyboard.py             # Keyboard automation module
├── Dictapp.py              # Dictionary/definitions module
├── Remember.txt            # Storage for remembered information
├── Alarmtext.txt           # Alarm configuration file
└── __pycache__/            # Python cache files
```

## Requirements

### Dependencies

```
pyttsx3              # Text-to-speech conversion
SpeechRecognition    # Voice command recognition
requests             # HTTP requests for APIs
beautifulsoup4       # Web scraping
pyautogui            # Keyboard and mouse automation
wolframalpha         # Advanced calculations
pywhatkit            # YouTube and web search integration
wikipedia            # Wikipedia queries
```

### System Requirements

- Python 3.6+
- Windows OS (due to SAPI5 text-to-speech engine)
- Microphone for voice input
- Internet connection for most features

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/siddhntt/JARVIS.git
   cd JARVIS
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**
   - WolframAlpha API: Sign up at [wolframalpha.com](https://www.wolframalpha.com/api)
   - News API: Sign up at [newsapi.org](https://newsapi.org)
   - Add your API keys to the respective modules

## Usage

### Starting JARVIS

```bash
python Jarvis_main.py
```

### Voice Commands

Once JARVIS is running, you can use the following types of commands:

- **"Wake up"** - Greets you based on the time of day
- **"Set an alarm for [time]"** - Creates an alarm for the specified time
- **"Get latest news [category]"** - Fetches news from specified category
- **"Calculate [mathematical expression]"** - Uses WolframAlpha to solve complex calculations
- **"Search [query]"** - Searches the web or Wikipedia
- **"Remember [information]"** - Stores information for later retrieval
- **"What did I tell you to remember?"** - Retrieves stored information

## Module Descriptions

### Jarvis_main.py
The core module that orchestrates all functionality. It handles:
- Voice input capture using Google Speech Recognition
- Command processing and routing
- Integration of all sub-modules

### greetME.py
Time-aware greeting system that:
- Detects the current time
- Provides appropriate greetings
- Uses text-to-speech for voice output

### alarm.py
Alarm management with:
- Voice command parsing for time extraction
- Alarm storage and scheduling
- Audio notification system

### news.py
Fetches latest news from multiple categories:
- Business
- Entertainment
- Health
- Science
- Sports

Uses the News API for data retrieval.

### Calculatenumbers.py
Advanced calculation module using WolframAlpha:
- Solves complex mathematical problems
- Provides step-by-step solutions
- Handles scientific and statistical queries

### SearchNow.py
Multi-source search functionality:
- Web search via PyWhatKit
- Wikipedia queries
- YouTube video search

## Configuration

### API Keys
Update the API keys in the respective modules:

1. **WolframAlpha** (in Calculatenumbers.py):
   ```python
   apikey = "YOUR_WOLFRAM_API_KEY"
   ```

2. **News API** (in news.py):
   ```python
   apikey = "YOUR_NEWS_API_KEY"
   ```

## Troubleshooting

### Microphone Issues
- Ensure your microphone is connected and properly configured
- Adjust `energy_threshold` and `pause_threshold` in the code if recognition is poor

### Speech Recognition Errors
- Speak clearly and at a normal pace
- Ensure stable internet connection for Google Speech Recognition
- Try adjusting the audio settings

### API Issues
- Verify API keys are correctly configured
- Check internet connectivity
- Ensure API quotas haven't been exceeded

## Future Enhancements

- [ ] Cross-platform support (Linux, macOS)
- [ ] Machine learning for personalized responses
- [ ] Integration with smart home devices
- [ ] Calendar and scheduling functionality
- [ ] Email and messaging capabilities
- [ ] Weather forecasting
- [ ] Traffic updates
- [ ] Stock market updates

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This is an educational project inspired by the JARVIS character from Marvel's Iron Man. It's designed for personal use and experimentation with voice recognition and natural language processing.

## Acknowledgments

- Google Speech Recognition API
- Microsoft SAPI5 Text-to-Speech
- WolframAlpha for computational knowledge
- NewsAPI for news aggregation
- Wikipedia API for information retrieval

## Author

Created as a personal voice assistant project.

---

**Note:** Ensure you have the necessary API keys and permissions before running this project. Some features require API calls which may have usage limits and associated costs.
