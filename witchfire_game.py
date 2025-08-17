from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class TemplateArchipelagoOptions:
    witchfire_include_non_familiar_bosses: WitchfireIncludeNonFamiliarBosses
    witchfire_exclude_maps: WitchfireExcludeMaps

# Main Class
class WitchfireGame(Game):
    name = "Witchfire"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = TemplateArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Equip WEAPONS, and demonic weapon, DEMONIC_WEAPON",
                data={
                    "WEAPONS": (self.weapons, 2),
                    "DEMONIC_WEAPON": (self.demonic_weapons, 1)
                }
            ),
            GameObjectiveTemplate(
                label="Equip fetish, FETISH, relic, RELIC, and ring, RING",
                data={
                    "FETISH": (self.fetishes, 1),
                    "RELIC": (self.relics, 1),
                    "RING": (self.rings, 1)
                }
            ),
            GameObjectiveTemplate(
                label="Equip light spell, LIGHT_SPELL, and heavy spell, HEAVY_SPELL",
                data={
                    "LIGHT_SPELL": (self.light_spells, 1),
                    "HEAVY_SPELL": (self.heavy_spells, 1),
                }
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Successfully extract from MAP with 7 manifestations",
                data={
                    "MAP": (self.maps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Successfully extract from MAP after completing all events",
                data={
                    "MAP": (self.maps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat a calamity in MAP",
                data={
                    "MAP": (self.calamity_maps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete the VAULT vault",
                data={
                    "VAULT": (self.vaults, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]

    @property
    def include_non_familiar_bosses(self) -> bool:
        return bool(self.archipelago_options.witchfire_include_non_familiar_bosses.value)
    
    @property
    def exclude_maps(self) -> Set[str]:
        return self.archipelago_options.witchfire_exclude_maps.value

    @functools.cached_property
    def maps_base(self) -> List[str]:
        return [
            "Island of the Damned",
            "Scarlet Coast",
            "Velmorne",
            "Irongate Castle",
            "Witch Mountain"
        ]
    
    @functools.cached_property
    def non_calamity_maps(self) -> List[str]:
        return [
            "Island of the Damned",
            "Witch Mountain",
        ]
    
    @functools.cached_property
    def vaults_base(self) -> List[str]:
        return [
            "Island of the Damned",
            "Scarlet Coast",
            "Irongate Castle"
        ]
    
    
    @functools.cached_property
    def familiars(self) -> List[str]:
        return [
            "Galley Slave",
            "The Widow",
            "Dimacher",
        ]
    
    @functools.cached_property
    def other_bosses(self) -> List[str]:
        return [
            "Prophet of the Whispering God",
            "Heart of the Labyrinth"
        ]
    

    def bosses(self) -> List[str]:
        bosses: List[str] = self.familiars[:]

        if self.include_non_familiar_bosses:
            bosses.extend(self.other_bosses[:])

        return sorted(bosses)
    
    def vaults(self) -> List[str]:
        vaults: List[str] = self.vaults_base[:]
        exclude: Set[str] = self.exclude_maps

        return [vault for vault in vaults if vault not in exclude]
    
    def maps(self) -> List[str]:
        maps: List[str] = self.maps_base[:]
        exclude: Set[str] = self.exclude_maps

        return [map for map in maps if map not in exclude]
    
    def calamity_maps(self) -> List[str]:
        maps: List[str] = self.maps_base[:]
        exclude: Set[str] = self.exclude_maps
        exclude.update(self.non_calamity_maps)

        return [map for map in maps if map not in exclude]
    
    @staticmethod
    def weapons() -> List[str]:
        return [
            "Koschei",
            "Angelus",
            "Midas",
            "Ricochet",
            "Hypnosis",
            "All-Seeing-Eye",
            "Frostbite",
            "Hangfire",
            "Duelist",
            "Hunger",
            "Nemesis",
            "Cricket",
            "Rotweaver",
            "Judgement",
            "Psychopomp",
            "Echo",
            "Oracle",
            "Basilisk",
            "Hailstorm",
            "Striga"
        ]
    
    @staticmethod
    def demonic_weapons() -> List[str]:
        return [
            "Vulture",
            "Falling Star",
            "Whisper",
        ]
    
    @staticmethod
    def light_spells() -> List[str]:
        return [
            "Lightning Bolt",
            "Stormball",
            "Blight Cyst",
            "Stigma Diabolicum",
            "Fireballs",
            "Firebreath",
            "Shockwave",
            "Frost Cone",
            "Ice Stiletto",
            "Twinshade"
        ]
    
    @staticmethod
    def heavy_spells() -> List[str]:
        return [
            "Iron Cross",
            "Miasma",
            "Rotten Fiend",
            "Burning Stake",
            "Cursed Bell",
            "Cornucopia",
            "Ice Sphere",
        ]
    
    @staticmethod
    def relics() -> List[str]:
        return [
            "Eye of the Madwoman",
            "Kirfane",
            "Book of Serpents",
            "Severed Ear",
            "Parasite",
            "Blood of a Banshee",
            "Painted Tooth",
            "Scourge",
            "Braid of a Seductress"
        ]
    
    @staticmethod
    def fetishes() -> List[str]:
        return [
            "Bittersweet Nightshade",
            "Henbane",
            "Monkshood",
            "Belladonna",
            "Balewort",
            "Mandrake",
            "Yew",
        ]
    
    @staticmethod
    def rings() -> List[str]:
        return [
            "Crown of Fire",
            "Dynamo Ring",
            "Meteor Ring",
            "Ring of Excreta",
            "Ring of Obedience",
            "Ring of Thorns",
            "Ring of Wings",
            "Shadowmist Ring"
        ]


# Archipelago Options
class WitchfireIncludeNonFamiliarBosses(Toggle):
    """
    Indicates whether to include the non-familiar bosses when generating Template objectives.
    """

    display_name = "Witchfire Include Non-Familiar Bosses"
    default = False

class WitchfireExcludeMaps(OptionSet):
    """
    Optional setting to exclude certain maps from objectives
    """

    display_name = "Witchfire Exclude Maps"
    valid_keys = [
            "Island of the Damned",
            "Scarlet Coast",
            "Velmorne",
            "Irongate Castle",
            "Witch Mountain",
        ]
    default = []
