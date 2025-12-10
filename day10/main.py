def part1(name):
    with open(name) as file:
        result = 0 
        for line in file.readlines():
            parttern, line = line.split(']')
            parttern = parttern[1:]
            parttern = sum([2**i if parttern[i] == '#' else 0 for i in range(len(parttern))])
            buttons, joltage = line.split('{')
            buttons = [b[1:-1].split(',') for b in buttons.split(' ')]
            buttons = [[int(b) for b in but] for but in buttons if but[0] != ""]
            print(parttern)
            print(buttons)
                    
            # Mark all the vertices as not visited
            visited = {}
            # Create a queue for BFS
            queue = []

            # Mark the source node as
            # visited and enqueue it
            queue.append(0)
            visited[0] = []

            while queue:

                # Dequeue a vertex from
                # queue and print it
                state = queue.pop(0)
                # print(state, end=" ")

                # Get all adjacent vertices of the
                # dequeued vertex s.
                # If an adjacent has not been visited,
                # then mark it visited and enqueue it
                for button in buttons:
                    new_state = state
                    for b in button:
                        new_state ^= 2**b

                    if new_state not in visited:
                        queue.append(new_state)
                        visited[new_state] = visited[state].copy()
                        visited[new_state].append(button)
                    if new_state == parttern:
                        print(visited[new_state])
                        queue = []
                        result += len(visited[new_state])
                        break
    return result


def part2(name):
    with open(name) as file:
        result = 0 
        for line in file.readlines():
            parttern, line = line.split(']')
            parttern = parttern[1:]
            parttern = sum([2**i if parttern[i] == '#' else 0 for i in range(len(parttern))])
            buttons, joltage = line.split('{')
            buttons = [b[1:-1].split(',') for b in buttons.split(' ')]
            buttons = [[int(b) for b in but] for but in buttons if but[0] != ""]
            joltage = [int(j) for j in joltage.strip()[:-1].split(',')]
            print('=============')
            print(parttern)
            print(buttons)
            print(joltage)
            print('-------------')
            # Mark all the vertices as not visited
            visited = {}
            # Create a queue for BFS
            queue = []

            # Mark the source node as
            # visited and enqueue it
            queue.append([0, [0 for i in range(len(joltage))]])
            visited[(0, (0 for i in range(len(joltage))))] = []

            while queue:

                # Dequeue a vertex from
                # queue and print it
                state = queue.pop(0)
                # print(state, end=" ")

                # Get all adjacent vertices of the
                # dequeued vertex s.
                # If an adjacent has not been visited,
                # then mark it visited and enqueue it
                for button in buttons:
                    new_state = state[0]
                    new_joltage = state[1]
                    for b in button:
                        new_state ^= 2**b
                        new_joltage[b] += 1

                    valid_joltage = 1
                    for j in range(len(new_joltage)):
                        if new_joltage[j] > joltage[j]:
                            valid_joltage = 0
                    
                    if valid_joltage and new_state not in visited:
                        queue.append([new_state, new_joltage])
                        visited[(new_state, (new_joltage))] = visited[(state)].copy()
                        visited[(new_state, new_joltage)][0].append(button)
                        visited[(new_state, new_joltage)][1] = new_joltage
                        if new_state == parttern:
                            print(visited[new_state])
                            queue = []
                            result += len(visited[new_state])
                            break

    return result



def main():
    print(" should be")
    # print(part1('day10/test.txt'))
    # print(part1('day10/data.txt'))

    # print(" should be")
    print(part2('day10/test.txt'))
    # print(part2('day02/data.txt'))

if __name__ == "__main__":
    main()