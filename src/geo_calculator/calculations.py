def find_average(data_list: list) -> float:
    sum = 0
    for i in data_list:
        sum += i
    return sum/len(data_list)

def gardners_equation(velocity):
    return 0.31*(velocity**0.25)