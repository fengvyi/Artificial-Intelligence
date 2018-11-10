package Generalized_Tic_tac_Toe;
import Generalized_Tic_tac_Toe.Algorithms;

import java.util.Scanner;

/**
 * For playing Tic Tac Toe in the console.
 */
public class Console {

    private Board board;
    private Scanner sc = new Scanner(System.in);

    /**
     * Construct Console.
     */
    private Console() {
        board = new Board();
    }

    /**
     * Begin the game.
     */
    private void play () {

        System.out.println("Starting a new game.");

        while (true) {
            printGameStatus();
            playMove();

            if (board.isGameOver()) {
                printWinner();

                if (!tryAgain()) {
                    break;
                }
            }
        }
    }

    /**
     * Handle the move to be played, either by the player or the AI.
     */
    private void playMove () {
    	int playMode = 0;
    	
    	int maxDepthX = 5;
    	int maxDepthO = 5;
    	
    	// PlayMode 0: AI VS AI
    	if(playMode == 0) {
    		if(board.getTurn() == Board.State.X) {
    			Algorithms.alphaBetaAdvanced(Board.State.X, board, maxDepthX);
    		}
    		else {
    			Algorithms.alphaBetaAdvanced(Board.State.O, board, maxDepthO);
    		}
    	}
    	// PlayMode 1: P VS AI
    	else if(playMode == 1) {
    		if (board.getTurn() == Board.State.X) {
    			getPlayerMove();
    		}
    		else {
    			Algorithms.alphaBetaAdvanced(Board.State.O, board, maxDepthO);
    		}
        }
    	// PlayMode 2: AI VS P
    	else if(playMode == 2) {
    		if (board.getTurn() == Board.State.X) {
    			Algorithms.alphaBetaAdvanced(Board.State.X, board, maxDepthX);
    		}
    		else {
    			getPlayerMove();
    		}
        }
    }

    /**
     * Print out the board and the player who's turn it is.
     */
    private void printGameStatus () {
        System.out.println("\n" + board + "\n");
        System.out.println(board.getTurn().name() + "'s turn.");
    }

    /**
     * For reading in and interpreting the move that the user types into the console.
     */
    private void getPlayerMove () {
        System.out.print("Index of move: ");

        int move_row = sc.nextInt();
        int move_col = sc.nextInt();
        int move = move_row * Board.BOARD_WIDTH + move_col;
        

        if (move < 0 || move >= Board.BOARD_WIDTH* Board.BOARD_WIDTH) {
            System.out.println("\nInvalid move.");
            System.out.println("\nThe index of the move must be between 0 and "
                    + (Board.BOARD_WIDTH * Board.BOARD_WIDTH - 1) + ", inclusive.");
        } else if (!board.move(move)) {
            System.out.println("\nInvalid move.");
            System.out.println("\nThe selected index must be blank.");
        }
        board.setPreMove(move);
    }

    /**
     * Print out the winner of the game.
     */
    private void printWinner () {
        Board.State winner = board.getWinner();

        System.out.println("\n" + board + "\n");

        if (winner == Board.State.Blank) {
            System.out.println("The TicTacToe is a Draw.");
        } else {
            System.out.println("Player " + winner.toString() + " wins!");
        }
    }

    /**
     * Reset the game if the player wants to play again.
     * @return      true if the player wants to play again
     */
    private boolean tryAgain () {
        if (promptTryAgain()) {
            board.reset();
            System.out.println("Started new game.");
            System.out.println("X's turn.");
            return true;
        }

        return false;
    }

    /**
     * Ask the player if they want to play again.
     * @return      true if the player wants to play again
     */
    private boolean promptTryAgain () {
        while (true) {
            System.out.print("Would you like to start a new game? (Y/N): ");
            String response = sc.next();
            if (response.equalsIgnoreCase("y")) {
                return true;
            } else if (response.equalsIgnoreCase("n")) {
                return false;
            }
            System.out.println("Invalid input.");
        }
    }

    public static void main(String[] args) {
        Console ticTacToe = new Console();
        ticTacToe.play();
    }

}
