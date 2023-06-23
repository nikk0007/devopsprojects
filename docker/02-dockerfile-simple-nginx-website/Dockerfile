FROM nginx
RUN apt update -y
RUN apt install wget -y
RUN apt install unzip -y
RUN rm -rf /usr/share/nginx/html/*
WORKDIR "tmp"
RUN wget https://www.tooplate.com/zip-templates/2125_artxibition.zip
RUN unzip 2125_artxibition.zip
RUN cp -r 2125_artxibition/* /usr/share/nginx/html
RUN echo '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script><script>$.getJSON("https://api.ipify.org?format=json", function(data) {$("#gfg").html(data.ip);})</script><h3>Public IP Address of user is: </h3>  <p id="gfg"></p>' > /usr/share/nginx/html/script
RUN cat /usr/share/nginx/html/index.html >> /usr/share/nginx/html/script
RUN mv /usr/share/nginx/html/script /usr/share/nginx/html/index.html
