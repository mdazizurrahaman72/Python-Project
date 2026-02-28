from datetime import datetime

# ======= FILE PATHS =======
BOOKS_FILE = "data/books.txt"
GENRES_FILE = "data/genres.txt"
REPORT_FILE = "reports/library_report.txt"

SEPARATOR = "|"


# ============================================
#  FILE SETUP
# ============================================

def setup_files():
    """Check if data files exist. If not, create them with defaults."""

    # --- Create genres.txt if missing ---
    try:
        file = open(GENRES_FILE, "r")
        file.close()
    except:
        file = open(GENRES_FILE, "w")
        file.write("Fiction\nNon-Fiction\nSci-Fi\nSelf-Help\nProgramming\nHistory\nBiography\nOther\n")
        file.close()
        print("✓ Genres file created")

    # --- Create books.txt if missing ---
    # TODO: Same pattern — check if file exists
    # If not, create it with the header line: Title|Author|Genre|Year|Status
    pass


# ============================================
#  LOAD DATA FUNCTIONS
# ============================================

def load_genres():
    """Load all genres from genres.txt and return as a list."""
    genres = []
    try:
        file = open(GENRES_FILE, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.strip()
            if line != "":
                genres.append(line)

        return genres

    except FileNotFoundError:
        print("⚠ Genres file not found!")
        return []


def load_all_books():
    """Load all books from books.txt and return as a list of lists."""
    books = []
    # TODO: Open books.txt, skip the header line
    # Split each line by SEPARATOR
    # Only add lines that have exactly 5 parts
    # Return the list of books
    return books


# ============================================
#  HELPER / VALIDATION FUNCTIONS
# ============================================

def display_menu():
    """Show the main menu."""
    print("\n" + "=" * 50)
    print("       📚 LIBRARY BOOK MANAGER 📚")
    print("=" * 50)
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search Books")
    print("4. Update Book Status")
    print("5. Delete a Book")
    print("6. Reading Statistics")
    print("7. Generate Library Report")
    print("8. Exit")
    print("=" * 50)


def get_valid_genre(genres):
    """Show genre list and let user pick one. Return the chosen genre."""
    print("\nAvailable Genres:")
    for i, genre in enumerate(genres, start=1):
        print(f"  {i}. {genre}")

    while True:
        try:
            choice = int(input(f"Select genre (1-{len(genres)}): "))
            if 1 <= choice <= len(genres):
                return genres[choice - 1]
            else:
                print(f"⚠ Please enter a number between 1 and {len(genres)}")
        except ValueError:
            print("⚠ Please enter a valid number!")


def get_valid_year():
    """Ask user for a year and validate it."""
    current_year = datetime.now().year
    while True:
        try:
            year = int(input("Enter publication year: "))
            # TODO: Check if year is between 1000 and current_year
            # If valid, return it as a string
            # If not, print a warning and loop again
            pass
        except ValueError:
            print("⚠ Please enter a valid year!")


def get_valid_status():
    """Let user pick a book status: Available, Reading, or Finished."""
    statuses = ["Available", "Reading", "Finished"]
    print("\nBook Status:")
    for i, status in enumerate(statuses, start=1):
        print(f"  {i}. {status}")

    # TODO: Ask user to pick 1-3, validate, return the chosen status
    pass


def save_book(title, author, genre, year, status):
    """Append one book to books.txt."""
    try:
        file = open(BOOKS_FILE, "a")
        line = SEPARATOR.join([title, author, genre, year, status])
        file.write(line + "\n")
        file.close()
        print("✓ Book saved successfully!")
        return True
    except Exception as error:
        print(f"⚠ Error saving book: {error}")
        return False


def save_all_books(books):
    """Rewrite the entire books.txt with header + all books in the list.
    Use this when you update or delete a book."""
    try:
        file = open(BOOKS_FILE, "w")
        file.write("Title|Author|Genre|Year|Status\n")  # Header

        for book in books:
            line = SEPARATOR.join(book)
            file.write(line + "\n")

        file.close()
        return True
    except Exception as error:
        print(f"⚠ Error saving books: {error}")
        return False


# ============================================
#  MAIN FEATURES
# ============================================

def add_book():
    """Feature 1: Add a new book."""
    print("\n=== ADD A BOOK ===")
    genres = load_genres()
    if not genres:
        print("⚠ No genres available!")
        return

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    # TODO: Get genre using get_valid_genre()
    # TODO: Get year using get_valid_year()
    # TODO: Get status using get_valid_status()
    # TODO: Call save_book() with all the data
    pass


def view_all_books():
    """Feature 2: View all books sorted by title."""
    print("\n=== ALL BOOKS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    # TODO: Sort books alphabetically by title (index 0)
    # Hint: books.sort()  will sort by first element

    # TODO: Loop through books and display each one nicely
    # Show: Title, Author, Genre, Year, Status
    # Print a separator line between books

    # TODO: Print total book count
    pass


def search_books():
    """Feature 3: Search books by keyword."""
    print("\n=== SEARCH BOOKS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    keyword = input("Enter search keyword: ").strip().lower()
    matches = []

    # TODO: Loop through books
    # Check if keyword is in title (index 0), author (index 1), or genre (index 2)
    # Remember: convert to .lower() for case-insensitive search
    # Add matching books to the matches list

    # TODO: If no matches, print "No results found"
    # If matches found, display them
    pass


def update_book_status():
    """Feature 4: Update a book's reading status."""
    print("\n=== UPDATE BOOK STATUS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    # TODO: Show all books with numbers (1, 2, 3...)
    # Let user pick a book by number
    # Show current status of that book
    # Let user pick new status using get_valid_status()
    # Update the book in the list (index 4 = status)
    # Call save_all_books() to rewrite the file
    pass


def delete_book():
    """Feature 5: Delete a book with confirmation."""
    print("\n=== DELETE A BOOK ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    # TODO: Show all books with numbers
    # Let user pick a book by number
    # Show the book details and ask: "Are you sure? (y/n)"
    # If yes, remove from list using books.pop(index) or del books[index]
    # Call save_all_books() to rewrite the file
    pass


def reading_statistics():
    """Feature 6: Show reading stats and genre breakdown."""
    print("\n=== READING STATISTICS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    # --- Count by status ---
    available_count = 0
    reading_count = 0
    finished_count = 0

    # TODO: Loop through books and count each status

    # --- Print status counts ---
    # TODO: Print Available, Reading, Finished counts and total

    # --- Genre breakdown ---
    genre_counts = {}

    # TODO: Loop through books
    # Count how many books are in each genre using the dictionary
    # Hint: Same pattern as category_wise_spending in Finance Manager

    # TODO: Print genre breakdown
    pass


def generate_report():
    """Feature 7: Generate and save a library report."""
    print("\n=== GENERATE LIBRARY REPORT ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    # TODO: Ask user — filter by genre or show all?
    # If filtering, only include books matching that genre
    # Build a report string (like monthly report in Finance Manager)
    # Include: total books, status breakdown, list of books
    # Save to REPORT_FILE
    pass


# ============================================
#  MAIN PROGRAM
# ============================================

def main():
    setup_files()
    print("\n🎉 Welcome to Library Book Manager!")

    while True:
        display_menu()

        try:
            choice = input("\n👉 Enter your choice (1-8): ")

            if choice == "1":
                add_book()

            elif choice == "2":
                view_all_books()

            elif choice == "3":
                search_books()

            elif choice == "4":
                update_book_status()

            elif choice == "5":
                delete_book()

            elif choice == "6":
                reading_statistics()

            elif choice == "7":
                generate_report()

            elif choice == "8":
                print("\n👋 Thank you for using Library Book Manager!")
                print("📚 Happy Reading! Goodbye!")
                break

            else:
                print("⚠ Invalid choice! Please enter a number between 1-8")

        except KeyboardInterrupt:
            print("\n👋 Program interrupted. Goodbye!")
            break

        except Exception as error:
            print(f"⚠ An error occurred: {error}")


main()
