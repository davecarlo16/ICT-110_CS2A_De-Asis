
"""
 Module
"""

def calculate_borrow(months_contributed):
    """
    Calculate the borrowable amount based on the total number of months of contribution.
    Parameter:
        months_contributed (int): The total number of months of contribution.
    Returns:
        float: The borrowable amount.
    """
    loan_factor = None
    borrowable_amount = None
    if months_contributed > 200:
        loan_factor = 0.90
    else:
        loan_factor = 0.80
    borrowable_amount = (months_contributed * 100) * loan_factor
    return borrowable_amount
