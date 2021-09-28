from os import close
import sys

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class PathPlanner():
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid

    def depth_first_search(self):
        if self.grid[self.start[1]][self.start[0]] == 1:
            print("You started on a 1")
            exit()
        elif self.grid[self.goal[1]][self.goal[0]] == 1:
            print("You're goal is unreachable due to ending on a 1")
            exit()
        
        if self.start == self.goal:
            print("You're start and goal points are the same")
            exit()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        x, y = self.start[0], self.start[1]
        path = [(self.start[1], self.start[0])]
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            while 0 <= nx + dx < len(self.grid) and 0 <= ny + dy < len(self.grid[0]) and self.grid[nx+dx][ny+dy] != 1:
                
                nx += dx
                ny += dy
            
            if self.grid[nx][ny] != 0:
                continue
            else:
                self.grid[nx][ny] = 2

            if self.depth_first_search():
                return path, len(path)
        
        return False
            

    def breadth_first_search(self):
        if self.grid[self.start[1]][self.start[0]] == 1:
            print("You started on a 1")
            exit()
        elif self.grid[self.goal[1]][self.goal[0]] == 1:
            print("You're goal is unreachable due to ending on a 1")
            exit()
        
        if self.start == self.goal:
            print("You're start and goal points are the same")
            exit()

        cols = len(self.grid[0])
        rows = len(self.grid)
        #dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dr = [-1, 1, 0, 0]
        dc = [0, 0, 1, -1]
        rq = []
        rc = []
        
        #path = [(self.start[1], self.start[0])]
        traversed = 0
        node_left_in_layer = 1
        node_in_next_layer= 0

        reached_end = False

        visited = [[False for i in range(cols)] for j in range(rows)]
        visited[self.start[1]][self.start[0]] = True
            #while 



        '''while path:
            x, y = path.pop(0)
            if x == self.grid[0] and y == self.grid[1]:
                return True
            for dx, dy in dirs:
                nx = x
                ny = y

                while 0 <= nx + dx < len(self.grid) and 0 <= ny + dy < len(self.grid[0]) and self.grid[nx+dx][ny+dy] != 1:
                    nx += dx
                    ny += dy

                if self.grid[nx][ny] != 0:
                    continue
                else:
                    self.grid[nx][ny] = 2
                    path.append((nx, ny))
        return False'''

    def a_star_search(self):
        if self.grid[self.start[1]][self.start[0]] == 1:
            print("You started on a 1")
            exit()
        elif self.grid[self.goal[1]][self.goal[0]] == 1:
            print("You're goal is unreachable due to ending on a 1")
            exit()
        
        start_node = Node(None, self.start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, self.goal)
        end_node.g = end_node.h = end_node.f = 0
        
        open_list = []
        closed_list = []

        open_list.append(start_node)

        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0

            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                
                return path[::-1], len(path)

            children = []

            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                if node_position[0] > (len(self.grid) - 1) or node_position[0] < 0 or node_position[1] > (len(self.grid[len(self.grid)-1]) -1) or node_position[1] < 0:
                    continue

                if self.grid[node_position[0]][node_position[1]] != 0:
                    continue

                new_node = Node(current_node, node_position)

                children.append(new_node)

            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                open_list.append(child)


#total arguments
n = len(sys.argv) #n = 9
arg_error = False
numbers = []

if(n > 9):
    sys.exit("Error: Too many command line arguments; there should be 9 arguments.")
elif(n < 9):
    sys.exit("Error: Not enough command line arguments; there should be 9 arguments.")
else:
    file_name = sys.argv[0] #main.py
    input_string = sys.argv[1] #--input
    input_file = sys.argv[2] #grid1.dat
    start_string = sys.argv[3] #--start
    start_node = sys.argv[4] #0,0
    goal_string = sys.argv[5] #--goal
    goal_node = sys.argv[6] #7,6
    search_string = sys.argv[7] #--search
    search_type = sys.argv[8] #A*

    if ',' not in start_node:
        print("Error: fifth argument should be in this form: 0,0\n")
        arg_error = True
    elif ',' not in goal_node:
        print("Error: fifth argument should be in this form: 0,0\n")
        arg_error = True

    start_node = start_node.split(',')
    goal_node = goal_node.split(',')

    if(input_string != "--input"):
        print("Error: second argument should be --input\n")
        arg_error = True
    if(start_string != "--start"):
        print("Error: fourth argument should be --start\n")
        arg_error = True
    if(not start_node[0].isnumeric() or not start_node[1].isnumeric()):
        print("Error: fifth argument should be in this form: 0,0\n")
        arg_error = True
    if(goal_string != "--goal"):
        print("Error: sixth argument should be --goal\n")
        arg_error = True
    if(not goal_node[0].isnumeric() or not goal_node[1].isnumeric()):
        print("Error: seventh argument should be in this form: 0,0\n")
        arg_error = True
    if(search_string != "--search"):
        print("Error: eighth argument should be --search\n")
        arg_error = True
    if(search_type != "BFS" and search_type != "DFS" and search_type != "A*" and search_type != "ALL"):
        print("Error: ninth argument should be either BFS, DFS, A*, or ALL\n")
        arg_error = True

if(arg_error == True):
    exit()

inner_numbers = []
file = open(input_file, "r")
while 1:
    char = file.read(1)
    if(char == ''):
        numbers.append(inner_numbers)
        break
    elif(char != '0' and char != '1' and char != ',' and char != '\n'):
        sys.exit("Error: file was not valid and included something other than a 0, 1, or \",\"")
    elif(char == ','):
        continue
    else:
        if(char != '\n'):
            inner_numbers.append(int(char))

    if(char == '\n'):
        numbers.append(inner_numbers)
        inner_numbers = []

file.close()

x_start = start_node[0]
y_start = start_node[1]
x_goal = goal_node[0]
y_goal = goal_node[1]
#print("x_start: {}".format(x_start))
#print("y_start: {}".format(y_start))
#print("x_goal: {}".format(x_goal))
#print("y_goal: {}".format(y_goal))
print(numbers)

if len(numbers[0]) <= int(x_start) or len(numbers[0]) <= int(x_goal):
    print("One of your x-coordinates is out of range")
    exit()
elif len(numbers) <= int(y_start) or len(numbers) <= int(y_goal):
    print("One of your y-coordinates is out of range")
    exit()

start = (int(x_start),int(y_start))
goal = (int(x_goal), int(y_goal))
#print(type(start))

if search_type == "BFS":
    bfs_path, bfs_traversed = PathPlanner(start, goal, numbers).breadth_first_search()
    print("Path: {}".format(bfs_path))
    print("Traversed: {}".format(bfs_traversed))
elif search_type == "DFS":
    dfs_path, dfs_traversed = PathPlanner(start, goal, numbers).depth_first_search()
    print("Path: {}".format(dfs_path))
    print("Traversed: {}".format(dfs_traversed))
elif search_type == "A*":
    a_star_path, a_star_traversed = PathPlanner(start, goal, numbers).a_star_search()
    print("Path: {}".format(a_star_path))
    print("Traversed: {}".format(a_star_traversed))
elif search_type == "ALL":
    bfs_path, bfs_traversed = PathPlanner(start, goal, numbers).breadth_first_search()
    dfs_path, dfs_traversed = PathPlanner(start, goal, numbers).depth_first_search()
    a_star_path, a_star_traversed = PathPlanner(start, goal, numbers).a_star_search()
    print("BFS Path: {}".format(bfs_path))
    print("Traversed: {}".format(bfs_traversed))
    print("DFS Path: {}".format(dfs_path))
    print("Traversed: {}".format(dfs_traversed))
    print("A* Path: {}".format(a_star_path))
    print("Traversed: {}".format(a_star_traversed))