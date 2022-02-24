import ast
from datetime import datetime
from decimal import Decimal

def convert_str_to_list(value):
    try:
        return ast.literal_eval(value)
    except Exception as e:
        return value

def convert_epoch_to_date(value):
    date = datetime.utcfromtimestamp(int(value)/1000.0).strftime('%Y-%m-%d %H:%M:%S')
    return date

def get_remaining_amount(spend,total):
    return round(Decimal(total) - Decimal(spend))

def calculate_percentage(spend,total):
    return round(Decimal(100) * Decimal(spend)/Decimal(total))



def convert_published_at(dt):
    return datetime.strptime(dt, "%Y-%m-%dT%H:%M:%SZ")
