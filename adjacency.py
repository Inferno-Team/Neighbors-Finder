
import heapq


class Point:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.name = f"{x},{y}"

    def __repr__(self):
        return f" {{{self.x},{self.y},{self.value}}}"

    def __lt__(self, other):
        return self.value < other.value

    def __hash__(self):
        return hash(f"({self.x}, {self.y}, {self.value})")

    def __eq__(self, other):
        if other is None:
            return False
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)


class NeighborMatrix:

    def __init__(self, matrix=[]):
        self._matrix = matrix

    def get4neighbors(self, x, y):
        neighbors = []
        if x+1 < len(self._matrix):
            neighbors.append(self._matrix[x+1][y])
        if x-1 >= 0:
            neighbors.append(self._matrix[x-1][y])
        if y+1 < len(self._matrix[x]):
            neighbors.append(self._matrix[x][y+1])
        if y-1 >= 0:
            neighbors.append(self._matrix[x][y-1])

        return neighbors

    def get8neighbors(self, x, y):
        neighbors = []
        if x+1 < len(self._matrix):
            neighbors.append(self._matrix[x+1][y])
            if y > 0:
                neighbors.append(self._matrix[x+1][y-1])
            if y+1 < len(self._matrix[x+1]):
                neighbors.append(self._matrix[x+1][y+1])

        if x-1 >= 0:
            neighbors.append(self._matrix[x-1][y])
            if y > 0:
                neighbors.append(self._matrix[x-1][y-1])
            if y+1 < len(self._matrix[x-1]):
                neighbors.append(self._matrix[x-1][y+1])

        if y+1 < len(self._matrix[x]):
            neighbors.append(self._matrix[x][y+1])
        if y-1 >= 0:
            neighbors.append(self._matrix[x][y-1])

        return neighbors


class NeighborPoint:

    def __init__(self, points=[]):
        self._points = points

    def _find_point(self, x, y):
        for index, point in enumerate(self._points):
            if point.x == x and point.y == y:
                return point
        return None

    def get4neighbors(self, point: Point):
        neighbors = []
        max_x = max([point.x for point in self._points])
        max_y = max([point.y for point in self._points])

        if point.x+1 <= max_x:
            neighbors.append(self._find_point(point.x+1, point.y))
        if point.x-1 >= 0:
            neighbors.append(self._find_point(point.x-1, point.y))
        if point.y+1 <= max_y:
            neighbors.append(self._find_point(point.x, point.y+1))
        if point.y-1 >= 0:
            neighbors.append(self._find_point(point.x, point.y-1))

        return neighbors

    def get4neighbors_by_coordinates(self, x: int, y: int):
        point = self._find_point(x, y)
        return self.get4neighbors(point)

    def get8neighbors(self, point: Point):
        neighbors = []
        max_x = max([point.x for point in self._points])
        max_y = max([point.y for point in self._points])
        if point.x+1 <= max_x:
            neighbors.append(self._find_point(point.x+1, point.y))
            if point.y > 0:
                neighbors.append(self._find_point(point.x+1, point.y-1))
            if point.y+1 <= max_y:
                neighbors.append(self._find_point(point.x+1, point.y+1))

        if point.x-1 >= 0:
            neighbors.append(self._find_point(point.x-1, point.y))
            if point.y > 0:
                neighbors.append(self._find_point(point.x-1, point.y-1))
            if point.y+1 <= max_y:

                neighbors.append(self._find_point(point.x-1, point.y+1))
        if point.y+1 <= max_y:
            neighbors.append(self._find_point(point.x, point.y+1))
        if point.y-1 >= 0:
            neighbors.append(self._find_point(point.x, point.y-1))

        return neighbors

    def get8neighbors_by_coordinates(self, x: int, y: int):
        point = self._find_point(x, y)
        return self.get8neighbors(point)


class AdjacencyMatrix:
    def __init__(self, matrix=[], v=[1]):
        self._matrix = matrix
        self._neighbor = NeighborMatrix(matrix)
        self._v = v  # if v not defined we will assume that this is bitmap list

    def get4adjacency(self, x, y):
        neighbors4 = self._neighbor.get4neighbors(x, y)
        agecencies4 = [item for item in neighbors4 if item in self._v]
        return agecencies4


class AdjacencyPoint:

    def __init__(self, points=[], v=[1]):
        self._points = points
        self._neighbor = NeighborPoint(points)
        self._v = v  # if v not defined we will assume that this is bitmap list

    def get4adjacency_for_point(self, point: Point):
        return self.get4adjacency(point.x, point.y)

    def get4adjacency(self, x: int, y: int):
        neighbors4 = self._neighbor.get4neighbors_by_coordinates(x, y)
        return [point for point in neighbors4 if point.value in self._v]

    def get8adjacency(self, x: int, y: int):
        neighbors8 = self._neighbor.get8neighbors_by_coordinates(x, y)
        return [point for point in neighbors8 if point.value in self._v]

    def get_mixed_nieghbors(self, x: int, y: int):
        neighbors = self.get4adjacency(x, y)
        max_x = max([point.x for point in self._points])
        max_y = max([point.y for point in self._points])
        neighbors8 = self.get8adjacency(x, y)

        if x < max_x and y > 0:
            bottom_left_di_neighbors = self._neighbor.get4neighbors_by_coordinates(
                x+1, y-1)
            bottom_left_di = [point for point in bottom_left_di_neighbors
                              if point in neighbors
                              and point.value in self._v]
            if not bottom_left_di:

                point = self._neighbor._find_point(x+1, y-1)
                if point.value in self._v:
                    neighbors.append(point)

        if x < max_x and y < max_y:
            bottom_right_di_neighbors = self._neighbor.get4neighbors_by_coordinates(
                x+1, y+1)
            bottom_right_di = [point for point in bottom_right_di_neighbors
                               if point in neighbors
                               and point.value in self._v]
            if not bottom_right_di:

                point = self._neighbor._find_point(x+1, y+1)
                if point.value in self._v:
                    neighbors.append(point)
        if x > 0 and y > 0:
            top_left_di_neighbors = self._neighbor.get4neighbors_by_coordinates(
                x-1, y-1)
            top_left_di = [point for point in top_left_di_neighbors
                           if point in neighbors
                           and point.value in self._v]

            if not top_left_di:
                point = self._neighbor._find_point(x-1, y-1)
                if point.value in self._v:
                    neighbors.append(point)

        if x > 0 and y < max_y:
            top_right_di_neighbors = self._neighbor.get4neighbors_by_coordinates(
                x-1, y+1)
            top_right_di = [point for point in top_right_di_neighbors
                            if point in neighbors
                            and point.value in self._v]

            if not top_right_di:
                point = self._neighbor._find_point(x-1, y+1)
                if point.value in self._v:
                    neighbors.append(point)
        # print(neighbors8)
        neighbors8_not_mixed = [
            point for point in neighbors8 if point not in neighbors]
        return (neighbors, neighbors8_not_mixed)


class PathSeeker:
    def __init__(self, points=[], vector=[1]) -> None:
        self._points = points
        self._neighbor = NeighborPoint(points)
        self._adjacency = AdjacencyPoint(points=points, v=vector)

    def get_all_paths(self, start: Point, end: Point):
        print(f"from point : {start} , to point : {end}")
        paths = []
        distances = []

        def dfs(point, path, distances):
            if point == end:
                paths.append(path)
                return
            path.append(point)
            for neighbor in self.adjacency(point):
                if neighbor not in path:
                    dfs(neighbor, path + [neighbor], distances+1)
        dfs(start, [start], 0)
        return paths

    def _get_distance(self, p1: Point, p2: Point):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def dijkstra(self, start_point, end_point):
        distances = {point: float('inf') for point in self._points}
        distances[start_point] = 0
        heap = [(0, start_point)]
        visited = {}
        while heap:
            (current_distance, current_point) = heapq.heappop(heap)
            if current_point == end_point:
                path = []
                while current_point is not None:
                    path.append(current_point)
                    current_point = visited.get(current_point)
                return (path[::-1], distances[end_point])
            if current_distance > distances[current_point]:
                continue
            for neighbor in self._adjacency.get4adjacency_for_point(current_point):
                distance = self._get_distance(current_point, neighbor)
                tentative_distance = distances[current_point] + distance
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    # old = visited[neighbor]
                    # if visited.get(neighbor) is None:
                    #     visited[neighbor] = []
                    visited[neighbor] = current_point
                    heapq.heappush(heap, (tentative_distance, neighbor))
        return (None, -1)
