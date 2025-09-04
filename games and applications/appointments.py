import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# === Database Setup ===
def init_db():
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            doctor TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            UNIQUE(doctor, date, time)
        )
    """)
    conn.commit()
    conn.close()

# === Booking Function ===
def book_appointment():
    name = name_entry.get()
    email = email_entry.get()
    doctor = doctor_combo.get()
    date = date_entry.get()
    time = time_combo.get()

    if not all([name, email, doctor, date, time]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter date as YYYY-MM-DD.")
        return

    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO appointments (name, email, doctor, date, time) VALUES (?, ?, ?, ?, ?)",
                       (name, email, doctor, date, time))
        conn.commit()
        messagebox.showinfo("Success", f"Appointment booked with Dr. {doctor} on {date} at {time}")
    except sqlite3.IntegrityError:
        messagebox.showwarning("Unavailable", "That time slot is already booked for this doctor.")
    finally:
        conn.close()
        clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    doctor_combo.set("")
    date_entry.delete(0, tk.END)
    time_combo.set("")
    
def view_appointments():
    view_window = tk.Toplevel(window)
    view_window.title("Booked Appointments")
    view_window.geometry("600x300")

    tree = ttk.Treeview(view_window, columns=("Name", "Email", "Doctor", "Date", "Time"), show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Email", text="Email")
    tree.heading("Doctor", text="Doctor")
    tree.heading("Date", text="Date")
    tree.heading("Time", text="Time")
    tree.pack(fill="both", expand=True)

    scrollbar = ttk.Scrollbar(view_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Load data from database
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, doctor, date, time FROM appointments ORDER BY date, time")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)
    conn.close()


# === GUI Setup ===
init_db()
window = tk.Tk()
window.title("Doctor Appointment Booking")
window.geometry("400x400")

tk.Label(window, text="Doctor Appointment Booking", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(window, text="Full Name:").pack()
name_entry = tk.Entry(window, width=30)
name_entry.pack()

tk.Label(window, text="Email:").pack()
email_entry = tk.Entry(window, width=30)
email_entry.pack()

tk.Label(window, text="Select Doctor:").pack()
doctor_combo = ttk.Combobox(window, values=["Smith", "Jones", "Lee", "Adams"], state="readonly")
doctor_combo.pack()

tk.Label(window, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(window, width=20)
date_entry.pack()

tk.Label(window, text="Select Time:").pack()
time_combo = ttk.Combobox(window, values=[
    "09:00 AM", "10:00 AM", "11:00 AM", "01:00 PM", "02:00 PM", "03:00 PM"
], state="readonly")
time_combo.pack()

tk.Button(window, text="Book Appointment", command=book_appointment, bg="green", fg="white").pack(pady=15)

tk.Button(window, text="View Appointments", command=view_appointments, bg="blue", fg="white").pack(pady=5)

window.mainloop()
