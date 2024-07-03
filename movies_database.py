# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'movies_database.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect('movies_database.db')
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()
    
    menu_choice =''
    while menu_choice = input('Welcome to the Movies database\n\n'
                              'Type the letter for the information you want:\n'
                              'A: All movies made in Japan\n '
                              'B: title, director & studio of movies made by Disney and Pixar\n'
                              'C: All the movies released in the 90s\n'
                              'D: Title and ratings of movies made by Warner Bros\n'
                              'E: title, country & studio of all movies made in NZ\n'
                              'F: title ratings & release date for all movies\n'
                              'G: title, studio & director of')
                              