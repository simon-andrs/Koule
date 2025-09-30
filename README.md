# N-body simulation
Jednoduchý engine na simulaci N objektů, působicích na sebe silami.

## Instalace
Program ke spuštění potřebuje  naistalovaný Python a Pygame, tu lze naistalovat pomocí:
```python3 -m pip install -U pygame==2.6.0```
Simulaci pak spouští buď jeden ze souborů začínajících `RUN_`, případně můžete nastavit vlastní počáteční parametry vytvořením nového souboru podle návodu níže.

## Vytvoření vlastní simulace
K vytvoření vlastní simulace je třeba v adresáři programu vytvořit nový soubor `.py`, začínající řádky:
```
from main import Main
m = Main()
```
`Main` může dostat následující parametry:
|Parametr    |Popis                                       |Formát        |Defaultní hodnota        |
|------------|--------------------------------------------|--------------|:-----------------------:|
|`dim`       |počet dimenzí simulace                      |číslo         |2                        |
|`deltat`    |délka jendoho kroku                         |číslo         |1                        |
|`g_const`   |hodnota gravitační konstanty                |číslo         |6.6743 × 10<sup>-11</sup>|
|`el_const`  |hodnota elektrické konstanty                |číslo         |8.9875 × 10<sup>9</sup>  |
|`screen`    |velikost okna, ve kterém se simulace zobrazí|(šířka, výška)|`(1400, 800)`            |
|`back_color`|barva pozadí okna                           |"jméno barvy" |`"white"`                |

Na dalších řádkách můžete definovat jednotlivá tělesa pomocí:
```m.obj()```
Tato funkce přijímá následující parametry:
|Parametr|Popis              |Formát       |Defaultní hodnota|
|--------|-------------------|-------------|:---------------:|
|`x`     |počáteční pozice   |vektor       |povinný parametr |
|`v`     |poočáteční rychlost|vektor       |povinný parametr |
|`m`     |hmotnost           |číslo        |1                |
|`r`     |zobrazovaný poloměr|číslo        |0                |
|`Q`     |elektrický náboj   |číslo        |0                |
|`col`   |zobrazovaná barva  |"jméno barvy"|`"black"`        |

Skript je potřeba zakončit řádkem:
```m.run()```

## Ovládání za běhu
Po spuštění je možné program ovládat těmito klávesami:
|Klávesy   |Funkce|
|:--------:|------|
|W/S       |Přiblížení/oddálení pohledu|
|šipky     |Pohyb kamery|
|Ctrl/tečka|Pohyb kamery nahoru/dolů (jen ve 3D zoobrazení)|
|E/Q       |Zrychlení/zpomalení (mění délku kroku, a tedy i přesnost simulace)|
|P/G       |Pozastaví/obnoví pohyb|
|X/C       |Půstí čas pozadu/popředu|
|H/B       |Pohyb čáry mezi nárysem a půdorysem (jen ve 3D)|
|A         |Pohne kamerou a změní přiblížení tak, aby byla vidět všechna tělesa|
|esc       |Ukončí program|
