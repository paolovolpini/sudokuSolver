import sys 

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print(f"{sys.argv[0]} must have <filename.txt> argument!")
        sys.exit(1)

