import random

def print_board(board):
    """Print the current game board"""
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    """Check if there's a winner or tie"""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    # Check for tie
    if " " not in board:
        return "Tie"
    
    return None

def get_ai_move(board):
    """Get AI move (random for now)"""
    available = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(available) if available else None

def get_human_move(current_player):
    """Get and validate human player's move"""
    while True:
        position = input(f"Player {current_player}'s turn (1-9): ")
        if not position.isdigit() or int(position) < 1 or int(position) > 9:
            print("Please enter a number between 1 and 9.")
            continue
        return int(position) - 1  # Convert to 0-based index

def play_game(vs_ai=False):
    """Main game function"""
    board = [" "] * 9
    current_player = "X"
    
    print("\nWelcome to Tic Tac Toe!")
    print("Enter a number (1-9) to make your move:")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print("\nLet's begin!\n")
    
    while True:
        print_board(board)
        
        # Get move
        if current_player == "X" or not vs_ai:
            position = get_human_move(current_player)
            if board[position] != " ":
                print("That position is already taken!")
                continue
        else:
            position = get_ai_move(board)
            print(f"AI chooses position {position + 1}")
            
        # Make move
        board[position] = current_player
        
        # Check game status
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Tie":
                print("It's a tie!")
            else:
                winner_name = "AI" if (winner == "O" and vs_ai) else f"Player {winner}"
                print(f"{winner_name} wins!")
            break
            
        # Switch players
        current_player = "O" if current_player == "X" else "X"

def main():
    """Entry point with game mode selection"""
    while True:
        print("\nTIC TAC TOE")
        print("1. Player vs Player")
        print("2. Player vs AI")
        print("3. Exit")
        choice = input("Select game mode (1-3): ")
        
        if choice == "1":
            play_game(vs_ai=False)
        elif choice == "2":
            play_game(vs_ai=True)
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        # Ask to play again
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()