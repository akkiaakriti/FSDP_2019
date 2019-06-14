#enter input----------------

user_input = input("Enter comma seperated Numbers: ").split(",")

user_list = []

for i in user_input:
    user_list.append(int(i))

user_list.sort()
final_list = user_list[1:-1]

#  average
average = sum( final_list ) / len( final_list )

print ("Average is :", int( average ))
