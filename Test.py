while True:
    # Print an opening statement
    print("Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until he reaches 17. Aces count as 1 or 11.")

    # Create & shuffle the deck, deal two cards to each player
    deck1 = Deck()
    deck1.shuffle()

    player1 = Hand()
    player1.add_card(deck1.deal())
    player1.add_card(deck1.deal())

    dealer = Hand()
    dealer.add_card(deck1.deal())
    dealer.add_card(deck1.deal())

    # Set up the Player's chips
    player1_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player1_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player1, dealer)

    while PLAYING:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck1, player1)

        # Show cards (but keep one dealer card hidden)
        show_some(player1, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player1.value > 21:
            player_busts(player1, deck1, player1_chips)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player1.value <= 21:

            while dealer.value < 17:
                hit(deck1, dealer)

                # Show all cards
        show_all(player1, dealer)

        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player1, deck1, player1_chips)

        elif player1.value > dealer.value:
            player_wins(player1, deck1, player1_chips)

        elif player1.value < dealer.value:
            dealer_wins(player1, deck1, player1_chips)

        else:
            push(player1, dealer)

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player1_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter Yes or No: ")

    if new_game.lower() == 'yes':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break