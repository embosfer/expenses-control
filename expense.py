import re
from enum import Enum


class Expense(Enum):
    # Left value: human readable description
    # Right value: (case un-sensitive) words to match in each transaction, separated by '|' if there are several of them

    # Replace the current 'right' dummy values by the ones that appear in your statement
    # Add more Enums as needed and they'll be automatically picked-up by the expense reports
    BANK_FEES = 'Bank maintenance fees', 'MONTHLY FEE'
    BILLS = 'Bills (gas, electricity, water, TV license)', 'BILL1|BILL2|BILL3'
    BOOKS = 'Books', 'BOOKSHOP1|BOOKSHOP2'
    CASH_WITHDRAWAL = 'Cash out', 'CASH WITHDRAWAL'
    CAR = 'Car (tax, fuel, servicing)', 'CAR1|CAR2|CAR3'
    CAR_INSURANCE = 'Car insurance', 'CARINSURANCE'
    COFFEE_OUT_WEEKLY = 'Coffee out weekly', 'COFFEESHOP1|COFFEESHOP2'
    COUNCIL_TAX = 'Council Tax', 'COUNCILBILL'
    CLOTHING = 'Clothing', 'CLOTHING1|CLOTHING2'
    DINNER_OUT = 'Dinner out', 'RESTAURANT1|RESTAURANT2'
    DRINKS = 'Drinks (pubs)', 'PUB1|PUB2'
    HOUSE_GOODS = 'House goods (furniture, plants)', 'FURNSHOP1|FURNSHOP2'
    HOUSEKEEPING_COSTS = 'Housekeeping costs (food, cleaning)', 'GROCERY1|GROCERY2'
    INSURANCE = 'House Insurance', 'HOUSEINSURANCE'
    INTERNET = 'Internet', 'INTERNETPROVIDER'
    HOLIDAYS = 'Holidays (flights, parking, insurance)', 'AIRLINE1|PARKING1'
    KIDS_EDUCATION = 'Kids education', 'NURSERY'
    MORTGAGE = 'Mortgage', 'BANK1'
    LIFE_ASSURANCE = 'Life assurance', 'LIFEINSURANCE'
    LUNCH_OUT = 'Lunch out (any day of the week)', 'RESTAURANT3|RESTAURANT4'
    PHONE = 'Phone', 'PHONEPROVIDER'
    SUBSCRIPTIONS = 'Subscriptions (TV Streaming)', 'NETFLIX|Spotify'
    TAKE_OUT = 'Take-out', 'TAKEOUT'
    TRAVEL_COSTS = 'Travel costs (tube, train, Uber)', 'TRAVEL1|TRAVEL2'
    UNKNOWN = 'Unknown', 'Unknown'

    @staticmethod
    def found(transaction_type, desc):
        return re.search(transaction_type.value[1], desc, re.IGNORECASE) is not None

    @staticmethod
    def from_description(desc):
        for tran_type in Expense:
            if Expense.found(tran_type, desc):
                return tran_type
        else:
            return Expense.UNKNOWN