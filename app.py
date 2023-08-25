import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz App")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin"],
                "correct": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter"],
                "correct": "Mars"
            },
            {
                "question": "What gas do plants use for photosynthesis?",
                "options": ["Oxygen", "Carbon Dioxide", "Nitrogen"],
                "correct": "Carbon Dioxide"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.label = tk.Label(root, text="")
        self.label.pack()
        
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(self.questions[self.current_question]["options"][i]))
            self.option_buttons.append(button)
            button.pack()
        
        self.hint_button = tk.Button(root, text="Hint", command=self.show_hint)
        self.hint_button.pack()
        
        self.timer_label = tk.Label(root, text="Timer: ")
        self.timer_label.pack()
        self.remaining_time = 10  # seconds
        self.update_timer()
        
        self.next_question()
    
    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
            
            self.current_question += 1
            self.remaining_time = 10  # Reset timer for each question
            self.update_timer()
            self.root.after(1000, self.update_timer)  # Start the timer countdown
        else:
            self.show_final_score()
    
    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question - 1]["correct"]
        if selected_option == correct_answer:
            self.score += 1
        self.next_question()
    
    def show_hint(self):
        hint = f"The correct answer is {self.questions[self.current_question - 1]['correct']}"
        messagebox.showinfo("Hint", hint)
    
    def update_timer(self):
        self.timer_label.config(text=f"Timer: {self.remaining_time}s")
        self.remaining_time -= 1
        if self.remaining_time >= 0:
            self.root.after(1000, self.update_timer)
        else:
            self.next_question()
    
    def show_final_score(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
