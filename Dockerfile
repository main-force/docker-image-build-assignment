FROM python:3.9.17-slim-bullseye
LABEL maintainer "mainforce <isu18390@gmail.com>"
RUN apt update
COPY ./app /app
WORKDIR /app
RUN python3 -m pip install scikit-learn numpy tensorflow pillow flask

# Use shell form of ENTRYPOINT to execute multiple commands
CMD python3 run_train.py && python3 -m flask run