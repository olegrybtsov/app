import os

import cherrypy

class Proj(object):
    auth = False
    name = "login"
    users = "users.txt"

    footer = """
            </div>
        </body>
    </html>"""

    @cherrypy.expose
    def index(self):
        if self.auth:
            return self.getHeader() + "<p><h2>Group list</h2></p>" + self.print() + self.footer

        return self.getHeader() + """
            <p><h2><a href="./login">Login</a> to become a part of DevOps Team</h2></p>
           """ + self.footer

    @cherrypy.expose
    def login(self, login='login', password='password'):
        error = 'no such user'
        self.name = login

        if login == '' or login == "login":
            error = 'enter login'
            self.name = 'login'

        elif password == '' or password == 'password':
            error = 'enter password'

        elif os.path.exists(self.users):
            file = open(self.users, 'r')

            for line in file:
                data = line.split(':')
                if login == data[0]:
                    if password == data[1]:
                        self.auth = True
                        return self.getHeader() + "<p><h2>Wellcome, " + self.name + "!</h2><p>" + self.footer
                    else:
                        error = "wrong password"
                    break


        return self.getHeader() + """
                   <p><h2>Login to become a part of DevOps Team</h2></p>
                   <form method="get" action="login">
                     <p><input type="text" value=""" + self.name + """ name="login" /></p>
                     <p><input type="password" value="password" name="password" /></p>
                     <p><button type="submit">Login</button></p>
                   </form>
                   <p><font color="red">""" + error + """</font></p>
                   <a href="./registration">Don't have an account?</a>
                  """ + self.footer

    @cherrypy.expose
    def logout(self):
        self.auth = False
        return self.getHeader() + "<p><h2>Goodbye...</h2></p>" + self.footer

    @cherrypy.expose
    def registration(self, login='login', password='password', passwordConfirm='password'):
        error = ''
        self.name = login

        if len(login) < 4 or login == 'login':
            error = 'enter correct login'
            self.name = 'login'
        elif ":" in login:
            error = "login can't contain ':'"
        elif len(password) < 3 or password == 'password':
            error = 'enter correct password'
        elif password != passwordConfirm:
            error = "passwords doesn't match"
        else:
            file = open(self.users, 'w')
            file.write(login + ":" + password)
            file.close()
            return self.header + """<p><h2>Now you can <a href="./">login</a></h2></p>"""

        return self.getHeader() + """
            <p><h2>Create your account</h2></p>
             <form method="get" action="registration">
               <p><input type="text" value=""" + self.name + """ name="login" /> </p>
               <p><input type="password" value="password" name="password" /></p>
               <p><input type="password" value="password" name="passwordConfirm" /></p><font color="red">
               """ + error + """</font>
               <p><button type="submit">Register</button></p>
             </form>
            """ + self.footer

    def print(self):
        file = open(self.users, 'r')
        table = ''
        name = ''
        for line in file:
            name = line.split(':')[0]
            table += name + "<br/>"
        return table

    def getHeader(self):

        logout = ''

        if self.auth == True:
            logout = """<a href="./logout">Logout</a>"""

        return """
        <html>
        <head>
            <font size=4>
            <title>DevOps-002</title>
            <a href="./">HOME</a>   """ + logout + """
        </head>
        <body>

            <div style="height:100px"></div>
             <div align="center">"""

if __name__ == '__main__':
    if not os.path.exists("sessions"):
        os.makedirs("sessions")
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8081,
        'tools.sessions.on': True,
        'tools.sessions.storage_type': "File",
        'tools.sessions.storage_path': 'sessions',
        'tools.sessions.timeout': 10
    })
    cherrypy.quickstart(Proj())
