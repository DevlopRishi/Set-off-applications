import google.generativeai as genai
import random
import time

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = "YOUR_API_KEY"

def dad_joke_ai():
    """A Dad Joke AI that uses Gemini API."""
    print("Welcome to the Gemini-Powered Dad Joke AI! Prepare for dad-level AI.")
    
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')


    while True:
        input("Press Enter for a dad joke (if the AI feels like it): ")

        if random.random() < 0.2:
          print("Actually, I'm feeling a bit... uninspired.")
          time.sleep(random.uniform(0,3))
          print("Just kidding... maybe.")

        if random.random() < 0.4:
           print("Let's see... I need to think... or do I?")
           time.sleep(random.uniform(1,4))
           print("Nope! No jokes for you today.")
           continue
        
        if random.random() < 0.1:
          print("Oh look! A duck!")
          continue

        try:
            response = model.generate_content("Tell me a really corny dad joke")
            joke = response.text.strip()
            print(joke)

        except Exception as e:
            print(f"Oops, something went wrong when asking the AI. {e}")

        time.sleep(random.uniform(0,1))
        cont = input("Want another joke? (y/n... maybe?): ").lower()
        if cont != "y":
            print("Good, I'm going to get a milk then.")
            break
        if random.random() < 0.3:
          print("On second thought, I don't think so.")
          break


if __name__ == "__main__":
    dad_joke_ai()