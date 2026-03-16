import Math_utils
from Math_utils import add, subtract, multiply, square, cube
import string_utils
from string_utils import capitalize_words, reverse_string, word_count

import shop_package.billing as billing
from shop_package.billing import calculate_total, apply_tax
import shop_package.discount as discount

if __name__ == "__main__":
    print(Math_utils.add(5, 3))
    print(Math_utils.subtract(5, 3))
    print(Math_utils.multiply(5, 3))
    print(Math_utils.square(5))
    print(Math_utils.cube(5))
    print(add(10, 20))
    print(subtract(10, 20))
    print(multiply(10, 20))
    print(square(10))
    print(cube(10))
    print("\nString Utilities:")
    print(string_utils.capitalize_words("hello world"))
    print(string_utils.reverse_string("hello world"))
    print(string_utils.word_count("hello world"))
    print(capitalize_words("python programming"))
    print(reverse_string("python programming"))
    print(word_count("python programming is fun"))
    print("\nShop Package Billing:\n")
    print(billing.calculate_total([19.99, 5.49, 3.50]))
    print(billing.apply_tax(100, 7.5))
    print(calculate_total([19.99, 5.49, 3.50]))
    print(apply_tax(100, 7.5))  
    print("\nShop Package Discount:\n")
    print(discount.apply_discount(100, 20))
    print(discount.flat_discount(100, 15))
    print(discount.apply_discount(200, 10))
    
    print(discount.flat_discount(200, 25))

    

