---

# Jeera AI Virtual Assistant

![Jeera Logo](https://via.placeholder.com/150) <!-- Add a logo if available -->

**Jeera** is a Python-based virtual assistant designed to help users perform various tasks using voice commands. It is a lightweight, modular, and customizable assistant that can be used for personal or educational purposes. Jeera is built using Python libraries such as `pyttsx3`, `speech_recognition`, `pywhatkit`, and more, making it easy to extend and modify.

---

## Features

- **Voice Commands**: Jeera can understand and execute voice commands.
- **Task Automation**: Perform tasks like opening websites, playing YouTube videos, searching Wikipedia, and more.
- **Multitasking**: Handle multiple commands sequentially without needing to restart.
- **Offline Functionality**: Works offline for basic tasks like text-to-speech and simple commands.
- **Customizable**: Easily add new features or modify existing ones using Python.

---

## Installation

### Prerequisites

- Python 3.8 or later
- Pip (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShreyasKapse/Jeera-AI-Virtual-Assistant.git
   cd Jeera-AI-Virtual-Assistant
   ```

2. **Install Dependencies**:
   Install the required Python libraries using the following command:
   ```bash
   pip install pyttsx3 speechrecognition datetime wikipedia pywhatkit requests pyjokes wolframalpha opencv-python numpy gTTS
   ```

   Alternatively, you can use the `requirements.txt` file if it is provided in the repository:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

---

### List of Libraries Used

Here are the key libraries used in the project and their purposes:

| Library            | Purpose                                                                 |
|--------------------|-------------------------------------------------------------------------|
| `pyttsx3`          | Text-to-speech conversion (offline).                                    |
| `speech_recognition`| Speech recognition (converts voice to text).                            |
| `datetime`         | Date and time operations (e.g., reminders, greetings).                  |
| `wikipedia`        | Fetching information from Wikipedia.                                    |
| `pywhatkit`        | Sending WhatsApp messages, playing YouTube videos, and Google searches. |
| `requests`         | Making HTTP requests (e.g., fetching data from APIs).                   |
| `pyjokes`          | Generating random jokes.                                                |
| `wolframalpha`     | Accessing Wolfram Alpha for computational knowledge.                    |
| `opencv-python`    | Computer vision tasks (if applicable).                                  |
| `numpy`            | Numerical operations (if applicable).                                   |
| `gTTS`             | Google Text-to-Speech (online text-to-speech conversion).               |

---

## Usage

Once the application is running, you can interact with Jeera using voice commands. Here are some examples of commands you can use:

- **Greet Jeera**: Say "Hello" or "Hi" to start the conversation.
- **Search Google**: Say "Search for Python programming on Google."
- **Play YouTube Videos**: Say "Play [video name] on YouTube."
- **Get Wikipedia Info**: Say "Tell me about Python programming."
- **Set Reminders**: Say "Set a reminder for 5 PM."
- **Exit**: Say "Goodbye" or "Exit" to stop the assistant.

---

## Project Structure

```
Jeera-AI-Virtual-Assistant/
├── main.py               # Main script to run the virtual assistant
├── requirements.txt       # List of dependencies
├── features/               # Custom modules for specific tasks   
├── README.md              # Project documentation
└── database/                # Additional assets (e.g., images, audio)
```

---

## Documentation

For more detailed information about the project, refer to the [Project Report](https://drive.google.com/file/d/1vKNDHWpKSk0D_AbVOdGrSW_r9IZglStR/view?usp=sharing). The report includes:
- **Introduction**: Overview of the project and its objectives.
- **Technical Requirements**: Hardware and software specifications.
- **System Design**: ER diagrams, activity diagrams, and use case diagrams.
- **Testing**: Functionality, usability, and security testing.
- **Future Scope**: Potential enhancements and applications.

---

## Contributing

Contributions are welcome! If you'd like to contribute to Jeera, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to the branch.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Shreyas Kapse** and **Ajinkya Kale** for developing Jeera.
- **Prof. K.M. Vaishnav** for guidance and support.
- All contributors and open-source libraries used in this project.

---

## Contact

For any questions or feedback, feel free to reach out:

- **Shreyas Kapse**: [shreyaskapse1234@gmail.com](mailto:shreyaskapse1234@gmail.com)
- **Ajinkya Kale**: [kaleajinkya2003@gmail.com.com](mailto:kaleajinkya2003@gmail.com)

---

Enjoy using Jeera! 🚀

---

This `README.md` file provides a clear and concise overview of the project, making it easy for users and contributors to understand and use the Jeera AI Virtual Assistant.
