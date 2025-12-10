import sympy as sp
import itertools
import time 

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

def find_all_natural_solutions(solution, all_vars, max_val):
    """
    Найти ВСЕ натуральные решения из символьного решения.
    solution: dict вида {x0: -x3 + x5 + 2, x1: 5 - x5, ...}
    """
    
    all_vars = set(all_vars)
    
    # Найти свободные переменные (которые НЕ в решении)
    free_vars = list(all_vars - set(solution.keys()))
    free_vars.sort(key=lambda x: int(str(x)[1:]))
    print(f'Подбираю {len(free_vars)} {max_val}')
    all_solutions = []
    min_value = None
    # Перебираем только свободные переменные (не все!)
    for values in itertools.product(range(0, max_val + 1), repeat=len(free_vars)):

        if min_value and sum(values) > min_value:
            continue
        subst = dict(zip(free_vars, values))
        
        full_sol = {}
        ok = True
        
        for var in all_vars:
            if var in solution:
                val = solution[var].subs(subst)
            else:
                val = subst[var]
            
            try:
                val_int = int(val)
                # Проверяем, что это натуральное число (>= 0)
                if val_int != val or val_int < 0:
                    ok = False
                    break
                full_sol[var] = val_int
            except (TypeError, ValueError):
                ok = False
                break
        
        if ok:
            s = sum(full_sol.values())
            all_solutions.append((full_sol, s))
            if min_value is None or min_value > s:
                min_value = s
                print(f'{min_value} {values}', end="\r", flush=True)
    # Сортируем по сумме
    all_solutions.sort(key=lambda x: x[1])
    
    return all_solutions


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

            args = [f'x{i}' for i in range(len(buttons))]
            args = sp.symbols(args, integer=True)
            eqs = []
            for i, j in enumerate(joltage):
                expr = 0
                for k, button in enumerate(buttons):
                    if i in button:
                        expr += args[k]
                eqs.append(sp.Eq(expr, j))
            
            for i, eq in enumerate(eqs):
                print(f'{i} {eq}')
            
            # Решаем систему и берём первое решение как dict
            sol = sp.solve(eqs, args, dict=True)
            
            if not sol:
                print("Решение не найдено!")
                continue
            
            sol = sol[0]  # берём первый dict из списка
            print(f"Символьное решение: {sol}\n")
            
            # Найти все натуральные решения
            max_val = max(joltage)
            all_sols = find_all_natural_solutions(sol, args, max_val)
            
            print(f"Найдено натуральных решений: {len(all_sols)}")
            for i, (sol_dict, sol_sum) in enumerate(all_sols[:5], 1):
                print(f"  {i}. {sorted(sol_dict.items(), key=lambda x: str(x[0]))} -> сумма: {sol_sum}")
            
            if all_sols:
                result += all_sols[0][1]  # берём минимальную сумму
    
    return result



def main():
    start_time = time.time()
    print(" should be")
    # print(part1('day10/test.txt'))
    # print(part1('day10/data.txt'))

    # print(" should be")
    print(part2('day10/test.txt'))
    print(part2('day10/data.txt'))
    print(f'task done in {time.time() - start_time}')

if __name__ == "__main__":
    main()