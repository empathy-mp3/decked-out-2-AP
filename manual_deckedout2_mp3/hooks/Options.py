# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class FillerTrapPercent(Range):
    """What percentage of Moments of Clarity (filler) should be replaced by Stumbles (traps)?
    0 means no Stumbles, 100 means all Moments of Clarity are replaced with Stumbles."""
    range_end = 100

class Embers(DefaultOnToggle):
    """Should there be locations for having at least a specified amount of Embers in hand at the end of a run?
    Adds 80 Locations, for having 1 Ember in hand to having 80 Embers."""
    display_name = "Frost Ember Locations"

class Crowns(DefaultOnToggle):
    """Should there be locations for having at least a specified amount of Crowns and Coins in hand at the end of a run?
    Adds 80 Locations, for having 1 Coin in hand to having 20 Crowns."""
    display_name = "Coin & Crown Locations"

class DifficultyObjectives(DefaultOnToggle):
    """Should there be locations for obtaining an artifact and beating a run on each difficulty?
    Adds 10 Locations, 2 for each difficulty."""
    display_name = "Difficulty Objective Locations"

class FrozenCaverns(DefaultOnToggle):
    """Should there be locations for going to some places and doing tasks in the Frozen Caverns (Level 1)?
    Most of these are for getting berries from Berry Bushes. Adds 15 Locations."""
    display_name = "Frozen Caverns Locations"

class CavesOfCarnage(DefaultOnToggle):
    """Should there be locations for going to some places and doing tasks in the Caves of Carnage (Level 2)?
    Most of these are for getting berries from Berry Bushes. Adds 13 Locations."""
    display_name = "Frozen Caverns Locations"

class BlackMines(DefaultOnToggle):
    """Should there be locations for going to some places and doing tasks in The Black Mines (Level 3)?
    Most of these are for getting berries from Berry Bushes. Adds 10 Locations."""
    display_name = "Frozen Caverns Locations"

class FloodedDepths(DefaultOnToggle):
    """Should there be locations for going to some places and doing tasks in The Flooded Depths (Alternate Level 3)?
    No berries in this one, actually! Adds 7 Locations."""
    display_name = "Frozen Caverns Locations"

class BurningDark(DefaultOnToggle):
    """Should there be locations for going to some places and doing tasks in The Burning Dark (Level 4)?
    Most of these are for getting berries from Berry Bushes. Adds 13 Locations."""
    display_name = "Frozen Caverns Locations"

class Common(DefaultOnToggle):
    """Should there be locations for Common Card purchases in the Ember Shop? Adds 5 Locations."""
    display_name = "Common Card Locations"

class Uncommon(DefaultOnToggle):
    """Should there be locations for Uncommon Card purchases in the Ember Shop? Adds 15 Locations."""
    display_name = "Uncommon Card Locations"
    range_start = 0
    range_end = 6
    default = 0

class Rare(DefaultOnToggle):
    """Should there be locations for Rare Card purchases in the Ember Shop? Adds 13 Locations."""
    display_name = "Rare Card Locations"
    range_start = 0
    range_end = 6
    default = 0

class Legendary(Toggle):
    """Should there be locations for Legendary Card purchases in the Ember Shop?
    Be warned: these are extremely lengthy and annoying locations. Adds 7 Locations."""
    display_name = "Legendary Card Locations"

class Tome(DefaultOnToggle):
    """Should there be locations for Victory Tome purchases in the Ember Shop?
    Adds 3 Locations."""
    display_name = "Victory Tome Locations"

class CrownShop(DefaultOnToggle):
    """Should there be locations for purchases in the Crown Shop? Adds 10 Locations."""
    display_name = "Crown Shop Locations"

class TacticalApproachCount(Range):
    """Number of filler to be replaced by the Tactical Approach Card (a single-use crown shop card)."""
    display_name = "Tactical Approach Count"
    range_start = 0
    range_end = 30
    default = 10

class PorkChopPowerCount(Range):
    """Number of filler to be replaced by the Pork Chop Power Card (a single-use crown shop card)."""
    display_name = "Pork Chop Power Count"
    range_start = 0
    range_end = 30
    default = 10

class DungeonLackeyCount(Range):
    """Number of filler to be replaced by the Dungeon Lackey Card (a single-use crown shop card)."""
    display_name = "Dungeon Lackey Count"
    range_start = 0
    range_end = 30
    default = 10

class PayToWinCount(Range):
    """Number of filler to be replaced by the Pay To Win Card (a single-use crown shop card)."""
    display_name = "Pay to Win Count"
    range_start = 0
    range_end = 30
    default = 10

class TailorForSuccessCount(Range):
    """Number of filler to be replaced by the Tailor for Success Card (a single-use strong crown shop card)."""
    display_name = "Tailor for Success Count"
    range_start = 0
    range_end = 16
    default = 6

class LastStandCount(Range):
    """Number of filler to be replaced by the Last Stand Card (a single-use strong crown shop card)."""
    display_name = "Last Stand Count"
    range_start = 0
    range_end = 16
    default = 6

class RevelationCount(Range):
    """Number of filler to be replaced by the Revelation Card (a single-use uncommon card)."""
    display_name = "Revelation Count"
    range_start = 0
    range_end = 12
    default = 5

class AquataBreatherCount(Range):
    """Number of filler to be replaced by the Aquata Breather Card (a single-use rare card)."""
    display_name = "Aquata Breather Count"
    range_start = 0
    range_end = 12
    default = 5

class ForTheWorthyCount(Range):
    """Number of filler to be replaced by the For the Worthy Card (a single-use legendary card).
    It's not very useful, to be honest."""
    display_name = "For the Worthy Count"
    range_start = 0
    range_end = 8
    default = 0

class EurekaCount(Range):
    """Number of filler to be replaced by the Eureka Card (a single-use legendary card)."""
    display_name = "Eureka Count"
    range_start = 0
    range_end = 4
    default = 2

class CavesOfCarnageKeyCount(Range):
    """Number of filler to be replaced by The Caves of Carnage Key (key to the second area)."""
    display_name = "The Caves of Carnage Key Count"
    range_start = 0
    range_end = 18
    default = 7

class BlackMinesKeyCount(Range):
    """Number of filler to be replaced by The Black Mines Key (key to the third area)."""
    display_name = "The Black Mines Key Count"
    range_start = 0
    range_end = 12
    default = 5

class FloodedDepthsKeyCount(Range):
    """Number of filler to be replaced by The Flooded Depths Key (key to the alt third area)."""
    display_name = "The Flooded Depths Key Count"
    range_start = 0
    range_end = 12
    default = 5

class BurningDarkKeyCount(Range):
    """Number of filler to be replaced by The Burning Dark Key (key to the fourth area)."""
    display_name = "The Burning Dark Key Count"
    range_start = 0
    range_end = 12
    default = 5

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["frost_ember_locations"] = Embers
    options["coin_crown_locations"] = Crowns
    options["difficulty_objective_locations"] = DifficultyObjectives
    options["frozen_caverns_locations"] = FrozenCaverns
    options["caves_of_carnage_locations"] = CavesOfCarnage
    options["the_black_mines_locations"] = BlackMines
    options["the_flooded_depths_locations"] = FloodedDepths
    options["the_burning_dark_locations"] = BurningDark
    options["common_card_locations"] = Common
    options["uncommon_card_locations"] = Uncommon
    options["rare_card_locations"] = Rare
    options["legendary_card_locations"] = Legendary
    options["victory_tome_locations"] = Tome
    options["crown_shop_locations"] = CrownShop
    options["tactical_approach_count"] = TacticalApproachCount
    options["pork_chop_power_count"] = PorkChopPowerCount
    options["dungeon_lackey_count"] = DungeonLackeyCount
    options["pay_to_win_count"] = PayToWinCount
    options["tailor_for_success_count"] = TailorForSuccessCount
    options["last_stand_count"] = LastStandCount
    options["revelation_count"] = RevelationCount
    options["aquata_breather_count"] = AquataBreatherCount
    options["for_the_worthy_count"] = ForTheWorthyCount
    options["eureka_count"] = EurekaCount
    options["caves_of_carnage_key_count"] = CavesOfCarnageKeyCount
    options["black_mines_key_count"] = BlackMinesKeyCount
    options["flooded_depths_key_count"] = FloodedDepthsKeyCount
    options["burning_dark_key_count"] = BurningDarkKeyCount
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    options["filler_traps"] = FillerTrapPercent
    return options