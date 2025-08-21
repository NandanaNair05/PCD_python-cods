import math

def calculate_lcm_using_gcd(num1, num2):

  greatest_common_divisor = math.gcd(num1, num2)
  least_common_multiple = (num1 * num2) // greatest_common_divisor
  return least_common_multiple
number1 = 12
number2 = 18
lcm_result = calculate_lcm_using_gcd(number1, number2)
print(f"The LCM of {number1} and {number2} is: {lcm_result}")