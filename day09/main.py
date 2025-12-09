def part1(name):
    with open(name) as file:
        result = 0
        points = []
        for line in file.readlines():
            x,y = line.split(',')
            points.append((int(x), int(y)))
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                area = abs(points[i][0]-points[j][0]+1)*abs(points[i][1]-points[j][1]+1)
                if area>result:
                    result = area        
    return result

def draw(min_x, min_y, max_x, max_y, points, area):
    with open('output.txt', 'w+') as f:

        for y in range(min_y-1, max_y+2):
            line = ""
            for x in range(min_x-1, max_x+2):
                if (x,y) == points[0]:
                    line += '0'
                
                elif (x,y) in points:
                    line += '#'
                elif (x,y) in area:
                    line += 'X'
                else:
                    line += '.'
            # f.write(f'{line}\n')
            print(line)
        print('='*20)

dirs = ((-1,0), (0, -1), (1,0), (0,1))           
def part2(name, is_test):
    with open(name) as file:
        result = 0
        points = []
        graph = {}
        area = []
        min_x, min_y, max_x, max_y = 0,0,0,0
        for line in file.readlines():
            x,y = line.split(',')

            points.append((int(x), int(y)))
            min_x = min(min_x, int(x))
            min_y = min(min_y, int(y))
            max_x = max(max_x, int(x))
            max_y = max(max_y, int(y))


        # draw(min_x, min_y, max_x, max_y, points, area)
        for i in range(len(points)):
            j = (i+1)%len(points)
            if points[i][0] == points[j][0]:
                for k in range(min(points[i][1], points[j][1]), max(points[i][1],points[j][1])+1):
                    area.append((points[i][0], k))
            elif points[i][1] == points[j][1]:
                for k in range(min(points[i][0], points[j][0]), max(points[i][0],points[j][0])+1):
                    area.append((k, points[i][1]))

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                if (points[i][0], points[j][1]) in area and (points[j][0], points[i][1]) in area:

                    current_area = abs(points[i][0]-points[j][0]+1)*abs(points[i][1]-points[j][1]+1)
                    if current_area > result:
                        result = current_area        


                # draw(min_x, min_y, max_x, max_y, points, area)
                    
            # print(graph[i])
        # queue = [(points[0][0]+1, points[0][1]+1)]
        # while queue:
        #     q = queue.pop(0)
        #     for d in dirs:
        #         if (q[0]+d[0], q[1]+d[1]) not in area:
        #             queue.append((q[0]+d[0], q[1]+d[1]))
        #             area.append((q[0]+d[0], q[1]+d[1]))
        #             print(len(area))
        if is_test:
            draw(min_x, min_y, max_x, max_y, points, area)
    return result



def main():
    print(" should be")
    # print(part1('day09/test.txt'))
    # print(part1('day09/data.txt'))

    # print(" should be")
    print(part2('day09/test.txt', True))
    print(part2('day09/data.txt', False))

if __name__ == "__main__":
    main()