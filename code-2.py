def get_random_move(board):
    valid_locations = [col for col in range(COLUMN_COUNT) if is_valid_location(board, col)]
    return random.choice(valid_locations)
def get_computer_move(board):
    return get_random_move(board)

agent = 0
while agent ==0 :
    print("Choose an agent to play against:")
    print("1. MinMAx agent")
    print("2. Alpha-Beta pruning agent")
    choice = input("> ")
    if choice == "1":
        agent =1
    elif choice == "2":
        depth = int(input("Enter Level for agent: "
                          "1-Easy "
                          "2-Medium "
                          "3-Hard "))
        if depth==1 :
            agent = 2
        if depth==2:
            agent = 4
        if depth==3:
            agent = 7

    else:
        print("Invalid choice. Please choose again.")



while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == PLAYER:
                posx = event.pos[0]
                # Computer's turn
                col = get_computer_move(board)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)

                if winning_move(board, PLAYER_PIECE):
                    label = myfont.render("Player 1 wins!!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True

                turn += 1
                turn = turn % 2

                print_board(board)
                draw_board(board)

    # # Ask for Player 2 Input
    if turn == AI and not game_over:

        # col = random.randint(0, COLUMN_COUNT-1)
        # col = pick_best_move(board, AI_PIECE)
        if agent==1:
            col, minimax_score = minimax(board, agent, True)
        else:
            col, minimax_score = minimax_AP(board, agent, -math.inf, math.inf, True)

        if is_valid_location(board, col):
            # pygame.time.wait(500)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)

            if winning_move(board, AI_PIECE):
                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

    if game_over:
        pygame.time.wait(3000)