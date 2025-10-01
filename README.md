# Simulace N těles
Jednoduchý engine na simulaci N koulí, působicích na sebe silami.

## Instalace a spuštění
Program ke spuštění potřebuje  naistalovaný Python a Pygame, tu lze naistalovat pomocí:
```python3 -m pip install -U pygame==2.6.0```
Simulaci pak spouští buď jeden ze souborů začínajících `RUN_`, případně můžete nastavit vlastní počáteční parametry vytvořením nového souboru podle návodu níže.

## Běh programu
Po spuštění se rozběhne simulace pohybu těles. Ve třech dimenzích program zobrazuje tzv. Mongeovo promítaní - v horní částí vidíme pohled zepředu, ve spodní zezhora. Počáteční nastavení přiblížení, pozice pozorovatele a rychlosti pohybu mohou být nepraktické, program je proto možné za běhu ovládat těmito klávesami:

|Klávesy   |Funkce|
|:--------:|------|
|W/S       |Přiblížení/oddálení pohledu|
|šipky     |Pohyb kamery|
|Ctrl/tečka|Pohyb kamery nahoru/dolů (jen ve 3D zoobrazení)|
|E/Q       |Zrychlení/zpomalení (mění délku kroku, a tedy i přesnost simulace)|
|P/G       |Pozastaví/obnoví pohyb|
|X/C       |Pustí čas pozadu/popředu|
|H/B       |Pohyb čáry mezi nárysem a půdorysem (jen ve 3D zobrazení)|
|A         |Pohne kamerou a změní přiblížení tak, aby byla vidět všechna tělesa|
|esc       |Ukončí program|

## Vytvoření vlastní simulace
K vytvoření vlastní simulace je třeba v adresáři programu vytvořit nový soubor `.py`, začínající řádky:
```
from main import Main
m = Main()
```
`Main` může dostat následující parametry:
|Parametr    |Popis                                       |Formát            |Defaultní hodnota        |
|------------|--------------------------------------------|------------------|:-----------------------:|
|`dim`       |počet dimenzí simulace                      |číslo             |2                        |
|`deltat`    |délka jendoho kroku                         |číslo             |1                        |
|`g_const`   |hodnota gravitační konstanty                |číslo             |6.6743 × 10<sup>-11</sup>|
|`el_const`  |hodnota elektrické konstanty                |číslo             |8.9875 × 10<sup>9</sup>  |
|`screen`    |velikost okna, ve kterém se simulace zobrazí|(šířka, výška)    |`(1400, 800)`            |
|`back_color`|barva pozadí okna                           |"název barvy"[^2] |`"white"`                |

Na dalších řádkách můžete definovat jednotlivá tělesa pomocí:
```
m.obj()
```
Tato funkce přijímá následující parametry:
|Parametr|Popis              |Formát           |Defaultní hodnota|
|--------|-------------------|-----------------|:---------------:|
|`x`     |počáteční pozice   |vektor[^1]       |povinný parametr |
|`v`     |poočáteční rychlost|vektor[^1]       |povinný parametr |
|`m`     |hmotnost           |číslo            |1                |
|`r`     |zobrazovaný poloměr|číslo            |0                |
|`Q`     |elektrický náboj   |číslo            |0                |
|`col`   |zobrazovaná barva  |"název barvy"[^2]|`"black"`        |


Skript je potřeba zakončit řádkem:
```
m.run()
```

### Komplexní čísla a více dimenzí
Programu můžete zadat problém i ve více než 3 dimenzích, v takovém případě bude výpočet probíhat v prostoru zadané dimenze, avšak zobrazí se pouze pozice v prvních 3 třech dimenzích.\
Stejně tak je možné jako hodnoty parametrů uvést komplexní čísla ve tvaru *2+3j*, výpočet pak bude probíhat v komplexních číslech. Ve 2 a více dimenzích se ale zobrazuje pouze reálná část pozice těles. Při simulaci v jediné dimenzi představuje vodorovná osa reálnou a svislá imaginární část polohy těles.

## Technický popis
  Program je rozdělen do několika souborů. [`vectors.py`](vectors.py) definuje třídu vektorů a umožňuje je sčítat, násobit skalárem... aby bylo možné zapisovat fyzikální vzorce ve vetorové formě přímo v Pythonu. [`physics.py`](physics.py) pak obsahuje metody pro samotnou simulaci pohybu těles. Pro řešení diferenciálních rovnic newtonovské mechaniky jsem použil Eulerovu metodu, která selhává při přílišném přiblížení těles, proto v takovém případě koule odlétají zcela bezprecedentní rychlostí. O vykreslování a ovládání programu uživatelem se pak stará [`graphics.py`](graphics.py) pomocí knihovny Pygame. [`main.py`](main.py) slouží jako celková režije ostaních skriptů, jejímž cílem je, aby psaní skriptů s počátečními podmínkami bylo co nejjednodušší.


[^1]: Vektory se zapisují ve formě *(x, y, z...)*, kde počet složek musí odpovídat počtu dimenzí definovanému na začátku souboru. V případě jednodimenzionální situace je potřeba psát vektory ve formě *(x,)*.
[^2]: Lze použít jakoukoli ze [seznamu barev](https://www.pygame.org/docs/ref/color_list.html) podporovaných Pygame.
