import cherrypy

class Proj(object):

    auth=False
    name='login'

    header="""
    <html>
        <head>
            <title>DevOps-002</title>
        </head>
        <body>
            <div style="height:100px"></div>
             <div align="center">"""
    footer="""
            </div>
        </body>
    </html>"""

    @cherrypy.expose
    def index(self):
        return Proj.header + """
            <p>Login to become a part of DevOps Team</p>
            <form method="get" action="login">
              <p><input type="text" value="login" name="name" /></p>
              <p><input type="password" value="Password" name="password" /></p>
              <p><button type="submit">Login</button></p>
            </form>
            <a href="./regPage">Don't have an account?</a>
           """ + Proj.footer

    @cherrypy.expose
    def login(self, name, password):
        if name == '':
            return 'Hello, user'
        return 'Hello, ' + name

    @cherrypy.expose
    def regPage(self):
        return Proj.header + """
             <form method="get" action="registration">
               <p><input type="text" value=""" + self.name + """ name="name" /></p>
               <p><input type="password" value="password" name="password" /></p>
               <p><input type="password" value="password" name="passwordConfirm" /></p>
               <p><button type="submit">Register</button></p>
             </form>
         """ + self.footer

    @cherrypy.expose
    def registration(self, login, password, passwordConfirm):
        if(login == ''):
            return self.regPage + "enter login"

        #if(password != passwordConfirm):


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 80,
        'tools.sessions.on': True,
        'tools.sessions.storage_type': "File",
        'tools.sessions.storage_path': 'sessions',
        'tools.sessions.timeout': 10
    })
    cherrypy.quickstart(Proj())
