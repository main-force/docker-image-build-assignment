FROM python:3.9.17-slim-bullseye
LABEL maintainer "mainforce <isu18390@gmail.com>"
RUN apt update
COPY ./app /app
WORKDIR /app
RUN python3 -m pip install scikit-learn numpy tensorflow pillow

ENTRYPOINT ["python3"]
CMD ["run_train.py"]

