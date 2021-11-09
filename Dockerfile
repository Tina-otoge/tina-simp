FROM python:3.10-alpine

WORKDIR /app
COPY . .
RUN pip install --upgrade -r requirements.txt
CMD python -m sssimp
