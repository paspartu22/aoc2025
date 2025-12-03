# def part1(name):
#     with open(name) as file:
#         result = 0
#         for line in file.readlines():
#             first, first_position, second = 0,0,0

#             for i in range(len(line.strip())-1):
#                 if int(line[i]) > first:
#                     first = int(line[i])
#                     first_position = i
#             for i in range(first_position+1, len(line.strip())):
#                 if int(line[i]) > second:
#                     second = int(line[i])
#             print (first*10+second)
#             result += first*10+second
#     return result



def part2(name, size):
    with open(name) as file:
        result = 0
        for line in file.readlines():
            # print(f'line = {line.strip()}')
            number_string = ""
            last_position = -1
            for i in range(size):
                number_string += "0"
                for j in range(last_position+1, len(line.strip())-size+1+i):
                    if int(line[j]) > int(number_string[-1]):
                        number_string = number_string[:-1]+line[j]
                        last_position = j
            # print(f'result = {number_string}')
            result += int(number_string)
    return result


def main():
    # print("357 should be")
    # print(part1('day03/test.txt'))
    # print(part1('day03/data.txt'))

    print("357")
    print(part2('day03/test.txt', 2))
    print(part2('day03/data.txt', 2))
    print("3121910778619")
    print(part2('day03/test.txt', 12))
    print(part2('day03/data.txt', 12))

if __name__ == "__main__":
    main()