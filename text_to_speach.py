from tkinter import Tk, Label, Entry, messagebox
from tkinter import ttk
from gtts import gTTS
from playsound import playsound
import os

# Function to play the entered text
def delete_file():
    if os.path.exists("output.mp3"):
        os.remove("output.mp3")

def play_text():
    delete_file()
    text = text_entry.get()
    if text.strip() == "":
        messagebox.showerror("Error", "Text field is empty. Please enter some text.")
    tts = gTTS(text)
    tts.save("output.mp3")
    playsound("output.mp3")


def set_text():
        text_entry.delete(0, 'end')
        text_entry.focus()
def exit_app():
    delete_file()
    root.quit()
root = Tk()
root.title("Text to Speech")
root.geometry("400x200")

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True)

label = ttk.Label(main_frame, text="Text to Speech", font=("Arial", 16))
label.pack(pady=10)

text_entry = ttk.Entry(main_frame, width=50, font=("Arial", 12))
text_entry.pack(pady=5)

buttons_frame = ttk.Frame(main_frame)
buttons_frame.pack(pady=10)

play_button = ttk.Button(buttons_frame, text="Play", command=play_text)
play_button.grid(row=0, column=0, padx=10)
play_button.configure(style="Green.TButton")

set_button = ttk.Button(buttons_frame, text="Set", command=set_text)
set_button.grid(row=0, column=1, padx=10)
set_button.configure(style="BlueBackground.TButton")

exit_button = ttk.Button(buttons_frame, text="Quit", command=exit_app)
exit_button.grid(row=0, column=2, padx=10)
exit_button.configure(style="RedBackground.TButton")

style = ttk.Style()
style.configure("Green.TButton", background="green", foreground="black")
style.configure("BlueBackground.TButton", background="blue", foreground="black")
style.configure("RedBackground.TButton", background="red", foreground="black")

root.mainloop()