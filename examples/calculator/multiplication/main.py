from celery_tasks.tasks import AdditionCeleryTask
from celery_tasks.utils import create_worker_from


class AdditionCeleryTaskImpl(AdditionCeleryTask):

    def run(self, payload):
        """ actual implementation """
        num_1 = float(payload['num_1'])
        num_2 = float(payload['num_2'])
        ans = num_1 * num_2
        return ans


# create celery app
app, _ = create_worker_from(AdditionCeleryTaskImpl)

# start worker
if __name__ == '__main__':
    app.worker_main()