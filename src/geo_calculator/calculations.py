def find_avrage(numbers):
    sum=0
    for i in numbers:
        sum += i
    length = len(numbers)
    avrage = sum/length
    return avrage