def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    a = 7
    b = 2
    return a // b


def float_multiplication():
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    a = 3.0
    b = 2
    return a * b


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    return (int_division() + float_multiplication())


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    string = 'Python is awesome!'
    # clean_string = "".join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), string))
    clean_string = ""
    for letter in string:
        if letter.isalpha() or letter.isdigit() or letter.isspace():
            clean_string += letter
    split_str = clean_string.split(" ")
    word = split_str[-1]
    return word


def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    string = 'Python is awesome!'
    lower_string =  string.lower()
    return lower_string

def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    string = 'Python is awesome!'
    count = 0
    for letter in string:
        if letter.lower() == "o":
            count += 1
    print(count)
    return count


def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    return not (5 > 3) and  (10 == 5 * 2)
