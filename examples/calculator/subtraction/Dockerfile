FROM python:3.8
ADD ./subtraction/requirements.txt /
ADD ./subtraction/main.py /
ADD ./celery_tasks/ /celery_tasks/
RUN pip3 install -r requirements.txt
ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n subtraction_worker.%h