#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SOLUTIONS 100 // Maximum number of solutions to store

typedef struct {
    char boards[MAX_SOLUTIONS][10][10]; // Store up to MAX_SOLUTIONS boards
    int count; // Number of valid solutions found
} SolutionStorage;

void solve(int col, char board[][10], SolutionStorage *solutions, int *leftrow, int *upperDiagonal, int *lowerDiagonal, int n) {
    if (col == n) {
        // Copy the board into the solutions storage
        for (int i = 0; i < n; i++) {
            strcpy(solutions->boards[solutions->count][i], board[i]);
        }
        solutions->count++;
        return;
    }

    for (int row = 0; row < n; row++) {
        if (leftrow[row] == 0 && lowerDiagonal[row + col] == 0 && upperDiagonal[n - 1 + col - row] == 0) {
            board[row][col] = 'Q';
            leftrow[row] = 1;
            lowerDiagonal[row + col] = 1;
            upperDiagonal[n - 1 + col - row] = 1;

            solve(col + 1, board, solutions, leftrow, upperDiagonal, lowerDiagonal, n);

            board[row][col] = '.';
            leftrow[row] = 0;
            lowerDiagonal[row + col] = 0;
            upperDiagonal[n - 1 + col - row] = 0;
        }
    }
}

SolutionStorage solveNQueens(int n) {
    SolutionStorage solutions;
    solutions.count = 0;

    char board[10][10]; // Maximum board size assumed to be 10x10
    for (int i = 0; i < n; i++) {
        memset(board[i], '.', n);
        board[i][n] = '\0'; // Null terminate for string compatibility
    }

    int leftrow[10] = {0};
    int upperDiagonal[20] = {0};
    int lowerDiagonal[20] = {0};

    solve(0, board, &solutions, leftrow, upperDiagonal, lowerDiagonal, n);
    
    return solutions;
}

int main() {
    int n = 4; // Board size and number of queens
    SolutionStorage solutions = solveNQueens(n);

    for (int i = 0; i < solutions.count; i++) {
        printf("Arrangement %d\n", i + 1);
        for (int j = 0; j < n; j++) {
            printf("%s\n", solutions.boards[i][j]);
        }
        printf("\n");
    }

    return 0;
}
