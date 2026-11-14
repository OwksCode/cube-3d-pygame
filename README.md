# Cube 3D en Pygame

Projet de terminale (spécialité NSI, 2023-2024), réalisé en binôme avec Paul Benoist.

Un petit moteur 3D écrit sans bibliothèque 3D : un cube tourne sur lui-même, dessiné face par face avec des triangles, et projeté à l'écran avec de simples formules mathématiques.

![Démo du cube 3D](cube-demo.gif)

## Ce que fait le programme

- **Modélisation en triangles** : chaque face du cube est découpée en deux triangles, comme dans les moteurs 3D classiques.
- **Rotation** : chaque sommet tourne autour d'un axe vertical, avec une matrice de rotation :
  `x' = x·cos(a) + z·sin(a)` et `z' = −x·sin(a) + z·cos(a)`.
- **Projection** : les points 3D sont projetés sur l'écran en 2D par une projection oblique :
  `X = x + 350` et `Y = (z − y) / √2 + 400`.
- **Algorithme du peintre** : les triangles sont triés selon leur profondeur moyenne, puis dessinés du plus lointain au plus proche, pour que les faces cachées soient recouvertes.
- **Interface** : boutons pause et vitesse, et icônes pour afficher le cube ou une pyramide.

## Lancer le projet

```bash
pip install pygame
python main.py
```

Commandes :
- `Espace` ou bouton pause : arrête ou relance la rotation
- `←` / `→` ou boutons : ralentit ou accélère (en changeant le nombre d'images par seconde)
- Icônes à droite : affiche ou masque le cube et la pyramide

## Limites connues

C'est un projet de lycée, laissé tel qu'il a été rendu :
- la rotation se fait autour d'un seul axe ;
- la projection est oblique, sans effet de perspective ;
- toutes les faces ont la même couleur, sans ombrage ;
- la face du dessous n'est pas dessinée, et la pyramide n'utilise pas le tri par profondeur ;
- le code repose sur des variables globales.

## Ce que j'en ai retenu

Ce projet m'a fait découvrir les bases du rendu 3D : représenter un objet par des triangles, passer de l'espace 3D à l'écran 2D, et gérer l'ordre d'affichage des faces. C'est aussi ce qui m'a donné le goût des projets qui mêlent mathématiques et programmation, comme ma [simulation N-body](https://github.com/OwksCode/nbody).
