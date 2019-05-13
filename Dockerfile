FROM centos:7

RUN yum update -y
RUN yum install epel-release -y
RUN yum update -y
RUN yum install -y python-pip python-dev mysql-devel gcc python-setuptools python-devel
RUN yum install MySQL-python -y
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install uwsgi
RUN pwd
WORKDIR /app
RUN pwd
RUN pip install --global-option=build_ext --global-option="-I/usr/include/python2.7" -r requirements.txt

COPY . /app
RUN pwd
CMD ["/usr/bin/uwsgi", "--http", ":9500", "--manage-script-name", "--mount", "/=__init__:application"]