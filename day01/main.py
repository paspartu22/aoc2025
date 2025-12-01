def part1(name):
    print()
    print(name)
    with open(name) as file:
        result = 0
        current_value = 50
        for line in file.readlines():
            # print(line.strip())
            if line[0] == 'R':
                current_value += int(line[1:])
            else:
                current_value -= int(line[1:])
            # print (current_value)
            if current_value%100 == 0:
                result += 1
        print (result)
            # if (current_value > 99)


def part2(name):
    print()
    print(name)
    with open(name) as file:
        result = 0
        current_value = 50
        for line in file.readlines():
            # print(line.strip())

            for i in range(int(line[1:])):
                if line[0] == 'R':
                    current_value += 1
                else:
                    current_value -= 1

                current_value %= 100
                # print(current_value)
                if (current_value == 0):
                    result += 1
            # print (current_value)

            # while current_value < 0 or current_value > 99:
            #     if current_value > 99:
            #         current_value -= 100
            #         result += 1
            #         print(f'{result}  {current_value}')
            #     if current_value < 0:
            #         current_value += 100
            #         result += 1
            #         print(f'{result}  {current_value}')

        print ("==="+str(result))
            # if (current_value > 99)

part1('day01/test.txt')
part1('day01/data.txt')

part2('day01/test2.txt')
part2('day01/test.txt')
part2('day01/data.txt')
