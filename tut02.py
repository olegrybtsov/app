import string

import cherrypy
import random

import os

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "hello new world!"


    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 80})
    cherrypy.quickstart(HelloWorld())
