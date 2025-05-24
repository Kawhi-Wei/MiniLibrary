class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.copies = 1


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}  # title: Book
        self.users = {}  # name: User

    def add_book(self, title, author, category):
        if title in self.books:
            self.books[title].copies += 1
        else:
            self.books[title] = Book(title, author, category)
        print(f"Added '{title}' by {author} to library.")

    def borrow_book(self, user_name, book_title):
        if book_title not in self.books or self.books[book_title].copies == 0:
            print("Book not available.")
            return

        user = self.users.get(user_name, User(user_name))
        self.users[user_name] = user

        user.borrowed_books.append(book_title)
        self.books[book_title].copies -= 1
        print(f"{user_name} has borrowed '{book_title}'.")

    def return_book(self, user_name, book_title):
        user = self.users.get(user_name)
        if not user or book_title not in user.borrowed_books:
            print("Return failed: book not found under user's name.")
            return

        user.borrowed_books.remove(book_title)
        self.books[book_title].copies += 1
        print(f"{user_name} has returned '{book_title}'.")

    def display_inventory(self):
        if not self.books:
            print("No books in inventory.")
            return
        print("\nCurrent Inventory:")
        for book in self.books.values():
            print(f"- {book.title} by {book.author} ({book.copies} available)")

    def display_user_books(self, user_name):
        user = self.users.get(user_name)
        if not user or not user.borrowed_books:
            print("No books found for user.")
            return
        print(f"\n{user.name} has:")
        for title in user.borrowed_books:
            print(f"- {title}")

def main():
    lib = Library()
    print("\nWelcome to MiniLibrary")

    while True:
        print("""
1. Add book
2. Borrow book
3. Return book
4. Show inventory
5. Show user history
0. Exit
        """)
        choice = input("Select an option: ").strip()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")
            lib.add_book(title, author, category)

        elif choice == "2":
            name = input("Enter your name: ")
            title = input("Enter book title to borrow: ")
            lib.borrow_book(name, title)

        elif choice == "3":
            name = input("Enter your name: ")
            title = input("Enter book title to return: ")
            lib.return_book(name, title)

        elif choice == "4":
            lib.display_inventory()

        elif choice == "5":
            name = input("Enter user name: ")
            lib.display_user_books(name)

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()