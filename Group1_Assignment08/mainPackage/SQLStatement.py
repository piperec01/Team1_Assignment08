#SQLStatement
#main.py
# Name: Elizabeth Piper, Juan Hill, Nosagie Sherman
# email: piperec@mail.uc.edu, hill4ju@mail.uc.edu, shermani@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/24
# Course/Section: IS 4010 Section 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Create a SQL statement to query a database
# Brief Description of what this module does: This module is the SQL statement query
# Citations:
# Anything else that's relevant:

def SQLString():
    '''
    Returns the sql statment used for the query pull.
    @param: None
    @return string
    '''
    string = 'SELECT LS.LoyaltyStatus, L.StoreID, COUNT(T.LoyaltyID) AS countLoyalty FROM GroceryStoreSimulator.dbo.tLoyaltyStatus AS LS, GroceryStoreSimulator.dbo.tLoyalty AS L, GroceryStoreSimulator.dbo.tTransaction AS T WHERE T.LoyaltyID = L.LoyaltyID AND L.LoyaltyStatusID = LS.LoyaltyStatusID GROUP BY LS.LoyaltyStatus, L.StoreID'
    return string
    
        
    