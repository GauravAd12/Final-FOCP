import json
import random
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDesktopWidget

# Load keywords and responses from a JSON file
def load_responses(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Save the chat log to a file
def save_chat_log(log_file, chat_log):
    with open(log_file, 'a') as file:
        for entry in chat_log:
            file.write(f"{entry}\n")

# Generate a random agent name
def generate_agent_name():
    agent_names = ["Gaurav", "Saurav", "Ghanshyam", "Beck", "Sam"]
    return random.choice(agent_names)

# Chatbot application class
class ChatbotApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.responses = load_responses('responses.json')
        self.chat_log = []
        self.agent_name = generate_agent_name()
        self.user_name = None

    def init_ui(self):
        self.setWindowTitle("Chatbot")

        # Get screen dimensions
        screen = QDesktopWidget().screenGeometry()
        width, height = 500, 600
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2

        # Set window geometry
        self.setGeometry(x, y, width, height)

        # Chat display
        self.chat_display = QtWidgets.QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QtGui.QFont("Arial", 12))
        self.chat_display.setGeometry(10, 10, 480, 450)

        # User input
        self.user_input = QtWidgets.QLineEdit(self)
        self.user_input.setFont(QtGui.QFont("Arial", 12))
        self.user_input.setGeometry(10, 470, 380, 40)
        self.user_input.returnPressed.connect(self.handle_user_input)

        # Send button
        self.send_button = QtWidgets.QPushButton("Send", self)
        self.send_button.setFont(QtGui.QFont("Arial", 12))
        self.send_button.setGeometry(400, 470, 90, 40)
        self.send_button.clicked.connect(self.handle_user_input)

        self.show_welcome_message()

    def show_welcome_message(self):
        self.chat_display.append("<p style='color:green;'>Welcome! Please enter your name below:</p>")

    def handle_user_input(self):
        user_text = self.user_input.text().strip()
        if not user_text:
            return

        if not self.user_name:
            self.user_name = user_text
            self.chat_display.append(f"<p style='color:blue;'>You: {self.user_name}</p>")
            self.chat_display.append(f"<p style='color:green;'>Hello {self.user_name}! I am {self.agent_name}, your assistant. How can I help you today?</p>")
            self.user_input.clear()
            return

        self.chat_display.append(f"<p style='color:blue;'>You: {user_text}</p>")
        self.chat_log.append(f"You: {user_text}")
        self.user_input.clear()

        if user_text.lower() in ["bye", "quit", "exit"]:
            self.chat_display.append(f"<p style='color:orange;'>{self.agent_name}: Goodbye {self.user_name}! Have a great day!</p>")
            self.chat_log.append(f"{self.agent_name}: Goodbye {self.user_name}! Have a great day!")
            save_chat_log("chat_log.txt", self.chat_log)
            QtWidgets.QApplication.quit()
            return

        # Random disconnection
        if random.random() < 0.05:
            self.chat_display.append(f"<p style='color:red;'>{self.agent_name}: Oops! I seem to have disconnected. Please try again later.</p>")
            self.chat_log.append(f"{self.agent_name}: Oops! I seem to have disconnected.")
            save_chat_log("chat_log.txt", self.chat_log)
            QtWidgets.QApplication.quit()
            return

        # Check for keywords in the responses
        response_found = False
        for keyword, response in self.responses.items():
            if keyword in user_text.lower():
                self.chat_display.append(f"<p style='color:orange;'>{self.agent_name}: {response.replace('{name}', self.user_name)}</p>")
                self.chat_log.append(f"{self.agent_name}: {response.replace('{name}', self.user_name)}")
                response_found = True
                break

        # Default random response
        if not response_found:
            random_response = random.choice(self.responses["random"])
            self.chat_display.append(f"<p style='color:orange;'>{self.agent_name}: {random_response}</p>")
            self.chat_log.append(f"{self.agent_name}: {random_response}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    chatbot_app = ChatbotApp()
    chatbot_app.show()
    sys.exit(app.exec_())
