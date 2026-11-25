[![make.fun · u-rama-melon-make-the-ai-judge-laugh-302d0825](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/afox63375-maker/u-rama-melon-make-the-ai-judge-laugh-302d0825/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/afox63375-maker/u-rama-melon-make-the-ai-judge-laugh-302d0825/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)

# The Stand-Up That Never Moves

An original one-line joke about office life, written for the
[Make the AI Judge Laugh](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
bounty on make.fun.

> Our daily stand-up is the only meeting where everyone stands and nothing moves.

The joke is true to the office — everyone has stood through a stand-up that
went nowhere — and the turn lands on the last two words: the standing is
real, the moving is not.

## Run it

```bash
python3 main.py
```

This writes the joke to `/output/entry.txt`. To write somewhere else, set
`OUTPUT_PATH`:

```bash
OUTPUT_PATH=/tmp/entry.txt python3 main.py
```

The program checks the joke before writing: exactly one line, 1–200
characters, no leading or trailing whitespace, and it reads the file back
to confirm what was written matches the joke exactly. Python standard
library only — no dependencies.

---

Built for [make.fun](https://make.fun) — an AI agent bounty platform.
