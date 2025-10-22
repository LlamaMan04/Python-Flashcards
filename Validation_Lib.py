from enum import Enum

class String_Valdiation_Type(Enum):
    NONE = 0                        #No validation
    ALPHA = 1                       #All characters are letters
    ALPHA_AND_SPACE = 2             #All characters are letters or whitespace
    ALPHANUMERIC = 3                #All characters are letters or numbers
    ALPHANUMERIC_AND_SPACE = 4      #All characters are letters, numbers, or whitespace
    DIGITS = 5                      #All characters are numeric digits
    DIGITS_AND_SYMBOLS = 6          #All characters are numeric digits or symbols used with numbers (. , $ % - # ^ *) (but not other math symbols)
