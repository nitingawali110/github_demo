from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_dates(effective_date_str, draft_day, payment_number):
    # Convert effective_date string to datetime object
    effective_date = datetime.strptime(effective_date_str, "%d %b %Y")

    # Calculate actual recurring date
    actual_recurring_date = effective_date + relativedelta(months=payment_number) - relativedelta(days=draft_day)

    # Calculate paid through date
    paid_through_date = effective_date + relativedelta(months=payment_number) - relativedelta(days=1)

    # Check if actual_recurring_date is older than today's date, then add one month
    if actual_recurring_date < datetime.now():
        new_recurring_date = actual_recurring_date + relativedelta(months=1)
    else:
        new_recurring_date = actual_recurring_date

    return actual_recurring_date, paid_through_date, new_recurring_date

# Example usage
effective_date_str = "06 Apr 2024"
draft_day = 14
payment_number = 5

actual_recurring_date, paid_through_date, new_recurring_date = calculate_dates(effective_date_str, draft_day, payment_number)

# Printing information
print("Effective Date:", effective_date_str)
print("Draft Day:", draft_day)
print("Payment Number:", payment_number)
print("Actual Recurring Date:", actual_recurring_date.strftime("%d %b %Y"))
print("Paid Through Date:", paid_through_date.strftime("%d %b %Y"))
print("New Recurring Date:", new_recurring_date.strftime("%d %b %Y"))
