# Allegro Summer e-Xperience 2021

# Zadanie rekrutacyjne nr 3

Zadanie polega na stworzeniu oprogramowania pozwalającego na:

- listowanie repozytoriów (nazwa i liczba gwiazdek)
- zwracania sumy gwiazdek

dla dowolnego użytkownika serwisu GitHub

## Zaimplementowane funkcjonalności:

- zwracanie wyszczególnionych danych w formacie JSON dla zapytań HTTP typu GET poprzez mini-API pod endpointem: {adres_hosta}/api/{nazwa_użytkownika}
- prosta strona WWW, stanowiąca minimalistyczny frontend w celu bardziej przejrzystego i interaktywnego przedstawienia zwracanych danych

## Instrukcja instalacji/uruchomienia:

**Publiczne wdrożenie na platformie Heroku:** https://github-api-userdata.herokuapp.com/,  
(endpointy mini-API dostępne pod https://github-api-userdata.herokuapp.com/api/{nazwa_użytkownika})

Instalacja lokalna:

1. Należy pobrać zawartość gałęzi 'main' repozytorium.
2. W systemie należy utworzyć następujące zmienne środowiskowe:
   - ['GITHUB_API_TOKEN'] - jako wartość przypisujemy wartość personalnego tokena wygenerowanego w ustawieniach profilu GitHub (https://github.com/settings/tokens)
   - ['FLASK_APP_SECRET_KEY'] - jako wartość przypisujemy unikalny ciąg znaków będący kluczem sekretnym naszej aplikacji
3. Dla środowiska Python (zaleca się stworzenie nowego wirtualnego środowiska) instalujemy potrzebne pakiety znajdujące się w pliku requirements.txt (polecenie: _pip install -r requirements.txt_ )
4. Jeśli korzystamy z systemu innego niż Windows, należy zakomentować/usunąć linię 49 w pliku _get_githubapi_data.py_
5. Uruchamiamy aplikacje na lokalnym serwerze uruchamiając skrypt main.py (_python3 main.py_)

## Propozycje rozwoju projektu:

- Zmiana pozyskiwania danych przez aplikację strony WWW (obecnie wykonuje ona zapytanie HTTP do serwera na którym sama się znajduje - poprzez zaimplementowane mini-API, nie jest to optymalne rozwiązanie)
- Rozbudowa rodzajów pozyskiwanych danych
- Zapis pozyskanych danych w bazie danych, w celu obserwacji rozwoju aktywności użytkowników/repozytoriów (np. poprzez generowanie cyklicznych raportów)
