
### Dans le détail

La définition de la commande est la suivante :

```mcfunction
give <targets> <item> [<count>]
```

Lors de l'exécution de la commande, l'item va apparaître en tant qu'entité à la position des joueurs sélectionnés. Cependant, si les joueurs ont leur inventaire plein, les autres joueurs ne pourront pas récupérer l'item car il **appartient** au joueur sélectionné.<br>
Au niveau technique, l'entité item possède le NBT `Owner` défini avec l'UUID du joueur.

La syntaxe permettant de se give un item personnalisé se fait au niveau de `<item>` sous le format suivant, une sorte de liste de components entre crochets :

```mcfunction
give <targets> minecraft:stone[component_1=X, component_2=X, ...]
```

