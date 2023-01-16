FROM python:3.9.4

RUN mkdir -p /root/backend
WORKDIR /root/backend
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r ./requirements.txt

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

