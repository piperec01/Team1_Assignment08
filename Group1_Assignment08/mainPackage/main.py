#main.py
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

from mainPackage.serverConnection import *
from mainPackage.outputFunction import *
from mainPackage.SQLStatement import *
import pyodbc

if __name__ == "__main__":

    cursor = ImportDatabase().cursor()
    cursor.execute(SQLString())
    sql_list = list()
    for row in cursor.fetchall():
        sql_list.append(row.LoyaltyStatus)
        sql_list.append(row.StoreID)
        sql_list.append(row.countLoyalty)
    PrintList(sql_list)

     