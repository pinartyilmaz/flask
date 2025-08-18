FROM python:3.12-slim

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install Flask && \
    pip install Flask==3.0.3

COPY .. .

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]