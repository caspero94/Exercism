def say(number):

    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    BILLION, MILLION, THOUSAND, HUNDRED = 1000000000, 1000000, 1000, 100

    ones = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    teens = {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 
        18: 'eighteen', 19: 'nineteen'
    }

    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    def less_than_100(n):
        if n < 10:
            return ones[n]
        elif n < 20:
            return teens[n]
        else:
            return tens[n // 10] + ('-' + ones[n % 10] if n % 10 != 0 else '')

    def hundred(n):
        return (ones[n // HUNDRED] + ' hundred' if (n//HUNDRED) != 0 else '') + ((' '+ less_than_100(n % HUNDRED)) if n % HUNDRED != 0 else '')
    
    def thousand(n):
        if (n//THOUSAND)<99:
            return less_than_100(n//THOUSAND) + ' thousand' + (' ' + hundred(n%THOUSAND) if n%THOUSAND != 0 else '')
        return hundred(n//THOUSAND) + ' thousand' + (' ' + hundred(n%THOUSAND) if n%THOUSAND != 0 else '')
    
    def millon(n):
        if (n//MILLION)<99:
            return less_than_100(n//MILLION) + ' million' + (' ' + thousand(n%MILLION) if n%MILLION != 0 else '')
        return hundred(n//MILLION) + ' million' + (' ' + thousand(n%MILLION) if n%MILLION != 0 else '')
    
    def billion(n):
        if (n//BILLION)<99:
            return less_than_100(n//BILLION) + ' billion' + (' ' + millon(n%BILLION) if n%BILLION != 0 else '')
        return hundred(n//BILLION) + ' billion' + (' ' + millon(n%BILLION) if n%BILLION != 0 else '')
    
    if number < HUNDRED:
        return less_than_100(number)

    if number < THOUSAND:
        return hundred(number)

    if number < MILLION:
        return thousand(number)
    
    if number < BILLION:
        return millon(number)
    
    else:
        return billion(number)
