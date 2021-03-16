import re 
def calculator(input_number, separator = ""):
    

    if input_number =="":
        return 0
    
    elif ',' in input_number:
        splitted = input_number.split(',')
        my_sum = 0
        for number in splitted:
            my_sum =calculator(number)+my_sum
        return my_sum
    elif '\n' in input_number:
        splitted = input_number.split('\n')
        my_sum = 0
        for number in splitted:
            my_sum =calculator(number)+my_sum
        return my_sum
    elif '//' in input_number:
       
        input_number=input_number.split("//")[1]
        separator=input_number[0:1]
        input_number =input_number[1:]
        splitted = input_number.split(separator)
        my_sum = 0
        for number in splitted:
            my_sum =calculator(number,separator)+my_sum
        return my_sum
    else: 
        if float(input_number)>1000:
            return 0
        if float(input_number)<0:
            raise
        return float(input_number)