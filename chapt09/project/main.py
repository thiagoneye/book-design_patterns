"""
MVC Pattern
"""

# Imports

from mvc import *


# Main

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
