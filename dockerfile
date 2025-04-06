FROM python:3.12
WORKDIR /usr/src/app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5600
ENV FLASK_DEBUG=0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5600
COPY . .
CMD ["flask", "run"]
#CMD ["python", "app.py"]