def classify(n):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if n < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    suma_alicuota = sum([i for i in range(1, n) if n % i == 0])
    
    if suma_alicuota == n:
        return "perfect"
    elif suma_alicuota > n:
        return "abundant"
    else:
        return "deficient"