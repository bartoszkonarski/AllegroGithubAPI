#Allegro Summer e-Xperience 2021 - zadanie rekrutacyjne nr 3

Zadanie polega na stworzeniu oprogramowania pozwalającego na:

- listowanie repozytoriów (nazwa i liczba gwiazdek)
- zwracania sumy gwiazdek
  dla dowolnego użytkownika serwisu GitHub

##Zaimplementowane funkcjonalności:

- zwracanie wyszczególninych danych w formacie JSON dostępnych pod endpointem: {adres_hosta}/api/{nazwa_użytkownika}
- prosta strona WWW, stanowiąca minimalistyczny frontend w celu bardziej przejrzystego przedstawienia zwracanych danych

##Propozycje rozwoju projektu:

- Implementacja równoległego wykonywania zapytań do GitHub API w celu skrócenia czasu odpowiedzi (szczególnie w przypadku użytkowników posiadających bardzo wiele repozytoriów, GitHub API pozwala na pobranie listy maksymalnie 100 repozytoriów jednocześnie)
- Rozbudowa rodzajów pozyskiwanych danych
