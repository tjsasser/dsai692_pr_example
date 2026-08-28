# Team Toolbox

A tiny command-line toolbox. Each teammate contributes one tool.

```bash
python toolbox.py shout hello world
# HELLO WORLD!
```

## Tools

| Tool | What it does | Author |
| --- | --- | --- |
| shout | upper-cases the text and adds `!` | dianewoodbridge |
| reverse | reverses the text |  |
| wordcount | counts the words |  |
| initials | returns the initials | |

## How to contribute

1. Clone this repo (ask the owner to add you as a collaborator first).
2. Create a branch: `git switch -c feature/<your-tool>`
3. Add `tools/<your_tool>.py`.
4. Import it and register it in `toolbox.py`.
5. Add one row at the **bottom** of the Tools table above.
6. Add `notes/<your-github-username>.md`.
7. Push your branch (`git push origin feature/<your-tool>`) and open a pull request
   against `main`. Never commit directly to `main`.
