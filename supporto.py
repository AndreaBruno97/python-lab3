file="task_list.txt"

comandi="""Insert the number corresponding to the action you want to perform:
1. insert a new task;
2. remove a task;
3. show all the tasks;
4. close the program.
Your choice: """

flag=True
lista=[]

f1=open(file, "r")
lista.extend(f1.read().splitlines())
lung=len(lista)

while flag:
    num=input(comandi)
    num=int(num)
    if num==1:
        new=input("Insert new task: ")
        lista.append(new)
        lung+=1
        print("")
    elif num==2:
        sub=input("Insert task to delete: ")
        i=0
        while i<lung:
            if lista[i].find(sub)>=0:
                del lista[i]
                i -= 1
                lung -= 1
            i+=1
        print("")
    elif num==3:
        print("Lista completa: ")
        for elem in sorted(lista):
            print(elem)
        print("")
    elif num==4:
        flag=False

f2=open(file, "w")
for task in lista:
    f2.write(task+"\n")