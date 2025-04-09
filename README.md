Below is an engaging README file in Markdown format for your GitHub repository. You can copy and paste the text below into your repository's README.md file.

---

# Triad Defender: The Phoenix Chronicles

![Banner](cia_game_for_fun/assets/banner.txt)

**Triad Defender: The Phoenix Chronicles** is an immersive, interactive terminal game developed for Kali Linux that challenges you to defend your digital fortress using the core principles of the CIA Triad—**Confidentiality, Integrity, and Availability**.

This game not only serves as a fun way to test your cybersecurity skills but also teaches you vital concepts about encryption, data integrity, and resource management—all while immersed in a cyber-defense narrative.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Cheat Mode](#cheat-mode)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

In **Triad Defender: The Phoenix Chronicles**, you assume the role of a Cyber Defender tasked with protecting sensitive mission data by overcoming a series of challenges. Each challenge corresponds to a principle of the CIA Triad:

- **Confidentiality:** Decode intercepted messages using various cipher puzzles (Caesar and Vigenère).
- **Integrity:** Identify tampered log entries and select the correct cryptographic hash to maintain data integrity.
- **Availability:** Restore system availability by correctly allocating bandwidth against simulated DDoS attacks.

The game dynamically randomizes puzzles and conditions in advanced mode to keep every playthrough unique, ensuring you'll never get bored and always learn something new!

---

## Features

- **Dual Difficulty Levels:**  
  - **Beginner:** Guided puzzles with extra hints.  
  - **Advanced:** Complex, randomized puzzles for a more unpredictable challenge.
- **Engaging Storyline:** Immerse yourself in a thrilling narrative where real cybersecurity challenges come to life.
- **Timed Challenges:** Answer quickly to earn bonus points!
- **Dynamic Puzzles:** Randomized Caesar shifts, Vigenère ciphers with random keys, and customizable log and resource challenges.
- **Cheat Mode:** Stuck on a puzzle? Activate Cheat Mode for full answers, detailed explanations, and hints.
- **Visual Enhancements:** Enjoy colorful terminal graphics and randomized ASCII art transitions between challenges.
- **High Score Tracking:** Record your scores locally and challenge yourself to beat the highest score.

---

## Installation

### Prerequisites

- **Kali Linux** (or any Linux terminal that supports ANSI colors)
- **Python 3**

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/beingphoenix/triad-defender.git
   cd triad-defender
   ```

2. **Prepare the Assets:**

   Create an `assets` folder in the repository directory (if it doesn't already exist) and add a file named `banner.txt` containing your ASCII art banner. For example:

   ```plaintext
   ********** Phoenix[CIA Game] **********
   ```

3. **Run the Game:**

   Simply execute the game script from the terminal:

   ```bash
   python3 triad_defender_super.py
   ```

No additional Python packages are required—this project relies solely on Python’s standard library and ANSI escape codes.

---

## Usage

After launching the game, you'll be greeted with a colorful banner and a prompt to select your desired difficulty level:

- **Beginner:** Enjoy puzzles with extra guidance.
- **Advanced:** Brace yourself for randomized and challenging puzzles that vary each time you play.

Follow the on-screen instructions to navigate the main menu. You can choose to start a new game, view detailed CIA Triad information, check high scores, change the difficulty level, or activate Cheat Mode if you need assistance.

---

## Gameplay

**Triad Defender: The Phoenix Chronicles** is split into three acts:

1. **Act I – Confidentiality Challenge:**  
   - **Beginner Mode:** Decode a Caesar cipher with a fixed shift.  
   - **Advanced Mode:** Solve a randomized Caesar cipher or a Vigenère cipher with a randomly selected key and phrase.

2. **Act II – Integrity Challenge:**  
   - **Beginner Mode:** Identify the tampered log entry in a fixed log list.  
   - **Advanced Mode:** Randomly generate log entries and require you to detect the anomaly, or choose the correct SHA-256 hash from a set of randomized options.

3. **Act III – Availability Challenge:**  
   - **Beginner Mode:** Allocate 100 bandwidth points among 3 servers with minimum values.  
   - **Advanced Mode:** Solve a dynamic resource allocation puzzle with randomized total points, minimum per server, and difference requirements.

Bonus points are awarded based on how quickly you answer. If you find yourself stuck, activate Cheat Mode!

---

## Cheat Mode

When activated, Cheat Mode reveals all correct answers and provides thorough explanations for each challenge. Use it to learn the underlying concepts or if you truly get stuck on a puzzle. (Use this feature wisely!)

---

## Contributing

Contributions, improvements, and new ideas are welcome! Feel free to fork this repository and submit pull requests. When contributing, please:
- Follow consistent coding styles.
- Include helpful comments and documentation.
- Test your changes thoroughly before submitting.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

If you have any questions, feedback, or ideas for new challenges, please contact me at:  
**Email:** parthpatel21274@gmail.com  
**GitHub:** [@BeingPhoenix](https://github.com/beingphoenix)

---

Enjoy defending the digital fortress and mastering the CIA Triad with **Triad Defender: The Phoenix Chronicles**!  
Happy hacking (ethically)!

---

Feel free to adjust any sections to suit your personal style or add additional badges, screenshots, or video demos to further enhance your repository's presentation.
