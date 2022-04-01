FROM python:3.9.5-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --user -r requirements.txt 
COPY . /code/
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD DJANGO_SUPERUSER_PASSWORD=admincael python manage.py createsuperuser --no-input --username=caeladmin  --email=cael@example.com
CMD python manage.py runserver 0.0.0.0:8000
