FROM python:3

RUN mkdir home_template

RUN mkdir hm1

RUN cd home_template

COPY requirements.txt .

COPY index.html .\hm1\.

RUN apt-get update

RUN apt-get install -y libgl1-mesa-dev

RUN pip3 install -r requirements.txt

COPY run.py .

COPY ImgClassicationV3.h5 .

EXPOSE 5000 

CMD ["python3", "run.py"]



