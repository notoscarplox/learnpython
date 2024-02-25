import random

def simulate_coin_flips(num_flips):
    flips = ['H' if random.random() < 0.5 else 'T' for _ in range(num_flips)]
    return flips

def count_streaks(flips, streak_length):
    streak_count = 0
    current_streak = 0

    for flip in flips:
        if flip == 'H':
            current_streak += 1
        else:
            current_streak = 0

        if current_streak == streak_length:
            streak_count += 1

    return streak_count

def main():
    num_simulations = 10000
    num_flips_per_simulation = 100

    total_streaks = 0

    for _ in range(num_simulations):
        flips = simulate_coin_flips(num_flips_per_simulation)
        total_streaks += count_streaks(flips, 6)

    average_streaks = total_streaks / num_simulations

    print(f"Average number of streaks of 6: {average_streaks}, {total_streaks}")

if __name__ == "__main__":
    main()