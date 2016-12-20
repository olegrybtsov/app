import cherrypy
import os

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "hello world"

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 80})
    cherrypy.quickstart(HelloWorld())