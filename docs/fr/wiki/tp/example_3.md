
### Plus gros exemples

Téléportation de toutes les entités non-joueurs 5 blocs au dessus de moi et tournés de 90° par rapport à moi :

```mcfunction
tp @e[type=!player] ~ ~5 ~ ~90 ~
```

Téléportation de tous les joueurs, dans un rayon de 100 blocs, 5 blocs devant moi en regardant mes pieds :

```mcfunction
tp @a[distance=..100] ^ ^ ^5 facing entity @s feet
```

