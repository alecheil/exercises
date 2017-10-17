UPPER_LIMIT = 5

def check_numbers(x,y,z):
    print(x,y,z)

    for x in range(UPPER_LIMIT):
        for y in range(UPPER_LIMIT):
            for z in range(UPPER_LIMIT):
                check_numbers(x,y,z)

