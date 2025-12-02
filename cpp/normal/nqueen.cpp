#include <bits/stdc++.h>
using namespace std;

int board[8][8];
int n;

bool isSafe(int row, int col) {
    // Check column
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 1)
            return false;
    }
    
    // Check upper left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1)
            return false;
    }
    
    // Check upper right diagonal
    for (int i = row, j = col; i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 1)
            return false;
    }
    
    return true;
}

bool solveNQueens(int row) {
    if (row == n) {
        return true;
    }
    
    for (int col = 0; col < n; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;
            if (solveNQueens(row + 1))
                return true;
            board[row][col] = 0;
        }
    }
    
    return false;
}

void printBoard() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    n = 4;
    memset(board, 0, sizeof(board));
    
    if (solveNQueens(0)) {
        cout << "Solution found:\n";
        printBoard();
    } else {
        cout << "No solution exists\n";
    }
    
    return 0;
}