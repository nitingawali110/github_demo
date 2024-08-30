from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def format_date(date_obj):
    # Format date in the desired format
    formatted_date = date_obj.strftime("%d-%m-%Y (%d %B %Y)")
    return formatted_date

def calculate_draft_date(effective_date, draft_day):
    # Convert effective_date to datetime object
    effective_date = datetime.strptime(effective_date, "%d-%m-%Y")
    # Calculate draft date
    draft_date = effective_date - timedelta(days=draft_day)
    return draft_date

def calculate_old_recurring_date(effective_date, draft_day, Refund_payment_number):
    # Convert effective_date to datetime object
    effective_date = datetime.strptime(effective_date, "%d-%m-%Y")
    # Calculate old recurring date
    old_recurring_date = effective_date + relativedelta(months=Refund_payment_number-1) - timedelta(days=draft_day)
    return old_recurring_date

def calculate_paid_through_date(effective_date, Refund_payment_number):
    # Convert effective_date to datetime object
    effective_date = datetime.strptime(effective_date, "%d-%m-%Y")
    # Calculate paid through date
    paid_through_date = effective_date + relativedelta(months=Refund_payment_number-1) - timedelta(days=1)
    return paid_through_date

# Input values
effective_date = "01-01-2024"
draft_day = 5
Refund_payment_number = 2

# Calculate the draft date
draft_date = calculate_draft_date(effective_date, draft_day)
formatted_draft_date = format_date(draft_date)

# Calculate the old recurring date
old_recurring_date = calculate_old_recurring_date(effective_date, draft_day, Refund_payment_number)
formatted_old_recurring_date = format_date(old_recurring_date)

# Calculate the paid through date
paid_through_date = calculate_paid_through_date(effective_date, Refund_payment_number)
formatted_paid_through_date = format_date(paid_through_date)

# Check if old recurring date is less than or equal to today's date
if old_recurring_date <= datetime.now():
    # Calculate new recurring date
    new_recurring_date = datetime.now() + relativedelta(months=1)
    formatted_new_recurring_date = format_date(new_recurring_date)
else:
    formatted_new_recurring_date = format_date(old_recurring_date)

# Format strings with ANSI escape codes for formatting
bold_start = "\033[1m"
bold_end = "\033[0m"
highlight_start = "\033[93m"  # Yellow color
highlight_end = "\033[0m"

# Display the details with formatting
print("1. Effective Date:", format_date(datetime.strptime(effective_date, "%d-%m-%Y")))
print("2. Draft Day:", draft_day)
print("3. Draft Date:", bold_start + highlight_start + formatted_draft_date + highlight_end + bold_end)
print("4. Refund_payment_number:", Refund_payment_number)
print("5. Old Recurring Date after Full Refund:", bold_start + highlight_start + formatted_old_recurring_date + highlight_end + bold_end)
print("6. Paid through Date after Full Refund:", bold_start + highlight_start + formatted_paid_through_date + highlight_end + bold_end)

# Print new recurring date with appropriate condition
if old_recurring_date <= datetime.now():
    # If old recurring date is before or equal to today's date
    print("   New Recurring Date after full refund of Payment no", Refund_payment_number, ":", bold_start + highlight_start + formatted_new_recurring_date + highlight_end + bold_end)
else:
    # If old recurring date is after today's date
    print("   New Recurring Date:", bold_start + highlight_start + formatted_new_recurring_date + highlight_end + bold_end)
