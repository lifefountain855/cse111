#!/usr/bin/env python3
import time

def run():
    activityList = ["volleyball", "gaming", "learning new things"]
    name = input("Hey! What is your name? ")
    print(f"Hello, {name}! Nice to meet you!\n")
    print("About me:")
    print("- I'm Kevin, an Software Engineer student at BYUI")
    print(f"- I love {activityList[0]}, {activityList[1]}, and {activityList[2]}")
    print("- I have been programming since I was a kid\n")
    info = input(f"What about you, {name}? What do you enjoy? ")
    print()
    if info.lower() == "programming":
        print("That's awesome! Programming is a great skill to have.")
        lang = input("What programming languages do you use? ")
        if lang.lower() == "python":
            passw = input("I like where this is going. You're close. Whats the secret password? ")
            if passw.lower() == "keviniscool":
                print("Congratulations! You've unlocked the secret message!")
                time.sleep(1)
                print("The secret message is: Kevin is the best programmer ever!")
            else:
                print("Sorry, that's not the correct password. Better luck next time!\n")
        else:
            print(f"That's great! {lang} is a powerful language.")
    elif info.lower() in activityList:
        print(f"Wow! {info} is one of my favorite activities too!")
    else:
        print(f"Interesting! {info} sounds like a great activity.")
def main():
    run()
    again = input("Press Enter to exit... or 'a' for again.")
    if again.lower() == 'a':
        main()
    else:
        print("=" * 50)
        print("Thanks for stopping by! Goodbye!")
        print("=" * 50)

if __name__ == "__main__":
    main()
