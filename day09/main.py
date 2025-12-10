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

def draw(min_x, min_y, max_x, max_y, points, area = []):
    with open('output.txt', 'w+') as f:
        print("012345678901")
        for y in range(min_y+1, max_y+1):
            line = str(y)
            for x in range(min_x+1, max_x+1):
                # if (x,y) == points[0]:
                #     line += '0'
                
                if (x,y) in area:
                    line += 'X'
                elif (x,y) in points:
                    line += '#'
                else:
                    line += '.'
           # f.write(f'{line}\n')
            print(line)
        print('='*20)

class Rect:
    def __init__(self, p1, p2):
        self.top = min(p1[1], p2[1])
        self.bot = max(p1[1], p2[1])
        self.left = min(p1[0], p2[0])
        self.right = max(p1[0], p2[0])
    
    def to_left(self, p):
        return p[0] <= self.left
    def to_right(self, p):
        return p[0] >= self.right    
    def to_top (self, p):
        return p[1] <= self.top
    def to_bot(self, p):
        return p[1] >= self.bot

    def check_lines(self, lines):
        for line in lines:
            if self.check_line(line):
                return False
        return True
    
    def check_line(self, line):
        if line[0][1] == line[1][1]: #vertical
            if self.to_top(line[0]) or self.to_bot(line[0]):
                return False
            if self.to_left(line[0]) and self.to_left(line[1]):
                return False
            if self.to_right(line[0]) and self.to_right(line[1]):
                return False 
            return True
        else:
            if self.to_left(line[0]) or self.to_right(line[0]):
                return False
            if self.to_top(line[0]) and self.to_top(line[1]):
                return False
            if self.to_bot(line[0]) and self.to_bot(line[1]):
                return False 
            return True

def part2(name, is_test):
    with open(name) as file:
        result = [0]
        points = []
        min_x, min_y, max_x, max_y = 0,0,0,0
        for line in file.readlines():
            x,y = line.split(',')

            points.append((int(x), int(y)))
            min_x = min(min_x, int(x))
            min_y = min(min_y, int(y))
            max_x = max(max_x, int(x))
            max_y = max(max_y, int(y))

        lines = []
        # draw(min_x, min_y, max_x, max_y, points, area)
        for i in range(len(points)):
            lines.append((points[i], points[(i+1)%len(points)]))
        if (is_test):
            draw(min_x, min_y, max_x, max_y, points)
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                rect = Rect(points[i], points[j])
                current_area = (abs(points[i][0]-points[j][0])+1)*(abs(points[i][1]-points[j][1])+1)
                if current_area > result[0]:
                    # print(current_area)
                    check =  rect.check_lines(lines)
                    # print (check)
                    # draw(min_x, min_y, max_x, max_y, points, [points[i], points[j]])

                    if check:
                        result = (current_area, p1, p2)         
    return result

#1410470448 too low

def main():
    print(" should be")
    # print(part1('day09/test.txt'))
    # print(part1('day09/data.txt'))

    # print(" should be")
    print(part2('day09/test.txt', True))
    print(part2('day09/data.txt', False))

if __name__ == "__main__":
    main()