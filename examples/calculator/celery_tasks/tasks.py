import celery


class AdditionCeleryTask(celery.Task):
    name = 'addition_celery_task'

    def run(self, payload):
        """
        place holder method
        """
        pass


class SubtractionCeleryTask(celery.Task):
    name = 'subtraction_celery_task'

    def run(self, payload):
        """
        place holder method
        """
        pass


class MultiplicationCeleryTask(celery.Task):
    name = 'multiplication_celery_task'

    def run(self, payload):
        """
        place holder method
        """
        pass


class DivisionCeleryTask(celery.Task):
    name = 'division_celery_task'

    def run(self, payload):
        """
        place holder method
        """
        pass
