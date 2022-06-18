import re


def validating_cpf(cpf):
    
    def remove_caracteres(cpf):
        new_cpf = re.sub(r'[^0-9]', '', cpf)
        return new_cpf

    def formula(value):
        formula = 11 - (value % 11)
        if formula > 9:
            formula = 0
        return formula
        

    new_cpf = remove_caracteres(cpf)
    validating_cpf = new_cpf[:-2]

    count = 10
    total = 0

    for number in validating_cpf:
        calculus = int(number) * count
        total += calculus
        count -= 1

    first_digit = formula(total)
    validating_cpf += str(first_digit)

    count = 10
    total = 0

    for number in validating_cpf:
        calculus = int(number) * (count+1)
        total += calculus
        count -= 1

    second_digit = formula(total)
    validating_cpf += str(second_digit)
    
    if validating_cpf == new_cpf:
        return True
    else:
        return False
        