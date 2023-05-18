"""
MVC Pattern
"""

# Imports

from mvc import *
from execute import _execute


# Main

if __name__ == "__main__":
    #Database
    query = "CREATE TABLE IF NOT EXISTS task \
            (id INTEGER PRIMARY KEY, \
            name TEXT, \
            status NUMERIC)"
    _execute(query)

    #Application
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
