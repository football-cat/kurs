# Kurs: konwerter ALL ⇄ PLN ⇄ EUR

Jednoplikowa apka webowa (`index.html`) do szybkiego przeliczania walut w Albanii. Używana na iPhonie
jako apka z ekranu początkowego. Hosting: GitHub Pages, https://football-cat.github.io/kurs/

Właściciel: Krzysztof. Komunikacja i cały interfejs po polsku. Odpowiedzi zwięzłe, rozwiązania od razu gotowe do użycia.

## Poprzeczka jakości: od pierwszej wersji jak natywna apka iOS

Nie oddawaj „wersji roboczej strony internetowej”. Każda zmiana ma wyglądać i zachowywać się jak apka
zaprojektowana przez dobrego projektanta iOS (Apple HIG, iOS 26 / Liquid Glass). Konkretnie:

- **Hierarchia**: najważniejsza jest wpisywana kwota (duża, cienka, SF Pro Display 200, auto-dopasowanie
  szerokości jak w Kalkulatorze). Wyniki mniejsze, ale czytelne. Bez zbędnych tytułów, nagłówków sekcji i etykiet.
- **Kontrolki systemowe**: przełącznik trybu = segmented control w kształcie kapsuły; przyciski okrągłe/kapsuły
  ze „szkłem” (backdrop-filter), cele dotyku min. 44 pt; haptyka (sztuczka z `<input type=checkbox switch>`).
- **Własna klawiatura numeryczna**, nigdy systemowa. Układ telefoniczny: **1 2 3 na górze** (nie 7 8 9).
  Przelicz: 1–9, `0` (podwójna szerokość), `000`, `,`, `C`, `⌫`, `⇅` (następna waluta, kolor akcentu). Suma: patrz niżej.
- **Kolory systemowe iOS** (#f2f2f7 / #000, akcent #007aff / #0a84ff), jasny i ciemny tryb zawsze oba.
  Delikatna poświata tła w kolorze flagi Albanii; w trybie ściemokursu akcent i poświata → pomarańcz (#ff9500).
- **Brak przewijania, zoomu i zaznaczania tekstu**; `prefers-reduced-motion` respektowane.
- **Ruch tylko jako odpowiedź na akcję** (wciśnięcie, zmiana waluty, przełączenie trybu), sprężyste krzywe.
- Unikaj szablonowych tików: etykiety WERSALIKAMI, ciągi „A · B · C”, karty na wszystko.

## Funkcje (nie usuwaj bez pytania)

Trzy karty w pływającym pasku kart na dole (kapsuła iOS 26): **Przelicz**, **Suma** i **Notatnik**. Przełącznik
Rynkowy/Ściemokurs i przycisk odświeżania są wspólne dla obu. Ostatnia karta zapamiętana w localStorage.

**Suma** (kalkulator dodający, jak taśma maszyny liczącej):
- Wpisz kwotę, wybierz walutę pozycji (segment ALL/PLN/EUR nad klawiaturą), stuknij `+` (dodaj) lub `−` (odejmij).
  Pusty `+`/`−` = potrząśnięcie polem wpisywania.
- Klawiatura: `1 2 3 C / 4 5 6 ⌫ / 7 8 9 − / 0 000 , +` (`+` w kolorze akcentu).
- Suma duża w wybranej walucie, pozostałe dwie jako kapsuły; stuknięcie kapsuły zmienia walutę sumy.
  Przytrzymanie sumy = kopiuj.
- Lista pozycji (szklana lista zgrupowana, najnowsze na górze): przesunięcie w lewo odsłania „Usuń”. „Wyczyść” wymaga drugiego stuknięcia („Wyczyścić wszystko?”).
  Po usunięciu i wyczyszczeniu toast z „Cofnij” (4,5 s).
- Kwoty w Sumie zawsze z 2 miejscami (`fmtS`), kapsuły walut przy braku miejsca tracą flagi, potem zmniejszają się.
- Pozycje zapisane w localStorage (`items`), przeliczane bieżącym kursem i trybem (ściemokurs też).
- Liczby zawsze grupowane spacją (także 4-cyfrowe: „1 050”), żeby wynik wyglądał jak wpisywana kwota.

**Notatnik** (jak Soulver, klawiatura systemowa):
- Linia = opis + kwota. Liczy się ostatnie wyrażenie w linii (`parseLine`): `pizza 3 × 800`, `taxi 500 + 300`,
  `reszta -200` (minus przed liczbą odejmuje), `/` dzieli. Tysiące: `2 400`, `1.500`; przecinek = grosze.
- Waluta w kapsule po prawej (menu jak w iOS: Lek / Złoty / Euro). `€`/`eur`, `zł`/`pln`, `lek`/`ALL` w tekście
  przestawiają walutę linii; usunięcie znacznika wraca do waluty bazowej linii (`L.b`). Wybór z menu ustawia też
  walutę domyślną nowych linii (`NT.def`, localStorage `ndef`).
- Po prawej: kwota w walucie linii + przeliczenie na PLN (dla linii w PLN – na EUR). `#` na początku = nagłówek.
- Enter dzieli linię w miejscu kursora, Backspace na początku łączy z poprzednią, stuknięcie pod listą = nowa linia.
- Pasek na dole: sumy w użytych walutach (każda w osobnej linii) i razem w PLN. Ściemokurs działa też tu.
- Udostępnij (tekst z kwotami i sumą, `navigator.share`), Wyczyść (drugie stuknięcie + Cofnij). Zapis w localStorage `notes`.
- Przy otwartej klawiaturze (`.kbd`, `visualViewport`) apka kurczy się do widocznej części, pasek kart znika,
  suma zostaje nad klawiaturą; `fitLayout` wtedy nic nie robi. Pola mają 17 px (iOS nie zoomuje przy ≥16 px).

**Przelicz**:

- Trzy waluty ALL / PLN / EUR. Stuknięcie wiersza = licz od tej waluty; przytrzymanie = kopiuj kwotę (toast).
- **Ściemokurs**: przelicza lek po kursie „ściemy” 1 EUR = SR ALL (domyślnie **90**, tzn. 2000 ALL = 22,22 EUR);
  EUR/PLN zostaje rynkowy. SR ustawiany w arkuszu (stuknij „Zmień” przy kursie albo ponownie aktywny segment
  „Ściemokurs”): −/+ (przytrzymanie powtarza), szybkie 90 / 95 / 100, zakres 50–150, zapis w localStorage `sr`.
  Arkusz pokazuje przykład 2000 ALL w EUR po ściemie i rynkowo. Widać też kurs rynkowy dla porównania.
- Kurs: `open.er-api.com` → rezerwowo currency-api z jsDelivr (`@fawazahmed0/currency-api`) → `latest.currency-api.pages.dev`
  (wszystkie z ALL i CORS, bez klucza; EBC/Frankfurter nie mają ALL). Potem ostatni zapisany kurs (localStorage),
  na końcu wbudowany (13.10.2026: 1 EUR = 91,55 ALL = 4,387 PLN). Auto-odświeżanie po >6 h przy powrocie do apki,
  ręczne odświeżenie pokazuje komunikat. Status: „Kurs: dziś, 02:02” / „wczoraj” / data; kropka zielona = świeży,
  pomarańczowa = starszy niż 3 dni albo przybliżony.
- Gest jak w Kalkulatorze: przesunięcie palcem w poziomie po wyświetlaczu (wiersze walut / pole wpisywania Sumy)
  usuwa ostatnią cyfrę.
- **Ciekawostki o Albanii**: 68 ręcznie napisanych (tasowane bez powtórzeń) + co 5. karta losowy fragment
  z polskiej Wikipedii. Karta przypięta nad klawiaturą, stała wysokość (3 linie; 2 w trybie zwartym;
  ukryta, gdy inaczej klawisze musiałyby być mniejsze niż 52 pt).
  Nowe ciekawostki dopisuj tylko, gdy są pewne faktograficznie.
- Ikona: `apple-touch-icon.png` (180 px) renderowana z `icon.svg` (bunkier-skarbonka z monetą €).
  Po zmianie ikony podbij `?v=N` w `<link rel="apple-touch-icon">`; iOS i tak wymaga ponownego dodania do ekranu.

## PWA: offline, manifest, ekrany startowe

- `sw.js`: strona najpierw z sieci (limit 2,5 s), offline z pamięci; pliki statyczne z pamięci z odświeżaniem w tle;
  zapytania o kurs (inne domeny) nie są przechwytywane. Podbij `V` w `sw.js`, gdy zmieniasz listę `SHELL`.
  Rejestracja tylko na https/localhost. Test offline: `python3 -m http.server` + Playwright `context.set_offline(True)`.
- `manifest.json` (+ `icon-192.png`, `icon-512.png` z `icon.svg`).
- `splash/*.png`: ekrany startowe = tło apki z poświatą (bez UI, żeby nic nie skakało przy starcie), jasne i ciemne,
  dla 11 rozmiarów iPhone'ów; generowane numpy (bez szumu, ~60 KB). Nowy rozmiar iPhone'a = dopisz do listy i `<link>`.
- Poziomo (`.land`): treść w lewej połowie, klawiatura (i pole wpisywania Sumy) przypięte w prawej, ciekawostki ukryte.

## Pułapki iOS (już rozwiązane, nie psuj)

- Strony `data:` nie da się dodać do ekranu początkowego. Potrzebny prawdziwy adres HTTPS (stąd GitHub Pages).
- iOS 26 w trybie apki: obszar strony kończy się nad paskiem Home, a `env(safe-area-inset-bottom)` i tak
  zwraca ~34 px. Nie wymuszaj wysokości z `screen.height` (ucina klawiaturę). Używaj `position:fixed; inset:0`,
  klasa `.gap` zdejmuje dolny margines, a `html{background}` = tło strony, żeby pas pod spodem nie odstawał.
- Clipboard w Safari tylko w handlerze zdarzenia (kopiowanie na `pointerup`, nie w `setTimeout`).
- **Wyspa / pasek statusu zabiera ~59 pt u góry** (iPhone 14 Pro+), a strona w trybie apki kończy się nad paskiem
  Home. Na iPhonie 16 Pro zostaje ok. 732 pt na całość. Zrzuty bez tej wstawki kłamią (tak powstał błąd, w którym
  pasek kart zasłaniał dolny rząd klawiszy).
- Układ jest dopasowywany w JS (`fitLayout`), nie media queries: pomiar karty Przelicz i Sumy naraz, wspólna
  wysokość klawiszy `--kh` (58→44 pt) dla obu kart (klawiatura nie skacze przy przełączaniu), poziomy ustępstw:
  `.c1` (zwarty nagłówek i pasek kart, gdy `.app` < 780 pt) → `.tight` (mniejszy wyświetlacz) → `.notv` (bez ciekawostek).
  `.pane{overflow:hidden}` + `ResizeObserver` → nic nigdy nie wchodzi pod pasek kart. Nowe elementy dodawaj tak,
  żeby `fitLayout` je uwzględniał.

## Przed każdym pushem

1. Składnia JS: `node -e "new Function(...skrypt z index.html...)"`.
2. `python3 tools/realtest.py` (z katalogu repo): symuluje realne iPhone'y w trybie apki (16 Pro 393×791 z wyspą 59 pt,
   SE 375×667 z paskiem 20 pt, Pro Max 440×895, 16 Pro poziomo 852×372), jasny i ciemny, **obie karty**; wypisuje elementy wchodzące pod
   pasek kart (`over` musi być puste).
   Zrzuty trafiają do /tmp/r_*.png. Obejrzyj je: nic nie może być ucięte ani zasłonięte, klawiatura i pasek kart całe widoczne.
   W Sumie przetestuj dodawanie w różnych walutach, odejmowanie, usuwanie przesunięciem i sprawdź sumę rachunkiem.
3. Commit po polsku, push na `main`. Pages publikuje sam w 1–2 min.

## Wdrożenie / GitHub

- Repo: `football-cat/kurs`, gałąź `main`, Pages z `/ (root)` (włączone ręcznie w Settings → Pages;
  endpoint API Pages jest zablokowany z sesji Claude).
- Sesja Claude nie może tworzyć nowych repo; do istniejących dostęp przez podpięcie repo.
