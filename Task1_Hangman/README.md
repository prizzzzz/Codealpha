# 🎮 Task 1: Hangman Game

**A fun word-guessing game where you try to guess a secret word letter by letter!**

---

## 🎯 What Is This?

This is a **Hangman game** - a classic word puzzle where:
- The computer picks a secret word
- You guess letters one at a time
- You win if you guess all letters before running out of tries
- You lose if you make too many wrong guesses

**It's like the game you played as a kid, but on your computer!**

---

## 🚀 How to Run (Super Simple!)

### Step 1: Open Terminal/Command Prompt
- **Windows:** Press `Win + R`, type `cmd`, press Enter
- **Mac:** Press `Cmd + Space`, type `terminal`, press Enter

### Step 2: Go to This Folder
```bash
cd Task1_Hangman
```

### Step 3: Run the Game
```bash
python hangman.py
```

### Step 4: Play!
The game will show you instructions. Just follow along!

---

## 🎮 How to Play

### When You Start:

1. **Choose Difficulty:**
   ```
   Select difficulty level:
   1. Easy (4-7 letters)      ← Good for beginners!
   2. Medium (8-11 letters)    ← Medium challenge
   3. Hard (12+ letters)       ← Hard challenge
   
   Enter choice (1-3): 
   ```
   Type `1`, `2`, or `3` and press Enter

2. **See the Word:**
   ```
   Word: _ _ _ _ _ _
   ```
   Each `_` is a letter you need to guess

3. **Guess Letters:**
   ```
   Guess a letter: a
   ```
   Type a single letter and press Enter

4. **See Results:**
   - ✅ **Correct guess:** The letter appears in the word!
   - ❌ **Wrong guess:** You lose one try (see the hangman drawing)

5. **Win or Lose:**
   - 🎉 **Win:** Guess all letters before running out of tries
   - 💀 **Lose:** Make too many wrong guesses

---

## 📋 Example Game Session

```
============================================================
Welcome to HANGMAN!
============================================================

Select difficulty level:
1. Easy (4-7 letters)
2. Medium (8-11 letters)
3. Hard (12+ letters)

Enter choice (1-3): 1

============================================================
Word length: 6 letters
Max incorrect guesses allowed: 7
============================================================

           +---+
           |   |
               |
               |
               |
               |
         =========

Word: _ _ _ _ _ _
Guessed letters: None
Incorrect guesses: 0/7

Guess a letter: p
✅ Good guess! 'p' appears 1 time(s) in the word!

Word: p _ _ _ _ _
Guessed letters: p
Incorrect guesses: 0/7

Guess a letter: y
✅ Good guess! 'y' appears 1 time(s) in the word!

Word: p y _ _ _ _
Guessed letters: p, y
Incorrect guesses: 0/7

Guess a letter: x
❌ Sorry! 'x' is not in the word.

           +---+
           |   |
           O   |
               |
               |
               |
         =========

Word: p y _ _ _ _
Guessed letters: p, x, y
Incorrect guesses: 1/7

... (continue guessing) ...

🎉 Congratulations! You won! The word was: PYTHON
```

---

## 🎯 Difficulty Levels Explained

### Easy Level (Option 1)
- **Word length:** 4-7 letters
- **Wrong guesses allowed:** 7
- **Example words:** python, hangman, computer
- **Best for:** Beginners, kids, quick games

### Medium Level (Option 2)
- **Word length:** 8-11 letters
- **Wrong guesses allowed:** 6
- **Example words:** programming, developer, algorithm
- **Best for:** Intermediate players

### Hard Level (Option 3)
- **Word length:** 12+ letters
- **Wrong guesses allowed:** 8
- **Example words:** encapsulation, polymorphism, inheritance
- **Best for:** Advanced players, challenge seekers

---

## 🎨 Visual Features

**The game shows a hangman drawing that gets completed as you make wrong guesses:**

```
Stage 0: Empty gallows
Stage 1: Head appears (O)
Stage 2: Body appears (|)
Stage 3: One arm (/|)
Stage 4: Both arms (/|\)
Stage 5: One leg (/)
Stage 6: Both legs (/ \) ← Game Over!
```

**This visual feedback helps you see how many tries you have left!**

---

## 💡 Tips for Playing

1. **Start with vowels** - Letters like A, E, I, O, U appear in most words
2. **Look for common letters** - R, S, T, L, N are very common
3. **Use Easy mode first** - Get comfortable before trying harder levels
4. **Don't repeat guesses** - The game will warn you if you try
5. **Type 'quit' anytime** - Exit the game whenever you want

---

## 🔧 What You Need

- **Python 3.6 or higher**
- That's it! No extra packages needed.

**Check if you have Python:**
```bash
python --version
```

---

## 📁 Files in This Folder

- **`hangman.py`** - The game code (this is what you run)
- **`README.md`** - This file (instructions and help)

---

## 🎓 What You'll Learn

By playing with this code, you'll learn about:

1. **Loops** - How the game keeps asking for guesses
2. **Conditionals** - Checking if guesses are correct
3. **Strings** - Working with words and letters
4. **Lists** - Keeping track of guessed letters
5. **Functions** - Organizing code into reusable parts
6. **User Input** - Getting input from the player

---

## 🛠️ Customizing the Game

**Want to make it your own? Try these modifications:**

### Add More Words
Open `hangman.py` and find the `word_bank` dictionary. Add your own words!

```python
word_bank = {
    "easy": ["python", "hangman", "YOUR_WORD_HERE"],
    # ... add more words
}
```

### Change Difficulty Settings
Find where `max_incorrect` is set and change the number of allowed wrong guesses.

### Add New Difficulty Level
Copy one of the existing difficulty sections and modify it!

---

## ❓ Common Questions

### Q: How do I quit the game?
**A:** Type `quit` when asked for a letter, or press `Ctrl + C`

### Q: Can I play again?
**A:** Yes! After each game, you'll be asked if you want to play again.

### Q: What if I type more than one letter?
**A:** The game will ask you to enter a single letter only.

### Q: Can I guess the whole word?
**A:** Not in this version - you guess one letter at a time. But you could modify the code to add that feature!

### Q: Why does it say I already guessed a letter?
**A:** The game remembers all your guesses to prevent duplicates.

---

## 🐛 Troubleshooting

### Problem: "python: command not found"
**Solution:** Make sure Python is installed. Try `python3` instead of `python`.

### Problem: "No module named..."
**Solution:** This shouldn't happen - the game only uses built-in Python modules. Make sure you're using Python 3.6+.

### Problem: Game won't start
**Solution:** 
1. Make sure you're in the `Task1_Hangman` folder
2. Check that `hangman.py` exists in that folder
3. Try: `python hangman.py` (make sure there are no typos)

---

## 🎉 Have Fun!

**This is a game - enjoy it!** Don't worry about winning or losing. The goal is to have fun and learn Python!

**Pro tip:** Try reading the code in `hangman.py` while playing. You'll start to understand how it works!

---

## 📞 Quick Commands

**Run the game:**
```bash
python hangman.py
```

**Check Python version:**
```bash
python --version
```

**See all files:**
```bash
dir    # Windows
ls     # Mac/Linux
```

---

**Ready to play? Run `python hangman.py` and have fun! 🎮**
