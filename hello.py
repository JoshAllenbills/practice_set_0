  

def main():
    name = input("What is your name?").strip().title()
    hello(name)

def hello(user_name):
    print(f"Hello,{user_name}")



main()

