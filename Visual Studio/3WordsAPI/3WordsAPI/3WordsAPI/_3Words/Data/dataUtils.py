
import pyodbc
import typing
"""Constuct connection"""
def returnConnection():
    server = "DESKTOP-GA81NK9"
    database = "dbTW"
    string_connection = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    con = pyodbc.connect(string_connection)
    return con

"""
    Receive the query with parameters
    Like: "selectQuery string ... WHERE ( ? , ? , ?)" , (param1 , param2 , param3 ,...)
"""
def select(selectQuery:str , parameters:tuple = None):
    conexao =  returnConnection()
    cursor = conexao.cursor()
    return cursor.execute(selectQuery )

"""
    Receive the query with parameters
    Like: "insertQuery string ... VALUES ( ? , ? , ?)" , (param1 , param2 , param3 ,...)
"""
def insert(insertQuery:str, parameters:tuple = None):
    conexao =  returnConnection()
    cursor = conexao.cursor()
    cursor.execute(insertQuery, parameters)
    conexao.commit()
    
"""
    Receive the query with parameters
    Like: "updateQuery string ... SET x = ? , y = ? , z = ?)" , (param1 , param2 , param3 ,...)
"""
def update(updateQuery:str, parameters:tuple = None):
    conexao =  returnConnection()
    cursor = conexao.cursor()
    cursor.execute(updateQuery , parameters)
    conexao.commit()

"""
    Receive the query with parameters
    Like: "selectQuery string ... WHERE ( ? , ? , ?)" , (param1 , param2 , param3 ,...)
"""
def delete(deleteQuery:str, parameters:tuple = None):
    conexao =  returnConnection()
    cursor = conexao.cursor()
    cursor.execute(deleteQuery , parameters)
    conexao.commit()
