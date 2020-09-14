import redis

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Add Task
def add_data(add_name):
    while True:
        input_data = input("Enter data to add: ")

        if input_data != "":
            r.rpush(add_name, input_data)
        else:
            print("Exit add data")
            break

    print()


# Delete Task
def del_data(del_name):
    data_list = r.lrange(del_name, 0, -1)
    if data_list:
        while True:
            input_data = input("Enter data to remove: ")

            if input_data != "":
                result = r.lrem(del_name, 0, input_data)

                if result == 0:
                    print("No data to remove in Redis!")

            else:
                print("Exit remove data")
                break
    else:
        print("No data for remove, Please add data!")

    print()


# View Task
def show_data(show_name):
    data_list = r.lrange(show_name, 0, -1)

    if data_list:
        for data in data_list:
            print(data.decode("utf-8"), end=" ")
    else:
        print("Empty list or set!", end="")

    print("\n")


# Easy Problems
def item1():
    try:
        while True:
            result = [
                "Fizz"
                if i % 3 == 0 and not i % 5 == 0
                else (
                    "Buzz"
                    if i % 5 == 0 and not i % 3 == 0
                    else ("FizzBuzz")
                    if i % 3 == 0 and i % 5 == 0
                    else i
                )
                for i in range(1, 101)
            ]
            print(result)
    except:
        menu_easy()


def item2():
    try:
        while True:
            year = int(input("Enter year: "))
            print(
                year, " -> ", [year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)]
            )
    except:
        menu_easy()


def item3_1():
    try:
        while True:
            number = int(input("Enter number: "))
            for i in range(1, number + 1):
                print("*" * i)
    except:
        menu_easy()


def item3_2():
    try:
        while True:
            number = int(input("Enter number: "))
            for i in range(1, number + 1):
                print(" " * (number - i) + "*" * i)
    except:
        menu_easy()


def item3_3():
    try:
        while True:
            number = int(input("Enter number: "))
            for i in range(number):
                print(" " * (number - i - 1) + "*", end="")
                if i >= 1:
                    print(" " * (2 * i - 1) + "*", end="")
                print()
    except:
        menu_easy()


def item3_4():
    try:
        while True:
            number = int(input("Enter number: "))
            star = "*" * number
            length = len(star)

            for i in range(length):
                for j in range(length):
                    if i == j or i + j == length - 1:
                        print(star[i], end="")
                    else:
                        print(" ", end="")
                print()
    except:
        menu_easy()


def item3_5():
    try:
        while True:
            number = int(input("Enter number: "))
            a = 1
            b = 1
            for a in range(number + 1):
                if a % 2 != 0:
                    val = (number - a) // 2
                    print(" " * val + "*" * (a) + " " * val, end="\n")
            for b in range(number - 1, 0, -1):
                if b % 2 != 0:
                    val2 = (number - b) // 2
                    print(" " * val2 + "*" * (b) + " " * val2, end="\n")
    except:
        menu_easy()


def item3_6():
    try:
        while True:
            number = int(input("Enter number: "))
            for i in range(0, number):
                for j in range(1, number - i):
                    print("A", end="")
                print("+", end="")
                if i > 0:
                    for j in range(0, (i * 2) - 1):
                        print("E", end="")
                    print("+", end="")
                for j in range(1, number - i):
                    print("B", end="")
                print(" ")

            for i in range(0, number - 1):
                for j in range(1, i + 2):
                    print("C", end="")
                print("+", end="")
                for j in range(0, ((number - i - 2) * 2) - 1):
                    print("E", end="")
                if i < number - 2:
                    print("+", end="")
                for j in range(1, i + 2):
                    print("D", end="")
                print(" ")
    except:
        menu_easy()


def item4():
    print("ข้อแตกต่างรหว่าง else กับ finally")
    print(
        "else จะทำงานก็ต้องเมื่อ try ไม่เกิด error\nfinally จะทำงานทุกครั้งโดยไม่สนว่า try จะ error รึเปล่า"
    )
    print("เช่น\nกรณีที่ try error")
    try:
        a = 10
        b = 0
        x = a / b
    except ZeroDivisionError:
        print("เกิด exception")
    else:
        print("เกิด else")
    finally:
        print("เกิด finally")
    print("\nกรณีที่ try ทำงานปกติ")
    try:
        a = 10
        b = 1
        x = a / b
    except ZeroDivisionError:
        print("exception")
    else:
        print("เกิด else")
    finally:
        print("เกิด finally")
    print(
        "จากที่เห็นเกิด finally ทั้งสองกรณีแต่ else เกิดแค่กรณีเดียวคือ try ยังทำงานได้ปกติ"
    )


# Menu and medium problems
def menu_medium():
    try:
        while True:
            inputNumber = input("Please enter a number? : ")
            number = int(inputNumber)
            if number >= 0:
                number = int(number)
                prime_list = [
                    x
                    for x in range(2, number + 1)
                    if all(x % y != 0 for y in range(2, x))
                ]
                print(number, " -> ", prime_list)
            elif number < 0:
                print("Please try again!")
                pass
    except:
        main_menu()


# Main menu
def main_menu():
    while True:
        print("\nSelect a function?\n")
        print("t - Todo List")
        print("e - Easy problems")
        print("m - Medium problems\n")

        inputMenu = input("Please enter a function? : ").lower().strip()

        if inputMenu == "t":
            todo_menu(redis_keys)
        elif inputMenu == "e":
            menu_easy()
        elif inputMenu == "m":
            menu_medium()
        else:
            pritn("Please try again!")
            pass


# Todo list menu
def todo_menu(todo_menu):
    print("\nSelect a function?\n")
    print("a - Add")
    print("d - Delete")
    print("v - View")
    print("\nb - Back to main menu")
    print("q - Quit program\n")

    while True:
        inputMenu = input("Please enter a function? : ").lower().strip()

        if inputMenu == "a":
            add_data(redis_keys)
        elif inputMenu == "d":
            del_data(redis_keys)
        elif inputMenu == "v":
            show_data(redis_keys)
        elif inputMenu == "b":
            main_menu()
        elif inputMenu == "q":
            exit()
        else:
            pritn("Please try again!")
            pass


# Menu easy problems
def menu_easy():
    print("\nSelect a function?\n")
    print("  1 - Numbers of multiply")
    print("  2 - Leap year\n")
    print("  3.1 - * Pattern 1")
    print("  3.2 - * Pattern 2\n")
    print("  3.3 - * Pattern 3")
    print("  3.4 - * Pattern 4\n")
    print("  3.5 - * Pattern 5")
    print("  3.6 - * Pattern 6\n")
    print("  4 - Difference between else and finally")
    print("\n  B - Back to main menu")
    print("  Q - Quit program\n")

    while True:
        inputMenu = input("Please enter a function? : ").lower().strip()

        if inputMenu == "1":
            item1()
        elif inputMenu == "2":
            item2()
        elif inputMenu == "3.1":
            item3_1()
        elif inputMenu == "3.2":
            item3_2()
        elif inputMenu == "3.3":
            item3_3()
        elif inputMenu == "3.4":
            item3_4()
        elif inputMenu == "3.5":
            item3_5()
        elif inputMenu == "3.6":
            item3_6()
        elif inputMenu == "4":
            item4()
        elif inputMenu == "b":
            main_menu()
        elif inputMenu == "q":
            exit()
        else:
            print("Please try again!")
            pass


redis_keys = "todolist"
main_menu()