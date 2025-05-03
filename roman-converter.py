
def int_to_roman(num):
    """
    Converts a number to Roman numeral.
    Only works for numbers between 1 and 3999.
    """
    if num < 1 or num > 3999:
        return "Invalid input"

    result = ""
    
    # Manually check from largest to smalest value
    while num >= 1000:
        result += "M"
        num -= 1000
    if num >= 900:
        result += "CM"
        num -= 900
    if num >= 500:
        result += "D"
        num -= 500
    if num >= 400:
        result += "CD"
        num -= 400
    while num >= 100:
        result += "C"
        num -= 100
    if num >= 90:
        result += "XC"
        num -= 90
    if num >= 50:
        result += "L"
        num -= 50
    if num >= 40:
        result += "XL"
        num -= 40
    while num >= 10:
        result += "X"
        num -= 10
    if num == 9:
        result += "IX"
        num -= 9
    if num >= 5:
        result += "V"
        num -= 5
    if num == 4:
        result += "IV"
        num -= 4
    while num >= 1:
        result += "I"
        num -= 1

    return result


# Function to convert Roman numera to integer
def roman_to_int(roman):
    """
    Converts a Roman numeral string to an integer.
    Assumes the input is a valid Roman numeral in uppercase.
    """
    total = 0
    i = 0
    while i < len(roman):
        # Handle subtractive combinations like IV, IX, etc.
        if i + 1 < len(roman) and roman[i:i+2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
            if roman[i:i+2] == "IV":
                total += 4
            elif roman[i:i+2] == "IX":
                total += 9
            elif roman[i:i+2] == "XL":
                total += 40
            elif roman[i:i+2] == "XC":
                total += 90
            elif roman[i:i+2] == "CD":
                total += 400
            elif roman[i:i+2] == "CM":
                total += 900
            i += 2
        else:
            # Handle single symbols
            if roman[i] == "I":
                total += 1
            elif roman[i] == "V":
                total += 5
            elif roman[i] == "X":
                total += 10
            elif roman[i] == "L":
                total += 50
            elif roman[i] == "C":
                total += 100
            elif roman[i] == "D":
                total += 500
            elif roman[i] == "M":
                total += 1000
            i += 1

    return total


# Example to test both functions
if __name__ == "__main__":
    print("Integer to Roman:")
    print("58 ->", int_to_roman(58))      # Should print LVIII
    print("1994 ->", int_to_roman(1994))  # Should print MCMXCIV

    print("\nRoman to Integer:")
    print("LVIII ->", roman_to_int("LVIII"))    # Should print 58
    print("MCMXCIV ->", roman_to_int("MCMXCIV"))  # Should print 1994
