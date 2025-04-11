# Create variables to handle variants
card_number = input("Enter a card number ")
card_number = card_number.replace(" ","")
card_number = card_number.replace("-","")
card_number = card_number[::-1]

sum_of_odd_nums = 0
sum_of_even_nums = 0
total = 0

# Loop for all odd places and sum them all up
for i in card_number[::2]:
    sum_of_odd_nums += int(i)

# Loop for all even places and multiply
for i in card_number[1::2]:
    x = int(i) * 2
    # If greater than 9
    if x >= 10:
        # Split it using modulus
        sum_of_even_nums += (1 + (int(x) % 10))
    else:
        # Else, sum them all up
        sum_of_even_nums += int(x)

# Sum the total of even places and odd places
total = sum_of_even_nums + sum_of_odd_nums

# If sum is divisible by 10, valid
if total % 10 == 0:
    print("Valid")
# Else, invalid
else:
    print("Invalid")
