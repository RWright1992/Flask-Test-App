FROM python:3.6

COPY . .

RUN pip3 install -r requirements.txt

ENV DATABASE_URI "$DATABASE_URI"
ENV SECRET_KEY "$SECRET_KEY"

EXPOSE 5000

RUN ["python3", "create.py"]

ENTRYPOINT ["python3", "app.py"]
