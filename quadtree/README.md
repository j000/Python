# QuadTree 

Drzewo czwórkowe - podział dwuwymiarowej powierzchni na 4 równe ćwiartki. Każdy węzeł ma nie więcej niż 4 potomków i przechowuje informacje o swoim rozmiarze oraz położeniu. Punkty przechowywane są jako liście. 

W celu przechowywania informacji powiązanych z punktem należy zaimplementować własną klasę Point. 

## quadtree.py

Plik z implementacją drzewa. 

Metoda `insert(point)` wstawia podany punkt do drzewa. 

Metoda `search(point, radius)` wyszukuje wszystkie punkty znajdujące się w promieniu `radius` od podanego punktu.  
Dodatkowo metoda search ustawia flagę `searched` w przeszukiwanych ćwiartkach, która można usunąć metodą `unmark`. 

## window.py 

Plik z wizualizacją napisaną z wykorzystaniem PyQt5. 

Punkty dodaje się klikając lewym klawiszem myszki.
Wyszukujemy prawym.
Klawisze `A` oraz `Z` służą do zmiany promienia wyszukiwania.
Klawisz spacji dodaje 150 losowych punktów. 

# Wnioski 

Niestety taka implementacja tworzy bardzo niezbilansowanie drzewo, jeśli punkty są zgrupowane. 

Drzewo czwórkowe znacznie poprawia średnią złożoność, ponieważ zależy ona od wysokości drzewa.
W najgorszym wypadku złożoność pozostaje liniowa.
W najlepszym przypadku (brak punktów w ćwiartce w której wyszukujemy) złożoność wynosi O(1). 
