
import math

#import Enum from custom class
from Validation_Lib import String_Valdiation_Type

def validated_input(prompt, data_type, allow_empty = False, trim_space = True, string_validation_type = String_Valdiation_Type.NONE, 
                    min_value = -math.inf, can_equal_min_value = True, max_value = math.inf, can_equal_max_value = True):
    """Inputs a value and validates it according to the arguments given

    Arguments:
    prompt: The prompt to give the user in the input() function.
    data_type: The type of data to accept as an input. 

    Optional keyword argument flags:
    For strings:
    allow_empty: whether or not to allow an empty string. (Default False)
    trim_space: whether or not to trim whitespace off of ends. (Default True)
    string_validation_type: selects the type of validation to check the input against. (Default String_Validation_Type.NONE)

    for ints, floats, and complexes:
    min_value: the minimum value to accept as a valid input. (Default -math.inf)
    can_equal_min_value: flag to include or exclude min_value from the validation comparison. (Default True)
    max_value: the maximum value to accept as a valid input. (Default math.inf)
    can_equal_max_value: flag to include or exclude max_value from the validation comparison. (Default True)

    for booleans:

    """

    if data_type is str:
        
        while True:
            user_input = input(prompt)

            #trim whitespace if indicated by flag
            if trim_space:
                user_input = user_input.strip()

            #check for empty string if indicated by flag
            if not allow_empty:
                if not user_input:
                    print("Input may not be empty")
                    continue

            #validate per String_Validation_Type enum
            match string_validation_type:
                case String_Valdiation_Type.ALPHA:

                    #all characters must be letters
                    if not user_input.isalpha():
                        print("Input must contain only letters")
                        continue

                case String_Valdiation_Type.ALPHA_AND_SPACE:

                    #all characters must be letters or whitespace
                    test_str = "".join(user_input.split())

                    if not test_str.isalpha():
                        print("Input may contain only letters and spaces")
                        continue

                case String_Valdiation_Type.ALPHANUMERIC:
                    
                    #all characters must be letters or numbers
                    if not user_input.isalnum():
                        print("Input may contain only letters and numbers")
                        continue

                case String_Valdiation_Type.ALPHANUMERIC_AND_SPACE:
                    
                    #all characters must be letters, numbers, or whitespace
                    test_str = "".join(user_input.split())

                    if not test_str.isalnum():
                        print("Input may contain only letters, numbers, and spaces")
                        continue

                case String_Valdiation_Type.DIGITS:
                    
                    #all characters must be digits
                    if not user_input.isdigit():
                        print("Input may contain only numbers")
                        continue

                case String_Valdiation_Type.DIGITS_AND_SYMBOLS:

                    #all characters must be digits or the symbols (. , $ % - # ^)
                    acceptable_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '$', '%', '#', '^', '*', )
                    #loop through each char in the input string
                    for char in user_input:
                        if char in acceptable_chars:
                            #if char is a valid char, go to next. Otherwise, break the loop
                            continue
                        break
                    else:
                        #if we never break, input is valid, return
                        return user_input
                    
                    #otherwise, jump to next cycle of while loop
                    print("Input may contain only numbers and symbols")
                    continue

                case _:
                    pass

            #if no other paths have continued the loop, return the input value
            return user_input

    elif data_type is int:

        while True:
            user_input = input(prompt).strip()

            #check if input value is empty
            if not user_input:
                print("Input may not be empty")
                continue

            try:
                #attempt to convert input value to int
                int_val = int(user_input)
            except:
                #if coversion failed, input is invalid, continue loop
                print("Input must be a valid integer")
                continue
            
            #check on min_value, depending on can_equal_min_value flag
            if can_equal_min_value:
                if int_val < min_value:
                    #invalid value, continue loop
                    print("Input out of range")
                    continue
            else:
                if int_val <= min_value:
                    #invalid value, continue loop
                    print("Input out of range")
                    continue

            #check on max_value, depending on can_equal_max_value flag
            if can_equal_max_value:
                if int_val > max_value:
                    #invalid value, continue loop
                    print("Input out of range")
                    continue
            else:
                if int_val >= max_value:
                    #invalid value, continue loop
                    print("Input out of range")
                    continue


            #validation passed, return value
            return int_val

    elif data_type is float:

        while True:
            user_input = input(prompt).strip()

            #check if input value is empty
            if not user_input:
                print("Input may not be empty")
                continue

            try:
                #attempt to convert input value to float
                float_val = float(user_input)
            except:
                #if coversion failed, input is invalid, continue loop
                print("Input must be a valid floating point number")
                continue
            
            #check on min_value, depending on can_equal_min_value flag
            if can_equal_min_value:
                if float_val < min_value:
                    #invalid value, continue loop
                    print("Input out of range")
                    continue
            else:
                if float_val <= min_value:
                    #invalid value, continue loop
                    print("Input out of range")
                    continue

            #check on max_value, depending on can_equal_max_value flag
            if can_equal_max_value:
                if float_val > max_value:
                    #invalid value, continue loop
                    print("Input out of range")
                    continue
            else:
                if float_val >= max_value:
                    #invalid value, continue loop
                    print("Input out of range")
                    continue

            #validation passed, return value
            return float_val

    elif data_type is complex:

        while True:
            user_input = input(prompt).strip()

            #check if input value is empty
            if not user_input:
                print("Input may not be empty")
                continue

            try:
                #attempt to convert input value to complex
                complex_val = complex(user_input)
            except:
                #if coversion failed, input is invalid, continue loop
                print("Input must be a valid complex number")
                continue
            
            #Only perform this check if min_value is a complex number
            if min_value is complex:
                #check on min_value, depending on can_equal_min_value flag
                if can_equal_min_value:
                    if complex_val < min_value:
                        #invalid value, continue loop
                        print("Input out of range")
                        continue
                else:
                    if complex_val <= min_value:
                        #invalid value, continue loop
                        print("Input out of range")
                        continue

            #Only perform this check if max_value is a complex number
            if max_value is complex:
                #check on max_value, depending on can_equal_max_value flag
                if can_equal_max_value:
                    if complex_val > max_value:
                        #invalid value, continue loop
                        print("Input out of range")
                        continue
                else:
                    if complex_val >= max_value:
                        #invalid value, continue loop
                        print("Input out of range")
                        continue

            #validation passed, return value
            return complex_val

    elif data_type is bool:
        
        true_inputs = ('1', 'y', 'yes', 't', 'true')
        false_inputs = ('0', 'n', 'no', 'f', 'false')

        while True:
            user_input = input(prompt).strip().lower()

            #verify input is not empty
            if not user_input:
                print("Input may not be empty")
                continue

            #verify if input is one of the valid inputs and assign correct value, otherwise loop
            if user_input in true_inputs:
                bool_val = True
            elif user_input in false_inputs:
                bool_val = False
            else:
                print("Input must be either yes or no")
                continue

            return bool_val

    else:
        raise ValueError("Unsupported data type")
    





