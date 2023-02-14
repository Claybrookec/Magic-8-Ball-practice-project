import random
name = "Brooke"
question = "Will humans live on Mars?"
answer = "Humans will live on Mars"
random_number = random.randint(1, 11)
print(random_number)
if random_number == 1:
  answer = "No shot"
elif random_number == 2:
  answer = "For sure"
elif random_number == 3:
  answer = "Maybe"
elif random_number == 4: 
  answer = "Possibly, but not likely"
elif random_number == 5:
  answer = "No"
elif random_number == 6:
  answer = "Yes"
elif random_number == 7: 
  answer = "Only Musk and Bezos know, ask them"
elif random_number == 8:
  answer = "Very likely"
elif random_number == 9:
  answer = "Humans will go extinct on Earth!"
elif random_number == 10:
  answer = "Absolutely not"
elif random_number == 11:
  answer = "Absolutely, probably by next year"
else:
  answer = "Error"
print(name + " asks " + question)
print("Magic 8-Ball's answer: " + answer)