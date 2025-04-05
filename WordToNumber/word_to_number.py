from __future__ import print_function


american_number_system = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'lac': 100000,
    'lakh': 100000,
    'lakhs': 100000,
    'crore': 10000000,
    'arba': 1000000000,
    'point': '.'
}

decimal_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


"""
function to form numeric multipliers for million, billion, thousand etc.

input: list of strings
return value: integer
"""


def number_formation(number_words):
    numbers = []
    for number_word in number_words:
        numbers.append(american_number_system[number_word])
    
    # Check for invalid number words
    if not numbers:
        return 0

    if len(numbers) == 4:
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif len(numbers) == 3:
        return numbers[0] * numbers[1] + numbers[2]
    elif len(numbers) == 2:
        if 100 in numbers:
            return numbers[0] * numbers[1]
        else:
            return numbers[0] + numbers[1]
    else:
        return numbers[0]

def get_decimal_sum(decimal_digit_words):
    decimal_number_str = []
    invalid_decimals = []
    
    for dec_word in decimal_digit_words:
        if dec_word not in decimal_words:
            invalid_decimals.append(dec_word)
    
    if invalid_decimals:
        error_msg = f"Invalid decimal digits found: {', '.join(invalid_decimals)}. Only words from 'zero' to 'nine' are allowed after 'point'."
        raise ValueError(error_msg)
            
    for dec_word in decimal_digit_words:
        decimal_number_str.append(american_number_system[dec_word])
        
    final_decimal_string = '0.' + ''.join(map(str, decimal_number_str))
    return float(final_decimal_string)

def word_to_num(number_sentence):
    if type(number_sentence) is not str:
        raise ValueError("Type of input is not string! Please enter a valid number word (e.g., 'two million twenty three thousand and forty nine')")

    number_sentence = number_sentence.replace('-', ' ')
    number_sentence = number_sentence.lower()  # converting input to lowercase

    if(number_sentence.isdigit()):  # return the number if user enters a number string
        return int(number_sentence)

    split_words = number_sentence.strip().split()  # strip extra spaces and split sentence into words

    clean_numbers = []
    invalid_words = []
    for word in split_words:
        if word in american_number_system:
            clean_numbers.append(word)
        elif word not in ['and', '&', ',', 'the']:  # Common words to ignore
            invalid_words.append(word)

    # Error message if the user enters invalid input with details on which words were invalid
    if len(clean_numbers) == 0:
        if invalid_words:
            error_msg = f"No valid number words found! Invalid words: {', '.join(invalid_words)}. Please enter valid number words."
        else:
            error_msg = "No valid number words found! Please enter a valid number word (e.g., 'two million twenty three thousand and forty nine')"
        raise ValueError(error_msg)
    
    if invalid_words:
        print(f"Warning: Ignoring invalid words: {', '.join(invalid_words)}")

    clean_decimal_numbers = []

    # Check for redundant number words and provide specific feedback
    redundant_terms = []
    for term in ['thousand', 'million', 'billion', 'arba', 'crore', 'lakh', 'lac', 'lakhs', 'point']:
        count = clean_numbers.count(term)
        if count > 1:
            redundant_terms.append(f"'{term}' (appears {count} times)")
    
    if redundant_terms:
        error_msg = f"Redundant number words found: {', '.join(redundant_terms)}. Each denomination should appear only once."
        raise ValueError(error_msg)

    # separate decimal part of number (if exists)
    if clean_numbers.count('point') == 1:
        point_index = clean_numbers.index('point')
        if point_index == len(clean_numbers) - 1:
            raise ValueError("'point' appears at the end with no decimal digits following it. Please specify decimal digits (e.g., 'point five').")
        clean_decimal_numbers = clean_numbers[point_index+1:]
        clean_numbers = clean_numbers[:point_index]

    billion_index = clean_numbers.index('billion') if 'billion' in clean_numbers else -1
    million_index = clean_numbers.index('million') if 'million' in clean_numbers else -1
    thousand_index = clean_numbers.index('thousand') if 'thousand' in clean_numbers else -1
    
    # Check for lakh/lac/lakhs
    lakh_index = -1
    lakh_term_used = None
    for lakh_word in ['lakh', 'lac', 'lakhs']:
        if lakh_word in clean_numbers:
            lakh_index = clean_numbers.index(lakh_word)
            lakh_term_used = lakh_word
            break
            
    crore_index = clean_numbers.index('crore') if 'crore' in clean_numbers else -1
    arba_index = clean_numbers.index('arba') if 'arba' in clean_numbers else -1

    # Check for valid number word order with specific error messages
    # For American system
    if billion_index > -1 and million_index > -1 and billion_index > million_index:
        raise ValueError("Incorrect order: 'billion' appears after 'million'. The correct order should be: 'billion' → 'million' → 'thousand'.")
    if million_index > -1 and thousand_index > -1 and million_index > thousand_index:
        raise ValueError("Incorrect order: 'million' appears after 'thousand'. The correct order should be: 'billion' → 'million' → 'thousand'.")
    if billion_index > -1 and thousand_index > -1 and billion_index > thousand_index:
        raise ValueError("Incorrect order: 'billion' appears after 'thousand'. The correct order should be: 'billion' → 'million' → 'thousand'.")
        
    # For Indian/Extended system with arba
    if arba_index > -1 and crore_index > -1 and arba_index > crore_index:
        raise ValueError("Incorrect order: 'arba' appears after 'crore'. The correct order should be: 'arba' → 'crore' → 'lakh' → 'thousand'.")
    if arba_index > -1 and lakh_index > -1 and arba_index > lakh_index:
        raise ValueError(f"Incorrect order: 'arba' appears after '{lakh_term_used}'. The correct order should be: 'arba' → 'crore' → 'lakh' → 'thousand'.")
    if arba_index > -1 and thousand_index > -1 and arba_index > thousand_index:
        raise ValueError("Incorrect order: 'arba' appears after 'thousand'. The correct order should be: 'arba' → 'crore' → 'lakh' → 'thousand'.")
    if crore_index > -1 and lakh_index > -1 and crore_index > lakh_index:
        raise ValueError(f"Incorrect order: 'crore' appears after '{lakh_term_used}'. The correct order should be: 'arba' → 'crore' → 'lakh' → 'thousand'.")
    if lakh_index > -1 and thousand_index > -1 and lakh_index > thousand_index:
        raise ValueError(f"Incorrect order: '{lakh_term_used}' appears after 'thousand'. The correct order should be: 'arba' → 'crore' → 'lakh' → 'thousand'.")
    if crore_index > -1 and thousand_index > -1 and crore_index > thousand_index:
        raise ValueError("Incorrect order: 'crore' appears after 'thousand'. The correct order should be: 'arba' → 'crore' → 'lakh' → 'thousand'.")
        
    # Mixing American and Indian/Extended systems - these should be mutually exclusive
    american_terms = []
    indian_terms = []
    
    if billion_index > -1:
        american_terms.append("billion")
    if million_index > -1:
        american_terms.append("million")
    if arba_index > -1:
        indian_terms.append("arba")
    if crore_index > -1:
        indian_terms.append("crore")
    if lakh_index > -1: 
        indian_terms.append(lakh_term_used)
        
    if american_terms and indian_terms:
        raise ValueError(f"Mixing number systems is not supported! Found American system terms ({', '.join(american_terms)}) mixed with Indian system terms ({', '.join(indian_terms)}). Please use either system consistently.")

    # Check for missing intermediate terms between large scales
    if billion_index > -1 and thousand_index > -1 and million_index == -1:
        raise ValueError("Missing 'million' between 'billion' and 'thousand'. The correct hierarchy is 'billion' → 'million' → 'thousand'.")
    
    if arba_index > -1 and thousand_index > -1:
        if crore_index == -1 and lakh_index == -1:
            raise ValueError("Missing 'crore' and 'lakh' between 'arba' and 'thousand'. The correct hierarchy is 'arba' → 'crore' → 'lakh' → 'thousand'.")
        elif crore_index == -1:
            raise ValueError("Missing 'crore' between 'arba' and 'lakh/thousand'. The correct hierarchy is 'arba' → 'crore' → 'lakh' → 'thousand'.")
        elif lakh_index == -1:
            raise ValueError("Missing 'lakh' between 'crore' and 'thousand'. The correct hierarchy is 'arba' → 'crore' → 'lakh' → 'thousand'.")
    
    if crore_index > -1 and thousand_index > -1 and lakh_index == -1:
        raise ValueError("Missing 'lakh' between 'crore' and 'thousand'. The correct hierarchy is 'crore' → 'lakh' → 'thousand'.")
    
    total_sum = 0  # storing the number to be returned

    if len(clean_numbers) > 0:
        # Handle both American and Indian/Extended number systems
        
        # American system (billion, million, thousand)
        if billion_index > -1 or million_index > -1 or (thousand_index > -1 and lakh_index == -1 and crore_index == -1 and arba_index == -1):
            if billion_index > -1:
                billion_multiplier = number_formation(clean_numbers[0:billion_index])
                total_sum += billion_multiplier * 1000000000

            if million_index > -1:
                if billion_index > -1:
                    million_multiplier = number_formation(clean_numbers[billion_index+1:million_index])
                else:
                    million_multiplier = number_formation(clean_numbers[0:million_index])
                total_sum += million_multiplier * 1000000

            if thousand_index > -1:
                if million_index > -1:
                    thousand_multiplier = number_formation(clean_numbers[million_index+1:thousand_index])
                elif billion_index > -1 and million_index == -1:
                    thousand_multiplier = number_formation(clean_numbers[billion_index+1:thousand_index])
                else:
                    thousand_multiplier = number_formation(clean_numbers[0:thousand_index])
                total_sum += thousand_multiplier * 1000

            if thousand_index > -1 and thousand_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[thousand_index+1:])
            elif million_index > -1 and million_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[million_index+1:])
            elif billion_index > -1 and billion_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[billion_index+1:])
            elif thousand_index == -1 and million_index == -1 and billion_index == -1:
                hundreds = number_formation(clean_numbers)
            else:
                hundreds = 0
            total_sum += hundreds
        
        # Indian/Extended system (arba, crore, lakh, thousand)
        elif arba_index > -1 or crore_index > -1 or lakh_index > -1:
            if arba_index > -1:
                arba_multiplier = number_formation(clean_numbers[0:arba_index])
                total_sum += arba_multiplier * 1000000000
                
            if crore_index > -1:
                if arba_index > -1:
                    crore_multiplier = number_formation(clean_numbers[arba_index+1:crore_index])
                else:
                    crore_multiplier = number_formation(clean_numbers[0:crore_index])
                total_sum += crore_multiplier * 10000000

            if lakh_index > -1:
                if crore_index > -1:
                    lakh_multiplier = number_formation(clean_numbers[crore_index+1:lakh_index])
                elif arba_index > -1 and crore_index == -1:
                    lakh_multiplier = number_formation(clean_numbers[arba_index+1:lakh_index])
                else:
                    lakh_multiplier = number_formation(clean_numbers[0:lakh_index])
                total_sum += lakh_multiplier * 100000

            if thousand_index > -1:
                if lakh_index > -1:
                    thousand_multiplier = number_formation(clean_numbers[lakh_index+1:thousand_index])
                elif crore_index > -1 and lakh_index == -1:
                    thousand_multiplier = number_formation(clean_numbers[crore_index+1:thousand_index])
                elif arba_index > -1 and crore_index == -1 and lakh_index == -1:
                    thousand_multiplier = number_formation(clean_numbers[arba_index+1:thousand_index])
                else:
                    thousand_multiplier = number_formation(clean_numbers[0:thousand_index])
                total_sum += thousand_multiplier * 1000

            # Fix for Indian system: Only add the hundreds part if there are words after the last denomination
            if thousand_index > -1 and thousand_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[thousand_index+1:])
                total_sum += hundreds
            elif lakh_index > -1 and lakh_index != len(clean_numbers)-1 and thousand_index == -1:
                # Only add if there's no thousand term (which would have been handled above)
                hundreds = number_formation(clean_numbers[lakh_index+1:])
                total_sum += hundreds
            elif crore_index > -1 and crore_index != len(clean_numbers)-1 and lakh_index == -1 and thousand_index == -1:
                # Only add if there are no lakh or thousand terms (which would have been handled above)
                hundreds = number_formation(clean_numbers[crore_index+1:])
                total_sum += hundreds
            elif arba_index > -1 and arba_index != len(clean_numbers)-1 and crore_index == -1 and lakh_index == -1 and thousand_index == -1:
                # Only add if there are no crore, lakh or thousand terms (which would have been handled above)
                hundreds = number_formation(clean_numbers[arba_index+1:])
                total_sum += hundreds
            elif thousand_index == -1 and lakh_index == -1 and crore_index == -1 and arba_index == -1:
                # If there are no denomination terms at all, treat it as a simple number
                hundreds = number_formation(clean_numbers)
                total_sum += hundreds
        
        # Simple numbers without any system-specific terms
        else:
            total_sum = number_formation(clean_numbers)

    # adding decimal part to total_sum (if exists)
    if len(clean_decimal_numbers) > 0:
        try:
            decimal_sum = get_decimal_sum(clean_decimal_numbers)
            total_sum += decimal_sum
        except ValueError as e:
            raise ValueError(f"Error in decimal part: {str(e)}")

    return total_sum