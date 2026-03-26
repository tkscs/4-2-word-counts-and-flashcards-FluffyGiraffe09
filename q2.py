"""
INSTRUCTIONS:
The code below has a lot of repetition. Use a dictionary and a for loop to 
make the code more compact.
"""

def pad_word_count(essay):
  new_essay = essay
  dictionary = {}
  dictionary["n't"] = " not"
  dictionary["'s"] = " is"
  dictionary["'re"] = " are"
  dictionary["'ve"] = " have"
  for key, value in dictionary.items():
    new_essay = new_essay.replace(key, value)
  return new_essay

print(pad_word_count(
  """
  Cats are cute.
  They've been pets for thousands of years.
  They're playful and cuddly, but they don't need as much attention as dogs.
  It's clear that they're silly, and they love knocking things over.
  It isn't possible to see a cat and not want to cuddle it.
  That's all I have to say about cats."""
))