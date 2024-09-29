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
        def isValid(row, col, num):
            for i in range(9):
                # check if number is in same row or column or square
                if(self.board[row][i] == num or self.board[i][col] == num or \
                        self.board[row - row % 3 + i // 3][col - col % 3 + i % 3] == num):
                    return False
            return True

        numbers = [i for i in range(1,10)]
        def backtrack():
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == 0:
                        for num in numbers:
                            if isValid(i,j,num):
                                self.board[i][j] = num
                                if(backtrack()):
                                    return True
                                self.board[i][j] = 0
                        return False
            return True
        
        backtrack()

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print(f"{sys.argv[0]} must have <filename.txt> argument!")
        sys.exit(1)
    solver = SudokuSolver()
    solver.initializeFromFile(sys.argv[1])
    solver.solve()
    solver.printBoard()
    
