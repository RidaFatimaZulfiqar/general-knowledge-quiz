"""
Decodelabs - Project 4: The General Knowledge Quiz
Goal: Ask 3 questions, keep a score counter (+1 for every correct answer)
      and print the final score at the end.
Key skills: If-Else logic & Variables (Control Flow).
"""

print("=" * 38)
print("   THE GENERAL KNOWLEDGE QUIZ")
print("=" * 38)
print("Answer 3 questions. You get +1 point for each correct answer.\n")

# Variable that keeps track of the score
score = 0

# ---------- Question 1 ----------
answer = input("Q1: What is the capital of France? ").strip().lower()
if answer == "paris":
    print("Correct! +1 point\n")
    score = score + 1
else:
    print("Wrong! The correct answer is Paris.\n")

# ---------- Question 2 ----------
answer = input("Q2: Which planet is known as the Red Planet? ").strip().lower()
if answer == "mars":
    print("Correct! +1 point\n")
    score = score + 1
else:
    print("Wrong! The correct answer is Mars.\n")

# ---------- Question 3 ----------
answer = input("Q3: How many continents are there on Earth? ").strip().lower()
if answer == "7" or answer == "seven":
    print("Correct! +1 point\n")
    score = score + 1
else:
    print("Wrong! The correct answer is 7.\n")

# ---------- Final score ----------
print("=" * 38)
print(f"Your final score: {score} out of 3")

if score == 3:
    print("Perfect score! Well done!")
elif score == 2:
    print("Great job! Almost perfect.")
elif score == 1:
    print("Good try! Keep practising.")
else:
    print("Better luck next time!")
print("=" * 38)
