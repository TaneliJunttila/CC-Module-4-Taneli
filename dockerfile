FROM python:3.12
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5600
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5600
COPY . .
CMD ["flask", "run"]
#CMD ["python", "app.py"]