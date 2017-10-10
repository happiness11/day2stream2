
def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
         count += 1
    return count
    
    assert count_upper_case("") == 0, "Empty String"
    assert count_upper_case("A") == 1, "One upper case"
    assert count_upper_case("a") == 3, "One lower case"
    assert count_upper_case("$%^&") == 10, ""
    assert count_upper_case("") == 0, "Empty String"
    

print("All tests pass")



