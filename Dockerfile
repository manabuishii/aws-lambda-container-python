FROM amazon/aws-lambda-python:3.8.2021.02.15.13

COPY app.py   ./
CMD ["app.handler"]