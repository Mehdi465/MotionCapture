## Create a file with int from 1 to n_max, it was the select the ritgh dots for the right part.

def create_file(n_max:int):
    with open("list_point.txt","w+") as list_file:
        for k in range(1,n_max+1):
            list_file.write(f"{k}\n")

def replace_R_by_L():
    with open("file_inter.txt", 'r+') as file_:
        lines = file_.readlines()
        list_element = []
        print(lines)
        
        for line in lines:
            if "R" in line:
                list_element.append(line.replace('R','L'))

    with open("file_inter.txt", 'w+') as file_:
        for element in list_element:
            file_.write(element)  
    
    print("Modification done")

if __name__ == "__main__":
    replace_R_by_L()

