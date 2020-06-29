
from models.customer import Customer


def delete(customerId):
    customer = Customer.objects.get_or_404(id=customerId)
    customer.delete()
    return {"status": "OK"}, 200
