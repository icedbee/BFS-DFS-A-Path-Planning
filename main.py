import sys

class PathPlanner:
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid

    def depth_first_search(self):
        print(self.start)
    def breadth_first_search(self):
        print(self.goal)
    def a_star_search(self):
        print(self.start)

 
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

    if(input_string != "--input"):
        print("Error: second argument should be --input\n")
        arg_error = True
    if(start_string != "--start"):
        print("Error: fourth argument should be --start\n")
        arg_error = True
    if(goal_string != "--goal"):
        print("Error: sixth argument should be --goal\n")
        arg_error = True
    if(search_string != "--search"):
        print("Error: eighth argument should be --search\n")
        arg_error = True

if(arg_error == True):
    exit()

file = open(input_file, "r")
while 1:
    char = file.read(1)
    if(char == ''):
        break
    elif(char != '0' and char != '1' and char != ',' and char != '\n'):
        sys.exit("Error: file was not valid and included something other than a 0, 1, or \",\"")
    elif(char == '\n'):
        continue
    else:
        numbers.append(char)

print(numbers)

file.close()