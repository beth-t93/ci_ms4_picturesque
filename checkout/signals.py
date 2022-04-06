from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from checkout.models import Order

from models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()
    """update order total when line item is created or updated"""
    
@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    instance.order.update_total()
    """update order total when line item is deleted"""
 