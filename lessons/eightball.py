from random import randint

question: str = input("What is your yes/no question? ")
response: int = randint(1, 5)

if response == 0:
    print("Yes, def")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("Yeah, ofc....not")
else:
    print("My sources say no")