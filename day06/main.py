import math

def part1(name):
    with open(name) as file:
        result = 0
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
        slices = ["" for i in range(len(lines))]
        tasks = []
        for i in range(len(lines[0])):
            for j in range(len(lines)):
                if (len(lines[j]) > i):
                    slices[j] += lines[j][i]
            if all(False for s in slices if s[-1] != " "):
                tasks.append(slices)
                slices = ["" for i in range(len(lines))]
        tasks.append(slices)
        print(tasks)
        for task in tasks:
            if "+" in task[-1]:
                result += sum([int(t) for t in task[:-1]])
            else:
                result += math.prod([int(t) for t in task[:-1]])
    return result


def part2(name):
    with open(name) as file:
        result = 0
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
        slices = ["" for i in range(len(lines))]
        tasks = []
        for i in range(len(lines[0])):
            for j in range(len(lines)):
                if (len(lines[j]) > i):
                    slices[j] += lines[j][i]
            if all(False for s in slices if s[-1] != " "):
                tasks.append(slices)
                slices = ["" for i in range(len(lines))]
        tasks.append(slices)
        for t in tasks:
            print(t)
        print()
        
        for task in tasks:
            numbers = []
            for i in range(len(task[0])):
                numbers.append("")
                for j in range(len(task)-1):
                    numbers[i] += task[j][i]
            print(numbers)            

            numbers = [int(t) if t.strip(" ").isdigit() else 0 for t in numbers]
            if 0 in numbers:
                numbers.pop()
            print(numbers)
            if "+" in task[-1]:
                result += sum(numbers)
            else:
                result += math.prod(numbers)

                


    return result


#5944540469792 to low
def main():
    print("4277556 should be")
    # print(part1('day06/test.txt'))
    # print(part1('day06/data.txt'))

    print(" should be")
    print(part2('day06/test.txt'))
    print(part2('day06/data.txt'))

if __name__ == "__main__":
    main()