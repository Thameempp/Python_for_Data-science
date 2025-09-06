
def raise_to_power(base, powr):
    result = 1
    for index in range(powr):
        result = result * base
    return result

#print(raise_to_power(3, 2))
print(3**2)