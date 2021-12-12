from django.db import models
from django.contrib.auth.models import User
import matplotlib.pyplot as plt
import base64
from io import BytesIO

class FinancialTracker(models.Model):
    """The Financial Tracker"""
    # TODO: make unique
    tracker_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="financialtracker",null=True)
    tracker_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tracker_name

class TrackerItem(models.Model):
    """A representation of each item in the tracker"""
    # the tracker
    tracker = models.ForeignKey(FinancialTracker, on_delete=models.CASCADE)

    # payment title
    pay_title = models.CharField(max_length=25)

    pay_amt = models.DecimalField(max_digits=6, decimal_places=2)

    # type of payment made
    pay_type = models.CharField(max_length=25)

    # brief description of a payment
    pay_description = models.CharField(max_length=100)

    purchase_date = models.DateField(auto_now_add=False, auto_now=False)


    def __str__(self):
        return (f"title: {self.pay_title} | amount: {self.pay_amt} | "
                f"type: {self.pay_type} | description: {self.pay_description} purchase date: {self.purchase_date}")

    

def calculate_total_spent(id):
    total = 0
    items =  TrackerItem.objects.filter(tracker_id=id)
    for i in items:
        total += i.pay_amt
    return total        

def get_pay_amounts(id):
    pay_amounts = []
    items =  TrackerItem.objects.filter(tracker_id=id)
    for i in items:
        pay_amounts.append(i.pay_amt)
    return pay_amounts        

def get_db_dates(id):
    dates = []
    items =  TrackerItem.objects.filter(tracker_id=id)
    for i in items:
        dates.append(i.purchase_date)
    return dates

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close() 
    return graph


def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title('Payment History')
    plt.plot(x, y)
    # plt.xticks(rotation=45)
    plt.xlabel('Months')
    plt.ylabel('Payments')
    plt.tight_layout()
    graph = get_graph()
    return graph
    
