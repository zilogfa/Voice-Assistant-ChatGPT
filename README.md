# Voice Assistant

A Python-based voice assistant with the ability to set reminders, manage to-do lists, perform web searches, and more using speech recognition and text-to-speech.

## Features

- **Speech Recognition**: Understands and processes user speech.
- **Text-to-Speech**: Articulates responses and confirmations.
- **Reminders**: Sets reminders for the user.
- **To-Do List**: Potential to manage a user's to-do list (functionality to be implemented).
- **Web Search**: Can perform web searches based on user commands (functionality to be implemented).

## Dependencies

- **speech_recognition**: Recognizes user's speech.
- **pyttsx3**: Text-to-speech conversion library in Python.
- **datetime**: For handling date and time operations.
- **PyAudio**: Required for microphone input.

## Setup

1. Install Python 3.x on your system.
2. Install the required libraries using `pip`:
   ```sh
   pip install speech_recognition pyttsx3 PyAudio
   ```
1. Clone this repository or copy the main.py script to your local machine.
2. Run the script with python main.py.

## Usage
1. Start the assistant and wait for the "Listening..." prompt.
2. Speak a command into your microphone:
- ** Say "reminder" to set a reminder.
- ** Say "to-do list" to manage your to-do list (functionality not yet implemented).
- ** Say "search" to perform a web search (functionality not yet implemented).
- ** Say "exit" or "bye" to terminate the assistant.
3. Follow the voice prompts to provide further details for each command.
