
### Meilleur stuff

Reprenons l'exemple précédent, on va cette fois-ci personnaliser les items :

```mcfunction
# Item renommé avec des enchantments
give @a[distance=..50] diamond_sword[item_name='{"text":"Sanglant","color":"red","italic":false}, enchantments={"minecraft:sharpness":5,"minecraft:unbreaking":3}]

# Plastron en cuir coloré et incassable.
give @a[distance=..50] leather_chestplate[dyed_color=56899,unbreakable={}]

# Pommes en or normales mais enchantées
give @a[distance=..50] golden_apple[enchantment_glint_override=true] 42
```

