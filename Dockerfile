FROM python:3.6.12-slim
MAINTAINER chenghaolee <harry83017622@gmail.com>
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        vim \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /home
COPY . .
RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0:8000"]