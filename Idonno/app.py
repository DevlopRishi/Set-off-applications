import tkinter as tk
from tkinter import ttk
import random
import time
from plyer import notification
import threading

class AnnoyanceApp:
    def __init__(self, master):
        self.master = master
        master.title("Notification Overload App")
        self.master.geometry("300x200")

        self.is_running = False
        self.notification_thread = None
        self.notifications = [
            "Your shoe is untied.",
            "The answer is 42, or is it?",
            "Did you remember to blink?",
            "Cats are probably plotting something...",
            "Your socks don't match.",
            "Is your refrigerator running?",
            "I think I hear a frog.",
            "The sky is a bit blue today.",
            "Please report to your nearest penguin.",
            "I saw a squirrel with a tiny hat.",
            "Have you considered the existential dread?",
            "The banana is probably yellow.",
            "Warning: Low Battery (on your sanity)",
            "Error 404: Purpose Not Found"
        ]
        
        self.start_button = ttk.Button(master, text="Start Annoyance", command=self.start_notifications)
        self.start_button.pack(pady=20)

        self.stop_button = ttk.Button(master, text="Please Make It Stop", command=self.stop_notifications)
        self.stop_button.pack()

    def send_notification(self):
      try:
        while self.is_running:
            content = random.choice(self.notifications)
            notification.notify(
                title="NOA!",
                message=content,
                timeout=5, #Notification will go away after 5 seconds
            )
            time_wait = random.uniform(1, 5)
            time.sleep(time_wait)
      except Exception:
        return

    def start_notifications(self):
        if not self.is_running:
            self.is_running = True
            self.notification_thread = threading.Thread(target=self.send_notification, daemon=True)
            self.notification_thread.start()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_notifications(self):
        if self.is_running:
            # Sometimes fail to stop
            if random.randint(1, 3) == 1: 
              notification.notify(
                    title="NOA!",
                    message="I cannot be stopped!",
                    timeout=5,
                )
              return
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            
root = tk.Tk()
app = AnnoyanceApp(root)
root.mainloop()