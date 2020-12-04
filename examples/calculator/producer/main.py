import random

from celery_tasks.tasks import AdditionCeleryTask, SubtractionCeleryTask, MultiplicationCeleryTask, DivisionCeleryTask
from celery_tasks.utils import create_worker_from
from flask import Flask

flask_app = Flask(__name__)

# create worker
_, addition_worker = create_worker_from(AdditionCeleryTask)
_, subtraction_worker = create_worker_from(SubtractionCeleryTask)
_, multiplication_worker = create_worker_from(MultiplicationCeleryTask)
_, division_worker = create_worker_from(DivisionCeleryTask)


@flask_app.route('/create_tasks/<count>')
def create_tasks(count):
    count = int(count)
    for i in range(count):
        num_1 = random.randint(1, 1000)
        num_2 = random.randint(1, 1000)
        payload = {
            'num_1': num_1,
            'num_2': num_2
        }
        addition_worker.apply_async(args=[payload, ])
        subtraction_worker.apply_async(args=[payload, ])
        multiplication_worker.apply_async(args=[payload, ])
        division_worker.apply_async(args=[payload, ])
    return "Done " + str(count)


if __name__ == '__main__':
    flask_app.run(host="0.0.0.0", port=5000)
