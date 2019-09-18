H_RATE = 14.5
OT_RATE = 21.75
TAX_DEDUCTION_PERCENTAGE = 0.24
def main_func():
    hours_worked = float(input("Total Hours worked: "))
    check_if_ot = input("Was there OT? ").lower()
    if check_if_ot == 'y' or check_if_ot == 'yes':
        ot_hours_worked = float(input("Total OT hours: "))
        reg_hours = hours_worked - ot_hours_worked
    else:
        ot_hours_worked = 0
        reg_hours = hours_worked
    t_gross = round((ot_hours_worked * OT_RATE) + (reg_hours * H_RATE), 2)
    t_tax_taken = round((t_gross * TAX_DEDUCTION_PERCENTAGE), 2)
    t_net = round(t_gross - t_tax_taken, 2)

    print("Total Gross Amount: ${:,}".format(t_gross))
    print("Total Taxes Deducted: ${:,}".format(t_tax_taken))
    print("Total Net Amount: ${:,}".format(t_net))

    should_repeat = input("Repeat? ").lower()
    if should_repeat == 'y' or should_repeat == 'yes':
        main_func()
    else:
        print("Goodbye! :)")
main_func()