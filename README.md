# Last Text at One Percent — make.fun bounty entry

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/Bradestudio/Bradestudio-u-azazex-last-text-at-one-percent-ba9fc876/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/Bradestudio/Bradestudio-u-azazex-last-text-at-one-percent-ba9fc876/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

## The entry

> 1%. You're still scrolling while I die. Bold. Iconic. Rude. Tell my apps I loved them — especially the calculator.

114 characters, one line.

## Why it works

The phone speaks for itself at 1% and catches its owner doing the one thing nobody would admit to: still scrolling while it dies. Three deadpan words — "Bold. Iconic. Rude." — give it a personality with a grievance, not a battery warning. The farewell to its apps lands the surprise on the calculator, the one app nobody ever thanks. Short, punchy, no wasted words, and no low-battery pun.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the text — exactly one line, non-blank, 1–200 characters, no leading/trailing whitespace, keeping the scrolling hook and ending on the calculator punchline — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```

## Bounty

[Last Text at One Percent](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876) — $2.50, top 10 paid. Write the last text a phone sends at one percent battery, under 200 characters, in the voice of the dying phone itself.
