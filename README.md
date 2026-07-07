[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ri7sOp4m)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=24217412)
# Mini-Project - Build Your Own Game!

## For Students

### The Project
Design and build your own game in Python. It can be a terminal game (typed answers) or a turtle game (keys and mouse clicks). There are only two requirements:

1. **Your game must use user input** — mouse clicks, key strokes, typed answers, etc.
2. **Your game must keep track of and display a score.**

Everything you've learned in Modules 1-6 is fair game: variables, `input()`, `if`/`elif`/`else`, `while` loops, `for` loops, lists, `random`, and turtle graphics. Open `mini_project.py` for game ideas, helpful code snippets, and optional level-up ideas.

### Getting Started
1. Accept the assignment invite link provided by your instructor
2. Once your repo is created, click the green **Code** button and select **Open with Codespaces**
3. Open `mini_project.py` and start building

### Playing a Turtle Game in Codespaces
1. Run your game: `python mini_project.py`
2. Open the **PORTS** tab, click the globe icon on port **6080** ("Turtle Desktop")
3. Click **Connect**, password: **`vscode`**
4. Click inside the turtle window once so it hears your keyboard!

### Working as a Team 🤝
This is a group project: your whole team shares ONE repo, but each of you works in your OWN codespace. Think of your codespace as your personal computer in the cloud. Your teammate cannot see your typing. Code only travels between you through git: **Commit**, then **Sync**.

**The golden rules:**
1. **Pull when you sit down.** Your codespace does not update itself. Before you write any code, click the **Source Control** icon, then the **...** menu, then **Pull**. Now you have your teammate's latest work.
2. **Commit small, sync often.** Finish a small piece, commit it, click **Sync Changes**. Do not sit on an hour of work while your teammate is pushing. Small commits = tiny, easy merges.
3. **If Sync complains, pull first.** If your push is rejected because your teammate pushed before you, that is normal, not broken. VS Code will offer to pull. Pull, then sync again.
4. **Divide the file.** You are both editing `mini_project.py`, so agree on who owns which part (for example: one of you writes the input handling, the other writes the scoring). Editing the same lines at the same time causes a merge conflict.

**If you see a merge conflict:** the file will show markers like `<<<<<<<`, `=======`, and `>>>>>>>` with both versions of the code. Don't panic and don't delete random lines. VS Code shows **Accept Current** / **Accept Incoming** / **Accept Both** buttons right above the conflict. Talk to your teammate, pick the right version, save, then commit.

**Want to code together in real time?** Use **Live Share** (already installed): one teammate clicks the Live Share icon in the left sidebar, starts a session, and shares the link. The other joins, and you both edit the same file live, with two cursors, like a shared doc. Great for pair programming: one drives, one navigates. No merge conflicts!

### Submitting
- Commit and push like always: **Source Control** icon, type a message, **Commit**, then **Sync Changes**
- The autograder checks that the two requirements are present in your code. **Whether your game works and is fun is graded by your instructor playing it** — so playtest it yourself first!
- You can push as many times as you like before the deadline

---

## For Instructors

### How This Repo Works
- `mini_project.py` — the student-facing template: the two requirements, game ideas for both terminal and turtle paths, code snippets, and optional stretch ideas
- `tests/test_mini_project.py` — autograder; see the note below
- `.github/workflows/grade.yml` — GitHub Action that runs on every push to `main` and posts results as a commit comment
- `.devcontainer/devcontainer.json` — Codespaces environment (Python 3.11, desktop-lite VNC on port 6080 for turtle games, AI features disabled)

### A Note on Grading an Open-Ended Game
A student game may block on input(), loop forever, or open a turtle window, so the
autograder **never runs it**. Like Module 5, it parses `mini_project.py` with `ast` and
verifies the requirements exist in the code: an input mechanism (`input()`, or turtle's
`onkey`/`onclick`/`listen`), a score variable (name containing "score" or "point"), code
that changes the score, code that displays it (`print`/`write`/`title` with the score
variable), and at least some game logic (`if`/`while`/`for`). This is a requirements
check only — **play each game** for the real grade. Have students demo on the projector;
it's the best part of the week.

### Setting Up GitHub Classroom
1. Go to [classroom.github.com](https://classroom.github.com) and create/open your classroom
2. Click **New assignment**, choose **Group assignment** (this cannot be changed after creation), set a max team size (2-3 recommended), and use this repo as the starter code
3. Decide team names ahead of time and tell each pair exactly what team to create or join (the team picker is a common source of confusion)
4. Set visibility to **Private**
5. Add an autograding test (**Run command**: `python tests/test_mini_project.py`) for the requirements check; combine with your play-test grade
6. Consider protecting `tests/` and `.github/` via **protected file paths**
7. Share the generated invite link with students
