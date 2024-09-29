import os
import pickle
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import self
from tkcalendar import DateEntry


class event:
    def _init_(self, data_layer):
        self._id = None
        self._time = None
        self._date = None
        self._eventID = None
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("event information ")
        # entry for event id
        self.eventID_label = tk.Label(self.root, text="Event ID:")
        self.eventID_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.eventID_entry = tk.Entry(self.root)
        self.eventID_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        # entry for event type
        self.eventType_label = tk.Label(self.root, text="Event type:")
        self.eventType_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.eventType_entry = tk.Entry(self.root)
        self.eventType_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        # selecting date
        self.date_label = tk.Label(self.root, text="Date:")
        self.date_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.date_entry = DateEntry(self.root)
        self.date_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        # selecting time
        self.time_label = tk.Label(self.root, text="Time:")
        self.time_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.time_entry = ttk.Combobox(self.root, values=["10:00 AM", "12:00 PM", "6:00 PM", "8:00 PM"])
        self.time_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        # submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

    def clearboxes(self):
        self.eventID_entry.delete(0, tk.END)
        self.eventType_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

    def submit(self):
        event_id = self.eventID_entry.get()
        event_type = self.eventType_entry.get()
        date: str = self.date_entry.get()
        time = self.time_entry.get()
        event_info = f"Event ID: {event_id}\nEvent Type: {event_type}\nDate: {date}\nTime: {time}"
        tk.messagebox.showinfo("Event Information", event_info)

        if date in self.data_layer.get_all_events():  # Move this check inside the method
            tk.messagebox.showinfo("booking successful", f"The selected '{date}' has been booked successfully.")
            self.data_layer.add_event(date)
            self.clearboxes()
        else:
            tk.messagebox.showinfo("booking failed", f"The selected date '{date}' has already been booked for an event")

    class Listevent:

        def _init_(self, data_layer):
            self.data_layer = data_layer

        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title("Event details")
        # create the table
        self.table = ttk.Treeview(self.root, columns=('Event ID', 'Event Type',
                                                      'Date', 'Time'), show='headings')
        self.table.heading('Event ID', text='Event ID')
        self.table.heading('Event Type', text='Event type')
        self.table.heading('Date', text='Date')
        self.table.heading('Time', text='Time')
        self.table.pack(pady=20)
        all_events = self.data_layer.get_all_events()
        for eventID, Events in all_events.items():
            self.table.insert('', 'end',
                              values=(eventID, Events.get_eventType(), Events.get_date(),  Events.get_time()))
        self.root.mainloop()

    class DataLayer:
        def _init_(self, filename):
            self.filename = filename
            self.allevents = set()

        def add_event(self, event_date):
            self.allevents.add(event_date)
            self.write_events_to_file()

        def get_all_events(self):
            return self.allevents

        def read_events_from_file(self):
            if os.path.exists(self.filename):
                with open(self.filename, 'rb') as file:
                    self.allevents = pickle.load(file)

        def write_events_to_file(self):
            with open(self.filename, 'wb') as file:
                pickle.dump(self.allevents, file)

    # Example usage
    if __name__ == "_main_":
        dt = DataLayer("allevents.pkl")
        dt.read_events_from_file()  # Load existing events
        form = Event()
