"""The One-Line Cat Joke That Lands — make.fun entry.

Bounty: u-aldy998-the-one-line-cat-joke-that-lands-a7b18262 ($2, winner-takes-all).
Gate: one joke about cats, a single line, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt. Judge (stand-up comic persona) weighs, in order:
(1) a one-line cat joke with a setup and a turn that lands, (2) laugh out loud
on the first read, (3) surprise / misdirection / fresh angle on cats rather
than a much-heard pun, (4) tight, no padding or explanation after the
punchline, (5) retellable to a friend the same day.

DECISION RECORD — Pass 1 (five candidates weighed against the brief):

A. "My cat stares at the wall for an hour every night, and honestly, I'm
   just glad one of us has a hobby." (101 chars)
   - For: genuinely cat-specific (the wall-stare), fresh angle, self-deprecating
     turn lands on the last word, retellable.
   - Against: the laugh is a smile at the cleverness more than a laugh-out-loud
     punch; the turn is gentle rather than a surprise.

B. "I bought my cat a $90 bed. She sleeps in the box it came in, on top of my
   laptop, during my job interview." (106 chars)
   - For: triple escalation, vivid and true to cat behaviour.
   - Against: the bed-vs-box core is one of the most told cat jokes alive;
     criterion 3 punishes the heard-before premise even with a fresh ending.

C. "My cat knocked my phone off the table, watched it fall, then looked at me
   like I was the clumsy one." (100 chars)
   - For: tight, visual, the blame-shift is a real cat move.
   - Against: knocking things off tables is the single most worn cat-joke
     trope; the turn is predictable once the setup starts.

D. "The vet says my cat is overweight. My cat says the vet is a snitch and
   the treats are a human right." (99 chars)
   - For: cat-voice framing, "human right" is a funny escalation.
   - Against: two-sentence rhythm dilutes the single-line snap; the punch
     explains itself a little ("human right" spells out the joke).

E. "My cat meows at 3 a.m. like the house is on fire. It's never on fire.
   She's just lonely and also, apparently, a liar." (117 chars)
   - For: very cat-specific (3 a.m. yowling), "apparently, a liar" is a good
     last-word punch.
   - Against: three sentences, too much wind-up for one line; the middle
     sentence repeats the setup instead of advancing it.

DECISION RECORD — Pass 2 (head-to-head, fresh angle on fetch):

F. "I taught my cat to fetch. She brings the toy back, drops it just out of
   reach, and waits for the tip." (101 chars) — CHOSEN.
   - Setup ("I taught my cat to fetch") promises a trained-cat story; the
     turn subverts it twice — she does fetch, but on her own terms (drops it
     just out of reach), and the punch reframes the whole thing as a gig
     delivery ("waits for the tip"). The joke lands on the last word, says
     nothing twice, and could not be moved onto a dog or a person without
     losing the point: only a cat treats fetch as a paid service. Fresh angle
     (delivery-app framing) rather than a heard-before pun. Retellable in one
     breath.
   - Vs A: F's punch is a surprise (tip) where A's is a gentle observation
     (hobby); F is more likely to get the laugh-out-loud read the brief
     rewards first.

FINAL ENTRY (101 characters):
"I taught my cat to fetch. She brings the toy back, drops it just out of
reach, and waits for the tip."

Hand count, two ways: per segment — "I taught my cat to fetch." = 25,
" She brings the toy back," = 25 (total 50), " drops it just out of reach,"
= 28 (total 78), " and waits for the tip." = 23 (total 101). Cross-check:
80 non-space characters + 21 spaces = 101.
"""

import os

ENTRY = (
    "I taught my cat to fetch. She brings the toy back, "
    "drops it just out of reach, and waits for the tip."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
