def convert(saying):
    saying_one = saying.replace(":)", "🙂")
    final_saying = saying_one.replace(":(","🙁" )
    print(final_saying)


def main():
    user_saying = input("What would you like to say?: ")
    convert(user_saying)

main()