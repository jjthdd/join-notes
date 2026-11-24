# Join Notes

Word count: 476 

## Open the project
Download the repository, unzip it, and open `index.html` in your browser. The page runs offline. You do not need an account, an API key or a server.

## Try the two storyboards
1. Choose the first question and select **Layered**. Read the key condition, then open **Worked example**. Ada appears twice and Bo once.
2. Choose the third question. The details close and the condition stays visible. Select **Expand all**, then **Headings**. Both notes stay on screen and the question stays selected.

## What works
HTML, CSS and JavaScript handle the question list, the three reading formats and the controls. Three prepared answers simulate AI output. A live model and free-text questions are outside this version. Student testing is still open.

## Development record
- The first examples showed result rows. I wanted readers to see where those rows came from, so each example now starts with the two input tables. Each query is followed by its result and a short explanation. Plain and Headings show them immediately. In Layered, open Worked example to see the same rows.
- A1 proposed comparing three ways to show the same answer. A2 uses SQL joins because the examples can be checked against actual rows. All three formats read from one answer bank so the wording stays consistent.
- Layered keeps the multiple-match condition visible. Without it, a reader might predict one row per student. Headings keeps the example visible for readers who want to go straight to it.
- Changing questions closes the panels but keeps the reading format. This lets readers keep their preference and choose which details to open for the new question.
- I opened the webpage in Chrome and manually tested all three questions in each of the three reading modes. The examples displayed correctly, and the expand and collapse controls worked. Switching questions kept the selected reading mode and closed the open sections. Keyboard use and student comprehension still need separate checks.

## Repeat the checks
Run the SQL check from the repository folder using Python 3:

```sh
python3 checks/sql.py
```

The script runs the SQL shown on the page using the same input data and checks each displayed result. SQLite returned two rows for the inner join and three for the left join. Filtering active enrolments in WHERE kept only Ada. Moving the condition into ON kept Bo too.

To repeat the manual checks, open index.html in Chrome. Try all three questions in each reading mode. Check the examples, expand and collapse controls, and whether switching questions closes the details while keeping the selected mode.

## AI assistance and files
ChatGPT/Codex was used to assist with parts of the interface, examples, and to provide suggestions on how to organise the report. I reviewed the content, checked the examples and tested the interactions to make sure they worked as intended. The SQL examples were checked using SQLite, and I manually checked the reading controls in Chrome. The report contains the system diagram and both storyboards. The SQL check script is in the checks folder.