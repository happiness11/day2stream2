
'''
def count_upper_case(message):
     return sum([1 for c in message if c.isupper()]) + sum([1 for c in message if c.ilower()])
     
            assert even_number_of_evens([]) == False, "No numbers"
            assert even_number_of_evens([2]) == False, "One even number"
            assert even_number_of_evens([2, 4]) == True, "Two even numbers"
            assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
            assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
            assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
            assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"
            

        
print(count_upper_case("Hello world"))
'''

from ryotest import *

test_are_equal(3,4)
         # test_is_in([1,2,3,4],5)

print("Al test are pass")
