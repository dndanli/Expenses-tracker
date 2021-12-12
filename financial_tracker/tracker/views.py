from django.shortcuts import render
from .models import FinancialTracker, calculate_total_spent
from .forms import CreateNewTrackerForm
from django.http import HttpResponseRedirect


def save_user_tracker_items(response, id):
    ft = FinancialTracker.objects.get(id=id)    
    if ft in response.user.financialtracker.all():
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
    return render(response, "tracker/tracker_views.html", {})


def create_tracker(response, id):
    
    if FinancialTracker.objects.filter(tracker_user_id=id).exists():
        """ user cannot create more trackers"""
        return HttpResponseRedirect("/trackerviews/")
    else:
        if response.method == "POST":
            form = CreateNewTrackerForm(response.POST)

            if form.is_valid():            
                new_tracker_name = form.cleaned_data["name"]
                new_financial_tracker = FinancialTracker(tracker_name = new_tracker_name)
                new_financial_tracker.save()
                response.user.financialtracker.add(new_financial_tracker)        

            return HttpResponseRedirect("/userhome/%i" %new_financial_tracker.id)
        else:
            # if get the just create the new tracker
            form = CreateNewTrackerForm()
        return render(response, "tracker/create.html", {"form":form})    



def get_total_spent_info(request):
    current_user = request.user
    return calculate_total_spent(current_user.id)


def view_trackers(request):
    current_user = request.user

    total_spent = get_total_spent_info(request)

    if FinancialTracker.objects.filter(id=current_user.id).exists():

        ft = FinancialTracker.objects.get(id=current_user.id)    
    
        context = {
            "id":current_user.id,
            "ft":ft,
            "totalspent":total_spent
        }
    
        return render(request, "tracker/tracker_views.html", context)
    else:

        context = {
            "id":current_user.id,
            "totalspent":total_spent
        }
        return render(request, "tracker/tracker_views.html", context)


