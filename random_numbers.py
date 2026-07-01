import random

def append_random_words(words_list,quantity=1):
    list_of_words=[""]
    for i in range(0,quantity):
        words_list.append(random.choice(list_of_words))

def append_random_numbers(numbers_list,quantity=1):
    for i in range(0,quantity):
        numbers_list.append(round(random.uniform(0.01,100.00),2))

def main():
    numbers=[]
    words=[]
    mode_select='def'
    while mode_select != 'e':
        mode_select=input("Choose mode: \n  -Words (w)\n  -Numbers (n)\n  -Reset (r)\n  -Exit (e)\nMode: ")
        match mode_select:
            case 'w':
                quant=int(input("Enter number of words you want: "))
                append_random_words(words,quant)
            case 'n':
                quant=int(input("Enter number of numbers you want: "))
                append_random_numbers(numbers,quant)
            case 'r':
                words=[]
                numbers=[]
            case 'e':
                break
        print(f"\n    Numbers: {numbers}\n    Words: {words}\n")
    # numbers = [16.2, 75.1, 52.3]
    # print(numbers)
    # append_random_numbers(numbers)
    # print(numbers)
    # append_random_numbers(numbers,3)
    # print(numbers)


if __name__ == "__main__":
    main()