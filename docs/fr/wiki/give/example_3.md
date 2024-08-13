
### A little trolling box

Faisons une chaine de commandes qui vont donner des items troll à des joueurs puis les téléporter dans une arène !

```mcfunction
# Une épée qui se mange et qui ne fait aucun dégât
give @a[distance=..50] diamond_sword[!attribute_modifiers, food={saturation:1.0,nutrition=2.0}]

# Pomme en or qui ne se mange pas, enchantée tranchant 10, et avec une durabilité de 42/100
give @a[distance=..50] golden_apple[!food, enchantments={"minecraft:sharpness":10}, max_damage=100, damage=42, max_stack_size=1]

# Une seconde après, on téléporte
tp @a[distance=..50] 378 122 289
```

On notera deux choses sur la pomme en or :
1. Le component `max_stack_size` doit obligatoirement être à 1 si un item possède une durabilité, autrement une erreur apparait lors de l'exécution de la commande.
2. La durabilité ne baissera pas quand des coups seront mis car aucun component permet de définir ce comportement à ce jour. (Des alternatives existent tel que l'utilisation d'`advancement` custom couplé à un `item_modifier` mais ce sera pour un prochain jour)

