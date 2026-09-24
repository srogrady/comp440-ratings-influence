# Ratings and social influence: writeup

Claude writes your answers into the slots below as you say them. You may ask it to change any of
your answers at any time, except the Part 0 predictions. Every `XXXX` in Parts 0 to 5 needs an
answer; the follow-up slots at the end are optional.

**Name:** Shaylee O'Grady
**Date:** 2026-09-24

## Part 0. Predictions

Answered before anything runs. Claude writes them in as you said them, and they stay as written.

**1. Once people can see the counts, which artist wins most often?** the one that has been downloaded the most by others.

**2. Does inequality rise or fall with social influence?** rise

**3. Does the best artist ever lose a world?** yes

**4. Can a recommender lower inequality without lowering fidelity to true taste?** No

## Part 1. Users on their own

Code: `part1_independent.py`. Figure: `figures/part1_strip.png`.

**What Gini and unpredictability each show, in your own words:** Gini is measuring inequality amoung artists whos the most popular in that world. (popular  = most downloads) Unpredictability shows that the artists popularity is dependent on it's world you can't compare if they arent in the same world

**What the figure shows, one sentence:** It shows that shares of the world depends a lot on the specific world they are in, but the overall true popularity will be high or low on a more general scale (between worlds and in each world specifically)

## Part 2. The recommender

Code: `recommender.py`, `part2_recommender.py`. Figure: `figures/part2_strip.png`.

**The capabilities and limitations of `top_five`, in your words:** top five can prioritize the most download artists and show those first, and also only pay attention to previously downloaded artists, and organize a list that gives opportunities to popular/downloaded artists. It can't show artists that arent downloaded at all

**What Claude corrected in your reading, in your words, or "nothing":** Claude corrected my statement that top five can't show artists without downloads, because it actually can but only very early on when less than five artists don't have downloads.

**What changed against Part 1, one sentence:** none of the true popularity diamonds are fully in their worlds of dots

## Part 3. Social influence

Code: `my_choice.py`, `hand_check.py`, `part3_influence.py`. Figures: `figures/part3_gini.png`,
`figures/part3_unpredictability.png`.

**Your rule in your words:** Placement of artists matters a lot, and downloads are influencial, but it  won't stop users from choosing more niche artists if they are going based on their own taste.

**Hand check, before the table: which artist your rule should favor, and by a little or a lot:** I'm going to go with justin bieber by a very small amount because I'm going off personal true taste more still

**Hand check: whether the table matched what you said:** It doesnt but I think i sort of expected that and I think my table is more correct!

**The shape you expect the two curves to have, as you told Claude before the run:** I think they will be a lot higher inequality at level one so higher gini different worlds would end up being more alike

**What you changed in your rule, at the hand check or after the run, or "nothing":** nothing

**What the two curves show against the paper's Figures 1 and 2, in one or two sentences:** both the papers figures and my curves positively grow with social influence (so gini increases as social influence increase on both and same with unpredictability)

**Revisited: which of your Part 0 predictions you would now change, and why:** I would change 1 because I think downloads are semi important but not the entire thing at all and that depends on what level of social influence we are looking at

## Part 4. Your recommender

Code: `my_recommender.py`, `part4_recommender.py`. Figure: `figures/part4_recommenders.png`.

**Your rule in words, before any code:** XXXX

**What you expect it to do to inequality, unpredictability and fidelity, as you told Claude before the run:** XXXX

**What it bought and what it cost, one sentence:** XXXX

## Part 5. Reflection

**Where this shows up in data you have already handled, or in an interface you use, one sentence:** XXXX

**A moment Claude was wrong or overconfident, or a judgment you kept for yourself, one sentence:** XXXX

## Follow-ups

Optional, and not graded. Nothing under this heading is ever counted as missing: leave a slot as
`XXXX` if you did not do that follow-up.

**What is shown (`followup_shown.py`): which market moved success further from quality:** XXXX

**One assumption (`followup_assumption.py`): the assumption you changed:** XXXX

**One assumption: whether the Part 3 conclusion survived:** XXXX

**Anything else you tried:** XXXX

**Anything else: what it showed:** XXXX
