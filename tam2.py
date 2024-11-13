
odd_numbers = [i for i in range(51) if i % 2 != 0]

for number in odd_numbers[:]:  
    if number % 5 == 0 or number % 3 == 0:
        odd_numbers.append(number)

print(odd_numbers)

