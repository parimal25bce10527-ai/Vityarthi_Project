# Vityarthi_Project
Lyrics_Search_Assistant
Here is the **humanized README** updated with the line that you used the **`lyricgenius` module** for fetching lyrics.

---

# **Lyrics Search Assistant 🎵**

The **Lyrics Search Assistant** is a simple and fun Python project.
**Type a song name or artist, and get the lyrics instantly.**

To make this possible, I used the **`lyricgenius` Python module**, which allows the program to fetch lyrics directly from the Genius API.

---

## **🌟 What This Project Does**

* Lets you **search for lyrics** using a song name, keyword, or artist
* Fetches lyrics using the **`lyricgenius` module**
* Displays full lyrics in a clean, readable way
* Handles errors politely (like “lyrics not found”)
* Works completely in the **command line**

---

## **🧰 Technologies Used**

* **Python 3**
* **`lyricgenius` module** (for fetching lyrics)
* `requests` (dependency for API communication)

---

## **📁 Project Structure**

```
Lyrics Search Assistant/
│
├── main.py
├── lyrics_fetcher.py
├── data/
├── README.md
└── requirements.txt
```

---

## **🚀 How to Run the Project**

1. Install Python 3.
2. Install the required modules:

```
pip install lyricgenius
pip install -r requirements.txt     # if you included one
```

3. Run the program:

```
python main.py
```

---

## **🔍 How It Works (Simple Explanation)**

1. The program asks what song or artist you want.
2. It uses **`lyricgenius`** to connect to the Genius API and fetch the lyrics.
3. If the lyrics exist, they’re shown on screen.
4. If not, the program informs you and asks again.

The flow is simple and user-friendly.

---

## **📝 Example Interaction**

```
Enter song name: Believer
Searching with lyricgenius...
Lyrics found!

"First things first
I'ma say all the words inside my head..."
```

---

## **📚 What I Learned From This Project**

* How to use third-party Python modules
* How APIs work behind the scenes
* Creating clean, modular Python code
* Input validation & error handling

This project really helped me improve my confidence with Python.

---

## **🚀 Future Ideas**

* GUI using Tkinter
* Voice-based search
* Save favourite lyrics
* Offline lyrics database
* Better search recommendations

---

## **👨‍💻 Developed By**

**Parimal Swami**
Lyrics Search Assistant 
