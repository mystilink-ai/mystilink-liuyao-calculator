# Mystilink Calculateur Liu Yao

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## Aperçu

Tire six lignes Liu Yao (bas → haut) selon un modèle à trois pièces. La sortie est un JSON de chart structuré avec chaînes de bits originale/résultante et indicateurs de lignes mobiles. Aucune image ni ressource CDN n’est incluse.

Sommes des pièces : 9 = vieux yang (mobile), 8 = jeune yang, 7 = jeune yin, 6 = vieux yin (mobile).

## Plateformes et langages

| Cible | Livraison |
|-------|----------|
| Python | Paquet installable `mystilink-liuyao-calculator` et CLI `liuyao` |
| JavaScript / Node | Paquet npm sous `bindings/js` (lance le CLI ; navigateur via `runCli` injectable) |
| C | En-tête + bibliothèque qui invoque le CLI et renvoie du JSON |
| C++ | Enveloppe légère sur l’API C |
| C# | Enveloppe de processus autour du CLI |
| Java | Enveloppe ProcessBuilder autour du CLI |

Toutes les liaisons non-Python appellent l’exécutable `liuyao` sur `PATH` (ou `MYSTILINK_LIUYAO_CLI`). L’alias long `mystilink-liuyao` reste installé pour compatibilité.

## Prérequis

- Python 3.9 ou plus récent
- Pour les liaisons de langage : le CLI doit être installé et disponible sur `PATH`

## Installation et démarrage rapide

```bash
cd mystilink-liuyao-calculator
python3 -m pip install -e .
liuyao cast --seed 123
```

Aussi :

```bash
python3 -m mystilink_liuyao cast --throws "9,8,7,6,8,9"
```

## CLI

Le stdout par défaut est le JSON de chart nu (`mystilink.liuyao.chart/0.1`).

```bash
liuyao cast [--seed N] [--throws "9,8,7,6,8,9"] [--envelope] [--locale en]
liuyao version
```

| Option | Description |
|--------|-------------|
| `--seed` | Graine RNG déterministe (ignorée si `--throws` est défini ; alors la sortie `seed` est `null`) |
| `--throws` | Six sommes de pièces dans `{6,7,8,9}`, séparées par virgule/deux-points/espace |
| `--envelope` | Envelopper en `mystilink.envelope/0.1` avec `system`=`liuyao` (subject omis) |
| `--locale` | Chaîne de locale avec `--envelope` (défaut `en`) |

## API Python

```python
from mystilink_liuyao import cast_lines

chart = cast_lines(seed=123)
# or: cast_lines(throws="9,8,7,6,8,9")
print(chart["original_bits"], chart["has_moving"])
```

## Exemples

Des exemples exécutables se trouvent sous `examples/{c,cpp,csharp,java,js,node,python}/`. Les sources des liaisons sont sous `bindings/`. Le JSON Schema du chart est dans `schema/chart.json`.

## Limites

- Le modèle de pièces correspond au script de tirage produit ; aucun nom d’hexagramme ni texte d’interprétation n’est généré.
- `--throws` manuel fixe la sortie `seed` à `null`.
- Ce paquet ne fournit ni polices, ni images, ni recherches d’assets distants.

## Licence

MIT. Voir [LICENSE](../../LICENSE).

## Retours

Signalez les défauts avec : version CLI (`liuyao version`), ligne de commande exacte (graines fictives uniquement), et JSON stderr/stdout.
