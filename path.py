from adjacency import Point, PathSeeker


def read_from_file(file_name='matrix.txt'):
    f = open(file_name, "r")
    return f.read()


def convert_lines2points(lines="", separator=" ", line_separator="\n"):
    lines_numbers = lines.split(line_separator)
    numbers = []
    for (x, line) in enumerate(lines_numbers):
        _numbers = line.split(separator)
        for (y, number) in enumerate(_numbers):
            point = Point(x, y, int(number))
            numbers.append(point)
    return numbers


lines = read_from_file()
points = convert_lines2points(lines)
path_seeker = PathSeeker(points, vector=[ 2, 3, 5])
path,dist= path_seeker.dijkstra(points[0], points[-1])
print(f'paths : {path} , dist : {dist}')
