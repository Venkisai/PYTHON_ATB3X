with open('Venkat.txt', 'r') as file:
    print(file.read())
    file.close()


try:
    with open('example.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as fnfe:
    print("I am not able to find the file, Please check the path")
finally:
    file.close()



try:
    with open('Venkat.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as fnfe:
    print("I am not able to find the file, Please check the path")
finally:
    print("Closing the file")
    file.close()


try:
    file = open('Venkat.txt', 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("I am not able to find the file, Please check the path")
finally:
    print("Executed")
    try:
        file.close()
    except NameError as ne:
        print(ne)

