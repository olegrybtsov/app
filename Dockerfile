FROM centos
EXPOSE 8081
RUN yum install git -y
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python35u python35u-libs python35u-devel python35u-pip
RUN easy_install-3.5 pip
RUN pip3.5 install cherrypy
RUN git clone https://github.com/olegrybtsov/app.git
CMD python3.5 /app/project/server.py