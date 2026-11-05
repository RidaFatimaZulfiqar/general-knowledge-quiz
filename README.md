<img width="1874" height="1110" alt="image" src="https://github.com/user-attachments/assets/eb236370-d673-4085-a2a3-702ff60c48d0" /># The General Knowledge Quiz

**Decodelabs Project 4**

A small quiz game that asks 3 general knowledge questions, adds 1 point for every correct answer, and prints the final score at the end. This repository has two versions of the same game:

- a **Python command-line program** (`quiz.py`)
- a **web app** (`index.html`) that runs in the browser

**Live demo:** https://ridafatimazulfiqar.github.io/general-knowledge-quiz/


---

## Project goal

Create a game that asks 3 questions (e.g., "What is the capital of France?"). Keep a score counter: +1 point for every correct answer. Print the final score at the end.

**Key skills practised:** if-else logic and variables.

**Why it matters:** it teaches "control flow", which means directing the program based on user choices.

---

## Questions

| # | Question | Answer |
|---|---|---|
| 1 | What is the capital of France? | Paris |
| 2 | Which planet is known as the Red Planet? | Mars |
| 3 | How many continents are there on Earth? | 7 |

---

## Project structure

```
.
├── index.html   # Web version (HTML, CSS and JavaScript in one file)
├── quiz.py      # Command-line version
└── README.md    # This documentation
```

---

## Getting started

### Python version

**Requirements:** Python 3.6 or newer. No extra packages are needed.

```bash
python quiz.py
```

**Example session**

```
======================================
   THE GENERAL KNOWLEDGE QUIZ
======================================
Answer 3 questions. You get +1 point for each correct answer.

Q1: What is the capital of France? paris
Correct! +1 point

Q2: Which planet is known as the Red Planet? venus
Wrong! The correct answer is Mars.

Q3: How many continents are there on Earth? 7
Correct! +1 point

======================================
Your final score: 2 out of 3
Great job! Almost perfect.
======================================
```

### Web version

**Locally:** double-click `index.html` to open it in any modern browser. No server or build step is needed.

**On GitHub Pages:**

1. Push the files to a GitHub repository.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select the `main` branch and the `/ (root)` folder, then click **Save**.
5. After a minute or two, the site is live at `https://<your-username>.github.io/<repository-name>/`.

---

## How it works

### Python version

**Variables.** A variable called `score` starts at `0` and stores the points. Another variable, `answer`, holds what the user typed.

**If-else logic.** Each question follows the same pattern:

```python
answer = input("Q1: What is the capital of France? ").strip().lower()
if answer == "paris":
    print("Correct! +1 point")
    score = score + 1
else:
    print("Wrong! The correct answer is Paris.")
```

- `input()` reads the user's answer.
- `.strip()` removes extra spaces and `.lower()` makes the check case-insensitive, so `Paris`, `PARIS` and ` paris ` all count as correct.
- `if` / `else` decides whether to add a point.

**Final message.** An `if` / `elif` / `else` chain prints a message based on the final score:

| Score | Message |
|---|---|
| 3 | Perfect score! Well done! |
| 2 | Great job! Almost perfect. |
| 1 | Good try! Keep practising. |
| 0 | Better luck next time! |

Question 3 accepts both `7` and `seven`, using `or` to combine two conditions.

### Web version

The web version works the same way, with buttons instead of typed answers.

| Part | Purpose |
|---|---|
| `questions` array | Stores each question, its four options and the index of the correct option. |
| `index` and `score` | Variables tracking the current question and the points so far. |
| `showQuestion()` | Displays the current question and builds the answer buttons. |
| `choose(i)` | The if-else check. A correct choice adds 1 to `score`, a wrong choice highlights the right answer. |
| `showResult()` | Shows the final score and a message using the same if / else-if chain as the Python version. |

Other features: a progress bar, a live score counter, a Play again button, keyboard-friendly buttons, and light and dark themes that follow the system setting.

---

## Possible improvements

- Add more questions and pick 3 at random each game.
- Store questions in a list or dictionary and loop over them instead of repeating code.
- Add a timer for each question.
- Add difficulty levels or categories.
- Keep a high score using `localStorage` in the web version.

---

## Author

Created as part of the **Decodelabs** internship, Project 4.
