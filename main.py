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

DECISION RECORD — REVISION PASS (kit check asked for a genuine revision;
three alternative revisions of F weighed):

R1. "I taught my cat to fetch. She brings the toy, drops it out of reach,
    and waits for the tip." (91 chars) — REJECTED.
    - For: ten characters tighter; same skeleton, same punch word.
    - Against: cutting "just" and "back" guts the joke's core image — the
      toy dropped JUST out of reach is the tease, and "brings the toy back"
      is the return trip the whole gag depends on. Shorter but weaker.

R2. "I taught my cat to fetch. She brings the toy back, drops it just out
    of reach, and holds out a paw for the tip." (111 chars) — REJECTED.
    - For: "holds out a paw" is a vivid, very cat-specific gesture; a second
      visual beat before the punch.
    - Against: ten characters longer and the extra beat delays the punch —
      the line's snap is its virtue, and "tip" now arrives after a longer
      clause. The paw image is charming but it is a detour, not a payoff.

R3. "I taught my cat to fetch. She brings the toy back, drops it just out
    of reach, and expects a tip." (97 chars) — CHOSEN.
    - One word changes, and it is the right word: "expects" carries the
      cat's entitlement in a single verb where "waits for" only described
      patience. A cat does not wait for a tip — she expects one, as a matter
      of course, and the demand is funnier than the waiting. The punch still
      lands on "tip" as the last word, the teasing "just out of reach"
      survives intact, and the line gets four characters tighter. Same setup,
      same turn, sharper verb, better joke.

FINAL ENTRY (97 characters):
"I taught my cat to fetch. She brings the toy back, drops it just out of
reach, and expects a tip."

Hand count, two ways: word by word — "I" 1, " taught" 7 (8), " my" 3 (11),
" cat" 4 (15), " to" 3 (18), " fetch." 7 (25), " She" 4 (29), " brings" 7
(36), " the" 4 (40), " toy" 4 (44), " back," 6 (50), " drops" 6 (56),
" it" 3 (59), " just" 5 (64), " out" 4 (68), " of" 3 (71), " reach," 7
(78), " and" 4 (82), " expects" 8 (90), " a" 2 (92), " tip." 5 (97).
Cross-check: 77 non-space characters + 20 spaces = 97.
"""

import os

ENTRY = (
    "I taught my cat to fetch. She brings the toy back, "
    "drops it just out of reach, and expects a tip."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
