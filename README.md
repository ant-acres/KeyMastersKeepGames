# KeyMastersKeepGames
Keymaster's Keep games maintained by ant-acres

## Witchfire Options

### witchfire_include_non_familiar_bosses
Whether or not to include Prophet of the Whispering God and Heart of the Labyrinth as options when generating the fight bosses goal. Defaults to false if not provided.

### witchfire_exclude_maps
A list of maps to exclude from all goals (excluding the fight bosses goal). Valid map names are "Island of the Damned", "Scarlet Coast", "Velmorne",  "Irongate Castle", and "Witch Mountain". Defaults to an empty list if not provided.

### Example
```
witchfire_include_non_familiar_bosses: true
witchfire_exclude_maps:
  ["Witch Mountain", "Scarlet Coast"]
```
