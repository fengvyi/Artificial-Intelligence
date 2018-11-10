package Generalized_Tic_tac_Toe;

import Generalized_Tic_tac_Toe.Board;

/**
 * Uses various algorithms to play Tic Tac Toe.
 */
public class Algorithms {

    /**
     * Algorithms cannot be instantiated.
     */
    private Algorithms() {}

    /**
     * Play a random move.
     * @param board     the Tic Tac Toe board to play on
     */
    public static void random (Board board) {
        Random.run(board);
    }

    /**
     * Play using the MiniMax Algorithm.
     * @param board     the Tic Tac Toe board to play on
     */
    public static void miniMax (Board board) {
        MiniMax.run(board.getTurn(), board, Double.POSITIVE_INFINITY);
    }

    /**
     * Play using the MiniMax algorithm. Include a depth limit.
     * @param board     the Tic Tac Toe board to play on
     * @param ply       the maximum depth
     */
    public static void miniMax (Board board, int ply) {
        MiniMax.run(board.getTurn(), board, ply);
    }

    /**
     * Play using the Alpha-Beta Pruning algorithm.
     * @param board     the Tic Tac Toe board to play on
     */
    public static void alphaBetaPruning (Board board) {
        AlphaBetaPruning.run(board.getTurn(), board, Double.POSITIVE_INFINITY);
    }

    /**
     * Play using the Alpha-Beta Pruning algorithm. Include a depth limit.
     * @param board     the Tic Tac Toe board to play on
     * @param ply       the maximum depth
     */
    public static void alphaBetaPruning (Board board, int ply) {
        AlphaBetaPruning.run(board.getTurn(), board, ply);
    }

    /**
     * Play using the Alpha-Beta Pruning algorithm. Include depth in the
     * evaluation function.
     * @param board     the Tic Tac Toe board to play on
     */
    public static void alphaBetaAdvanced (Board board) {
        AlphaBetaAdvanced.run(board.getTurn(), board, 3);
    }

    /**
     * Play using the Alpha-Beta Pruning algorithm. Include depth in the
     * evaluation function and a depth limit.
     * @param board     the Tic Tac Toe board to play on
     * @param ply       the maximum depth
     */
    public static void alphaBetaAdvanced (Board.State player, Board board, int maxDepth) {
        AlphaBetaAdvanced.run(player, board, maxDepth);
    }

}
