def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers) 
    #This is improved code as it handles empty list and prevents ZeroDivisionError