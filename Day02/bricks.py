

def make_bricks(small, big, goal):
    if goal % 5 > small:
        print (False) 
    else:    
        c = big*5 + small
        if c >= goal:
            print (True)
        else:
            print (False)

lst = input("Enter Numbers: ").split(",")

my_list=[]

for i in lst:
    my_list.append(int(i))
    
make_bricks(my_list[0], my_list[1], my_list[2])