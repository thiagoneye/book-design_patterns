"""
MVC Pattern
"""

# Imports

import sqlite3


# Functions

def _execute(query: str):
    todos = None
    conn = sqlite3.connect('project_database.db')

    if query[:6] == "CREATE":
        conn.execute(query)
    else:
        cur = conn.cursor()
        cur.execute(query)

    if query[:6] == "SELECT":
        todos = cur.fetchall()
    elif query[:6] in ["INSERT", "UPDATE", "DELETE"]:
        conn.commit()

    conn.close()

    print(todos)
    return todos
