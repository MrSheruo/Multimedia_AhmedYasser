from tkinter import *
from tkinter import messagebox
from yt_dlp import YoutubeDL

# Functions to handle download
def download_high_quality():
    try:
        url = url_entry.get()
        options = {
            'format': 'bestvideo+bestaudio/best',  # Best video and audio available
            'outtmpl': '%(title)s.%(ext)s',       # Save file with title as filename
        }
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "High-quality video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {e}")

def download_low_quality():
    try:
        url = url_entry.get()
        options = {
            'format': 'worstvideo+worstaudio/worst',  # Lowest video and audio available
            'outtmpl': '%(title)s_low_quality.%(ext)s',  # Add '_low_quality' to filename
        }
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Low-quality video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {e}")

def download_audio():
    try:
        url = url_entry.get()
        options = {
            'format': 'bestaudio/best',            # Best audio-only stream available
            'outtmpl': '%(title)s_audio.%(ext)s',  # Add '_audio' to filename
            'postprocessors': [{                  # Convert audio to MP3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Audio downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {e}")

# GUI Setup
root = Tk()
root.geometry("500x500")
root.title("YouTube Downloader")
root.configure(bg="black")

# URL Entry
Label(root, text="Enter Link To Download:", font="Tahoma 25", bg="black", fg="white").pack()
url_entry = Entry(root, width=35, font="Tahoma 15")
url_entry.pack(pady=15)

# Buttons
Button(root, text="High Quality", bg="red", fg="white", font="Tahoma 15", command=download_high_quality).pack(pady=10)
Button(root, text="Low Quality", bg="red", fg="white", font="Tahoma 15", command=download_low_quality).pack(pady=10)
Button(root, text="Audio", bg="red", fg="white", font="Tahoma 15", command=download_audio).pack(pady=10)

root.mainloop()
