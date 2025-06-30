def find_average(data_list: list) -> float:
    sum = 0
    for i in data_list:
        sum += i
    return sum/len(data_list)