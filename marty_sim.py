#MARTINGALE SIMULATOR

#generating random EU roulette numbers (0-36)
import random
import matplotlib.pyplot as plt

def marty(spins, balance, stake, bet_type):
    count = 0
    balances_list = []
    spins_list = []
    initial_stake = stake

        # European Roulette Even-Money Bets

    # Red Numbers
    reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    # Black Numbers
    blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    # Even Numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

    # Odd Numbers
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

    # Low Numbers (1-18)
    lows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    # High Numbers (19-36)
    highs = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    if bet_type == "reds":
        winners = reds
    elif bet_type == "blacks":
        winners = blacks
    

    for i in range(spins):
        count += 1
        print(f"\nspin: {count}")
        spin_result = random.randint(0,36)
        print(f"the number {spin_result} appeared")
        print(f"your stake is {stake}")


        #bet on high numbers (19-36)
        if spin_result in winners:
            balance += stake
            print(f"you win! your balance is £{balance}")
            stake = initial_stake
        else:
            balance -= stake
            print(f"you lose! your balance is £{balance}")
            stake *= 2
        spins_list.append(count)
        balances_list.append(balance)

        if balance <= 0 or balance < stake:
            print("you ve ran out of funds")
            break

    plt.plot(spins_list, balances_list)
    plt.show()

marty(1000, 10000, 9, "reds")