#serverConnection.py
# Name: Elizabeth Piper, Juan Hill, Nosagie Sherman
# email: piperec@mail.uc.edu, hill4ju@mail.uc.edu, shermani@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/24
# Course/Section: IS 4010 Section 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Create a SQL statement to query a database

# Brief Description of what this module does: This module puts together all of the functions
# Citations:
# Anything else that's relevant:

def ImportDatabase():
    '''
    Imports and returns varible conn which is the database that is used.
    @param: none
    @return conn
    '''
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=IS4010;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
    return conn