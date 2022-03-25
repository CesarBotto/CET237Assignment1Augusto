FROM ubuntu
RUN apt-get update
RUN apt-get install -y python
RUN apt-get -y install git
RUN git clone https://github.com/CesarBotto/CET237Assignment1Augusto.git