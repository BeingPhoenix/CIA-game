#!/usr/bin/env python3
import os
import sys
import time
import json
import random
import getpass

# ANSI color codes for improved graphics
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# File paths and configuration
HIGH_SCORE_FILE = "highscores.json"
ASSETS_DIR = "assets"
BANNER_FILE = os.path.join(ASSETS_DIR, "banner.txt")
TIME_LIMIT = 25  # base seconds for timed challenges

# Global difficulty and cheat mode flag
DIFFICULTY = "beginner"
CHEAT_MODE = False

# ------------------------------
# Random ASCII Art Transitions
# ------------------------------
def random_art():
    arts = [
        BOLD + CYAN +
        """
  ___       ___           ___           ___           ___     
 /\\  \\     /\\  \\         /\\  \\         /\\  \\         /\\  \\    
 \\:\\  \\   /::\\  \\       /::\\  \\       /::\\  \\       /::\\  \\   
  \\:\\  \\ /:/\\:\\  \\     /:/\\:\\  \\     /:/\\:\\  \\     /:/\\:\\  \\  
  /::\\  /::\\~\\:\\  \\   /::\\~\\:\\  \\   /::\\~\\:\\  \\   /::\\~\\:\\  \\ 
 /:/\\:\\/:/\\:\\ \\:\\__\\ /:/\\:\\ \\:\\__\\ /:/\\:\\ \\:\\__\\ /:/\\:\\ \\:\\__\\
 \\/__\\::/  \\:\\ \\/__/ \\/__\\:\\/:/  / \\/__\\:\\/:/  / \\/__\\:\\/:/  /
      \\:\\   \\:\\__\\        \\::/  /       \\::/  /       \\::/  / 
       \\:\\  /:/  /        /:/  /        /:/  /        /:/  /  
        \\:\\/:/  /        /:/  /        /:/  /        /:/  /   
         \\::/  /         \\/__/         \\/__/         \\/__/    
          \\/__/                                                  
        """ + RESET,
        BOLD + MAGENTA +
        """
  ______     ______     ______     ______     ______    
 /\\  __ \\   /\\  __ \\   /\\  __ \\   /\\  ___\\   /\\  ___\\   
 \\ \\ \\/\\ \\  \\ \\ \\/\\ \\  \\ \\  __ \\  \\ \\___  \\  \\ \\___  \\  
  \\ \\____ \\  \\ \\____ \\  \\ \\_\\ \\_\\  \\/\\_____\\  \\/\\_____\\ 
   \\/___/ /   \\/___/ /   \\/_/\\/_/   \\/_____/   \\/_____/ 
       / /                                            
      / /                                             
     / /                                              
    /_/                                               
        """ + RESET,
    ]
    art = random.choice(arts)
    print(art)

# ------------------------------
# Utility Functions
# ------------------------------
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def print_banner():
    if os.path.isfile(BANNER_FILE):
        with open(BANNER_FILE, "r") as f:
            print(BOLD + f.read() + RESET)
    else:
        print(BOLD + f"{CYAN}********** Phoenix[CIA S\\V] **********{RESET}\n")

def pause():
    input("\nPress Enter to continue...")

def load_high_scores():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as f:
            return json.load(f)
    else:
        return {"highest": 0, "name": ""}

def save_high_scores(score, name):
    data = {"highest": score, "name": name}
    with open(HIGH_SCORE_FILE, "w") as f:
        json.dump(data, f)

def print_high_scores():
    scores = load_high_scores()
    print(f"\n{BOLD}{YELLOW}--- High Score ---{RESET}")
    if scores["highest"] > 0:
        print(f"Score: {GREEN}{scores['highest']}{RESET} by {CYAN}{scores['name']}{RESET}")
    else:
        print("No high scores yet!")
    print(f"{BOLD}{YELLOW}------------------{RESET}\n")

def timed_input(prompt, time_limit):
    print(f"{YELLOW}(You have {time_limit} seconds for this challenge...){RESET}")
    start = time.time()
    answer = input(prompt)
    elapsed = time.time() - start
    if elapsed > time_limit:
        print(f"{RED}Time's up! You took {int(elapsed)} sec (limit was {time_limit} sec).{RESET}")
        return None, elapsed
    return answer, elapsed

# ------------------------------
# Difficulty & Cheat Mode
# ------------------------------
def choose_difficulty():
    global DIFFICULTY
    clear_screen()
    print_banner()
    print(BOLD + "\nSelect Difficulty Level:" + RESET)
    print("1. Beginner (simpler puzzles with more hints)")
    print("2. Advanced (more complex and randomized puzzles)")
    choice = input("\nEnter your choice (1 or 2): ").strip()
    if choice == "2":
        DIFFICULTY = "advanced"
        print(GREEN + "\nAdvanced mode selected. Prepare for unpredictable challenges!" + RESET)
    else:
        DIFFICULTY = "beginner"
        print(GREEN + "\nBeginner mode selected. Enjoy the guided challenges!" + RESET)
    time.sleep(2)

def cheat_menu():
    global CHEAT_MODE
    cheat_text = (
        BOLD + CYAN +
        "\n=== CHEAT MODE ACTIVATED ===\n\n"
        "Act I: Confidentiality Challenge\n"
        "  - Beginner (Caesar cipher): Answer = 'this is a secret code'\n"
        "  - Advanced (Vigenère cipher): Secret depends on random generation.\n\n"
        "Act II: Integrity Challenge\n"
        "  - Beginner (Log anomaly): Tampered line = 4\n"
        "  - Advanced (Hash selection): Correct SHA-256 hash is the 64-character string\n\n"
        "Act III: Availability Challenge\n"
        "  - Beginner: Allocate 100 points among 3 servers; each ≥20\n"
        "  - Advanced: Allocate 150 points among 4 servers; each ≥25 and Server1 ≥ Server4 + 10\n"
        "============================\n" + RESET
    )
    print(cheat_text)
    CHEAT_MODE = True
    pause()

# ------------------------------
# Act I: Confidentiality Challenge
# ------------------------------
def act_confidentiality():
    clear_screen()
    print_banner()
    random_art()  # Show random graphic transition
    print(BOLD + "\nAct I: Confidentiality Challenge" + RESET)
    print("\nStory: A confidential message containing sensitive mission data has been intercepted.")
    print("Your task is to decode it, learning why confidentiality is vital.\n")
    time.sleep(1)

    # Beginner variant: Fixed Caesar cipher with shift=3
    def puzzle_caesar_beginner():
        print("Puzzle: Decode this simple Caesar cipher.")
        ciphertext = "Wklv lv d vhfuhw frgh!"
        print(f"\nCiphertext: {MAGENTA}{ciphertext}{RESET}")
        print(BLUE + "Hint: Shift each letter 3 positions to the left." + RESET)
        answer, elapsed = timed_input("\nEnter the decoded message (all lowercase): ", TIME_LIMIT)
        correct = "this is a secret code"
        if answer is None or answer.strip().lower() != correct:
            print(RED + "\nIncorrect! Confidentiality is at risk." + RESET)
            return 0
        bonus = max(0, TIME_LIMIT - int(elapsed))
        print(GREEN + f"\nCorrect! Confidentiality maintained. Bonus: {bonus} points." + RESET)
        return 10 + bonus

    # Advanced variant: Randomized Caesar cipher
    def puzzle_caesar_advanced():
        shift_val = random.randint(3, 7)
        # Randomly select a secret phrase from a list
        phrases = [
            "cybersecurity is vital",
            "data protection matters",
            "encryption saves secrets"
        ]
        correct = random.choice(phrases)
        # Encrypt using Caesar with shift_val
        ciphertext = ""
        for ch in correct:
            if ch.isalpha():
                # assuming lowercase only
                ciphertext += chr((ord(ch) - ord('a') + shift_val) % 26 + ord('a'))
            else:
                ciphertext += ch
        print("Puzzle: Decode this advanced Caesar cipher.")
        print(f"\nCiphertext: {MAGENTA}{ciphertext}{RESET}")
        print(BLUE + f"Hint: Shift each letter {shift_val} positions to the left." + RESET)
        answer, elapsed = timed_input("\nEnter the decoded message: ", TIME_LIMIT + 5)
        if answer is None or answer.strip().lower() != correct:
            print(RED + "\nIncorrect! Confidentiality compromised." + RESET)
            return 0
        bonus = max(0, (TIME_LIMIT + 5) - int(elapsed))
        print(GREEN + f"\nExcellent! Advanced confidentiality maintained. Bonus: {bonus} points." + RESET)
        return 15 + bonus

    # Advanced Vigenère variant: Random key and phrase
    def puzzle_vigenere_advanced():
        key_list = ["cyber", "crypto", "secure", "defend"]
        key = random.choice(key_list)
        phrases = ["protect data", "keep secrets", "information shield"]
        correct = random.choice(phrases)
        ciphertext = ""
        key_index = 0
        for ch in correct:
            if ch.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('a')
                ciphertext += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
                key_index += 1
            else:
                ciphertext += ch
        print("Puzzle: Decode this advanced Vigenère cipher.")
        print(f"\nCiphertext: {MAGENTA}{ciphertext}{RESET}")
        print(BLUE + f"Hint: The key is '{key}'." + RESET)
        answer, elapsed = timed_input("\nEnter the decoded message: ", TIME_LIMIT + 5)
        if answer is None or answer.strip().lower() != correct:
            print(RED + "\nIncorrect! Confidentiality is compromised." + RESET)
            return 0
        bonus = max(0, (TIME_LIMIT + 5) - int(elapsed))
        print(GREEN + f"\nExcellent! Advanced confidentiality maintained. Bonus: {bonus} points." + RESET)
        return 15 + bonus

    # Select the puzzle based on DIFFICULTY and randomize further in advanced
    if DIFFICULTY == "advanced":
        puzzle = random.choice([puzzle_caesar_advanced, puzzle_vigenere_advanced])
    else:
        puzzle = puzzle_caesar_beginner

    if CHEAT_MODE:
        # Updated cheat message for advanced puzzles:
        print(YELLOW + "\n[CHEAT MODE] Beginner Caesar answer: 'this is a secret code'" + RESET)
        print(YELLOW + "[CHEAT MODE] Advanced Caesar: Depends on random shift and phrase. Advanced Vigenère: key is one of ['cyber','crypto','secure','defend'] and plaintext is one of ['protect data','keep secrets','information shield']." + RESET)
        pause()
        return 10 + TIME_LIMIT
    score = puzzle()
    pause()
    return score

# ------------------------------
# Act II: Integrity Challenge
# ------------------------------
def act_integrity():
    clear_screen()
    print_banner()
    random_art()
    print(BOLD + "\nAct II: Integrity Challenge" + RESET)
    print("\nStory: Our system logs have been tampered with. You must spot the anomaly to ensure data integrity.\n")
    time.sleep(1)
    
    def puzzle_logs_beginner():
        logs = [
            "1. LOGIN: UserA | Timestamp: 2025-04-07 10:00:00",
            "2. LOGIN: UserB | Timestamp: 2025-04-07 10:05:00",
            "3. LOGIN: UserC | Timestamp: 2025-04-07 10:10:00",
            "4. L0GIN: UserD | Timestamp: 2025-04-07 10:15:00",
            "5. LOGIN: UserE | Timestamp: 2025-04-07 10:20:00"
        ]
        print("Puzzle: Which log entry is tampered with?")
        for line in logs:
            print(line)
        print(BLUE + "\nHint: Look for a spelling mistake." + RESET)
        answer, elapsed = timed_input("\nEnter the line number (1-5): ", TIME_LIMIT)
        try:
            ans_int = int(answer.strip())
        except Exception:
            print(RED + "Invalid input!" + RESET)
            return 0
        if ans_int == 4:
            bonus = max(0, TIME_LIMIT - int(elapsed))
            print(GREEN + f"\nCorrect! Integrity maintained. Bonus: {bonus} points." + RESET)
            return 10 + bonus
        else:
            print(RED + "\nIncorrect. Integrity is compromised." + RESET)
            return 0

    def puzzle_logs_advanced():
        # Generate a random log set where one random line (between 2 and 4) is altered randomly.
        base_logs = [
            "LOGIN: UserA | Timestamp: 2025-04-07 10:00:00",
            "LOGIN: UserB | Timestamp: 2025-04-07 10:05:00",
            "LOGIN: UserC | Timestamp: 2025-04-07 10:10:00",
            "LOGIN: UserD | Timestamp: 2025-04-07 10:15:00",
            "LOGIN: UserE | Timestamp: 2025-04-07 10:20:00"
        ]
        tamper_index = random.randint(1, 3)  # random line between 2 and 4 (0-indexed)
        # Replace first letter of the word LOGIN with 'L0GIN'
        base_logs[tamper_index] = base_logs[tamper_index].replace("LOGIN", "L0GIN", 1)
        print("Puzzle: Identify the tampered log entry from the following:")
        for idx, line in enumerate(base_logs, 1):
            print(f"{idx}. {line}")
        print(BLUE + "\nHint: Look for character anomalies in the login entries." + RESET)
        answer, elapsed = timed_input("\nEnter the tampered line number (1-5): ", TIME_LIMIT)
        try:
            ans_int = int(answer.strip())
        except Exception:
            print(RED + "\nInvalid input!" + RESET)
            return 0
        if ans_int == tamper_index + 1:
            bonus = max(0, TIME_LIMIT - int(elapsed))
            print(GREEN + f"\nCorrect! Integrity is intact. Bonus: {bonus} points." + RESET)
            return 10 + bonus
        else:
            print(RED + "\nIncorrect. Integrity is compromised." + RESET)
            return 0

    def puzzle_hash():
        print("Puzzle: Which of these is a valid SHA-256 hash?")
        correct_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        decoy_hash = "5d41402abc4b2a76b9719d911017c592"
        options = [correct_hash, decoy_hash]
        random.shuffle(options)
        for idx, opt in enumerate(options, 1):
            print(f"{idx}. {opt}")
        print(BLUE + "\nHint: A valid SHA-256 hash contains 64 hexadecimal characters." + RESET)
        answer, elapsed = timed_input("\nSelect the correct option (1 or 2): ", TIME_LIMIT)
        try:
            ans_int = int(answer.strip())
        except Exception:
            print(RED + "\nInvalid input!" + RESET)
            return 0
        if options[ans_int - 1] == correct_hash:
            bonus = max(0, TIME_LIMIT - int(elapsed))
            print(GREEN + f"\nWell done! Integrity verified. Bonus: {bonus} points." + RESET)
            return 15 + bonus
        else:
            print(RED + "\nIncorrect. Integrity remains unverified." + RESET)
            return 0

    if DIFFICULTY == "advanced":
        challenge = random.choice([puzzle_logs_advanced, puzzle_hash])
    else:
        challenge = puzzle_logs_beginner

    if CHEAT_MODE:
        print(YELLOW + "\n[CHEAT MODE] For logs: tampered entry is the one altered (random); for hash: choose the 64-character string." + RESET)
        pause()
        return 10 + TIME_LIMIT
    score = challenge()
    pause()
    return score

# ------------------------------
# Act III: Availability Challenge
# ------------------------------
def act_availability():
    clear_screen()
    print_banner()
    random_art()
    print(BOLD + "\nAct III: Availability Challenge" + RESET)
    print("\nStory: A DDoS attack has disrupted our network! Your mission is to restore system availability by correctly")
    print("allocating limited bandwidth resources to our servers.\n")
    
    def puzzle_simple():
        print("Puzzle: Allocate 100 bandwidth points among 3 servers (each must get at least 20 points).")
        answer, elapsed = timed_input("Enter three numbers separated by spaces (e.g., 35 30 35): ", TIME_LIMIT)
        try:
            alloc = list(map(int, answer.strip().split()))
            if len(alloc) != 3:
                raise ValueError("Enter exactly three numbers.")
        except Exception as e:
            print(RED + "\nInvalid input: " + str(e) + RESET)
            return 0
        if sum(alloc) != 100:
            print(RED + f"\nTotal allocated is {sum(alloc)} (should equal 100)." + RESET)
            return 0
        if any(a < 20 for a in alloc):
            print(RED + "\nEach server must receive at least 20 points." + RESET)
            return 0
        bonus = max(0, TIME_LIMIT - int(elapsed))
        print(GREEN + f"\nCorrect allocation! Bonus: {bonus} points." + RESET)
        return 10 + bonus

    def puzzle_advanced():
        # Advanced variant: Randomize total allocation between 140 and 160, random minimum and difference constraint
        total_points = random.choice([150, 155])
        min_per_server = random.choice([25, 30])
        diff_requirement = random.choice([10, 15])
        print(f"Puzzle: Allocate {total_points} bandwidth points among 4 servers with these conditions:")
        print(f"  - Each server must receive at least {min_per_server} points.")
        print(f"  - Server 1 must receive at least {diff_requirement} more points than Server 4.\n")
        answer, elapsed = timed_input(f"Enter four numbers separated by spaces (sum must equal {total_points}): ", TIME_LIMIT + 5)
        try:
            alloc = list(map(int, answer.strip().split()))
            if len(alloc) != 4:
                raise ValueError("Enter exactly four numbers.")
        except Exception as e:
            print(RED + "\nInvalid input: " + str(e) + RESET)
            return 0
        if sum(alloc) != total_points:
            print(RED + f"\nTotal allocated is {sum(alloc)} (should equal {total_points})." + RESET)
            return 0
        if any(a < min_per_server for a in alloc):
            print(RED + f"\nEach server must receive at least {min_per_server} points." + RESET)
            return 0
        if alloc[0] < alloc[3] + diff_requirement:
            print(RED + f"\nServer 1 must receive at least {diff_requirement} more points than Server 4." + RESET)
            return 0
        bonus = max(0, (TIME_LIMIT + 5) - int(elapsed))
        print(GREEN + f"\nAdvanced allocation successful! Bonus: {bonus} points." + RESET)
        return 15 + bonus

    if DIFFICULTY == "advanced":
        challenge = random.choice([puzzle_simple, puzzle_advanced])
    else:
        challenge = puzzle_simple

    if CHEAT_MODE:
        print(YELLOW + "\n[CHEAT MODE] For the simple puzzle: any allocation summing to 100 with each ≥20 is correct.")
        print("[CHEAT MODE] For advanced: ensure total equals the randomized total, each server gets at least the minimum, and Server1 is greater than Server4 by the required difference." + RESET)
        pause()
        return 10 + TIME_LIMIT
    score = challenge()
    pause()
    return score

# ------------------------------
# High Score System
# ------------------------------
def update_high_score(final_score):
    scores = load_high_scores()
    if final_score > scores.get("highest", 0):
        print(GREEN + "\nNew High Score!" + RESET)
        name = input("Enter your name: ").strip()
        save_high_scores(final_score, name)
    else:
        print("\nNo new high score this time.")
    pause()

def print_high_scores_screen():
    scores = load_high_scores()
    print(BOLD + "\n--- High Score ---" + RESET)
    if scores["highest"] > 0:
        print(f"Score: {GREEN}{scores['highest']}{RESET} by {CYAN}{scores['name']}{RESET}")
    else:
        print("No high scores yet!")
    print(BOLD + "------------------\n" + RESET)
    pause()

# ------------------------------
# Extra: Show CIA Triad Information
# ------------------------------
def show_cia_info():
    clear_screen()
    print_banner()
    info = f"""
{BOLD}{CYAN}--- CIA Triad Overview ---{RESET}

{BOLD}Confidentiality:{RESET}
  - Protects sensitive data from unauthorized access using encryption.
  - Our challenges (Caesar/Vigenère) simulate how encryption hides information.

{BOLD}Integrity:{RESET}
  - Ensures data remains accurate and unaltered.
  - Puzzles focus on detecting anomalies in log entries or validating cryptographic hashes.

{BOLD}Availability:{RESET}
  - Guarantees access to systems and data when needed.
  - Resource allocation puzzles simulate maintaining system uptime during disruptions.

Mastering these principles is essential for effective cybersecurity.
{BOLD}{CYAN}--------------------------{RESET}
    """
    print(info)
    pause()

# ------------------------------
# Cheat Mode: Reveal Answers and Explanations
# ------------------------------
def activate_cheat():
    global CHEAT_MODE
    cheat_menu()

# ------------------------------
# Main Game Loop & Menu System
# ------------------------------
def game_loop():
    total_score = 0
    clear_screen()
    print_banner()
    random_art()  # Transition graphic
    print(BOLD + "\nWelcome, Cyber Defender, to Triad Defender: The Phoenix Chronicles!" + RESET)
    print("\nIn this mission, you will face three challenges that test your knowledge of Confidentiality, Integrity, and Availability.")
    print("Answer quickly to earn bonus points and improve your cybersecurity skills!\n")
    input("Press Enter to begin your mission...")
    
    total_score += act_confidentiality()
    total_score += act_integrity()
    total_score += act_availability()
    
    clear_screen()
    print_banner()
    random_art()
    print(BOLD + "\nMission Complete!" + RESET)
    print(f"\nYour total score: {BOLD}{YELLOW}{total_score}{RESET} / 90\n")
    if total_score >= 70:
        print(GREEN + "\nOutstanding performance, Defender! You've mastered the CIA Triad." + RESET)
    elif total_score >= 40:
        print(YELLOW + "\nNot bad, but there's room for improvement. Keep training until you're invincible!" + RESET)
    else:
        print(RED + "\nThe system is still vulnerable. Study the principles and try again!" + RESET)
    
    update_high_score(total_score)
    print_high_scores_screen()

def interactive_menu():
    while True:
        clear_screen()
        print_banner()
        random_art()
        print(BOLD + "====== Triad Defender: Main Menu ======" + RESET)
        print("1. Start New Game")
        print("2. Show CIA Triad Information")
        print("3. View High Scores")
        print("4. Change Difficulty (Current: " + MAGENTA + DIFFICULTY.capitalize() + RESET + ")")
        print("5. Activate Cheat Mode (Reveal Answers & Explanations)")
        print("6. Exit Game")
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice == "1":
            game_loop()
        elif choice == "2":
            show_cia_info()
        elif choice == "3":
            print_high_scores_screen()
        elif choice == "4":
            choose_difficulty()
        elif choice == "5":
            activate_cheat()
        elif choice == "6":
            print(CYAN + "\nExiting game. Stay secure, Defender!" + RESET)
            sys.exit(0)
        else:
            print(RED + "\nInvalid choice! Please enter a number between 1 and 6." + RESET)
            time.sleep(1)

def choose_difficulty():
    global DIFFICULTY
    clear_screen()
    print_banner()
    print(BOLD + "\nSelect Difficulty Level:" + RESET)
    print("1. Beginner (guided puzzles with plenty of hints)")
    print("2. Advanced (complex, randomized puzzles)")
    choice = input("\nEnter your choice (1 or 2): ").strip()
    if choice == "2":
        DIFFICULTY = "advanced"
        print(GREEN + "\nAdvanced mode selected. Prepare for unpredictable challenges!" + RESET)
    else:
        DIFFICULTY = "beginner"
        print(GREEN + "\nBeginner mode selected. Enjoy the guided challenges!" + RESET)
    time.sleep(2)

def main():
    clear_screen()
    print_banner()
    print(BOLD + "\nTriad Defender: The Phoenix Chronicles" + RESET)
    print("\nDeveloped for Kali Linux - Embark on an epic journey into the core principles of the CIA Triad.")
    print("Learn how confidentiality, integrity, and availability protect our digital world as you solve educational puzzles.\n")
    choose_difficulty()
    interactive_menu()

if __name__ == "__main__":
    main()
