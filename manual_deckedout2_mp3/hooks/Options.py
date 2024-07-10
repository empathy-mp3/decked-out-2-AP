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

class Legendary(DefaultOnToggle):
    """Should there be locations for the Legendary Cards (which are much harder to get, but a lot more interesting, logic-wise!)"""
    display_name = "Legendary Card Locations"

class Sixth(Toggle):
    """Should there be 6 locations for each purchase, or 5?"""
    display_name = "Sixth Locations"

class TacticalApproachCount(Range):
    """Number of filler to be replaced by the Tactical Approach Card (a single-use crown shop card)."""
    display_name = "Tactical Approach Count"
    range_start = 0
    range_end = 30
    default = 15

class PorkChopPowerCount(Range):
    """Number of filler to be replaced by the Pork Chop Power Card (a single-use crown shop card)."""
    display_name = "Pork Chop Power Count"
    range_start = 0
    range_end = 30
    default = 15

class DungeonLackeyCount(Range):
    """Number of filler to be replaced by the Dungeon Lackey Card (a single-use crown shop card)."""
    display_name = "Dungeon Lackey Count"
    range_start = 0
    range_end = 30
    default = 15

class PayToWinCount(Range):
    """Number of filler to be replaced by the Pay To Win Card (a single-use crown shop card)."""
    display_name = "Pay to Win Count"
    range_start = 0
    range_end = 30
    default = 15

class TailorForSuccessCount(Range):
    """Number of filler to be replaced by the Tailor for Success Card (a single-use strong crown shop card)."""
    display_name = "Tailor for Success Count"
    range_start = 0
    range_end = 16
    default = 8

class LastStandCount(Range):
    """Number of filler to be replaced by the Last Stand Card (a single-use strong crown shop card)."""
    display_name = "Last Stand Count"
    range_start = 0
    range_end = 16
    default = 8

class RevelationCount(Range):
    """Number of filler to be replaced by the Revelation Card (a single-use uncommon card)."""
    display_name = "Revelation Count"
    range_start = 0
    range_end = 12
    default = 6

class AquataBreatherCount(Range):
    """Number of filler to be replaced by the Aquata Breather Card (a single-use rare card)."""
    display_name = "Aquata Breather Count"
    range_start = 0
    range_end = 12
    default = 6

class ForTheWorthyCount(Range):
    """Number of filler to be replaced by the For the Worthy Card (a single-use rare card)."""
    display_name = "For the Worthy Count"
    range_start = 0
    range_end = 8
    default = 4

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
    default = 9

class BlackMinesKeyCount(Range):
    """Number of filler to be replaced by The Black Mines Key (key to the third area)."""
    display_name = "The Black Mines Key Count"
    range_start = 0
    range_end = 12
    default = 6

class FloodedDepthsKeyCount(Range):
    """Number of filler to be replaced by The Flooded Depths Key (key to the alt third area)."""
    display_name = "The Flooded Depths Key Count"
    range_start = 0
    range_end = 12
    default = 6

class BurningDarkKeyCount(Range):
    """Number of filler to be replaced by The Burning Dark Key (key to the fourth area)."""
    display_name = "The Burning Dark Key Count"
    range_start = 0
    range_end = 12
    default = 6

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["Legendary_Card_Locations"] = Legendary
    options["Sixth_Locations"] = Sixth
    options["Tactical_Approach_Count"] = TacticalApproachCount
    options["Pork_Chop_Power_Count"] = PorkChopPowerCount
    options["Dungeon_Lackey_Count"] = DungeonLackeyCount
    options["Pay_To_Win_Count"] = PayToWinCount
    options["Tailor_For_Success_Count"] = TailorForSuccessCount
    options["Last_Stand_Count"] = LastStandCount
    options["Revelation_Count"] = RevelationCount
    options["Aquata_Breather_Count"] = AquataBreatherCount
    options["For_The_Worthy_Count"] = ForTheWorthyCount
    options["Eureka_Count"] = EurekaCount
    options["Caves_Of_Carnage_Key_Count"] = CavesOfCarnageKeyCount
    options["Black_Mines_Key_Count"] = BlackMinesKeyCount
    options["Flooded_Depths_Key_Count"] = FloodedDepthsKeyCount
    options["Burning_Dark_Key_Count"] = BurningDarkKeyCount
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    options["filler_traps"] = FillerTrapPercent
    return options