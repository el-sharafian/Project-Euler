def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True

def find_factors():
    largest_palindrome = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            a = i * j
            if(is_palindrome(a) and a > largest_palindrome):
                largest_palindrome = a
                break
    return largest_palindrome
            
a = find_factors()
print(a)