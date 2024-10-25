def simulate_robot(commands):

    x, y = 0, 0
    direction = 'north'

    directions = ['north', 'east', 'south', 'west']
    movements = {
        'north': (0, 1),
        'east': (1, 0),
        'south': (0, -1),
        'west': (-1, 0)
    }

    visited = set()
    visited.add((x, y))

    path = [(x, y)]

    for command in commands:
        if command == 'F':

            dx, dy = movements[direction]
            x, y = x + dx, y + dy

            if (x, y) in visited:
                print(f"Path crosses itself at: ({x}, {y})")
            visited.add((x, y))
            path.append((x, y))
        elif command == 'L':

            current_index = directions.index(direction)
            direction = directions[(current_index - 1) % 4]
        elif command == 'R':

            current_index = directions.index(direction)
            direction = directions[(current_index + 1) % 4]
        elif command == 'S':

            break
        else:

            print(f"Unknown command: {command}")


    draw_path(path)


def draw_path(path):

    min_x = min(x for x, y in path)
    max_x = max(x for x, y in path)
    min_y = min(y for x, y in path)
    max_y = max(y for x, y in path)


    shift_x = -min_x

    width = max_x - min_x + 1
    height = max_y - min_y + 1


    grid = [[' ' for _ in range(width)] for _ in range(height)]


    for x, y in path:
        grid[max_y - y][x + shift_x] = '*'


    for row in grid:
        print(''.join(row))



commands = "FFFFFLFFFLFFFFRRRFXFFFFFFS"
simulate_robot(commands)
