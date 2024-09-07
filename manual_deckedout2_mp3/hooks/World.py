# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################



# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    leg = is_option_enabled(multiworld, player, "Legendary_Card_Locations")
    sixth = is_option_enabled(multiworld, player, "Sixth_Locations")
    # Use this hook to remove locations from the world
    locationNamesToRemove = [] # List of location names

    # Add your code here to calculate which locations to remove

    for location in world.location_table:
        if "Legendary Card Locations" in location.get("category", []) and not leg:
            locationNamesToRemove.append(location["name"])
        elif "6th Locations" in location.get("category", []) and not sixth:
            locationNamesToRemove.append(location["name"])

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)
    if hasattr(multiworld, "clear_location_cache"):
        multiworld.clear_location_cache()

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    tactical_approach = get_option_value(multiworld, player, "Tactical_Approach_Count")
    pork_chop_power = get_option_value(multiworld, player, "Pork_Chop_Power_Count")
    dungeon_lackey = get_option_value(multiworld, player, "Dungeon_Lackey_Count")
    pay_to_win = get_option_value(multiworld, player, "Pay_To_Win_Count")
    tailor_for_success = get_option_value(multiworld, player, "Tailor_For_Success_Count")
    last_stand = get_option_value(multiworld, player, "Last_Stand_Count")
    revelation = get_option_value(multiworld, player, "Revelation_Count")
    aquata_breather = get_option_value(multiworld, player, "Aquata_Breather_Count")
    for_the_worthy = get_option_value(multiworld, player, "For_The_Worthy_Count")
    eureka = get_option_value(multiworld, player, "Eureka_Count")
    caves_of_carnage_key = get_option_value(multiworld, player, "Caves_Of_Carnage_Key_Count")
    black_mines_key = get_option_value(multiworld, player, "Black_Mines_Key_Count")
    flooded_depths_key = get_option_value(multiworld, player, "Flooded_Depths_Key_Count")
    burning_dark_key = get_option_value(multiworld, player, "Burning_Dark_Key_Count")
    # Use this hook to remove items from the item pool
    itemNamesToRemove = [] # List of item names

    for i in range(30-tactical_approach):
        itemNamesToRemove.append("Tactical Approach")
    for i in range(30-pork_chop_power):
        itemNamesToRemove.append("Pork Chop Power")
    for i in range(30-dungeon_lackey):
        itemNamesToRemove.append("Dungeon Lackey")
    for i in range(30-pay_to_win):
        itemNamesToRemove.append("Pay to Win")
    for i in range(16-tailor_for_success):
        itemNamesToRemove.append("Tailor for Success")
    for i in range(16-last_stand):
        itemNamesToRemove.append("Last Stand")
    for i in range(12-revelation):
        itemNamesToRemove.append("Revelation")
    for i in range(12-aquata_breather):
        itemNamesToRemove.append("Aquata Breather")
    for i in range(8-for_the_worthy):
        itemNamesToRemove.append("For the Worthy")
    for i in range(4-eureka):
        itemNamesToRemove.append("Eureka")
    for i in range(18-caves_of_carnage_key):
        itemNamesToRemove.append("The Caves of Carnage Key")
    for i in range(12-black_mines_key):
        itemNamesToRemove.append("The Black Mines Key")
    for i in range(12-flooded_depths_key):
        itemNamesToRemove.append("The Flooded Depths Key")
    for i in range(12-burning_dark_key):
        itemNamesToRemove.append("The Burning Dark Key")
    # Add your code here to calculate which items to remove.
    #
    # Because multiple copies of an item can exist, you need to add an item name
    # to the list multiple times if you want to remove multiple copies of it.

    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        item_pool.remove(item)

    return item_pool

    # Some other useful hook options:

    ## Place an item at a specific location
    # location = next(l for l in multiworld.get_unfilled_locations(player=player) if l.name == "Location Name")
    # item_to_place = next(i for i in item_pool if i.name == "Item Name")
    # location.place_locked_item(item_to_place)
    # item_pool.remove(item_to_place)

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location

    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True

    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int) -> list:
    pass

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass
