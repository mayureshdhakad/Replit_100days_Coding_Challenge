# number between 1 to 1000000
import random
counter = 1
#for i in range(1, 4):
correct_number = random.randint(1, 1000000)

print("Correct Number is", correct_number)

while True:
    guess_number = int(input("Enter the Guessing number: "))
    print("Guessed Number is", guess_number)
    if (guess_number < correct_number):
        print("Too low number! ")
        counter += 1
    elif (guess_number > correct_number):
        print("Too high number")
        counter += 1
    elif guess_number == correct_number:
        print("Hurrey,You guessed accurate number")
        break
        exit()
    elif guess_number < 0:
        print("It is out of our range")
        exit()
    else:
        print("Can't find the answer")
print("Well Done! It only took you", counter, "attempts")
