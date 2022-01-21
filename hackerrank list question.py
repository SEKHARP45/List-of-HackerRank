# HackerRank list question
n=int(input())
list=[] #Creating empty list
for i in range(1,n+1):
    splited_list=input().split() #spliting the full operation of input  and enter that part in list named splited_list
    if len(splited_list)==3: # checking the length of splited_list
        task=splited_list[0] # asigning the first item of splited_list as task
        index=int(splited_list[1])
        value=int(splited_list[2])
        if task=="insert":
            list.insert(index,value)  # Inserts x in to the list in the position specified by i
    elif len(splited_list)==2:
        task=splited_list[0]
        value=int(splited_list[1])
        if task=="remove":
            list.remove(value)  #Removes value from the list
        elif task=="append": 
            list.append(value) # Appends value at the end of the list
    else:
        task=splited_list[0]
        if task=="sort":
            list.sort()   # Sorts the elements of list into ascending order 
        elif task=="pop": 
            if len(list)>0: # Checking if there is any element in the list
                list.pop()  # Removes the ending element from the list
        elif task=="reverse":
            list.reverse()  # Reverse the sequence of elements in the list
        else:
            print(list)  #Print the list