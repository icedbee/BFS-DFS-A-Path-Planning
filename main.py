from os import close
import sys

def findNeighbor(grid, popped):
    '''
        A function to find the nodes 1 space away
        for DFS and BFS algorithms
        neighbor is the list of nodes 1 space away
        popped is the node we're looking at
        grid is the maze layout
        south, north, west, and east are each node that's 1 space away
    '''
    neighbor = []
    if popped[1] - 1 in range(0, len(grid)):
        south = (popped[0]+ 0, popped[1] - 1)
        neighbor.append(south)

    if popped[1] + 1 in range(0, len(grid)):
        north = (popped[0] + 0, popped[1] + 1)
        neighbor.append(north)

    if popped[0] - 1 in range(0, len(grid[0])):
        west = (popped[0] - 1, popped[1] + 0)
        neighbor.append(west)
    
    if (popped[0] + 1) in range(0, len(grid[0])):
        east = (popped[0] + 1, popped[1] + 0)
        neighbor.append(east)

    return neighbor

class Node():
    '''
        A class for nodes in A* search
        parent is parent of the current node
        position is the current positional coordinates of node in the maze
        g is the cost from start to current node
        h is the hueristic estimated cost from current node to goal node
        f is the total cost of the node: f = g + h
    '''
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class PathPlanner():
    '''
        This class is for finding a path to the goal node
        Uses three different searching algorithms: DFS, BFS, A*
        start is the node to start with
        goal is the node to end on
        grid is the maze
    '''
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid

    '''
        DFS searching algorithm to find goal node while traversing though maze
        Uses same variable as in constructor for PathPlanner class
    '''
    def depth_first_search(self):
        if self.grid[self.start[1]][self.start[0]] == 1: #if starting node is 1
            print("You started on a 1")
            exit()
        elif self.grid[self.goal[1]][self.goal[0]] == 1: #if goal node is 1
            print("You're goal is unreachable due to ending on a 1")
            exit()
        
        if self.start == self.goal: #if starting node and goal node are the same 
            return [self.goal], 1

        visit = [] #initialize visited to see visited nodes

        stack = [] #initialize stack for neighbors

        stack.append(self.start)

        while(len(stack)): #go until stack empty
            popped = stack.pop() #take value off of stack
            
            if self.goal == popped: #if found goal node, return path and traversed nodes
                visit.append(popped)
                return visit, len(visit)

            if popped not in visit: #if not goal node,find neigbors
                visit.append(popped)
                neighbors = findNeighbor(self.grid, popped)
            
                for neighbor in neighbors:
                    if self.grid[neighbor[1]][neighbor[0]] == 1: #if neighbor is a 1, don't put in stack
                        continue

                    if neighbor not in visit: #if neighbor is 0, put in stack
                        stack.append(neighbor)

    '''
        BFS searching algorithm to find goal node while traversing though maze
        Uses same variable as in constructor for PathPlanner class
    '''
    def breadth_first_search(self):
        if self.grid[self.start[1]][self.start[0]] == 1: #if starting node is 1
            print("You started on a 1")
            exit()
        elif self.grid[self.goal[1]][self.goal[0]] == 1: #if goal node is 1
            print("You're goal is unreachable due to ending on a 1")
            exit()
        
        if self.start == self.goal: #if starting node and goal node are the same
            return [self.goal], 1

        visit = [] #initialize visited to see visited nodes

        queue = [] #initialize queue for neighbors

        queue.append(self.start)

        while(len(queue)): #go until queue empty
            popped = queue.pop(0) #take value off of queue
            
            if self.goal == popped: #if found goal node, return path and traversed nodes
                visit.append(popped)
                return visit, len(visit)

            if popped not in visit: #if not goal node,find neigbors
                visit.append(popped)
                neighbors = findNeighbor(self.grid, popped)
            
                for neighbor in neighbors:
                    if self.grid[neighbor[1]][neighbor[0]] == 1: #if neighbor is a 1, don't put in queue
                        continue

                    if neighbor not in visit: #if neighbor is 0, put in queue
                        queue.append(neighbor)

    '''
        A* searching algorithm to find goal node while traversing though maze
        Uses same variable as in constructor for PathPlanner class
    '''
    def a_star_search(self):
        if self.grid[self.start[1]][self.start[0]] == 1: #if starting node is 1
            print("You started on a 1")
            exit()
        elif self.grid[self.goal[1]][self.goal[0]] == 1: #if goal node is 1
            print("You're goal is unreachable due to ending on a 1")
            exit()

        if self.start == self.goal: #if starting node and goal node are the same
            return [self.goal], 1
        
        #initialize start and goal nodes
        start_node = Node(None, self.start)
        start_node.g = start_node.h = start_node.f = 0
        goal_node = Node(None, self.goal)
        goal_node.g = goal_node.h = goal_node.f = 0
        
        open_list = [] #open list for unvisited nodes
        closed_list = [] #closed list for visited nodes

        open_list.append(start_node)
        
        outer_iterations = 0
        max_iterations = (len(self.grid) // 2) ** 10 #if close to inifinite loop, will stop itself

        rows = len(self.grid)
        cols = len(self.grid[0])

        while len(open_list) > 0:

            outer_iterations += 1
            current_node = open_list[0] #getting current node
            current_index = 0 #getting current index

            for index, item in enumerate(open_list): #going through unvisited nodes and seeing which one has lowest cost
                if item.f < current_node.f:
                    current_node = item
                    current_index = index


            if outer_iterations > max_iterations: #if too many iterations, return what we have
                path = []
                current = current_node
                while current is not None: #getting the path took to get to goal node
                    path.append(current.position)
                    current = current.parent
                
                return path[::-1], len(path) #returning reversed path and it's length

            open_list.pop(current_index) #popping off node we just visited in the univisited list
            closed_list.append(current_node) #appending node we just visited in the visited list

            if current_node == goal_node: #if we reached the goal node go through current nodes parents
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position) #put in node position into our path
                    current = current.parent
                
                return path[::-1], len(path) #return reversed path and how many nodes traversed

            neighbors = [] #create list for children, i.e. neighbors
            dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            for dir in dirs: #positions node can travel to
                #neighbor we're on
                node_position = (current_node.position[0] + dir[0], current_node.position[1] + dir[1])

                if (node_position[1] > (rows - 1) or 
                    node_position[1] < 0 or 
                    node_position[0] > (cols -1) or 
                    node_position[0] < 0): #don't want to have neighbor be outside of maze
                    continue

                if self.grid[node_position[1]][node_position[0]] != 0: #if node is 1 don't want to go through
                    continue

                new_node = Node(current_node, node_position) #creating new node with our coordinates and the current node

                neighbors.append(new_node) #put new node in children list

            for neighbor in neighbors: #traverse through children list and calculate costs
                
                if len([visited_neighbor for visited_neighbor in closed_list if visited_neighbor == neighbor]) > 0:
                    continue    

                neighbor.g = current_node.g + 1 #calculate distance cost
                neighbor.h = (((neighbor.position[0] - goal_node.position[0]) ** 2) + #calculate hueristic cost 
                          ((neighbor.position[1] - goal_node.position[1]) ** 2))
                neighbor.f = neighbor.g + neighbor.h #overall cost

                if len([i for i in open_list if neighbor == i and neighbor.g > i.g]) > 0: #don't want cost greater than what we already have
                    continue

                open_list.append(neighbor) #put child in unvisited list

#initializing variables
n = len(sys.argv) #get total number of arguments; n = 9
arg_error = False
numbers = []

#has to be exactly 9 arguments
if(n > 9):
    sys.exit("Error: Too many command line arguments; there should be 9 arguments.")
elif(n < 9):
    sys.exit("Error: Not enough command line arguments; there should be 9 arguments.")
else:
    #get each argument
    file_name = sys.argv[0] #main.py
    input_string = sys.argv[1] #--input
    input_file = sys.argv[2] #grid1.dat
    start_string = sys.argv[3] #--start
    start_node = sys.argv[4] #0,0
    goal_string = sys.argv[5] #--goal
    goal_node = sys.argv[6] #7,6
    search_string = sys.argv[7] #--search
    search_type = sys.argv[8] #A*

    #start and goal node need to be in 0,0 format
    if ',' not in start_node:
        print("Error: fifth argument should be in this form: 0,0\n")
        arg_error = True
    elif ',' not in goal_node:
        print("Error: fifth argument should be in this form: 0,0\n")
        arg_error = True

    #split start and goal node to individual numbers
    start_node = start_node.split(',')
    goal_node = goal_node.split(',')

    #error checking if entered correct command line arguments
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

#exiting if there is an error in the command line arguments
if(arg_error == True):
    exit()

#building maze grid with 2d list
inner_numbers = []
file = open(input_file, "r") #opening file
while 1:
    char = file.read(1) #reading 1 byte at a time
    if(char == ''): #when we reach the end of the maze
        numbers.append(inner_numbers)
        break
    elif(char != '0' and char != '1' and char != ',' and char != '\n'): #maze has to be 1s, 0s, ","s, or \n
        sys.exit("Error: file was not valid and included something other than a 0, 1, or \",\"")
    elif(char == ','): #don't want to put comma in the maze grid
        continue
    else:
        if(char != '\n'): #not a new line so stay on current row
            inner_numbers.append(int(char))

    if(char == '\n'): #new line so put on a different row
        numbers.append(inner_numbers)
        inner_numbers = []

file.close()

#getting the start and goal nodes
x_start = start_node[0]
y_start = start_node[1]
x_goal = goal_node[0]
y_goal = goal_node[1]

#error checking to see if coordinates given are out of range of maze
if (len(numbers[0])-1) < int(x_start) or (len(numbers[0])-1) < int(x_goal):
    print("One of your x-coordinates is out of range")
    exit()
elif (len(numbers)-1) < int(y_start) or (len(numbers)-1) < int(y_goal):
    print("One of your y-coordinates is out of range")
    exit()

#putting start and goal nodes in tuples
start = (int(x_start),int(y_start))
goal = (int(x_goal), int(y_goal))

#printing out path for BFS, DFS, A*, or all of them together
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
    print("Path: {}".format(bfs_path))
    print("Traversed: {}".format(bfs_traversed))

    dfs_path, dfs_traversed = PathPlanner(start, goal, numbers).depth_first_search()
    print("Path: {}".format(dfs_path))
    print("Traversed: {}".format(dfs_traversed))

    a_star_path, a_star_traversed = PathPlanner(start, goal, numbers).a_star_search()
    print("Path: {}".format(a_star_path))
    print("Traversed: {}".format(a_star_traversed))