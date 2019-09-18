# Define constant global variables
H_RATE = 14.5
OT_RATE = 21.75
TAX_DEDUCTION_PERCENTAGE = 0.24
# Main Calculation Function
def main_func():
    # Get total hours for paycheck
    hours_worked = float(input("Total Hours worked: "))
    # Ask user if there was any overtime
    check_if_ot = input("Was there OT? ").lower()
    # Check if user had overtime or not
    if check_if_ot == 'y' or check_if_ot == 'yes':
        # Get total overtime hours
        ot_hours_worked = float(input("Total OT hours: "))
        # Set amount of regular hours worked
        reg_hours = hours_worked - ot_hours_worked
    # If there was no overtime
    else:
        ot_hours_worked = 0
        reg_hours = hours_worked
    # Calculate total gross amount of paycheck
    t_gross = round((ot_hours_worked * OT_RATE) + (reg_hours * H_RATE), 2)
    # Calculate total tax being taken out of paycheck
    t_tax_taken = round((t_gross * TAX_DEDUCTION_PERCENTAGE), 2)
    # Calculate total net amount of paycheck
    t_net = round(t_gross - t_tax_taken, 2)

    # Print/Display Gross, Tax Deduction and Net amounts for the user
    print("Total Gross Amount: ${:,}".format(t_gross))
    print("Total Taxes Deducted: ${:,}".format(t_tax_taken))
    print("Total Net Amount: ${:,}".format(t_net))

    # Ask if the user wants to do another calculation
    # Get user input
    should_repeat = input("Repeat? ").lower()
    # Check what the user inputs (if input is anything other than 'y' or 'yes')
    if should_repeat == 'y' or should_repeat == 'yes':
        main_func()
    else:
        print("Goodbye! :)")
# ********** Start Program **********
main_func()