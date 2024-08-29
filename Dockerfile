FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    gcc \
    build-essential \
    python3-dev \
    default-libmysqlclient-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install gunicorn
RUN mkdir -p /tmp
CMD ["gunicorn", "--bind", "unix:/tmp/gunicorn.sock", "hongsam_BE.wsgi:application"]