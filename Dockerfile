FROM python:3.6

COPY . .

RUN pip3 install -r requirements.txt

ENV DATABASE_URI=sqlite:///data.db SECRET_KEY=shhhhh

EXPOSE 5000

RUN ["python3", "create.py"]

ENTRYPOINT ["python3", "app.py"]
