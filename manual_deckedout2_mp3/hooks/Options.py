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

class Legendary(Toggle):
    """Should there be locations for the Legendary Cards (which are much harder to get, but a lot more interesting, logic-wise!)
    Don't disable both this and Sixth_Locations."""
    display_name = "Legenary Card Locations"

class Sixth(Toggle):
    """Should there be 6 locations for each purchase, or 5?
    Don't disable both this and Legendary_Card_Locations."""
    display_name = "Action Rando"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["Legendary_Card_Locations"] = Legendary
    options["Sixth_Locations"] = Sixth
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    options["filler_traps"] = FillerTrapPercent
    return options