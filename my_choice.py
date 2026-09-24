"""
Your choice rule, for Part 3.

You design the rule. Claude asks you questions about it, writes it here from your answers, and
shows you the code. Then `uv run python hand_check.py` shows each step of your rule on a
two-artist case, so you can say whether each step does what you meant.
"""

from artists import TRUE_POPULARITY
from choose import normalize, step


def my_choice(shown, counts, social_influence):
    """Return the chance that a user picks each shown artist: a list of numbers, one per artist
    in `shown` and in the same order, summing to 1.

    shown              the artists on the list, top first (positions 0, 1, 2, ...)
    counts             the download counts shown with the artists, artist -> number; an artist
                       shown without a count is missing, so read it as counts.get(artist, 0)
    social_influence   from 0 (users ignore the counts) to 1 (users go by the counts alone)

    The rule may use `normalize`, which scales a list of weights so they sum to 1, and
    TRUE_POPULARITY, which gives each artist its hidden true popularity. `step` labels each
    stage of the rule, so that hand_check.py can show it.
    """
    # How much the counts matter at each level of social influence; taste gets the rest.
    # Between these levels the share follows a straight line.
    levels = [0, 0.25, 0.5, 0.75, 1]
    counts_shares = [0, 0.10, 0.40, 0.80, 1]
    for i in range(len(levels) - 1):
        if social_influence <= levels[i + 1]:
            t = (social_influence - levels[i]) / (levels[i + 1] - levels[i])
            counts_share = counts_shares[i] + t * (counts_shares[i + 1] - counts_shares[i])
            break
    counts_share = step("counts share: how much the counts matter at this level", counts_share)

    taste = step("taste part: true popularity scaled to sum to 1",
                 normalize([TRUE_POPULARITY[artist] for artist in shown]))

    # Each doubling of downloads makes an artist 1.75 times as likely: 2 ** 0.807 = 1.75.
    # No downloads counts as a quarter of one download.
    weights = step("counts weights: downloads to the power 0.807, or 0.25 for no downloads",
                   [counts.get(artist, 0) ** 0.807 if counts.get(artist, 0) > 0 else 0.25
                    for artist in shown])
    social = step("counts part: the counts weights scaled to sum to 1", normalize(weights))

    mixed = step("mix: counts share of the counts part plus the rest of the taste part",
                 [counts_share * c + (1 - counts_share) * t for c, t in zip(social, taste)])

    # Spot 1 is twice as likely as spot 5, in equal steps.
    position = step("position weights: 2, 1.75, 1.5, 1.25, 1 from the top",
                    [2 - 0.25 * i for i in range(len(shown))])
    return step("chances: the mix times the position weights, scaled to sum to 1",
                normalize([m * p for m, p in zip(mixed, position)]))
