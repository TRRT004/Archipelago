"""
Convergence Trials – Archipelago world definition.

Item/location IDs here must stay in sync with the TypeScript constants in
src/shared/items.ts and src/shared/locations.ts.
"""

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import World, WebWorld

from .items import ITEM_TABLE, ConvergenceTrialsItem
from .locations import LOCATION_TABLE, ConvergenceTrialsLocation
from .regions import REGIONS


class ConvergenceTrialsWebWorld(WebWorld):
    theme = "ocean"
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide for setting up Convergence Trials to be played in Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["TRRT004"],
        )
    ]


class ConvergenceTrialsWorld(World):
    """
    Convergence Trials is a modular minigame suite built for the Archipelago
    Multiworld Randomizer. Complete minigames, collect items, and unlock new
    challenges across a shared multiworld.
    """

    game = "Convergence Trials"
    web = ConvergenceTrialsWebWorld()

    item_name_to_id = {name: data["id"] for name, data in ITEM_TABLE.items()}
    location_name_to_id = {name: data["id"] for name, data in LOCATION_TABLE.items()}

    def create_item(self, name: str) -> ConvergenceTrialsItem:
        data = ITEM_TABLE[name]
        return ConvergenceTrialsItem(name, data["classification"], data["id"], self.player)

    def create_items(self) -> None:
        for name, data in ITEM_TABLE.items():
            self.multiworld.itempool.append(self.create_item(name))

    def create_regions(self) -> None:
        region_map: dict[str, Region] = {}

        for region_def in REGIONS:
            region = Region(region_def["name"], self.player, self.multiworld)
            region_map[region_def["name"]] = region
            self.multiworld.regions.append(region)

        # Wire locations into their regions.
        for loc_name, loc_data in LOCATION_TABLE.items():
            region = region_map[loc_data["region"]]
            location = ConvergenceTrialsLocation(self.player, loc_name, loc_data["id"], region)
            region.locations.append(location)

        # Connect sub-regions to their parent via Entrance (rules added in set_rules).
        for region_def in REGIONS:
            if region_def["name"] == "Menu":
                continue
            parent_name = region_def.get("parent", "Menu")
            parent = region_map[parent_name]
            entrance = parent.create_exit(f"{parent_name} -> {region_def['name']}")
            entrance.connect(region_map[region_def["name"]])

    def set_rules(self) -> None:
        from worlds.generic.Rules import set_rule

        for region_def in REGIONS:
            if not region_def.get("unlock_item"):
                continue
            entrance_name = f"{region_def.get('parent', 'Menu')} -> {region_def['name']}"
            entrance = self.multiworld.get_entrance(entrance_name, self.player)
            item_name = region_def["unlock_item"]
            set_rule(entrance, lambda state, itm=item_name: state.has(itm, self.player))

    def generate_basic(self) -> None:
        goal = self.multiworld.get_location("Final Challenge - Complete", self.player)
        goal.place_locked_item(
            ConvergenceTrialsItem("Victory", ItemClassification.progression, None, self.player)
        )
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
