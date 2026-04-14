"""
Item definitions for Convergence Trials.

ID range: 8650000–8650999 (provisional — update once registered with Archipelago).
Keep item IDs in sync with src/shared/items.ts on the TypeScript side.
"""

from BaseClasses import Item, ItemClassification


class ConvergenceTrialsItem(Item):
    game = "Convergence Trials"


# fmt: off
ITEM_TABLE: dict[str, dict] = {
    # Minigame unlocks -------------------------------------------------------
    "Minigame Beta Unlock":   {"id": 8650001, "classification": ItemClassification.progression},
    "Final Challenge Access": {"id": 8650099, "classification": ItemClassification.progression},

    # Sub-region unlocks (Minigame Alpha) ------------------------------------
    "Alpha Room 2 Key":       {"id": 8650201, "classification": ItemClassification.progression},
    "Alpha Boss Key":         {"id": 8650202, "classification": ItemClassification.progression},

    # Filler -----------------------------------------------------------------
    "Filler":                 {"id": 8650900, "classification": ItemClassification.filler},
}
# fmt: on
