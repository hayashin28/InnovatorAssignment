# 2D Multiplication Table (九九表)

def print_multiplication_table() -> None:
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i * j:2}", end=" ")
        print()


print_multiplication_table()




def print_odd_multiplication_table() -> None:
    for i in range(1, 10):
        for j in range(1, 10):
            if i % 2 != 0 and j % 2 != 0:
                print(f"{i * j:2}", end=" ")
        print()


print_odd_multiplication_table()


def print_multiplication_table_stop_at_50() -> None:
    for i in range(1, 10):
        for j in range(1, 10):
            product = i * j
            if product >= 50:
                break
            print(f"{product:2}", end=" ")
        print()


print_multiplication_table_stop_at_50()