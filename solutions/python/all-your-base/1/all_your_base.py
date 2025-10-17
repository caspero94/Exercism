def rebase(input_base, digits, output_base):
    # Error in input, digits or output
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if -1 in digits or (input_base) in digits:
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    # Convertirmos digits en decimal
    decimal = 0
    power = len(digits) - 1
    for digit in digits:
        decimal += digit * (input_base ** power)
        power -= 1
    # Convertimos decimal a base salida
    result = []
    while decimal > 0:
        remainder = decimal % output_base
        result.insert(0, remainder)
        decimal //= output_base
    return result if result else [0]    