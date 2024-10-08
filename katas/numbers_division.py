from ansible_collections.community.sap_libs.plugins.modules.sap_company import return_analysis


def numbers_division(a, b):
    """
    Performs division on two integers.
    """

    c = a / b
    return c


result = numbers_division(10, 3)
print(result)  # Expected output: 3.3333

result = numbers_division(8, 2)
print(result)  # Expected output: 4.0

result = numbers_division(5, 2)
print(result)  # Expected output: 2.5

"""
To complete this exercise:
--------------------------
Implement the function to perform integers division and return the result.


Exercise Breakdown:
-------------------
In Python, `int` type represents whole numbers (integers) without any fractional part. 
The returned value (assigned to the `result` variable) is of type `float`.
"""
