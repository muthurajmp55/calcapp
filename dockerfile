##FROM registry.access.redhat.com/ubi8/ubi:8.1


#RUN yum install python3
#FROM python:alpine3.7
#RUN apk update
#RUN apk add make automake gcc g++ subversion
#RUN apk add --update --no-cache python-scipy
FROM python:3.8.1-alpine3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#RUN pip install Flask-MonitoringDashboar --ignore-installed scipy
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "calc.py" ]
