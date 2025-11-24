import lyricsgenius
import sys

# Paste token here
TOKEN = "1m5_29XHfEjgPfsyAHzw7-PGsosrAKJBvNuhqVDEwZSfH5I6vRbitqNDW7Z5TZHZ"

def main():
    print("--- Lyrics Searcher (Terminal Version) ---")
    print("Initializing Genius API...")

    try:
        # Initialize Genius
        genius = lyricsgenius.Genius(TOKEN)
        
        print("Ready! Type 'exit' or 'quit' at any time to stop.\n")
    except Exception as e:
        print(f"Error connecting to Genius API: {e}")
        return

    while True:
        print("-" * 40)
        
        # 1. Get Input
        s_name = input("Enter Song Name: ").strip()
        if s_name.lower() in ['exit', 'quit']:
            break
            
        a_name = input("Enter Artist Name: ").strip()
        if a_name.lower() in ['exit', 'quit']:
            break

        # Validation
        if not s_name or not a_name:
            print(">> Warning: Song and Artist fields cannot be empty.")
            continue

        # 2. Search for lyrics
        try:
            print(f"\nSearching for '{s_name}' by '{a_name}'...")
            song = genius.search_song(s_name, a_name)

            if song:
                # 3. Display Results
                print("\n" + "="*20 + " LYRICS FOUND " + "="*20)
                print(f"Title: {song.title}")
                print(f"Artist: {song.artist}")
                print("-" * 40)
                print(song.lyrics)
                print("="*54 + "\n")

                # 4. Ask to Save
                save_choice = input("Do you want to save these lyrics to a file? (y/n): ").lower()
                if save_choice == 'y':
                    save_lyrics_to_file(song)
            else:
                print("\n>> Song not found! Please check the spelling.")

        except Exception as e:
            print(f"\n>> An error occurred: {e}")

    print("Goodbye!")

def save_lyrics_to_file(song):
    clean_title = "".join(x for x in song.title if x.isalnum() or x in " _-").strip()
    default_filename = f"{clean_title}_lyrics.txt"
    
    filename = input(f"Enter filename (press Enter for '{default_filename}'): ").strip()
    
    if not filename:
        filename = default_filename
        
    # Ensure extension exists
    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        # Prepare text data
        text_data = f"Title: {song.title}\nArtist: {song.artist}\n\n{song.lyrics}"
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text_data)
        print(f">> Success: Saved to '{filename}'")
    except Exception as e:
        print(f">> Error saving file: {e}")

if __name__ == "__main__":
    main()

