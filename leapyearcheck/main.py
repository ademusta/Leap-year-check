# This is a sample Python script.
year = int(input("Which year do you want to check? "))
if year%400==0:
    print("Leap year")
elif year%100==0  :
    print("Not leap")
elif year%4==0 :
    print("Leap year")
else:
    print("Not leap")
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
