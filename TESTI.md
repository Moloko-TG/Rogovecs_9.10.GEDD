## 1. Programmas apraksts

05_min_un_max.py,
Lietotājs norāda skaitļu daudzumu (veselu skaitli) un pēc tam ievada pašus skaitļus,
Programmai jāizvada mazākais un lielākais no lietotāja ievadītajiem skaitļiem,
Algoritma darbība:
1. Algoritms prasa ievadīt cikla reižu skaitu (SycleRange).
2. Pārbauda, vai skaits nav 0 vai negatīvs.
3. Ja ievade ir korekta, tiek definētas sākotnējās vērtības minNumber = 0 un maxNumber = 0.
4. Cikla ietvaros nolasa lietotāja skaitļus un salīdzina tos ar pašreizējo minimumu un maksimumu, nepieciešamības gadījumā tos pārrakstot.
5. Beigās izvada rezultātu. Nepareizas ievades (teksta) gadījumā nostrādā try...except ValueError bloks un izvada kļūdas paziņojumu.


## 2. Izpildes izsekošana

Izvēlētā ievade: SycleRange = 2; skaitļi = 5, 10.

```markdown
| Solis | Nosacījums | Mainīgie pirms  | Veiktā darbība        | Mainīgie pēc    |                   Izvade                   |
|------:|------------|-----------------|-----------------------|-----------------|--------------------------------------------|
| 0     |     —      |        -        | Sākums  - try         |       -         |                                            |
| 1     |            |        -        | Ievada SycleRange=2   |  SycleRange=2   |      Cik skaitļus jūs gribat ievadīt?      |
| 2     |   2 == 0   |   SycleRange=2  |  Nosacījums aplams    |  SycleRange=2   |                                            |
| 3     |   2 < 0    |   SycleRange=2  |  Nosacījums aplams    |  SycleRange=2   |                                            |
| 4     |   else     |   SycleRange=2  |  Inicializē min/max   |  minNumber=0,   |                                            |
|       |            |                 |                       |  maxNumber=0    |                                            |
| 5     |  for i=0   |    min/max=0    |Cikls 1 solis,ievada 5 |i=0,UserNumber=5 |          Ievadi savu 1 skaitli:            |
| 6     |   0 > 5    |   minNumber=0   |  Nosacījums aplams    |   minNumber=0   |                                            |
| 7     |   0 < 5    |   maxNumber=0   | Atjaunina maksimumu   |   maxNumber=5   |                                            |
| 8     |  for i=1   |   maxNumber=5   |Cikla 2 solis,ievada 10|i=1,UserNumber=10|          Ievadi savu 2 skaitli:            |
| 9     |   0 > 10   |   minNumber=0   |  Nosacījums aplams    |   minNumber=0   |                                            |
| 10    |   5 < 10   |   maxNumber=5   | Atjaunina maksimumu   |   maxNumber=10  |                                            |
| 11    |Cikla beigas|  min=0, max=10  |    Izvada rezultātu   |  min=0, max=10  |Mazakais skaitlis: 0, lielākais skaitlis: 10|
```

## 3. Testa piemēri

Izveido vismaz četrus atšķirīgus testus.

```markdown
| Testa veids | Ievade | Sagaidāmais rezultāts | Faktiskais rezultāts | Tests izturēts? |
|-------------|--------|-----------------------|---------------------|-----------------|
| Tipisks     |        |                       |                     |                 |
| Robežgadījums |      |                       |                     |                 |
| Tukša vai nederīga ievade | |                 |                     |                 |
| Papildu tests |      |                       |                     |                 |
```

## 4. Kļūda, pretpiemērs vai uzlabojums

Ja tests atklāj kļūdu, pieraksti ievadi, sagaidāmo rezultātu, faktisko rezultātu, kļūdas cēloni un labojumu.

Ja programma visus testus iztur, izvēlies agrāku kļūdainu `commit` vai paskaidro, kura ievade radītu kļūdu bez vienas no tavām pārbaudēm.

**Ieteiktais commit:** `Pievienots algoritms un tā testi`

## Programmēšanas ĢEDD iesniegšanas pārbaude

- [ ] repozitorijs atveras Gitea;
- [ ] repozitorijā ir README un sāktie `.py` faili;
- [ ] programmās redzams `if`, `for` un `while` lietojums;
- [ ] programmas ir palaistas un pārbaudītas;
- [ ] versiju vēsturē ir vismaz trīs jēgpilni `commit`;
- [ ] jaunākā versija nosūtīta ar `push`;
- [ ] repozitorija saite iesniegta skolotājam.

## Algoritmu pamatu ĢEDD iesniegšanas pārbaude

- [ ] repozitorijā ir vismaz viens 4.–9. uzdevuma `.py` fails;
- [ ] algoritms darbojas vai ir skaidri norādīta atrastā kļūda;
- [ ] kodā izmantots cikls, nosacījums un mainīgo vērtību atjaunināšana;
- [ ] failā `TESTI.md` redzama izpildes izsekošana;
- [ ] izveidoti vismaz četri atšķirīgi testi;
- [ ] ir tipiska, robežas un tukša vai nederīga ievade;
- [ ] izmaiņas saglabātas ar `commit` un `push`;
- [ ] aizpildīts pašvērtējums.
