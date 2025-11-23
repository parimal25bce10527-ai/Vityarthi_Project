import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import lyricsgenius

# Paste token here
TOKEN = "1m5_29XHfEjgPfsyAHzw7-PGsosrAKJBvNuhqVDEwZSfH5I6vRbitqNDW7Z5TZHZ"

class LyricsApp:
    def __init__(self, window):
        self.window = window
        self.window.title("My Lyrics Finder")
        self.window.geometry("500x600")
        self.window.configure(bg="lightgray")

        # Title
        self.title_lbl = tk.Label(window, text="Lyrics Searcher", font=("Arial", 16, "bold"), bg="lightgray")
        self.title_lbl.pack(pady=15)

        # Input area
        self.frame = tk.Frame(window, bg="lightgray")
        self.frame.pack(pady=5)

        tk.Label(self.frame, text="Song Name:", bg="lightgray").grid(row=0, column=0, padx=5)
        self.entry_song = tk.Entry(self.frame, width=25)
        self.entry_song.grid(row=0, column=1, padx=5)

        tk.Label(self.frame, text="Artist:", bg="lightgray").grid(row=1, column=0, padx=5)
        self.entry_artist = tk.Entry(self.frame, width=25)
        self.entry_artist.grid(row=1, column=1, padx=5)

        # Search Button
        self.btn_search = tk.Button(window, text="Find Lyrics", command=self.get_lyrics, bg="white")
        self.btn_search.pack(pady=15)

        # Text box for results
        self.txt_box = scrolledtext.ScrolledText(window, width=55, height=20)
        self.txt_box.pack(pady=5)

        # Save Button
        self.btn_save = tk.Button(window, text="Save to File", command=self.save_lyrics, bg="white")
        self.btn_save.pack(pady=5)

    def get_lyrics(self):
        # Get data from entries
        s_name = self.entry_song.get()
        a_name = self.entry_artist.get()

        if s_name == "" or a_name == "":
            messagebox.showwarning("Warning", "Please fill in all fields")
            return

        try:
            genius = lyricsgenius.Genius(TOKEN)
            # search for the song
            song = genius.search_song(s_name, a_name)

            self.txt_box.delete(1.0, tk.END) # clear old text

            if song:
                result = f"Title: {song.title}\nArtist: {song.artist}\n\n"
                result += song.lyrics
                self.txt_box.insert(tk.INSERT, result)
            else:
                self.txt_box.insert(tk.INSERT, "Song not found!")

        except:
            messagebox.showerror("Error", "Something went wrong with the connection.")

    def save_lyrics(self):
        text_data = self.txt_box.get(1.0, tk.END)
        
        # open save dialog
        f = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        
        if f:
            with open(f, "w", encoding="utf-8") as file:
                file.write(text_data)
            messagebox.showinfo("Saved", "File saved successfully")

# Run the app
root = tk.Tk()
app = LyricsApp(root)
root.mainloop()