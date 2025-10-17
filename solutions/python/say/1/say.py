def say(number):

    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

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
        return (ones[n // 100] + ' hundred' if (n//100) != 0 else '') + ((' '+ less_than_100(n % 100)) if n % 100 != 0 else '')
    
    def thousand(n):
        if (n//1000)<99:
            return less_than_100(n//1000) + ' thousand' + (' ' + hundred(n%1000) if n%1000 != 0 else '')
        return hundred(n//1000) + ' thousand' + (' ' + hundred(n%1000) if n%1000 != 0 else '')
    
    def millon(n):
        if (n//1000000)<99:
            return less_than_100(n//1000000) + ' million' + (' ' + thousand(n%1000000) if n%1000000 != 0 else '')
        return hundred(n//1000000) + ' million' + (' ' + thousand(n%1000000) if n%1000000 != 0 else '')
    
    def billion(n):
        if (n//1000000000)<99:
            return less_than_100(n//1000000000) + ' billion' + (' ' + millon(n%1000000000) if n%1000000000 != 0 else '')
        return hundred(n//1000000000) + ' billion' + (' ' + millon(n%1000000000) if n%1000000000 != 0 else '')
    
    if number < 100:
        return less_than_100(number)

    if number < 1000:
        return hundred(number)

    if number < 1000000:
        return thousand(number)
    
    if number < 1000000000:
        return millon(number)
    
    if number < 1000000000000:
        return billion(number)
