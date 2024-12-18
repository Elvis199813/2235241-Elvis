# Library Management System
books_dict = {}  # Dictionary to store books with ISBN as the key
def Library_Management():  # funtion to display Library Management System
    menu_options = {
        "1": ("Add a Book", adding_newbook), # printing Add a Book
        "2": ("Search for a Book", searching_a_book), # displaying Search for a Book
        "3": ("Delete a Book", remove_a_book), # Delete a Book
        "4": ("List All Books",listing_all_book),# List All Books
        "5": ("Exit", exit_program)
    }
    while True: # for stating loop , until exit 
        print("\n--- Library Management System ---") 
        for key, (description, _) in menu_options.items():  # element _ is the function connected with Library_Management which is ignored here since only the description is displayed
            print(f"{key}. {description}") #(description) contains the menu item's name, such "Add a Book."
        choice = input("Enter your choice: ").strip() #taking input from the user and strip used to remove white space from input
        if choice in menu_options: 
            if choice == "5":
                menu_options[choice][1]()  # Call the exit function
                break
            else:
                menu_options[choice][1]()  # Call the corresponding function
        else:
            print("Invalid choice. Please try again.")
def adding_newbook():  # Function to add a book
    print("\n--- Add a New Book ---")
    title = input("Enter book title: ").strip() # taking input from user for title
    author = input("Enter book author: ").strip() # Taking input from user for Author
    ISBN = input("Enter book ISBN: ").strip() # taking input from user for ISBN
    if ISBN in books_dict: # if the book is already stored 
        print("A book with this ISBN already exists.") #message come
    elif title and author and ISBN: # if not
        books_dict[ISBN] = {"Title": title, "Author": author} # adding book 
        print("Book added successfully!") # message arrive 
    else:
        print("Invalid input. All fields are required.") # if invalid input selected
def searching_a_book():  # Function to search for a book
    print("\n--- Search for a Book ---")
    search_term = input("Enter title, author, or ISBN to search: ").strip().lower() # taking input from the user for finding book
    results = [
        {"ISBN": ISBN, **details} # CHEAKING ISBN 
        for ISBN, details in books_dict.items() #if ISBN is present in books_dict
        if search_term in ISBN.lower() or # doing lower case of input 
           search_term in details["Title"].lower() or
           search_term in details["Author"].lower()
    ]
    if results:
        for book in results: #, if given input, matches with the book then print
            print(f"ISBN: {book['ISBN']}, Title: {book['Title']}, Author: {book['Author']}")
    else:
        print("No matching books found.")
def remove_a_book():  # Function to remove a book
    print("\n--- Remove a Book ---")
    ISBN = input("Enter the ISBN of the book to delete: ").strip() #Taking input from user for ISBN

    if ISBN in books_dict: # if ISBN is match with book_dict 
        del books_dict[ISBN] #deliting the book
        print("Book deleted successfully!") # message come
    else:
        print("No book found with the given ISBN.") #if book not found
def listing_all_book():  # Function to list all books
    print("\n--- List of All Books ---")
    if not books_dict: #if book_dict is empty
        print("No books available.") # message come
    else:
        for ISBN, details in books_dict.items(): # if book is present
            print(f"ISBN: {ISBN}, Title: {details['Title']}, Author: {details['Author']}") # showing all Books 
def exit_program():  # Function to exit the program
    print("Exiting... Thank you!")
if __name__ == "__main__":  # Run the main menu
    Library_Management()