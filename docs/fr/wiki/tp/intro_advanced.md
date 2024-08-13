
### Dans le détail

Penchons-nous sur deux premières définitions de la commande :

```mcfunction
tp <destination>
tp <targets> <destination>
```

On constate que le second argument de la commande est optionnel. Cela veut dire que n'importe quelle entité tapant `/tp <selector>` va se téléporter à la position de l'entité sélectionnée (avec sa rotation). Signifiant que le sélecteur ne doit renvoyer qu'une seule entité. Ou alors simplement les coordonnées à la place du sélecteur<br>
Si on ajoute un second argument (selecteur ou coordonnées), cette fois-ci toutes les entités sélectionnées par le premier argument vont être téléportés vers la destination. Ici aussi, la destination doit être unique.

Mais encore, voici d'autres définitions plus complètes de la commande :

```mcfunction
tp <targets> <location> <rotation>
tp <targets> <location> facing <facing_location>
tp <targets> <location> facing entity <facing_entity> [<facing_anchor>]
```

Alors la première est simple, en plus des coordonnées vous pouvez définir la rotation (le pitch et le yaw).<br>
La deuxième va permettre de préciser une destination à regarder (comme un bloc par exemple).<br>
Le dernier lui, plus complexe, va permettre d'être dirigé vers une entité prise par un sélecteur. L'argument optionnel `facing_anchor` précise si on doit regarder les pieds (feet) ou les yeux (eyes) de l'entité avec comme valeur par défaut: feet.

