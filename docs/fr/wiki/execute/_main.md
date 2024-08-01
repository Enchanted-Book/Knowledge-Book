
# /execute

```{toctree}
:hidden:
:caption: Wiki

as_at_positioned_rotated_in/_main
align_anchored_facing/_main
if_unless/_main
store/_main
on/_main
summon/_main
```

```{include} ./intro_simple.md
```

```{include} ./intro_advanced.md
```

---

## Sous-commandes

::::{grid} 2

:::{grid-item-card} 👨‍🎓 as/at/positioned/rotated/in
:link: as_at_positioned_rotated_in/_main
:link-type: doc
:margin: 0 3 0 0

Celles-ci permettent de modifier le contexte d'exécution de la commande.
Elles sont utilisées partout lorsqu'il est nécessaire de spécifier une entité, une position ou une rotation.
:::

:::{grid-item-card} 🔧 align/anchored/facing
:link: align_anchored_facing/_main
:link-type: doc
:margin: 0 3 0 0

En revanche, celles-ci se concentrent spécialement sur la position et l'orientation lors de l'exécution de la commande, mais de manières différentes.
:::

::::

::::{grid} 2

:::{grid-item-card} ❓ if/unless
:link: if_unless/_main
:link-type: doc
:margin: 0 3 0 0

Si vous avez besoin de vérifier une condition avant d'exécuter une commande, ces sous-commandes sont là pour vous.
:::

:::{grid-item-card} 🧰 store
:link: store/_main
:link-type: doc
:margin: 0 3 0 0

Intimement lié à `/data`, `execute store` permet de stocker le résultat d'une commande dans un emplacement spécifique (scoreboard, block, storage, bossbar).
:::

::::

::::{grid} 2

:::{grid-item-card} 🚗 on
:link: on/_main
:link-type: doc
:margin: 0 3 0 0

Cette sous-commande permet de changer le contexte d'exécution de la commande sur des entités spécifiques tels que les passagers d'un véhicule, la dernière entité qui vous a infligé des dégâts, etc.
:::

:::{grid-item-card} 🌌 summon
:link: summon/_main
:link-type: doc
:margin: 0 3 0 0

À ne pas confondre avec `/summon`, `execute summon` permet de créer une entité et d'effectuer directement des actions sur celle-ci.
:::

::::
