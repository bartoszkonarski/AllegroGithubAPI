# Allegro Summer e-Xperience 2021 - zadanie rekrutacyjne nr 3

Zadanie polega na stworzeniu oprogramowania pozwalającego na:

- listowanie repozytoriów (nazwa i liczba gwiazdek)
- zwracania sumy gwiazdek

dla dowolnego użytkownika serwisu GitHub

## Zaimplementowane funkcjonalności:

- zwracanie wyszczególninych danych w formacie JSON dostępnych poprzez mini-API pod endpointem: {adres_hosta}/api/{nazwa_użytkownika}
- prosta strona WWW, stanowiąca minimalistyczny frontend w celu bardziej przejrzystego i interaktywnego przedstawienia zwracanych danych

## Propozycje rozwoju projektu:

- Zmiana pozyskiwania danych przez aplikację strony WWW (obecnie wykonuje ona zapytanie HTTP do serwera na którym sama się znajduje - poprzez zaimplementowane mini-API)
- Rozbudowa rodzajów pozyskiwanych danych
- Zapis pozyskanych danych w bazie danych, w celu obserwacji rozwoju aktywności użytkowników/repozytoriów (np. poprzez generowanie cyklicznych raportów)
