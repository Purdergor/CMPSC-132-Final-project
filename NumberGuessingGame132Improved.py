import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number guessing game")
        self.setStyleSheet("background-color: #1e2030;")
        
        self.button1 = QPushButton("Easy",self)
        self.button2 = QPushButton("Medium",self)
        self.button3 = QPushButton("Hard",self)
        self.button4 = QPushButton("Submit",self)
        self.button4.hide()
    
        
        self.line_edit = QLineEdit(self)
        self.line_edit.hide()
        
        self.label = QLabel("Welcome pick a mode",self)
        #required dict
        self.difficulty_settings = {
    "Easy": {"min": 1, "max": 10, "color": "#8aadf4"},
    "Medium": {"min": 1, "max": 100, "color": "#eed49f"},
    "Hard": {"min": 1, "max": 1000, "color": "#ed8796"}
}
        self.setGeometry(700,300,500,500)
        self.initUI()
        
    def initUI(self):
        self.button1.setGeometry(150,100,200,100)
        self.button1.setStyleSheet("font-size: 30px; color: #ed8796; background-color: #8aadf4;")
        self.button1.clicked.connect(lambda: self.start_game(1,10,"Easy")) #To temp store this value since you only click the button once
        
        self.button2.setGeometry(150,200,200,100)
        self.button2.setStyleSheet("font-size: 30px; color: #b7bdf8; background-color: #eed49f;")
        self.button2.clicked.connect(lambda: self.start_game(1,100,"medium",))
        
        self.button3.setGeometry(150,300,200,100)
        self.button3.setStyleSheet("font-size: 30px; color:#91d7e3; background-color:#ed8796;")
        self.button3.clicked.connect(lambda: self.start_game(1,1000,"hard"))
        
        self.label.setGeometry(10,70,400,50)
        self.label.setStyleSheet("font-size: 15px; color:#cad3f5")
        
    def start_game(self, low, high, level_name):
        # Set the numbers based on what the button passed in
        self.lowest_num = low
        self.highest_num = high
        self.guess = 0
        self.answer = random.randint(self.lowest_num, self.highest_num)
        
        # UI Updates
        #print(f"Button Clicked: {level_name}") This was for debugging
        self.label.setText(level_name)
        
        # Hide the selection buttons
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.button4.show()
        self.line_edit.show()
        
       
        self.line_edit.setGeometry(10, 10, 200, 50)
        self.button4.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size:25px; font-family:Arial; color:#cad3f5;")
        self.button4.setStyleSheet("font-size:25px; font-family:Arial; color:#b8c0e0; background-color:#363a4f;")
        
        self.line_edit.setPlaceholderText("Enter your guess")
        
        # Reset the submit button connection
        try: 
            self.button4.clicked.disconnect()
        except: 
            pass 
        self.button4.clicked.connect(self.process_guess)
    
    def process_guess(self):
        text_input = self.line_edit.text()  
        if text_input.isdigit():
            guess = int(text_input)
            self.guess += 1

            if guess < self.lowest_num or guess > self.highest_num:
                self.label.setText("out of bounds")
                self.label.setText(f"Select a number {self.lowest_num} and {self.highest_num}")
            elif guess < self.answer:
                self.label.setText("Too low! Try again!")
            elif guess > self.answer:
                self.label.setText("Too high! Try again!")
            else:
                self.label.setText(f"CORRECT! The answer was {self.answer} you got that in {self.guess} guesses")
                self.button4.setDisabled(True)

        else:
            self.label.setText("Invalid guess")
            
        self.line_edit.clear()
                
        
                   

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()