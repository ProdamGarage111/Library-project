import sqlite3

class Book:
    def __init__(self, id, title, author):
        self.id = id 
        self.title = title
        self.author = author
        self.availability_status = True

    def update_status(self, status):
        self.availability_status = status
    
    def update_author(self, author):
        self.author = author
    
    def update_title(self, title):
        self.title = title

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Available: {self.availability_status}")
    
    def add_to_db(self):
        connection= sqlite3.connect('example.db')
        cursor = connection.cursor()
        cursor.execute(f'''INSERT INTO books(id,title,author,availability_status) VALUES('{self.id}', '{self.title}', '{self.author}', '{self.availability_status}');''')
        connection.commit()
        connection.close()
    
    def delete_from_db(self):
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()
        cursor.execute(f''' DELETE FROM books WHERE id = {self.id}''')
        connection.commit()
        connection.close()
        
    def show_from_terminal(self):
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM books''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connection.commit()
        connection.close()

    def update_in_db(self):
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()
        cursor.execute(f'''UPDATE books SET column1 = value1, column2 = value2, ... WHERE id = {self.id}; ''')
        connection.commit()
        connection.close()

    


book1 = Book(2,"book name","AUTHOR")
book1.delete_from_db()
book1.show_from_terminal()
#cursor.execute('''CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, availability_status TEXT)''')

