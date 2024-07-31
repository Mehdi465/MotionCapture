def create_file(n_max:int):
    with open("list_point.txt","w+") as list_file:
        for k in range(1,n_max+1):
            list_file.write(f"{k}\n")

        
if __name__ == "__main__":
    create_file(468)
