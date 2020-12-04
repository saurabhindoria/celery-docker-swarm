FROM python:3.8
ADD ./addition/requirements.txt /
ADD ./addition/main.py /
ADD ./celery_tasks/ /celery_tasks/
RUN pip3 install -r requirements.txt
ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n addition_worker.%h