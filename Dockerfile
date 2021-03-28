FROM python:latest
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
RUN apt-get -y update
RUN apt-get install -y python-psycopg2 postgresql-client postgis gdal-bin libgdal-dev
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
RUN apt-get -y update && apt-get -y autoremove
WORKDIR /code

