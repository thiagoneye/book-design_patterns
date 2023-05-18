"""
MVC Pattern
"""

# Imports

import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
from execute import _execute


# Classes

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = "SELECT * FROM task"
        todos = _execute(query)
        self.render("index.html", todos=todos)

class NewHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument("name", None)

        query = "CREATE TABLE IF NOT EXISTS task \
            (id INTEGER PRIMARY KEY, \
            name TEXT, \
            status NUMERIC)"
        _execute(query)

        query = f"INSERT INTO task (name, status) \
            VALUES ('{name}', 1)"
        _execute(query)

        self.redirect("/")

    def get(self):
        self.render("new.html")

class UpdateHandler(tornado.web.RequestHandler):
    def get(self, id, status):
        query = f"UPDATE task SET status={int(status)} WHERE id={id}"
        _execute(query)
        self.redirect("/")

class DeleteHandler(tornado.web.RequestHandler):
    def get(self, id):
        query = f"DELETE FROM task WHERE id={id}"
        _execute(query)
        self.redirect("/")

class RunApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/todo/new", NewHandler),
            (r"/todo/update/(\d+)/status/(\d+)", UpdateHandler),
            (r"/todo/delete/(\d+)", DeleteHandler),
        ]
        settings = dict(
            debug=True,
            template_path="templates",
            static_path="static"
        )
        tornado.web.Application.__init__(self, handlers, **settings)
