# Chatbot Application

Welcome to the **Chatbot Application**! This is an interactive, GUI-based chatbot program designed to simulate a conversational assistant. Built with Python and PyQt5, it is both engaging and user-friendly, with a simple yet effective design. Here's everything you need to know about the application.

---

## **Features**

### 1. **Dynamic Conversations**
- Responds to user input based on predefined keywords.
- Includes random responses to keep conversations engaging and fresh.

### 2. **Personalized Chat**
- The chatbot greets you by your name and remembers it throughout the session.
- Uses a randomly generated agent name to make interactions feel more human.

### 3. **Realism**
- Introduces a 5% chance of random disconnection to simulate real-life challenges.

### 4. **Graphical User Interface (GUI)**
- Built with PyQt5 for an intuitive and responsive interface.
- Includes:
  - A chat display for viewing conversations.
  - An input field for typing messages.
  - A send button for ease of use.

### 5. **Chat History Logging**
- Saves the chat log to a text file (`chat_log.txt`) for later reference.

---

## **How It Works**

### **1. Initialization**
- Loads predefined responses from a `responses.json` file.
- Generates a random agent name from a list.

### **2. User Interaction**
- Starts with a welcome message and asks for your name.
- Handles input dynamically, checking for keywords, random responses, or exit commands.

### **3. Response Mechanism**
- Matches keywords in the input to provide predefined responses.
- Defaults to random responses if no match is found.

### **4. Exit and Save**
- Ends the session when you type "bye," "quit," or "exit."
- Logs the conversation to `chat_log.txt` before closing.

---

## **Getting Started**

### **Prerequisites**
- Python 3.x
- PyQt5 library

### **Setup Instructions**
1. Clone or download this repository.
2. Ensure Python 3.x is installed on your system.
3. Install PyQt5 by running:
   ```bash
   pip install pyqt5
   ```
4. Place your `responses.json` file in the same directory as the script. The file should contain a dictionary of keywords and responses in the following format:
   ```json
   {
       "hello": "Hi there! How can I assist you?",
       "help": "Sure! What do you need help with?",
       "random": [
           "I'm here to chat!",
           "Can you tell me more?",
           "Interesting!"
       ]
   }
   ```

### **Running the Application**
1. Open a terminal in the project directory.
2. Run the following command:
   ```bash
   python chatbot.py
   ```
3. Interact with the chatbot through the GUI.

---

## **File Structure**
- **chatbot.py**: Main application file.
- **responses.json**: JSON file containing predefined keywords and responses.
- **chat_log.txt**: File where chat logs are saved (created after first run).

---

## **Demo**
### Chat Interface
- Displays the conversation in a clear, readable format.
- Includes a text input field and a send button.

![Chatbot GUI Screenshot](#) *(Add screenshot if available)*

---

## **Contributing**
We welcome contributions! If you'd like to improve this chatbot or add new features, follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes and push them to your fork.
4. Open a pull request.

---

## **License**
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

---

## **Contact**
If you have any questions or feedback, feel free to reach out via [Your Contact Information].

---




