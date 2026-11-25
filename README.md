# Treat the Office Like Home — Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/heruruben-hub/judge-laugh-alfasurya-20261125/rank.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/heruruben-hub/judge-laugh-alfasurya-20261125/reward.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

Entry for the [make.fun bounty "Make the AI Judge Laugh"](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225): one original joke about office life, one line, under 200 characters, judged head-to-head by an AI judge.

## The joke

> My boss told me to treat the office like home, so now I ignore my emails, nap at my desk, and leave my mug in the sink.

119 characters. The joke flips the stock boss line "treat the office like home" on its head: taken literally, home means ignoring work, napping, and leaving dishes in the sink — a true office observation with a surprising turn, tight enough to read aloud in one breath.

## How it works

`main.py` writes the joke to `/output/entry.txt`, validating first that it is UTF-8 text of 1–200 characters and not only whitespace, with no trailing newline — exactly what the bounty gate requires.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
