#MadLib.py
#Name: Samantha Roth
#Date: 8/27/2024
#Assignment: Lab 1

def main():
  print("Let’s play Mad-Libs!")
  #Ask user for words
  print("Let's write a story called: A Day at the Park")
  name = input("First, let's name our character. ")
  print("Let's describe", name )
  print("Give me an adjective.") 
  adj1 = input("Remember, that's a descriptive word descriptive word like red, tall, or happy.) ")
  animal = input("Now, what is your favorite animal? ")
  color = input("What about your favorite color? ")
  noun1 = input("This time we need a noun. (Remember elementary? Person, place, thing.) ")
  verb1 = input("What about a verb? That describes what they're doing like run, jump, or eat. ")
  adj2 = input("Now, we need another adjective. ")
  noun2 = input("And another noun... ")
  verb2 = input("Finally, we need a verb ending in -ed. ")
  #Print the story with the user supplied words.
  print("Yay! Our Mad-Lib is finished! Do you want to see the final story?")
  yes = input('Hopefully you say "Yes!" ')
  if yes.lower() == "yes":
    print("Here's your story!")
    print("Today,", name, "went to the park with a", adj1, animal,".")
    print("They found a", color, noun1, "and decided to", verb1, "it. ")
    print("Suddenly, a", adj2, noun2, "appeared, and they all", verb2, "together! ")
  else:
    print("After all that work?! Come back if you change your mind!")
#Call the main function if this is the file being run.
if __name__ == '__main__':
  main()
