from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

def tntLake(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it down and back up from the TNT Lake?"""
    return (state.has("Ambrosia", player) and state.has_group("Card", player, 3)) or state.has("Second Wind", player)

def cryptKeyPlatform(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player jump onto the key platform in the crypt?"""
    return state.has("Bounding Strides", player) or (state.has("Boots of Swiftness", player) and state.has_group("Card", player, 3))

def cardCount(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How many cards does the player have?"""
    if state.count_group("Card", player) < 40:
        return state.count_group("Card", player)
    return 40

def rarity(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How rare are the player's cards?"""
    return state.count_group("Uncommon", player)/2 + state.count_group("Rare", player) + state.count("Legendary", player)*2

def enoughRarity(world: World, multiworld: MultiWorld, state: CollectionState, player: int, rarity: int):
    """Are the player's cards rare enough??"""
    if rarity(state) >= rarity:
        return True
    return False

def clankBlock(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How much clank can the player block?"""
    clankBlock = state.count_group("Clank Block", player)/2 + state.count("Evasion", player)/2 + state.count("Eerie Silence", player) + state.count("Enlightenment", player)*3/2 + state.count("Glorious Moment", player)*3/2
    if state.has("Silent Runner", player):
        clankBlock += (state.count_group("Speed", player)/2 + state.count("Sprint", player)/2)
    if clankBlock > 5:
        clankBlock += state.count_group("Fuzzy Bunny Slippers", player)*2
    return clankBlock

def enoughClankBlock(world: World, multiworld: MultiWorld, state: CollectionState, player: int, clank: int):
    """Can the player block enough clank?"""
    if clankBlock(state) >= clank:
        return True
    return False

def hazardBlock(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How much hazard can the player block?"""
    hazardBlock = state.count_group("Hazard Block", player)/2 + state.count("Tread Lightly", player)/2 + state.count("Dungeon Repairs", player) + state.count("Bounding Strides", player) + state.count("Boots of Swiftness", player)*2
    return hazardBlock

def enoughHazardBlock(world: World, multiworld: MultiWorld, state: CollectionState, player: int, hazard: int):
    """Can the player block enough hazard?"""
    if hazardBlock(state) >= hazard:
        return True
    return False

def treasure(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How much treasure can the player acquire?"""
    treasure = state.count_group("Treasure", player)/2 + state.count("Loot and Scoot", player)*2/3 + state.count("Nimble Looting", player) + state.count("Smash & Grab", player) + state.count("Adrenaline Rush", player) + state.count("Swagger", player)
    if state.has("Cash Cow", player):
        treasure += cardCount(state)/10
    return treasure

def enoughTreasure(world: World, multiworld: MultiWorld, state: CollectionState, player: int, crowns: int):
    """Can the player get enough treasure?"""
    if treasure(state) >= crowns:
        return True
    return False

def embers(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How many embers can the player acquire?"""
    embers = state.count_group("Frost Ember", player)/2 + state.count("Frost Focus", player)/2 + state.count("Reckless Charge", player)/2 + state.count("Swagger", player) + state.count("Chill Step", player)*state.count("Sneak", player)/8
    if state.has("Avalanche", player):
        embers += cardCount(state)/10
    if embers > 3:
        embers += state.count("Cold Snap", player)
    return embers

def enoughEmbers(world: World, multiworld: MultiWorld, state: CollectionState, player: int, frostEmbers: int):
    """Can the player get enough embers?"""
    if embers(state) >= frostEmbers:
        return True
    return False

def levelTwoAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player enter level 2 and escape?"""
    return enoughClankBlock(state,3) and enoughHazardBlock(state,2) and (enoughTreasure(state,1.5) or cryptKeyPlatform(state) or tntLake(state)) and cardCount(state,12)

def backLevelTwoAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player enter the back of level 2 and escape?"""
    return enoughClankBlock(state,3.5) and enoughHazardBlock(state,2.5) and (enoughTreasure(state,1.5) or cryptKeyPlatform(state) or tntLake(state)) and enoughRarity(2, state) and cardCount(state,19)

def levelThreeAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player enter level 3 and escape?"""
    return enoughClankBlock(state,4) and enoughHazardBlock(state,3) and enoughTreasure(state,4) and enoughRarity(5, state) and cardCount(state,19)

def bottomBlackMinesAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to the bottom of the black mines and escape?"""
    return enoughClankBlock(state,4.5) and enoughHazardBlock(state,3.5) and enoughTreasure(state,4) and enoughRarity(5.5, state) and cardCount(state,26)

def backFloodedDepthsAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to the back of the flooded depths and escape?"""
    return enoughClankBlock(state,5.5) and enoughHazardBlock(state,4.5) and enoughTreasure(state,6) and enoughRarity(5.5, state) and cardCount(state,31)

def levelFourAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to level 4 and escape?"""
    return enoughClankBlock(state,6) and enoughHazardBlock(state,5) and enoughTreasure(state,8) and enoughRarity(7.5, state) and (state.has("Bounding Strides", player, 3) or (state.has("Bounding Strides", player) and state.has("Boots of Swiftness", player))) and state.has_group("Speed", player, 2) and cardCount(state,37) and state.has_group("Survival", player, 2)

def backLevelFourAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to the back of level 4 and escape?"""
    return enoughClankBlock(state,7) and enoughHazardBlock(state,6) and enoughTreasure(state,8) and enoughRarity(9.5, state) and (state.has("Bounding Strides", player, 3) or (state.has("Bounding Strides", player) and state.has("Boots of Swiftness", player))) and state.has_group("Speed", player, 4) and cardCount(state,37) and state.has_group("Survival", player, 2)

def gatewayAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to the gatway and escape?"""
    return enoughClankBlock(state,8) and enoughHazardBlock(state,7) and enoughTreasure(state,8) and enoughRarity(11.5, state) and (state.has("Bounding Strides", player, 3) or (state.has("Bounding Strides", player,2) and state.has("Boots of Swiftness", player))) and state.has_group("Speed", player, 6) and cardCount(state,37) and state.has_group("Survival", player, 2)

def emberCount(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How many embers can the player end the run with?"""
    ember = 0
    if gatewayAccess(state):
        ember = 60
    elif backLevelFourAccess(state):
        ember = 50
    elif levelFourAccess(state):
        ember = 45
    elif bottomBlackMinesAccess(state):
        ember = 40
    elif levelThreeAccess(state):
        ember = 30
    elif backLevelTwoAccess(state):
        ember = 20
    elif levelTwoAccess(state):
        ember = 13
    else:
        ember = 10
    if tntLake(state):
        ember += 3
    if backLevelTwoAccess(state) and enoughTreasure(state,5):
        ember += 5
    ember += embers(state)
    return ember

def endEmbers(world: World, multiworld: MultiWorld, state: CollectionState, player: int, frostEmbers: int):
    """Can the player get enough embers?"""
    if emberCount(state) >= frostEmbers:
        return True
    return False

def crownCount(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How many crowns can the player end the run with?"""
    crowns = 0
    if gatewayAccess(state):
        crowns = 15
    elif bottomBlackMinesAccess(state):
        crowns = 7
    elif levelThreeAccess(state):
        crowns = 5
    elif backLevelTwoAccess(state):
        crowns = 3
    elif levelTwoAccess(state):
        crowns = 2
    if tntLake(state):
        crowns += 3
    if backLevelTwoAccess(state) and enoughTreasure(state,5):
        crowns += 5
    crowns += treasure(state)
    return crowns

def endCrowns(world: World, multiworld: MultiWorld, state: CollectionState, player: int, crowns: int):
    """Can the player get enough crowns?"""
    if crownCount(state) >= crowns:
        return True
    return False

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(world: World, multiworld: MultiWorld, state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"
