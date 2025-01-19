from enum import Enum
from datetime import datetime

from enum import Enum

class RentalOption(Enum):
    GPS = "gps"
    AIR_CONDITIONING = "air_conditioning"
    CHILD_SEAT = "child_seat"
    BABY_SEAT = "baby_seat"
    INSURANCE = "insurance"

def calculate_price(date_from, date_to, additional_options):
    valid_options = set(option.value for option in RentalOption)
    options_list = additional_options.split()

    for option in options_list:
        if option not in valid_options:
            raise ValueError(f"Invalid option: {option}. Please use valid RentalOption values.")
        
    try:
        date_from = datetime.strptime(date_from, "%Y-%m-%d")
        date_to = datetime.strptime(date_to, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expected format is YYYY-MM-DD.")
    
    base_price = 100
    days_rented = (date_to - date_from).days
    total_price = base_price * days_rented
    
    for option in options_list:
        if option == RentalOption.GPS.value:
            total_price += 10 * days_rented
        elif option == RentalOption.AIR_CONDITIONING.value:
            total_price += 5 * days_rented
        elif option == RentalOption.CHILD_SEAT.value:
            total_price += 15 * days_rented
        elif option == RentalOption.BABY_SEAT.value:
            total_price += 20 * days_rented
        elif option == RentalOption.INSURANCE.value:
            total_price += 80 * days_rented
    
    return total_price