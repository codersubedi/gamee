import random

def gameManager():
    def create_deck():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return [f"{rank} of {suit}" for suit in suits for rank in ranks]

    def deal_cards(deck, num_cards):
        hand = []
        for _ in range(num_cards):
            card = random.choice(deck)
            deck.remove(card)
            hand.append(card)
        return hand

    def evaluate_hand(hand):
        # Simple hand evaluation for demo purposes
        return len(hand)

    class Player:
        def __init__(self, name, is_human=False):
            self.name = name
            self.hand = []
            self.is_human = is_human
            self.is_blind = False
    
    # Initialize players and deck
    player = Player("You", is_human=True)
    bot = Player("Bot")
    players = [player, bot]
    deck = create_deck()

    # Game loop
    while True:
        # Deal cards
        for p in players:
            p.hand = deal_cards(deck, 3)

        # Blind option
        if player.is_human:
            blind = input("Do you want to play blind? (y/n): ").lower()
            if blind == "y":
                player.is_blind = True

        # Bid
        current_bid = 0
        current_bidder = 1  # Bot starts
        while True:
            p = players[current_bidder]
            if p.is_human:
                try:
                    bid = int(input("Your turn to bid: "))
                except ValueError:
                    print("Invalid bid. Please enter a number.")
                    continue
            else:
                # Ensure a valid range for bot's bid
                if current_bid > 0:
                    min_bid = current_bid + 1
                    max_bid = min(current_bid * 2, 500)
                    if min_bid > max_bid:
                        bid = min_bid
                    else:
                        bid = random.randint(min_bid, max_bid)
                else:
                    bid = random.randint(1, 500)
                print(f"Bot bids: {bid}")

            if bid > current_bid:
                current_bid = bid
                current_bidder = (current_bidder + 1) % 2
            else:
                break

        # Showdown
        for p in players:
            if not p.is_blind:
                print(f"{p.name}'s hand: {p.hand}")

        # Determine winner based on hand evaluation
        winner = max(players, key=lambda p: evaluate_hand(p.hand))
        print(f"{winner.name} wins!")

        # End game or continue?
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break

# Example usage
gameManager()
