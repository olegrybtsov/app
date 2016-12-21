import string

import cherrypy
import random


class HelloWorld(object):

    auth=False

    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="enter">
              <input type="text" value="Login" name="name" />
              <input type="password" value="Password" name="password" />
              <button type="submit">Enter</button>
            </form>
            <a href="./regPage">Register</a>
          </body>
        </html>"""

    @cherrypy.expose
    def enter(self, name, password):
        if name == '':
            return 'Hello, user'
        return 'Hello, ' + name

    @cherrypy.expose
    def regPage(self):
        return """<html>
           <head></head>
           <body>
             <form method="get" action="register">
               <input type="text" value name="name" />
               <input type="password" value name="password" />
               <input type="password" value name="passwordConfirm" />
               <button type="submit">Enter</button>
             </form>
             <a href="./register">Register</a>
           </body>
         </html>"""


# @cherrypy.expose
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
