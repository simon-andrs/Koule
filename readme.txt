Program simuluje a zobrazuje (pomocí Pygame) pohyb N těles, které na sebe působí gravitační (a případně i elektrostatickou) silou.
Výpočetní část (soubory vectors a physics) umožňuje simulaci v jakémkoli počtu dimenzí a případně i v komplexních číslech
(čehož praktická využitelnost je nejspíše nulová). Vykreslení (pomocí souboru graphics) pak zobrazuje vždy 2 nebo 3 dimenze.
Ve 3 dimenzích se objekty zobrazují v "Mongeově promítání" - v horní polovině vidíme pohled zepředu, ve spodní zezhora.
Ve více dimenzích se zobrazují vždy jen první 3 souřadnice objektů. Naopak v jedné dimenzi slouží svislá osa jako imaginární
a při komplexních počátečních podmínkách pak zobrazení odpovídá 2D problému s reálnými čísly. Ke spuštění je potřeba spustit
jeden ze souborů začínajících "RUN_" případně napsat vlastní program importující soubor main
(podle vzoru přiložených souborů RUN_...) a nastavující jiné počáteční podmínky.

Po spuštění se program ovládá klávesami:
W/S: zoom
šipky a crtl/tečka: pohyb kamery
E/Q: rychlost (změní délku kroku a tedy i přesnost)
P/G: zastaví/obnoví pohyb
X/C: pustí čas dozadu/dopředu
H/B: pohybuje dělící čarou (jen ve 3 dimenzích)
A: změní kameru a přiblížení, aby byly vidět všechny objekty
esc: ukončí program

Možná vylepšení programu:
Detekce a simulace srážek (vyřešilo by současný problém, kdy program nezvládá přílišná přiblížení objektů)
Použít lepší numerickou metodu
Koule za sebou kreslí čáry - je lépe vidět jejich trajektorie

...
