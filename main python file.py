import tkinter as tk
import time
from datetime import datetime
import threading
import os

class DigitalClockWithAlarm:
    def _init_(self, root):
        self.root = root
        self.root.title("Digital Clock with Alarm")
        self.root.geometry("400x250")
        self.root.config(bg="black")

        self.label_time = tk.Label(self.root, font=("Helvetica", 48), fg="white", bg="black", relief="solid", width=15)
        self.label_time.pack(pady=20)

        self.label_alarm = tk.Label(self.root, font=("Helvetica", 14), fg="white", bg="black", relief="solid", width=20)
        self.label_alarm.pack(pady=10)

        self.alarm_time = None
        self.alarm_set = False

        self.alarm_button = tk.Button(self.root, text="Set Alarm", font=("Helvetica", 14), command=self.set_alarm)
        self.alarm_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", font=("Helvetica", 14), command=self.quit_program)
        self.quit_button.pack(pady=10)

        self.update_clock()

    def update_clock(self):
        """Update the current time and check if the alarm should trigger."""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.label_time.config(text=current_time)

        if self.alarm_set and current_time == self.alarm_time:
            self.trigger_alarm()

        self.root.after(1000, self.update_clock)  # Update every second

    def set_alarm(self):
        """Prompt user to input alarm time."""
        alarm_time_input = tk.simpledialog.askstring("Set Alarm", "Enter alarm time (HH:MM:SS):")

        if alarm_time_input:
            try:
                # Validate the time format
                datetime.strptime(alarm_time_input, "%H:%M:%S")
                self.alarm_time = alarm_time_input
                self.alarm_set = True
                self.label_alarm.config(text=f"Alarm set for: {self.alarm_time}")
            except ValueError:
                self.label_alarm.config(text="Invalid time format! Use HH:MM:SS.")

    def trigger_alarm(self):
        """Trigger the alarm sound."""
        self.label_alarm.config(text="Alarm ringing!")
        self.alarm_set = False
        self.play_alarm_sound()

    def play_alarm_sound(self):
        """Play alarm greeting."""
        greeting = self.get_greeting()
        for _ in range(10):
            os.system(f"say '{greeting}'")  # Use macOS "say" command
            time.sleep(3)  # Wait 3 seconds before repeating

    def get_greeting(self):
        """Return a greeting based on the current time."""
        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            return "Good morning, get up!"
        elif 12 <= current_hour < 17:
            return "Good afternoon, time to get going!"
        else:
            return "Good night, wake up now!"

    def quit_program(self):
        """Quit the program."""
        self.root.quit()

def main():
    root = tk.Tk()
    app = DigitalClockWithAlarm(root)
    root.mainloop()

if _name_ == "_main_":
    main()
