import pyodbc

def get_connection():

    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=.;"
        "DATABASE=HospitalDB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return conn 

print("Connected successfully!")
