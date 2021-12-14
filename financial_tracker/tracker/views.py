from django.shortcuts import redirect, render
from .models import (
    FinancialTracker,
    TrackerItem,
    calculate_total_spent,
    get_db_dates,
    get_expenses,
    get_payment_history_plot,
    get_category_spending_plot,
    get_categories_for_current_user,
    get_category_count,
)
from .forms import CreateNewTrackerForm
from django.http import HttpResponseRedirect


def save_user_tracker_items(response, id):
    ft = FinancialTracker.objects.get(id=id)
    if ft in response.user.financialtracker.all():
        if response.method == "POST":
            if response.POST.get("new-payment"):

                # get all inputs
                new_pay_title = response.POST.get("pay-title")
                new_pay_amount = response.POST.get("pay-amt")
                new_pay_type = response.POST.get("pay-type")
                new_pay_description = response.POST.get("pay-desc")
                new_purchase_date = response.POST.get("purchase-date")
                new_category = response.POST.get("category")

                ft.trackeritem_set.create(
                    pay_title=new_pay_title,
                    pay_amt=new_pay_amount,
                    pay_type=new_pay_type,
                    pay_description=new_pay_description,
                    purchase_date=new_purchase_date,
                    category=new_category,
                )
        return render(response, "tracker/user-tracker.html", {"ft": ft})
    return render(response, "tracker/tracker_views.html", {})


def delete_tracker_items(request, items_id):
    item_row = TrackerItem.objects.get(id=items_id)
    item_row.delete()
    return redirect("/trackerviews")


def edit_items(request, items_id):
    # get the items_row on from database
    item_row = TrackerItem.objects.get(id=items_id)
    save_edited_items(request, item_row)
    return render(request, "tracker/edit-items.html", {"itemrow": item_row})


def save_edited_items(request, item_row):
    if request.method == "POST":
        if request.POST.get("edited-payment"):
            # get form info
            item_row.pay_title = request.POST.get("pay-title")
            item_row.pay_amt = request.POST.get("pay-amt")
            item_row.pay_type = request.POST.get("pay-type")
            item_row.pay_description = request.POST.get("pay-desc")
            item_row.purchase_date = request.POST.get("purchase-date")
            item_row.category = request.POST.get("category")
            item_row.save()
        return redirect("/trackerviews")


def create_tracker(response, id):

    if FinancialTracker.objects.filter(tracker_user_id=id).exists():
        """user cannot create more trackers"""
        return HttpResponseRedirect("/trackerviews/")
    else:
        if response.method == "POST":
            form = CreateNewTrackerForm(response.POST)

            if form.is_valid():
                new_tracker_name = form.cleaned_data["name"]
                new_financial_tracker = FinancialTracker(tracker_name=new_tracker_name)
                new_financial_tracker.save()
                response.user.financialtracker.add(new_financial_tracker)

            return HttpResponseRedirect("/userhome/%i" % new_financial_tracker.id)
        else:
            # if get the just create the new tracker
            form = CreateNewTrackerForm()
        return render(response, "tracker/create.html", {"form": form})


def get_total_spent_info(request):
    current_user = request.user
    return calculate_total_spent(current_user.id)


def view_trackers(request):
    # the current logged user
    current_user = request.user

    # total of how much has spent
    total_spent = get_total_spent_info(request)

    # user purchase dates
    dates = get_db_dates(current_user.id)

    # each user expense
    amount_spent = get_expenses(current_user.id)

    # payment history chart
    chart = ""

    pie_chart = ""
    # if there are dates and a track of money spent
    if len(dates) > 0 and len(amount_spent) > 0:

        # then unpack for the graph
        dates, amount_spent = zip(*sorted(zip(dates, amount_spent)))
        chart = get_payment_history_plot(dates, amount_spent)

        # prepare data for pie chart
        categories = get_categories_for_current_user(current_user.id)
        filtered_categories = {}

        for i in categories:
            category_count = get_category_count(categories, i)
            filtered_categories.update({i: category_count})

        pie_chart = get_category_spending_plot(
            filtered_categories.keys(), filtered_categories.values()
        )

    if FinancialTracker.objects.filter(id=current_user.id).exists():

        ft = FinancialTracker.objects.get(id=current_user.id)

        context = {
            "id": current_user.id,
            "ft": ft,
            "totalspent": total_spent,
            "chart": chart,
            "piechart": pie_chart,
        }

        return render(request, "tracker/tracker_views.html", context)
    else:

        context = {
            "id": current_user.id,
            "totalspent": total_spent,
            "chart": chart,
        }
        return render(request, "tracker/tracker_views.html", context)
