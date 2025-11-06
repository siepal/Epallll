import random 

def generate_random_quotes():
  quotes = [
    "be great for yourself and everyone around you","know what you desire and what you need","always be the best version of yourself","every second is count","you will get what you do now","be a good man, not a nice guy","know your strength, and proud of your weakness","git gud"
    ]
  return random.choice(quotes)
    
if __name__ ==  "__main__":
    print("here's a random quote for you")
    print(generate_random_quotes())
  
  