# KeyMastersKeepGames
Keymaster's Keep games maintained by ant-acres

## V Rising Options
This implementation for V Rising assumes you have access to a save file in a near complete state. This should allow you to fight any boss and change gear to set your item level to an arbitrary number between 15 and 90.

### v_rising_boss_level_lower_bound
Lower bound for how much lower than a V Blood's level a player's item level can be in an objective. Defaults to 3. Item levels aren't allowed to go lower than 15 because that's the lowest level for certain weapon types.

### v_rising_boss_level_upper_bound
Upper bound for how much higher than a V Blood's level a player's item level can be in an objective. Defaults to 3.

### v_rising_boss_exclusions
An optional list of bosses to exclude from goals. Defaults to an empty list.


### Example
```
v_rising_boss_level_lower_bound: 3
v_rising_boss_level_upper_bound: 0
v_rising_boss_exclusions:
  ["Adam the Firstborn", "Nibbles the Putrid Rat"]
```

## Witchfire Options

### witchfire_include_non_familiar_bosses
Whether or not to include Prophet of the Whispering God and Heart of the Labyrinth as options when generating the fight bosses goal. Defaults to false if not provided.

### witchfire_exclude_maps
An optional list of maps to exclude from all goals (excluding the fight bosses goal). Valid map names are "Island of the Damned", "Scarlet Coast", "Velmorne",  "Irongate Castle", and "Witch Mountain". Defaults to an empty list if not provided.

### Example
```
witchfire_include_non_familiar_bosses: true
witchfire_exclude_maps:
  ["Witch Mountain", "Scarlet Coast"]
```
