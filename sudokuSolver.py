import sys 

class SudokuSolver:
    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
    
    def initializeFromFile(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            lineIndex = 0
            for line in lines:
                index = 0
                elab = line.strip()
                for char in elab: 
                    self.board[lineIndex][index] = int(char)
                    index += 1
                lineIndex += 1
        file.close()
    
    def printBoard(self):
        for line in self.board:
            for number in line:
                print(number, end = " ")
            print()
    
    def solve(self):
        numbers = [i for i in range(1,10)]
        
        def backtrack():
            pass

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print(f"{sys.argv[0]} must have <filename.txt> argument!")
        sys.exit(1)
    solver = SudokuSolver()
    solver.initializeFromFile(sys.argv[1])
    solver.printBoard()
