memo = {}
def dfs(graph, path, end):    
    if path[-1] == end:
        yield path
        print(path)
        return
    if path[-1] in graph:
            
        for p in graph[path[-1]]:
            if p not in path:
                new_path = path.copy()
                new_path.append(p)
                yield from dfs(graph, new_path, end)

                # result = result
    

def part1(name):
    with open(name) as file:
        result = 0
        graph = {}
        for line in file.readlines():
            graph[line.split(":")[0]] = line.strip().split(":")[1].split(" ")[1:]
        print(graph)
        result = len(list(dfs(graph, ["you"])))
    return result
    
def part2(name):
    with open(name) as file:
        result = 0
        graph = {}
        for line in file.readlines():
            graph[line.split(":")[0]] = line.strip().split(":")[1].split(" ")[1:]
        print(graph)
        result = list(dfs(graph, ["fft"], "dac"))
        print(result)
        # result = len([r for r in result if "dac" in r and "fft" in r])
    return result



def main():
    print(" should be")
    # print(part1('day11/test.txt'))
    # print(part1('day11/data.txt'))

    # print(" should be")
    print(part2('day11/test2.txt'))
    print(part2('day11/data.txt'))

if __name__ == "__main__":
    main()