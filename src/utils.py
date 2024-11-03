from datetime import date

def get_days_to_xmas(current_date: date) -> int:
    # Return days to xmas as int. 
    # If days to xmas is negative, get
    # days to xmas up to next year. 
    if not isinstance(current_date, date):
        raise TypeError("only datetime.date type is accepted as input for get_days_to_xmas")
    current_year = current_date.year
    xmas_this_year = date(current_year, 12, 25)
    xmas_next_year = date(current_year+1, 12, 25)
    days_to_xmas = (xmas_this_year - current_date).days
    if days_to_xmas < 0:
        days_to_xmas = (xmas_next_year - current_date).days
    if days_to_xmas >= 365:
        raise ValueError(f"days_to_xmas should be less than 365, not {days_to_xmas}.")
    return days_to_xmas

def buffer_digit(input_digit: int) -> str: 
    """Buffer the days with a space before hand if they are 
         less than three digits long."""  
       input_digit_as_str = str(input_digit) 
       if len(input_digit_as_str) > 3: 
           raise ValueError("digit input should not be greater than len 3.") 
       while len(input_digit_as_str) < 3: 
           input_digit_as_str = "" + input_digit_as_str 
       return input_digit_as_str 

