#include <stdio.h>
#include <stdlib.h>

#define N 8 // Define board size (change for different sizes)

// Possible moves of the knight
int dx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};

// Function to print the chessboard with the knight's path
void printSolution(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%2d ", board[i][j]); // Print with spacing
        printf("\n");
    }
    printf("\n");
}

// Utility function to check if the next move is valid
int isValid(int x, int y, int board[N][N]) {
    return (x >= 0 && x < N && y >= 0 && y < N && board[x][y] == -1);
}

// Recursive function to solve Knight's Tour
int solveKnightTour(int x, int y, int moveCount, int board[N][N]) {
    if (moveCount == N * N) // All squares visited
        return 1;

    // Try all 8 possible moves
    for (int i = 0; i < 8; i++) {
        int newX = x + dx[i];
        int newY = y + dy[i];

        if (isValid(newX, newY, board)) {
            board[newX][newY] = moveCount;
            if (solveKnightTour(newX, newY, moveCount + 1, board))
                return 1; // If a solution is found, return success
            board[newX][newY] = -1; // Backtrack
        }
    }
    return 0;
}

// Main function to initialize and solve the Knight's Tour
void knightTour() {
    int board[N][N];

    // Initialize board with -1 (unvisited)
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            board[i][j] = -1;

    // Starting position (0,0)
    board[0][0] = 0;

    // Start the tour
    if (solveKnightTour(0, 0, 1, board))
        printSolution(board);
    else
        printf("No solution found\n");
}

int main() {
    knightTour();
    return 0;
}
