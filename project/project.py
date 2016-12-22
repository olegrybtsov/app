import os

import cherrypy

class Proj(object):
    auth = False
    name = "login"
    users = "users.txt"

    header = """
        <html>
        <head>
            <font size=4>
            <title>DevOps-002</title>
            <a href="./">HOME</a>
            <a href="./logout">Logout</a>
        </head>
        <body>

            <div style="height:100px"></div>
             <div align="center">"""

    footer = """
            </div>
        </body>
    </html>"""

    @cherrypy.expose
    def index(self):
        if self.auth:
            return self.header + "<p><h2>Group list</h2></p>" + self.print() + self.footer

        return self.header + """
            <p><a href="./login">Login</a> to become a part of DevOps Team</p>
           """ + Proj.footer

    def print(self):
        file = open(self.users, 'r')
        table = ''
        name = ''
        for line in file:
            name = line.split(':')[0]
            table += name + "<br/>"
        return table

    @cherrypy.expose
    def login(self, login='login', password=''):
        error = ''
        self.name = login

        if os.path.exists(self.users):
            file = open(self.users, 'r')
            error = 'no such user'

            for line in file:
                data = line.split(':')
                if login == data[0]:
                    if password == data[1]:
                        self.auth = True
                        return self.header + "<p>Wellcome, " + self.name + "!<p>" + self.footer
                    else:
                        error = "wrong password"
                    break
        else:
            error = 'no such user'

        return self.header + """
                   <p>Login to become a part of DevOps Team</p>
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
        return self.header + "<p>Goodbye...</p>" + self.footer

    @cherrypy.expose
    def registration(self, login='login', password='', passwordConfirm=''):
        error = ''
        self.name = login

        if len(login) < 4 or login == 'login':
            error = 'enter correct login'
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
            return self.header + """Now you can <a href="./">login</a>"""

        return self.header + """
             <form method="get" action="registration">
               <p><input type="text" value=""" + self.name + """ name="login" /> </p>
               <p><input type="password" value="password" name="password" /></p>
               <p><input type="password" value="password" name="passwordConfirm" /></p><font color="red">
               """ + error + """</font>
               <p><button type="submit">Register</button></p>
             </form>
            """ + self.footer

if __name__ == '__main__':
    if not os.path.exists("sessions"):
        os.makedirs("sessions")
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 80,
        'tools.sessions.on': True,
        'tools.sessions.storage_type': "File",
        'tools.sessions.storage_path': 'sessions',
        'tools.sessions.timeout': 10
    })
    cherrypy.quickstart(Proj())
