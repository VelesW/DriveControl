from enum import Enum
from datetime import datetime

class RentalOption(Enum):
    gps = 15.0
    insurance = 20.0
    baby_seat = 10.0
    additional_driver = 25.0

def calculate_price(day_from: str, day_to: str, options: str):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(day_from, date_format)
    end_date = datetime.strptime(day_to, date_format)
    
    rental_days = (end_date - start_date).days
    
    if rental_days < 0:
        raise ValueError("Invalid date range: day_from must be before day_to.")
    
    base_price_per_day = 100.0
    
    base_price = rental_days * base_price_per_day
    
    additional_cost = 0.0
    for option in options.split(" "):
        if isinstance(option, RentalOption):
            additional_cost += option.value
        else:
            raise ValueError(f"Invalid option: {option}. Please use valid RentalOption values.")
    
    total_price = base_price + additional_cost
    return total_price