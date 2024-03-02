# Lab7
# Author: Dylan Nhan


## add in functions from test.py's test statements here to make the pytest work
## Use this file and your test plan to complete the lab

def calculate_rectangle_area(length: int, width: int) -> int:
    """Calculate the area of a rectangle

    Args:
        length (int): The length of the rectangle
        width (int): The width of the rectangle
    """
    return length * width

def calculate_hypotenuse(a: int, b: int) -> int:
    """Calculate the hypotenuse using the pythagorean theorem

    Args:
        a (int): a side of the triangle
        b (int): b side of the triangle
    """
    return (a**2 + b**2)**0.5

def is_even(number: int) -> bool:
    """return true or false if the number is even"""
    return(
        number % 2 == 0
    )

def find_maximum(a: int, b: int) -> int:
    """Find the maximum of two numbers
    
    Args:
        a (int): number1
        b (int): number 2

    Returns:
        int: the maximum of the two numbers
    """
    if a > b:
        return a
    else:
        return b

def grade_calculator(score: int) -> str:
    """Return the letter grade for a given score
    Use the following grading scale:
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59

    Args:
        score (int): grade score

    Returns:
        str: The letter grade
    """
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    #print(calculate_rectangle_area(3, 4))
    #print(calculate_hypotenuse(3, 4))
    #print(is_even(2))
    #print(find_maximum(3, 4))
    #print(grade_calculator(90)) 

if __name__ == "__main__":
    main()
