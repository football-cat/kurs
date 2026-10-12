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
  Klawisze: 1–9, `0` (podwójna szerokość), `000`, `,`, `C`, `⌫`, `⇅` (następna waluta, kolor akcentu).
- **Kolory systemowe iOS** (#f2f2f7 / #000, akcent #007aff / #0a84ff), jasny i ciemny tryb zawsze oba.
  Delikatna poświata tła w kolorze flagi Albanii; w trybie ściemokursu akcent i poświata → pomarańcz (#ff9500).
- **Brak przewijania, zoomu i zaznaczania tekstu**; `prefers-reduced-motion` respektowane.
- **Ruch tylko jako odpowiedź na akcję** (wciśnięcie, zmiana waluty, przełączenie trybu), sprężyste krzywe.
- Unikaj szablonowych tików: etykiety WERSALIKAMI, ciągi „A · B · C”, karty na wszystko.

## Funkcje (nie usuwaj bez pytania)

- Trzy waluty ALL / PLN / EUR. Stuknięcie wiersza = licz od tej waluty; przytrzymanie = kopiuj kwotę (toast).
- **Ściemokurs**: przelicza lek po 100 ALL = 1 EUR; EUR/PLN zostaje rynkowy. Widać też kurs rynkowy dla porównania.
- Kurs z `https://open.er-api.com/v6/latest/EUR` (ma ALL i CORS; EBC/Frankfurter nie mają ALL).
  Fallback wbudowany + ostatni kurs w localStorage. Auto-odświeżanie po >6 h przy powrocie do apki.
  Kropka statusu: zielona = świeży, pomarańczowa = stary/przybliżony.
- **Ciekawostki o Albanii**: 68 ręcznie napisanych (tasowane bez powtórzeń) + co 5. karta losowy fragment
  z polskiej Wikipedii. Karta przypięta nad klawiaturą, stała wysokość (3 linie; 2 na niskich ekranach).
  Nowe ciekawostki dopisuj tylko, gdy są pewne faktograficznie.
- Ikona: `apple-touch-icon.png` (180 px) renderowana z `icon.svg` (bunkier-skarbonka z monetą €).
  Po zmianie ikony podbij `?v=N` w `<link rel="apple-touch-icon">`; iOS i tak wymaga ponownego dodania do ekranu.

## Pułapki iOS (już rozwiązane, nie psuj)

- Strony `data:` nie da się dodać do ekranu początkowego. Potrzebny prawdziwy adres HTTPS (stąd GitHub Pages).
- iOS 26 w trybie apki: obszar strony kończy się nad paskiem Home, a `env(safe-area-inset-bottom)` i tak
  zwraca ~34 px. Nie wymuszaj wysokości z `screen.height` (ucina klawiaturę). Używaj `position:fixed; inset:0`,
  klasa `.gap` zdejmuje dolny margines, a `html{background}` = tło strony, żeby pas pod spodem nie odstawał.
- Clipboard w Safari tylko w handlerze zdarzenia (kopiowanie na `pointerup`, nie w `setTimeout`).

## Przed każdym pushem

1. Składnia JS: `node -e "new Function(...skrypt z index.html...)"`.
2. Zrzuty Playwright (Chromium, `is_mobile`, `has_touch`): 390×786 jasny i ciemny, 375×647 (SE).
   Obejrzyj je: nic nie może być ucięte, klawiatura cała widoczna, ciekawostki widoczne.
3. Commit po polsku, push na `main`. Pages publikuje sam w 1–2 min.

## Wdrożenie / GitHub

- Repo: `football-cat/kurs`, gałąź `main`, Pages z `/ (root)` (włączone ręcznie w Settings → Pages;
  endpoint API Pages jest zablokowany z sesji Claude).
- Sesja Claude nie może tworzyć nowych repo; do istniejących dostęp przez podpięcie repo.
