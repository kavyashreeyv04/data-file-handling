print("***********************************")
print("* file handling *")
print("***********************************")
import os
while True:
    def f():
        print("1.create the file")
        print("2.read the file")
        print("3.list the file")
        print("4.edit the file")
        print("5.delete the file")
        print("6.stop the program")
    a=input("enter the choice")
    match a:
        case"1":
            print("creating a file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"w")
            file.write("welcome")
            print("--------------------------")
            print("file created successfully")
            print("--------------------------")
        case"2":
            print("reading a file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"r")
            print("-------------------------")
            print(file.read())
            print("-------------------------")
            f()
        case"3":
            print("listing a file")
            print("-------------------------")
            path="D:\KAVYASHREE"
            file=os.listdir(path)
            for file in file:
                print(file)
            print("-------------------------")
            f()
        case"4":
            print("editing a file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"a")
            print(file.write("kavu"))
            print("-------------------------")
            print("edited the file")
            print("-------------------------")
        case"5":
            print("deleting a file")
            name=input("enter the file name:")
            name=name+".txt"
            os.remove(name)
            print("file",name,"deleted successfully")
            print("-------------------------")
        case"6":
                print("stop the program")
    print("end")
                
            
