FROM python:3.11-slim

WORKDIR /backend-kycverfication

COPY requirements.txt /backend-kycverification/
RUN pip3 install -r /backend-kycverification/requirements.txt

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
