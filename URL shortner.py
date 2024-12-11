import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# Dictionary to store URL mappings
url_mapping = {}

def generate_short_url():
    """Generates a random 6-character short URL."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url():
    """Shortens the entered URL and displays the result."""
    original_url = entry_url.get().strip()
    if not original_url:
        messagebox.showerror("Error", "Please enter a URL!")
        return
    
    # Check if the URL is already shortened
    for short, original in url_mapping.items():
        if original == original_url:
            short_url = f"http://short.ly/{short}"
            display_result(short_url)
            return
    
    # Generate a new short URL
    short_url = generate_short_url()
    url_mapping[short_url] = original_url
    display_result(f"http://short.ly/{short_url}")

def expand_url():
    """Expands the entered short URL and displays the original URL."""
    short_url = entry_url.get().strip()
    if not short_url.startswith("http://short.ly/"):
        messagebox.showerror("Error", "Please enter a valid short URL!")
        return
    
    short_key = short_url.split("/")[-1]
    original_url = url_mapping.get(short_key)
    if original_url:
        display_result(original_url)
    else:
        result_label.config(text="Short URL not found!")
        copy_button.pack_forget()

def display_result(url):
    """Displays the URL result and shows the copy button."""
    result_label.config(text=url)
    copy_button.pack(pady=10)

def copy_to_clipboard():
    """Copies the displayed result to the clipboard."""
    result = result_label.cget("text")
    if result:
        app.clipboard_clear()
        app.clipboard_append(result)
        app.update()  # Keeps the clipboard content after the app is closed
        messagebox.showinfo("Copied", "URL copied to clipboard!")

# Create the main application window
app = tk.Tk()
app.title("URL Shortener")
app.geometry("500x400")
app.resizable(False, False)

# Style configuration
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("Title.TLabel", font=("Helvetica", 16, "bold"), foreground="#333")
style.configure("Result.TLabel", font=("Helvetica", 12, "italic"), foreground="blue")

# Title
title_label = ttk.Label(app, text="URL Shortener App", style="Title.TLabel")
title_label.pack(pady=20)

# Input frame
frame = ttk.Frame(app, padding=(20, 10))
frame.pack(pady=10)

url_label = ttk.Label(frame, text="Enter your URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

entry_url = ttk.Entry(frame, width=40)
entry_url.grid(row=0, column=1, padx=5, pady=5)

# Buttons
button_frame = ttk.Frame(app, padding=(20, 10))
button_frame.pack(pady=10)

shorten_button = ttk.Button(button_frame, text="Shorten URL", command=shorten_url)
shorten_button.grid(row=0, column=0, padx=10, pady=5)

expand_button = ttk.Button(button_frame, text="Expand URL", command=expand_url)
expand_button.grid(row=0, column=1, padx=10, pady=5)

# Result label
result_label = ttk.Label(app, text="", style="Result.TLabel", wraplength=450, anchor="center")
result_label.pack(pady=20)

# Copy button (initially hidden)
copy_button = ttk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack_forget()

# Footer
footer_label = ttk.Label(app, text="Parth Darda", style="TLabel")
footer_label.pack(side="bottom", pady=10)

# Run the application
app.mainloop()