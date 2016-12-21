import string

import cherrypy
import random

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="enter">
              <input type="text" value name="login" />
              <button type="submit">Enter</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def enter(self, name=8):
        #login=name
        return name

#    @cherrypy.expose
#    def display(self):
#        return cherrypy.session['mystring']

if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 80,
        'tools.sessions.on': True,
        'tools.sessions.storage_type': "File",
        'tools.sessions.storage_path': 'sessions',
        'tools.sessions.timeout': 10
        })
    cherrypy.quickstart(HelloWorld())