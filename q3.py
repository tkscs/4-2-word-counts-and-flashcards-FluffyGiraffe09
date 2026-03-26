# Update this dictionary with questions and answers:
import random
flashcards = {
    "what is the conjugation of the shoresh ctv, in the binyan nifal": "nichtav", "what is the conjugation of the shoresh ctv, in the binyan hifil": "hichtiv", "what is the conjugation of the shoresh ctv, in shem hapoal in nifal": "l'hicatev", "what is the conjugation of the shoresh ctv, shem peula for nifal": "hicatvut"
}

# Get a list of keys (questions) from the dictionary
#### YOUR CODE HERE
list_keys = []
for key in flashcards:
    list_keys.append(key)

# Randomly sample one question
#### YOUR CODE HERE

question = random.choice(list_keys)

# Use the `input` function to ask the user the question and get their response
#### YOUR CODE HERE

user_answer = input(question)

# Use the question as a key to look up the answer in the dicitonary
#### YOUR CODE HERE

answer = flashcards[question]

if answer == user_answer:
    print("Good job!! You got it right")
else:
    print("Yikkkkkeeeess...Thats really awkward that you don't know that one yet.")

# Check if the response is the same as the answer, and give the user
# feedback based on whether their response was correct or incorrect
#### YOUR CODE HERE