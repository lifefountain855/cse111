def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    print(f"reverse: {fruit_list.reverse()}")
    fruit_list.append("orange"); print(fruit_list)
    fruit_list.remove("banana"); print(fruit_list)
    print(f"popped: {fruit_list.pop()} list: {fruit_list}")
    fruit_list.sort(); print(fruit_list)
    fruit_list.clear(); print(fruit_list)




# run if main
if __name__ == "__main__": main()