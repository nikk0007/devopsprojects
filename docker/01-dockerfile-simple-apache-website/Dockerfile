FROM httpd:2.4
RUN apt update -y
RUN apt install wget -y
RUN apt install unzip -y
RUN mkdir tmp
RUN rm -rf /htdocs/*
WORKDIR "tmp"
RUN wget https://www.tooplate.com/zip-templates/2125_artxibition.zip
RUN unzip 2125_artxibition.zip
RUN cp -r 2125_artxibition/* /usr/local/apache2/htdocs/
RUN echo $HOSTNAME > /usr/local/apache2/htdocs/hostname
RUN cat /usr/local/apache2/htdocs/index.html >> /usr/local/apache2/htdocs/hostname
RUN mv /usr/local/apache2/htdocs/hostname /usr/local/apache2/htdocs/index.html
