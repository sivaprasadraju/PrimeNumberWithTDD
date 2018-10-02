def prime_number(number):
	if number < 0:
        raise ValueError('Input should be positive')
		
	if number == 0:
        return False
		
	if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False