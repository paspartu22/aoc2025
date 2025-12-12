def part1(name):
    with open(name) as file:
        result = 0
        block = []
        blocks = file.read().split('\n\n')
        for item in blocks[:-1]:
            print(item)
            print()
            block.append(item.count('#'))
        print(block)
        for task in blocks[-1].split('\n'):
            left = task.split(':')[0].split('x')
            left = int(left[0]) * int(left[1])
            right = task.split(':')[1].split(' ')[1:]
            right = sum([int(amount)*block[i] for i,amount in enumerate(right)])
            # print(f'{left} {right}')
            if left*0.8 > right:
                    result += 1

    return result


def part2(name):
    with open(name) as file:
        result = 0

    return result



def main():
    print(" should be")
    print(part1('day12/test.txt'))
    print(part1('day12/data.txt'))

    # print(" should be")
    # print(part2('day02/test.txt'))
    # print(part2('day02/data.txt'))

if __name__ == "__main__":
    main()