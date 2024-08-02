import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class DateTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Date and Time Entry App")
        self.root.geometry("700x500")
        
        # Date Entry
        self.calendar_label = ttk.Label(root, text="Select Date:")
        self.calendar_label.pack(pady=5)
        
        self.calendar = Calendar(root, selectmode='day', date_pattern='dd-mm-y')
        self.calendar.pack(pady=5)
        
        # Time Entry
        self.time_label = ttk.Label(root, text="Select Time (HH:MM AM/PM):")
        self.time_label.pack(pady=5)
        
        self.time_frame = ttk.Frame(root)
        self.time_frame.pack(pady=5)
        
        self.hour_spinbox = ttk.Spinbox(self.time_frame, from_=1, to=12, wrap=True, width=2, format="%02.0f")
        self.hour_spinbox.pack(side='left', ipadx=5)
        
        self.colon_label = ttk.Label(self.time_frame, text=":")
        self.colon_label.pack(side='left', padx=1)
        
        self.minute_spinbox = ttk.Spinbox(self.time_frame, from_=0, to=59, wrap=True, width=2, format="%02.0f")
        self.minute_spinbox.pack(side='left', ipadx=5)
        
        self.period_var = tk.StringVar(value='AM')
        self.period_combobox = ttk.Combobox(self.time_frame, textvariable=self.period_var, values=['AM', 'PM'], width=3)
        self.period_combobox.pack(side='left', padx=10)
        
        # Submit Button
        self.submit_button = ttk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)
        
        # Result Label
        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def submit(self):
        date = self.calendar.get_date()
        hour = self.hour_spinbox.get()
        minute = self.minute_spinbox.get()
        period = self.period_var.get()
        date_time = f"Date: {date}, Time: {hour}.{minute} {period}"
        self.result_label.config(text=date_time)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = DateTimeApp(root)
    root.mainloop()
