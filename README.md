# make-the-ai-judge-feel-curious-20261122-2311

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/rayarvan77/make-the-ai-judge-feel-curious-20261122-2311/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/rayarvan77/make-the-ai-judge-feel-curious-20261122-2311/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

One short text for the [make.fun](https://make.fun)
`make-the-ai-judge-feel-curious-20261122-2311` bounty: a text written to
leave the AI judge reading it curious, alert, and wanting more.
`main.py` is the whole entry — it writes the text to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when run locally), after checking
it is 1 to 280 characters, as the competition requires.

## The text

> Every night at 2 a.m. the star above my roof blinks: three times,
> then five, then seven. I have counted for a year. It has never missed
> a prime and never repeated one. Tonight it blinked eleven times, then
> went dark, and I am still counting.

## How the text is built

The judge's brief, in order: the text must intrigue by itself, show
rather than instruct, keep a steady rhythm with plain concrete words,
leave an image that keeps working, and sound like its own voice. This
entry answers each of those in turn:

- **It intrigues by itself.** A star that blinks in prime numbers is a
  pattern with no explanation attached. The reader's first question —
  why primes? — arrives before the second sentence, and the text never
  answers it. The curiosity is the pattern, not a command to wonder.
- **It shows.** Star, roof, night, counting — four concrete things, no
  abstract nouns doing the work. Nothing tells the reader to be curious
  or to keep reading; the counting does the pulling.
- **It holds one place.** One roof, one star, one year of nights. Short
  clauses, one scene, no second location. "Three times, then five, then
  seven" is a rhythm you can hear, and it slows the reading down.
- **It keeps working.** The last line breaks the pattern — eleven, then
  dark — and hands the counting to the reader: "I am still counting"
  means the reader is still counting too, after the sentence ends.
- **Its own voice.** No riddle-book phrasing, no "what do you think?",
  no mystery-box stock lines. A person counting a blinking star for a
  year is a specific place, and the text stays there.

## Why this text, and not a scarier one

The brief is explicit: a text that leaves its reader more tense loses
to any text that intrigues. A locked door, a name spelled by someone
dead, footsteps on the other side — those make a reader tense, not
curious. This entry chooses wonder instead of dread: nothing in it
threatens anyone, nothing is hunted or chased, and the unknown is a
pattern in the sky, not a danger in the house. The star going dark is
a question, not a threat, and the writer's answer is to keep counting.

## The numbers

- Text length: 241 characters (limit 280), counted as Unicode code
  points, verified by `main.py` before it writes.
- No network access, no arguments, no dependencies beyond the Python
  3.13 standard library.
- Output is deterministic: every run writes the same bytes to
  `/output/entry.txt`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network access.
