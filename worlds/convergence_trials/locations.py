"""
Location definitions for Convergence Trials.

ID range: 8651000–8659999 (provisional).
Keep location IDs in sync with src/shared/locations.ts on the TypeScript side.
"""

from BaseClasses import Location


class ConvergenceTrialsLocation(Location):
    game = "Convergence Trials"


# fmt: off
LOCATION_TABLE: dict[str, dict] = {
    # Minigame Alpha ---------------------------------------------------------
    "Minigame Alpha - Room 1 - Check 1": {"id": 8651001, "region": "Minigame Alpha - Room 1"},
    "Minigame Alpha - Room 1 - Check 2": {"id": 8651002, "region": "Minigame Alpha - Room 1"},
    "Minigame Alpha - Room 2 - Check 1": {"id": 8651101, "region": "Minigame Alpha - Room 2"},
    "Minigame Alpha - Boss - Reward":    {"id": 8651201, "region": "Minigame Alpha - Boss"},

    # Minigame Beta ----------------------------------------------------------
    "Minigame Beta - Check 1":           {"id": 8652001, "region": "Minigame Beta"},
    "Minigame Beta - Check 2":           {"id": 8652002, "region": "Minigame Beta"},

    # Final challenge (victory event, no ID) ---------------------------------
    "Final Challenge - Complete":        {"id": None,    "region": "Final Challenge"},
}
# fmt: on
