# Asking the user how far we are from the cave
print("How far are we from the cave?")
distance = int(input())

# Step loop that minuses by 1
for count in range (distance, 0, -1):
    print(str(count) + " steps remaining")

# End of loop
print("We have reached the cave!")