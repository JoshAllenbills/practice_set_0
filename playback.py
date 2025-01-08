def main():
    name = input("Enter anything please").strip().title()
    hello(name)

def hello(user_name):
    modified_name = user_name.replace(" ", "...")
    print(modified_name)

main()