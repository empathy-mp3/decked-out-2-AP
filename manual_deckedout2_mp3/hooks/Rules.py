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

def enoughCards(world: World, multiworld: MultiWorld, state: CollectionState, player: int, cards: int):
    """Does the player have enough cards?"""
    if cardCount(world, multiworld, state, player) >= cards:
        return True
    return False

def rarity(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How rare are the player's cards?"""
    return state.count_group("Uncommon Cards", player)/2 + (state.count_group("Rare Cards", player) - state.count("Eyes on the Prize", player)) + state.count_group("Legendary Cards", player)*2

def enoughRarity(world: World, multiworld: MultiWorld, state: CollectionState, player: int, rare: int):
    """Are the player's cards rare enough??"""
    if rarity(world, multiworld, state, player) >= rare:
        return True
    return False

def clankBlock(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How much clank can the player block?"""
    clankBlock = 0.5 + state.count_group("Clank Block", player)/2 + state.count("Evasion", player)/2 + state.count("Eerie Silence", player) + state.count("Enlightenment", player)*3/2 + state.count("Glorious Moment", player)*3/2
    if state.has("Silent Runner", player):
        clankBlock += (state.count_group("Speed", player)/2 + state.count("Sprint", player)/2)
    if clankBlock > 5:
        clankBlock += state.count("Fuzzy Bunny Slippers", player)*2
    if clankBlock >= 2 and state.has("Brilliance", player):
        clankBlock += 1
    return clankBlock

def enoughClankBlock(world: World, multiworld: MultiWorld, state: CollectionState, player: int, clank: int):
    """Can the player block enough clank?"""
    if clankBlock(world, multiworld, state, player) >= clank:
        return True
    return False

def hazardBlock(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How much hazard can the player block?"""
    hazardBlock = 0.5 + state.count_group("Hazard Block", player)/2 + state.count("Tread Lightly", player)/2 + state.count("Dungeon Repairs", player) + state.count("Bounding Strides", player) + state.count("Boots of Swiftness", player)*2
    if hazardBlock >= 2 and state.has("Brilliance", player):
        hazardBlock += 1
    return hazardBlock

def enoughHazardBlock(world: World, multiworld: MultiWorld, state: CollectionState, player: int, hazard: int):
    """Can the player block enough hazard?"""
    if hazardBlock(world, multiworld, state, player) >= hazard:
        return True
    return False

def treasure(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How much treasure can the player acquire?"""
    treasure = 0.5 + state.count_group("Treasure", player)/2 + state.count("Loot and Scoot", player)*2/3 + state.count("Nimble Looting", player) + state.count("Smash & Grab", player) + state.count("Adrenaline Rush", player) + state.count("Swagger", player)
    if state.has("Cash Cow", player):
        treasure += cardCount(world, multiworld, state, player)/10
    if treasure >= 2 and state.has("Brilliance", player):
        treasure += 1
    return treasure

def enoughTreasure(world: World, multiworld: MultiWorld, state: CollectionState, player: int, crowns: int):
    """Can the player get enough treasure?"""
    if treasure(world, multiworld, state, player) >= crowns:
        return True
    return False

def embers(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How many embers can the player acquire?"""
    embers = 0.5 + state.count_group("Frost Ember", player)/2 + state.count("Frost Focus", player)/2 + state.count("Reckless Charge", player) + state.count("Swagger", player) + state.count("Chill Step", player)*state.count("Sneak", player)/6 + state.count("Avalanche", player)*cardCount(world, multiworld, state, player)/10
    if embers > 3:
        embers += state.count("Cold Snap", player)
    if embers >= 2 and state.has("Brilliance", player):
        embers += 1
    return embers

def enoughEmbers(world: World, multiworld: MultiWorld, state: CollectionState, player: int, frostEmbers: int):
    """Can the player get enough embers?"""
    if embers(world, multiworld, state, player) >= frostEmbers:
        return True
    return False

def cardsOrClankHazard(world: World, multiworld: MultiWorld, state: CollectionState, player: int, cards: int, clank: int, hazard: int):
    """Can the player get enough cards? or enough clank and hazard block?"""
    if enoughCards(world, multiworld, state, player, cards) or (enoughClankBlock(world, multiworld, state, player, clank) and enoughHazardBlock(world, multiworld, state, player, hazard)):
        return True
    return False

def levelTwoAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player enter level 2 and escape?"""
    return enoughClankBlock(world, multiworld, state, player,3) and enoughHazardBlock(world, multiworld, state, player,2) and (enoughTreasure(world, multiworld, state, player,2) or cryptKeyPlatform(world, multiworld, state, player)) and cardsOrClankHazard(world, multiworld, state, player, 11, 4, 3)

def backLevelTwoAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player enter the back of level 2 and escape?"""
    return enoughClankBlock(world, multiworld, state, player,3) and enoughHazardBlock(world, multiworld, state, player,2) and (enoughTreasure(world, multiworld, state, player,2) or cryptKeyPlatform(world, multiworld, state, player)) and enoughRarity(world, multiworld, state, player,2) and cardsOrClankHazard(world, multiworld, state, player, 17, 4, 3)

def levelThreeAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player enter level 3 and escape?"""
    return enoughClankBlock(world, multiworld, state, player,4) and enoughHazardBlock(world, multiworld, state, player,3) and enoughTreasure(world, multiworld, state, player,4) and enoughRarity(world, multiworld, state, player,5) and enoughCards(world, multiworld, state, player,20)

def bottomBlackMinesAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to the bottom of the black mines and escape?"""
    return enoughClankBlock(world, multiworld, state, player,4) and enoughHazardBlock(world, multiworld, state, player,3) and enoughTreasure(world, multiworld, state, player,4) and enoughRarity(world, multiworld, state, player,5) and enoughCards(world, multiworld, state, player,26)

def backFloodedDepthsAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to the back of the flooded depths and escape?"""
    return enoughClankBlock(world, multiworld, state, player,5) and enoughHazardBlock(world, multiworld, state, player,4) and enoughTreasure(world, multiworld, state, player,4) and (enoughTreasure(world, multiworld, state, player,6) or state.has("Pirate's Booty", player) or state.has("Ambrosia", player) or state.has("Second Wind", player, 2)) and enoughRarity(world, multiworld, state, player,5) and enoughCards(world, multiworld, state, player,31)

def levelFourAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to level 4 and escape?"""
    return enoughClankBlock(world, multiworld, state, player,6) and enoughHazardBlock(world, multiworld, state, player,5) and enoughTreasure(world, multiworld, state, player,8) and enoughRarity(world, multiworld, state, player,7) and (state.has("Bounding Strides", player, 3) or (state.has("Bounding Strides", player) and state.has("Boots of Swiftness", player))) and state.has_group("Speed", player, 2) and enoughCards(world, multiworld, state, player,37) and state.has_group("Survival", player, 2)

def backLevelFourAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to the back of level 4 and escape?"""
    return enoughClankBlock(world, multiworld, state, player,7) and enoughHazardBlock(world, multiworld, state, player,6) and enoughTreasure(world, multiworld, state, player,8) and enoughRarity(world, multiworld, state, player,9) and (state.has("Bounding Strides", player, 3) or (state.has("Bounding Strides", player) and state.has("Boots of Swiftness", player))) and state.has_group("Speed", player, 4) and enoughCards(world, multiworld, state, player,37) and state.has_group("Survival", player, 2)

def gatewayAccess(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Can the player make it to the gatway and escape?"""
    return enoughClankBlock(world, multiworld, state, player,8) and enoughHazardBlock(world, multiworld, state, player,7) and enoughTreasure(world, multiworld, state, player,8) and enoughRarity(world, multiworld, state, player,11) and (state.has("Bounding Strides", player, 3) or (state.has("Bounding Strides", player,2) and state.has("Boots of Swiftness", player))) and state.has_group("Speed", player, 6) and enoughCards(world, multiworld, state, player,37) and state.has_group("Survival", player, 2)

def emberCount(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How many embers can the player end the run with?"""
    ember = 0
    if gatewayAccess(world, multiworld, state, player):
        ember = 55
    elif backLevelFourAccess(world, multiworld, state, player):
        ember = 45
    elif levelFourAccess(world, multiworld, state, player):
        ember = 40
    elif bottomBlackMinesAccess(world, multiworld, state, player):
        ember = 35
    elif levelThreeAccess(world, multiworld, state, player):
        ember = 30
    elif backLevelTwoAccess(world, multiworld, state, player):
        ember = 22
    elif levelTwoAccess(world, multiworld, state, player):
        ember = 17
    elif enoughCards(world, multiworld, state, player, 3):
        ember = 13
    else:
        ember = 10
    if enoughTreasure(world, multiworld, state, player, 8) and levelThreeAccess(world, multiworld, state, player):
        ember += 9
    elif enoughTreasure(world, multiworld, state, player, 4) and backLevelTwoAccess(world, multiworld, state, player):
        ember += 6
    elif enoughTreasure(world, multiworld, state, player, 2) or cryptKeyPlatform(world, multiworld, state, player):
        ember += 3
    if tntLake(world, multiworld, state, player):
        ember += 2
    if backLevelTwoAccess(world, multiworld, state, player) and enoughTreasure(world, multiworld, state, player,5): #rusty
        ember += 5
    ember += embers(world, multiworld, state, player)
    return ember

def endEmbers(world: World, multiworld: MultiWorld, state: CollectionState, player: int, frostEmbers: int):
    """Can the player get enough embers?"""
    if emberCount(world, multiworld, state, player) >= frostEmbers:
        return True
    return False

def crownCount(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """How many crowns can the player end the run with?"""
    crowns = 0
    if gatewayAccess(world, multiworld, state, player):
        crowns = 8
    if bottomBlackMinesAccess(world, multiworld, state, player):
        treasures = 16
    elif backLevelTwoAccess(world, multiworld, state, player):
        treasures = 9
    elif enoughCards(world, multiworld, state, player, 11):
        treasures = 6
    else:
        treasures = 4
    if tntLake(world, multiworld, state, player):
        treasures += 1
    if backLevelTwoAccess(world, multiworld, state, player) and enoughTreasure(world, multiworld, state, player,5): #rusty
        crowns += 4
    crowns += treasure(world, multiworld, state, player)*treasures/6
    return crowns

def endCrowns(world: World, multiworld: MultiWorld, state: CollectionState, player: int, crowns: int):
    """Can the player get enough crowns?"""
    if crownCount(world, multiworld, state, player) >= crowns:
        return True
    return False