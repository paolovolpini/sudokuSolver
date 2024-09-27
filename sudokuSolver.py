import sys 

class SudokuSolver:
    def __init__(self):
        self.board = [[0] * 9] * 9
        print(self.board)
    
    def initializeFromFile(self, filename):
        pass

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print(f"{sys.argv[0]} must have <filename.txt> argument!")
        sys.exit(1)
    solver = SudokuSolver()
    solver.initializeFromFile(sys.argv[0])

