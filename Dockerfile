FROM python:3.6

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV DATABASE_URI=${DATABASE_URI} SECRET_KEY=${SECRET_KEY}

RUN ["python3", "create.py"]

ENTRYPOINT ["python3", "app.py"]
