
from datetime import datetime, timedelta

#time of invoice creation
now = datetime.now()
print "Invoice date: " + (now.strftime("%d/%m/%Y %I:%M"))

#date invoice is due, add days from today's date and provide d
def deadline():
    date_due = raw_input ("How many days from creation is the invoice due?")
    if date_due.isdigit():
        date_due = int(date_due)
        return date_due
    else:
        print "You need to input number of days!"
        return deadline()

# Need to try to ensure this function makes the user validate their inputs
def correct_input():
    print ("Is this information correct?")
    answer = raw_input("True or False?")
    if answer.upper() == 'TRUE':
        return True
    else:
        print 'Rewrite it again and do it right this time!'
        return False

def loop_until_correct():
    right_input = False
    while right_input == False:
        deadline_output = deadline()
        right_input = correct_input()
    return deadline_output

date_due = loop_until_correct()

# blanket argument to ask user for an integer only - need to complete
# def only_number():
#     user_input_number = raw_input()
#     if user_input_number.isdigit():
#         user_input_number = int(user_input_number)
#         return user_input_number
#     else:
#         print "You need to input a number value!"
#         return only_number(raw_input)
#

print "Invoice deadline: " + (now + timedelta(days=date_due)).strftime("%d/%m/%Y")

#the Borrower's information to prove debt attached
name = raw_input ("What is the debtor's name?")
address = raw_input ("What is the debtor's Address?")

print "{}, {}".format (name, address)

#defines the type of invoice we are billing the debtor
def case_type():
    print "What type of case is this invoice?"
    answer = raw_input ("Type either Damage(d), Late-fees(l)or Non-return(nr) and hit 'Enter'.")
    if answer == "Damage" or answer == "damage" or answer == "d":
        print "Damage invoice"
    elif answer == "Late-fees" or answer == "late-fees" or answer == "l":
        print "Late-fees invoice"
    elif answer == "Non-return " or answer == "non-return" or answer == "nr":
        print "Non-return case"
    else:
        print "You didn\'t pick the right case, try again!"
        case_type()

case_type()

#need to apply function only_number(raw_input) as I've created blanket argument above
#and the below follows the same method...

def price_no_fees():
    price = raw_input("What is the value of the outstanding debt?")
    if price.isdigit():
        price = int(price)
        return price
    else:
        print "You need to input a number value!"
        return price_no_fees()
price = price_no_fees()

#fees is 30%
fees =  price * 0.3
print fees

#total outstanding libaility including fees
price += fees
#print "The outstanding libaility is GBP" + price + " (inc. fees)."
print "The outstanding libaility is GBP {} (inc. fees).".format(price)
