"""
Region graph for Convergence Trials.

Mirrors the GameRegion definitions on the TypeScript side — keep them in sync.
Each entry may carry:
  name         – must match the TypeScript region name exactly
  parent       – parent region for sub-regions (default: "Menu")
  unlock_item  – item name that gates the entrance from the parent
"""

REGIONS: list[dict] = [
    # Top-level regions ------------------------------------------------------
    {"name": "Menu"},
    {"name": "Minigame Alpha"},
    {"name": "Minigame Beta",   "unlock_item": "Minigame Beta Unlock"},
    {"name": "Final Challenge", "unlock_item": "Final Challenge Access"},

    # Sub-regions within Minigame Alpha --------------------------------------
    {"name": "Minigame Alpha - Room 1", "parent": "Minigame Alpha"},
    {"name": "Minigame Alpha - Room 2", "parent": "Minigame Alpha", "unlock_item": "Alpha Room 2 Key"},
    {"name": "Minigame Alpha - Boss",   "parent": "Minigame Alpha", "unlock_item": "Alpha Boss Key"},
]
