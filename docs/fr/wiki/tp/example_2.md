
### Un peu plus de détail

Cette fois-ci voici des exemples permettant de téléporter toutes les entités sur soi, ou à une position précise.

```mcfunction
tp @e @s
tp @e 284 72 1292
```

Si je souhaite me téléporter sur le mouton le plus proche :

```mcfunction
tp @n[type=sheep]
tp @e[type=sheep,sort=nearest,limit=1]
```

