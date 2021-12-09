from django.shortcuts import render
from .models import FinancialTracker, TrackerItem
from .forms import CreateNewTracker

def userTracker(response, id):
    ft = FinancialTracker.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("new-payment"):

            # get all inputs
            new_pay_title = response.POST.get("pay-title")
            new_pay_amount=response.POST.get("pay-amt")
            new_pay_type =response.POST.get("pay-type")
            new_pay_description=response.POST.get("pay-desc")
            
            ft.trackeritem_set.create(
                pay_title=new_pay_title, pay_amt=new_pay_amount, pay_type=new_pay_type, pay_description=new_pay_description
            )
    return render(response, "tracker/user-tracker.html", {"ft":ft})


def create(response):
    # for post methods
    if response.method == "POST":
        form = CreateNewTracker(response.POST)

        if form.is_valid():            
            new_tracker_name = form.cleaned_data["name"]
            new_financial_tracker = FinancialTracker(tracker_name = new_tracker_name)
            new_financial_tracker.save()
    else:
        # if get the just create the new tracker
        form = CreateNewTracker()
        
    return render(response, "tracker/create.html", {"form":form})