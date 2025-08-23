from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import OptionSet, Range

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

# Option Dataclass
@dataclass
class TemplateArchipelagoOptions:
    v_rising_boss_level_lower_bound: VRisingBossLevelLowerBound
    v_rising_boss_level_upper_bound: VRisingBossLeveUpperBound
    v_rising_boss_exclusions: VRisingBossExclusions

# Main Class
class VRisingGame(Game):
    name = "V Rising"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [KeymastersKeepGamePlatforms.PS5]

    is_adult_only_or_unrated = False

    options_cls = TemplateArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Use only ELEMENT spells",
                data={
                    "ELEMENT": (self.elements, 1)
                },
                weight=3
            ),
            GameObjectiveTemplate(
                label="Use the basic spells, SPELLS",
                data={
                    "SPELLS": (self.basic_spells, 2)
                },
                weight=3
            ),
            GameObjectiveTemplate(
                label="Use the ultimate spell, ULT",
                data={
                    "ULT": (self.ultimate_spells, 1)
                },
                weight=3
            ),
            GameObjectiveTemplate(
                label="Use VEIL and the basic spells, SPELLS",
                data={
                    "VEIL": (self.veils, 1),
                    "SPELLS": (self.basic_spells, 2)
                },
                weight=2
            ),
            GameObjectiveTemplate(
                label="Use VEIL and the ultimate spell, ULT",
                data={
                    "VEIL": (self.veils, 1),
                    "ULT": (self.ultimate_spells, 1)
                },
                weight=2
            ),
            GameObjectiveTemplate(
                label="Use VEIL the basic spells, SPELLS, and the ultimate spell, ULT",
                data={
                    "VEIL": (self.veils, 1),
                    "SPELLS": (self.basic_spells, 2),
                    "ULT": (self.ultimate_spells, 1)
                },
                weight=1
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives = []
        available_v_bloods = self.available_v_bloods()
        for v_blood, level in available_v_bloods.items():
            objective = GameObjectiveTemplate(
                label="Defeat V_BLOOD at or below level LEVEL while using the WEAPON",
                data={
                    "V_BLOOD": (lambda name=v_blood: [name], 1),
                    "WEAPON": (self.weapons, 1),
                    "LEVEL": (self.level_range(level), 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            )
            objectives.append(objective)
        return objectives

    @property
    def level_bounds(self) -> tuple:
        lower_bound = int(self.archipelago_options.v_rising_boss_level_lower_bound.value) * -1
        upper_bound = int(self.archipelago_options.v_rising_boss_level_upper_bound.value)
        return (lower_bound, upper_bound)
    
    @property
    def boss_exclusions(self) -> Set[str]:
        return self.archipelago_options.v_rising_boss_exclusions.value
    
    @staticmethod
    def weapons() -> List[str]:
        return [
            "Axes",
            "Crossbow",
            "Mace",
            "Spear",
            "Sword",
            "Claws",
            "Daggers",
            "Greatsword",
            "Pistols",
            "Reaper",
            "Slashers",
            "Twinblade",
            "Whip",
        ]
        
    
    @staticmethod
    def elements() -> List[str]:
        return [
            "Blood",
            "Chaos",
            "Unholy",
            "Illusion",
            "Frost",
            "Storm",
        ]
    
    @staticmethod
    def veils() -> List[str]:
        return [
            "Veil of Blood",
            "Veil of Chaos",
            "Veil of Bones",
            "Veil of Illusion",
            "Veil of Frost",
            "Veil of Storm",
        ]
    
    @staticmethod
    def basic_spells() -> List[str]:
        return [
            "Shadowbolt",
            "Blood Rite",
            "Blood Rage",
            "Blood Fountain",
            "Sanguine Coil",
            "Carrion Swarm",
            "Chaos Volley",
            "Power Surge",
            "Aftershock",
            "Void",
            "Chaos Barrier",
            "Rain of Chaos",
            "Corrupted Skull",
            "Ward of the Damned",
            "Bone Explosion",
            "Death Knight",
            "Soulburn",
            "Unholy Chains",
            "Spectral Wolf",
            "Phantom Aegis",
            "Wraith Spear",
            "Mosquito",
            "Mist Trance",
            "Curse",
            "Frost Bat",
            "Cold Snap",
            "Ice Nova",
            "Crystal Lance",
            "Frost Barrier",
            "Arctic Storm",
            "Cyclone",
            "Discharge",
            "Ball Lightning",
            "Polarity Shift",
            "Lightning Curtain",
            "Lightning Tendrils",
        ]
    
    @staticmethod
    def ultimate_spells() -> List[str]:
        return [
            "Crimson Beam",
            "Heart Strike",
            "Merciless Charge",
            "Chaos Barrage",
            "Army of the Dead",
            "Volatile Arachnid",
            "Spectral Guardian",
            "Wisp Dance",
            "Arctic Leap",
            "Ice Block",
            "Raging Tempest",
            "Lightning Typhoon",
        ]
    
    # bosses dict with their level as the value
    @staticmethod
    def v_bloods() -> Dict[str, int]:
        return {
            "Alpha the White Wolf": 16,
            "Keely the Frost Archer": 20,
            "Errol the Stonebreaker": 20,
            "Rufus the Foreman": 20,
            "Grayson the Armourer": 27,
            "Goreswine the Ravager": 27,
            "Lidia the Chaos Archer": 30,
            "Clive the Firestarter":30 ,
            "Nibbles the Putrid Rat": 30,
            "Finn the Fisherman": 32,
            "Polora the Feywalker": 35,
            "Kodia the Ferocious Bear": 35,
            "Nicholaus the Fallen": 35,
            "Quincey the Bandit King": 37,
            "Beatrice the Tailor": 40,
            "Vincent the Frostbringer": 44,
            "Christina the Sun Priestess": 44,
            "Tristan the Vampire Hunter": 44,
            "Sir Erwin the Gallant Cavalier": 46,
            "Kriig the Undead General": 47,
            "Leandra the Shadow Priestess": 47,
            "Maja the Dark Savant": 47,
            "Bane the Shadowblade": 50,
            "Grethel the Glassblower": 50,
            "Meredith the Bright Archer": 50,
            "Terah the Geomancer": 53,
            "Frostmaw the Mountain Terror": 53,
            "General Elena the Hollow": 53,
            "Gaius the Cursed Champion": 55,
            "General Cassius the Betrayer": 57,
            "Jade the Vampire Hunter": 57,
            "Raziel the Shepherd": 57,
            "Octavian the Militia Captain": 58,
            "Ziva the Engineer": 60,
            "Domina the Blade Dancer": 60,
            "Angram the Purifier": 61,
            "Ungora the Spider Queen": 63,
            "Ben the Old Wanderer": 63,
            "Foulrot the Soultaker": 63,
            "Albert the Duke of Balaton": 64,
            "Willfred the Village Elder": 64,
            "Cyril the Cursed Smith": 65,
            "Sir Magnus the Overseer": 66,
            "Baron du Bouchon the Sommelier": 70,
            "Morian the Stormwing Matriarch": 70,
            "Mairwyn the Elementalist": 70,
            "Henry Blackbrew the Doctor": 74,
            "Jakira the Shadow Huntress": 75,
            "Stavros the Carver": 75,
            "Lucile the Venom Alchemist": 76,
            "Matka the Curse Weaver": 76,
            "Terrorclaw the Ogre": 76,
            "Azariel the Sunbringer": 79,
            "Voltatia the Power Master": 79,
            "Simon Belmont the Vampire Hunter": 80,
            "Dantos the Forgebinder": 82,
            "Lord Styx the Night Champion": 84,
            "Gorecrusher the Behemoth": 84,
            "General Valencia the Depraved": 84,
            "Solarus the Immaculate": 86,
            "Talzur the Winged Horror": 86,
            "Adam the Firstborn": 88,
            "Megara the Serpent Queen": 88,
            "Dracula the Immortal King": 91,
        }
    
    def available_v_bloods(self) -> Dict[str, int]:
        remaining_v_bloods = self.v_bloods()
        for exclusion in self.boss_exclusions:
            del remaining_v_bloods[exclusion]
        return remaining_v_bloods

    def level_range(self, boss_level):
        bounds = self.level_bounds
        lower_bound = max(15, boss_level + bounds[0])
        upper_bound = min(91, boss_level + bounds[1])
        def boss_range() -> range:
            return range(lower_bound, upper_bound)
        return boss_range

# Archipelago Options
class VRisingBossLevelLowerBound(Range):
    """
    Lower bound for how much lower than a V Blood's level a player's item level can be in an objective.
    """

    display_name = "V Rising Boss Level Lower Bound"
    default = 3
    range_start = 0
    range_end = 40

class VRisingBossLeveUpperBound(Range):
    """
    Upper bound for how much higher than a V Blood's level a player's item level can be in an objective.
    """

    display_name = "V Rising Boss Level Upper Bound"
    default = 3
    range_start = 0
    range_end = 40

class VRisingBossExclusions(OptionSet):
    """
    Optional list of bosses to exclude from objectives.
    """

    display_name = "V Rising Boss Exclusions"
    valid_keys = list(VRisingGame.v_bloods().keys())
    default = []


