
n1 = 2
n2 = 4

print('{} + {}'.format(n1, n2))

answer = n1 + n2
guess = int(input("> "))

if guess == answer:
    print("Correct!")
else:
    print("Wrong!")
