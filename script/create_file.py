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

def get_test_points(steps:int)->list:
    list_res = []
    lines = []
    with open("list_point.txt","r") as list_file:
        lines = list_file.readlines()
    index = 0
    for line in lines:
        if index>steps:
            break
        list_res.append(int(line.strip()))
        index +=1

    # rewrite the left points not yet processed
    with open("list_point.txt","+w") as list_file:
        list_file.writelines(lines[steps:])

    return list_res

def remove_int_by_str():
    l = []
    with open("input.txt","r+") as opt_file:
        lines = opt_file.readlines()
        for line in lines:
            line.strip()
            line_split = line.split("=")
            l.append((line_split[0].strip(),f"\"{line_split[0].strip()}\""))

    with open("input_final.txt","w+") as opt_file:
        for line in l:
            opt_file.write(f"{line[0]} = {line[1]} \n")

if __name__ == "__main__":
    remove_int_by_str()



