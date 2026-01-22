import sqlite3

# Performs a query on "gutenberg" which is an export of gutenberg.sqbpro.
def tiny_database():
    mydatabase = "gutenberg"

    db_portal = sqlite3.connect(mydatabase) # connect to the database

    db_cursor = db_portal.cursor() # create a file handler for the database

    doit = """
    SELECT p.pers_name, t.title,t.pub_date,t.source,t.text_id from "persons" p
    JOIN texts t ON t.text_id = p.text_fk
    ORDER BY pub_date ASC

    """
    db_cursor.execute(doit) # execute the query

    myresult = db_cursor.fetchall()

    for x in myresult: # print all the results, not just one
        print(x)


    db_portal.close() # keep things tidy
