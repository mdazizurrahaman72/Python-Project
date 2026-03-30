from datetime import datetime
import os

os.makedirs("DATA", exist_ok=True)
os.makedirs("REPORTS", exist_ok=True)

# ======= FILE PATHS =======
BOOKS_FILE = "DATA/books.txt"
GENRES_FILE = "DATA/genres.txt"
REPORT_FILE = "REPORTS/library_report.txt"

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
    try:
        file = open(BOOKS_FILE,"r")
        file.close()
    except:
        file = open(BOOKS_FILE,"w")
        file.write("Title|Author|Genre|Year|Status\n")
        file.close()
        print("✓ Books file created")


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
    try:
        with open(BOOKS_FILE,"r") as file:
            lines = file.readlines()

            for i,line in enumerate(lines):
                if i == 0:
                    continue
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(SEPARATOR)
                books.append(parts)
            return books
    except:
        return []


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
            if 1000 <= year <= current_year:
                return str(year)
            else:
                print(f"⚠ Year must be between 1000 and {current_year}!")
        except ValueError:
            print("⚠ Please enter a valid year!")


def get_valid_status():
    """Let user pick a book status: Available, Reading, or Finished."""
    statuses = ["Available", "Reading", "Finished"]
    print("\nBook Status:")
    for i, status in enumerate(statuses, start=1):
        print(f"  {i}. {status}")

    while True:
        try:
            choice = int(input("Choose status (1-3): "))
            if 1 <= choice <= 3:
                return statuses[choice - 1]
            else:
                print("⚠ Please enter a number between 1 and 3!")
                    
        except ValueError:
            print("⚠ Invalid input! Please enter a number.")


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
    genre = get_valid_genre(genres)
    year = get_valid_year()
    status = get_valid_status()
    save_book(title,author,genre,year,status)


def view_all_books():
    """Feature 2: View all books sorted by title."""
    print("\n=== ALL BOOKS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    books.sort(key=lambda x:x[0],reverse=True)

    for book in books:
        print(f"Titel : {book[0]}")
        print(f"Author : {book[1]}")
        print(f"Cenre : {book[2]}")
        print(f"Year : {book[3]}")
        print(f"Status : {book[4]}")
        print("-"*40)

    print(f"Total Books : {len(books)}")


def search_books():
    """Feature 3: Search books by keyword."""
    print("\n=== SEARCH BOOKS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    keyword = input("Enter search keyword: ").strip().lower()

    if keyword == "":
        print("⚠ Please enter a keyword!")
        return
    
    matches = []

    for book in books:
        titel = book[0].lower()
        author = book[1].lower()
        genre = book[2].lower()

        if keyword in titel or keyword in author or keyword in genre:
            matches.append(book)
    
    if len(matches) == 0:
        print("No results found for '" + keyword + "'")
        return  
    
    print("\nFound", len(matches), "matching Books(s):\n")
    for book in matches:
        print(f"Title : {book[0]}")
        print(f"Author : {book[1]}")
        print(f"Genre : {book[2]}")
        print(f"Year : {book[3]}")
        print(f"Status : {book[4]}")
        print("-"*40)


def update_book_status():
    """Feature 4: Update a book's reading status."""
    print("\n=== UPDATE BOOK STATUS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    for index, book in enumerate(books,1):
        print(f"{index}. {book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]}")
    
    try:
        choice = int(input(f"Pick book number you update book(1 - {len(books)}): "))
        if 1 <= choice and choice <= len(books):
            select_book = books[choice-1]

            print(f"\nCurrent Book Status : {select_book[4]}")
            new_status = get_valid_status()

            select_book[4] = new_status
            print("✅ Book status updated successfully!")
            
            save_all_books(books)
        else:
            print("❌ Invalid choice!")
    except ValueError:
        print("❌ Please enter a valid number!")


def delete_book():
    """Feature 5: Delete a book with confirmation."""
    print("\n=== DELETE A BOOK ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    for index, book in enumerate(books,1):
        print(f"{index}. {book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]}")

    try:
        choice = int(input(f"Pick book number you delete book(1 - {len(books)}): "))

        if 1 <= choice and choice <= len(books):
            permution = input("Are you sure?(yes/no): ").lower()

            if permution == "yes":
                books.pop(choice-1)
                save_all_books(books)
                print("✅ Book status delete successfully!")
            else:
                print("ok")
        else:
            print("❌ Invalid choice!")
            
    except ValueError:
        print("❌ Please enter a valid number!")


def reading_statistics():
    """Feature 6: Show reading stats and genre breakdown."""
    print("\n=== READING STATISTICS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    status = []

    # --- Count by status ---
    available_count = 0
    reading_count = 0
    finished_count = 0

    for book in books:
        status.append(book[4])
    
    available_count = status.count("Available")
    reading_count = status.count("Reading")
    finished_count = status.count("Finished")
    total = len(books)

    print("\n📊 Status Overview:")
    print(f"Available: {available_count}")
    print(f"Reading: {reading_count}")
    print(f"Finished: {finished_count}")
    print(f"Total Books: {total}")
    
    # --- Genre breakdown ---
    genre_counts = {}

    for book in books:
        genre = book[2]   # assuming genre is index 2

        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

    # --- Print genre breakdown ---
    print("\n📚 Genre Breakdown:")
    for genre, count in genre_counts.items():
        print(f"{genre}: {count}")


def generate_report():
    """Feature 7: Generate and save a library report."""
    print("\n=== GENERATE LIBRARY REPORT ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    print("\n1. Show All Books")
    print("2. Filter by Genre")
    choice = input("Enter choice (1/2): ")

    filtered_books = books

    if choice == "2":
        genre_filter = input("Enter genre: ").strip()
        filtered_books = [book for book in books if book[2].lower() == genre_filter.lower()]

        if len(filtered_books) == 0:
            print("No books found for this genre!")
            return

    # --- Status count ---
    available = 0
    reading = 0
    finished = 0

    for book in filtered_books:
        if book[4] == "Available":
            available += 1
        elif book[4] == "Reading":
            reading += 1
        elif book[4] == "Finished":
            finished += 1

    total = len(filtered_books)

    # --- Build report string ---
    report = ""
    report += "===== LIBRARY REPORT =====\n\n"
    report += f"Date: {datetime.now().strftime('%Y-%B-%d')}\n\n"

    report += f"Total Books: {total}\n"
    report += f"Available: {available}\n"
    report += f"Reading: {reading}\n"
    report += f"Finished: {finished}\n\n"

    report += "----- BOOK LIST -----\n"

    for i, book in enumerate(filtered_books, start=1):
        report += f"{i}. Title: {book[0]} | Author: {book[1]} | Genre: {book[2]} | Year: {book[3]} | Status: {book[4]}\n"

    # --- Save to file ---
    with open(REPORT_FILE, "w") as file:
        file.write(report)

    print("\n✅ Report generated successfully!")
    print(f"Saved to: {REPORT_FILE}")

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