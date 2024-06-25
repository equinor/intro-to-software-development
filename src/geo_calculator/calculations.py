def find_average(num_list):
    if len(num_list) == 0:
        return 0
    average = 0
    for i in num_list:
        average += i
    return average / len(num_list)
