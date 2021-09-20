import sys
 
#total arguments
n = len(sys.argv) #n = 9

if(n > 9):
    print("Error: Too many command line arguments")
elif(n < 9):
    print("Error: Not enough command line arguments")
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

print(start_node[0])

if(input_string != "--input"):
    print("Error: second argument should be --input\n")
if(start_string != "--start"):
    print("Error: fourth argument should be --start\n")
if(goal_string != "--goal"):
    print("Error: sixth argument should be --goal\n")
if(search_string != "--search"):
    print("Error: eighth argument should be --search\n")

'''
#print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)'''