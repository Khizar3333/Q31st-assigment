import os
from sqlmodel import SQLModel,create_engine


conn_str=os.getenv('DB_SECRET')
print(conn_str)
connection=create_engine(conn_str)

def createtables():
 SQLModel.metadata.create_all(connection)
