FROM python:3.6

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

RUN ["python3", "create.py"]

ENTRYPOINT ["python3", "app.py"]