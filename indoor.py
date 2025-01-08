def main():
    name = input("Enter anything please").casefold()
    hello(name)

def hello(user_name):
    print(f"Hello,{user_name}")



main()


