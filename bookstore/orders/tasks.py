from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def OrderCreated(order_id):
    """
    Send Email on order created
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ с номером {}'.format(order.id)
    message = 'Дорогой {}, вы успешно создали заказ.\
              Номер заказа {} '.format(order.first_name, order.id)
    mail_send = send_mail(subject, message, 'root@localhost', [order.email])
    return mail_send
