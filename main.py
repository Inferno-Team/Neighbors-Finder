
from adjacency import Point,AdjacencyPoint,NeighborPoint

def read_from_file(file_name='matrix.txt'):
    f = open(file_name, "r")
    return f.read()

def convert_lines2matrix(lines="",separator=" ",line_separator="\n"):
    lines_numbers = lines.split(line_separator)
    numbers = []
    for (index,line) in enumerate(lines_numbers):
        _numbers = line.split(separator)
        ns = []
        for(index,number) in enumerate(_numbers):
            ns.append(int(number))
           
        numbers.append(ns)
    return numbers

def convert_lines2points(lines="",separator=" ",line_separator="\n"):
    lines_numbers = lines.split(line_separator)
    numbers = []
    for (x,line) in enumerate(lines_numbers):
        _numbers = line.split(separator)
        for(y,number) in enumerate(_numbers):
            point = Point(x,y,int(number))
            numbers.append(point)
    return numbers




if __name__ =='__main__':
    print("Hello, Please enter matrix file name (defualt name is matrix.txt)\n if you want to be default enter -1")
    name = input()
    if name == '-1':
        name = 'matrix.txt'
    lines = read_from_file(name)
    points = convert_lines2points(lines)
    neighbor_point = NeighborPoint(points)
    
    print("1. Neighbors\n")
    print("2. Adjacencies\n")
    print('3. exit\n')
    choice = int(input())
    if choice >=3 or choice<0:
        exit()
    if choice == 1:
        print("Neighbors : ")
        print("1. 4 neighbors by coordinates (x,y)\n")
        print("2. 8 neighbors by coordinates (x,y)\n")
        second_choice = int(input())
        print("please enter the number x :")
        x= int(input())
        print("please enter the number y :")
        y= int(input())
        if second_choice == 1:
            neighbors = neighbor_point.get4neighbors_by_coordinates(x, y)
        if second_choice == 2:
            neighbors = neighbor_point.get8neighbors_by_coordinates(x, y)
        print(neighbors)
    if choice == 2:
        print("Adjacencies : ")
        print("1. 4 Adjacencies by coordinates (x,y)\n")
        print("2. mixed Adjacencies by coordinates (x,y)\n")
        print("3. 8 Adjacencies by coordinates (x,y)\n")
        second_choice = int(input())
        print("please enter the number x :")
        x= int(input())
        print("please enter the number y :")
        y= int(input())
        print("please enter the v (enter -1 if it's bitmap 1):")
        c = input()
        v=[]
        if c == "-1":
            v=[1]
        else:
            v= [int(x) for x in c.split()]
        adjacency = AdjacencyPoint(points,v)
        if second_choice == 1:
            adjacencies = adjacency.get4adjacency(x, y)
        elif second_choice == 2:
            adjacencies = adjacency.get_mixed_nieghbors(x, y)
        else :
            adjacencies = adjacency.get8adjacency(x, y)
        print(adjacencies)
        
        
        
            