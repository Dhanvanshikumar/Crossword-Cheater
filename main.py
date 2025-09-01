import re

def load_dictionary(file_path="/usr/share/dict/words"):
    """Load words from the Linux dictionary file"""
    words = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                word = line.strip().lower()
                if word.isalpha():
                    words.append(word)
    except FileNotFoundError:
        print("Dictionary file not found. Install it using: sudo apt install wamerican")
    return words

def crossword_cheater(pattern, words):
    """Find words matching the crossword pattern"""
    regex_pattern = "^" + pattern.replace("*", ".") + "$"
    regex = re.compile(regex_pattern)
    matches = [word for word in words if regex.match(word)]
    return matches

if __name__ == "__main__":
    # Load dictionary
    words = load_dictionary()

    if not words:
        print("No words loaded. Please check your dictionary file.")
    else:
        # Ask user for input
        pattern = input("Enter pattern (use * for unknown letters): ").lower().strip()
        matches = crossword_cheater(pattern, words)

        if matches:
            print("\nPossible matches:")
            for word in matches:
                print(word)
        else:
            print("No matches found.")
