def calc_dist(a, b):
    return abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2 + abs(a[2]-b[2])**2

def part1(name, is_test):
    with open(name) as file:
        result = 0
        points = []
        for line in file.readlines():
            x,y,z = line.strip().split(',')
            points.append((int(x), int(y), int(z)))
        connections = {}
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                connections[(i,j)] = calc_dist(points[i], points[j])
        
        connections = sorted(connections.items(), key=lambda item: item[1])
        
    # список рёбер (третьи числа игнорируем)
    edges = [c[0] for c in connections]

    N = 10  # сколько первых рёбер рассматривать
    # -------- DSU (Union-Find) --------
    class DSU:
        def __init__(self):
            self.parent = {}

        def find(self, x):
            if x not in self.parent:
                self.parent[x] = x
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, a, b):
            ra = self.find(a)
            rb = self.find(b)
            if ra == rb:
                return False  # ребро НЕ расширяет сеть
            self.parent[rb] = ra
            return True       # ребро расширило сеть


    # -------- логика --------
    dsu = DSU()
    useful_edges = []  # рёбра, которые расширяют сеть

    for a, b in edges[:1000]:
        dsu.union(a, b)


    # формирование компонент
    components = {}
    for node in dsu.parent:
        root = dsu.find(node)
        components.setdefault(root, []).append(node)

    print("\nКомпоненты:")
    print(components)
    for comp in components.values():
        print(sorted(comp), "кол-во:", len(comp))
    components = sorted(components.items(), key= lambda item:len(item[1]), reverse= True)
    print(components)
    result = len(components[0][1])* len(components[1][1])* len(components[2][1])
    return result


def part2(name):

    with open(name) as file:
        result = 0
        points = []
        for line in file.readlines():
            x,y,z = line.strip().split(',')
            points.append((int(x), int(y), int(z)))
        connections = {}
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                connections[(i,j)] = calc_dist(points[i], points[j])
        
        connections = sorted(connections.items(), key=lambda item: item[1])


    # список рёбер (третьи числа игнорируем)
    edges = [c[0] for c in connections]

    N = 10  # сколько первых рёбер рассматривать


    # -------- DSU (Union-Find) --------
    class DSU:
        def __init__(self):
            self.parent = {}

        def find(self, x):
            if x not in self.parent:
                self.parent[x] = x
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, a, b):
            ra = self.find(a)
            rb = self.find(b)
            if ra == rb:
                return False  # ребро НЕ расширяет сеть
            self.parent[rb] = ra
            return True       # ребро расширило сеть


    # -------- логика --------
    dsu = DSU()

    for a, b in edges:
        dsu.union(a, b)


        # формирование компонент
        components = {}
        for node in dsu.parent:
            root = dsu.find(node)
            components.setdefault(root, []).append(node)
        # print(components)
        components = list(components.values())[0]
        # print(components)
        if (len(components) == len(points)):
            print(f'{points[a][0]}, {points[b][0]}, {points[a][0]*points[b][0]}')
            break

    # print(components)
    # for comp in components.values():
    #     print(sorted(comp), "кол-во:", len(comp))
    # components = sorted(components.items(), key= lambda item:len(item[1]), reverse= True)
    # print(components)
    # result = len(components[0][1])* len(components[1][1])* len(components[2][1])
    return result





def main():
    print(" should be")
    # print(part1('day08/test.txt', True))
    # print(part1('day08/data.txt', False))

    # print(" should be")
    print(part2('day08/test.txt'))
    print(part2('day08/data.txt'))

if __name__ == "__main__":
    main()