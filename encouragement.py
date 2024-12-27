import random
import time

def cheer(fn):
    cheers = [
        "You got this!",
        "Way to go!",
        "Great work!",
        "Sweeeeeet!",
        "Keep it up!"
        ]

    def get_encouragement(*args, **kwargs):
        output = fn(*args, **kwargs)
        random.seed(time.time_ns())
        print(cheers[random.randint(0, len(cheers))])
        return output

    return get_encouragement

@cheer
def nap():
    time.sleep(10)

@cheer
def pig_latin(sentence):
    words = sentence.split()
    
    def platinfy(word):
      word = word.lower()
      vowels = ["a", "e", "i", "o", "u"]
      if word[0] in vowels:
        return word + "way"
      elif word[1] in vowels + ["y"]:
        return word[1:] + word[0] + "ay"
      else:
        return word[2:] + word[0:2] + "ay"

    words_with_ay = map(platinfy, words)

    return " ".join(words_with_ay)
