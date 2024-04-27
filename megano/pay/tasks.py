from megano.celery import app
from pay.models import Transaction


@app.task
def process_payment(transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    if transaction.uuid // 2 == 0:
        transaction.is_paid = True
        transaction.save()
        transaction.order.is_paid = True
        transaction.order.save()

