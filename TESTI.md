## 1. Programmas apraksts

05_min_un_max.py,
Lietotājs norāda skaitļu daudzumu (veselu skaitli) un pēc tam ievada pašus skaitļus,
Programmai jāizvada mazākais un lielākais no lietotāja ievadītajiem skaitļiem,
Algoritma darbība:
1. Algoritms prasa ievadīt cikla reižu skaitu (SycleRange).
2. Pārbauda, vai skaits nav 0 vai negatīvs.
3. Ja ievade ir korekta, tiek definētas sākotnējās vērtības minNumber = None un maxNumber = None.
4. Cikla ietvaros nolasa lietotāja skaitļus un salīdzina tos ar pašreizējo minimumu un maksimumu, nepieciešamības gadījumā tos pārrakstot.
5. Beigās izvada rezultātu. Nepareizas ievades (teksta) gadījumā nostrādā try...except ValueError bloks un izvada kļūdas paziņojumu.


## 2. Izpildes izsekošana

Izvēlētā ievade: SycleRange = 2; skaitļi = 5, 10.

```markdown
| Solis | Nosacījums       | Mainīgie pirms  | Veiktā darbība        | Mainīgie pēc    |                   Izvade                   |
|-------|------------------|-----------------|-----------------------|-----------------|--------------------------------------------|
| 0     |         —        |        -        | Sākums  - try         |       -         |                                            |
| 1     |                  |        -        | Ievada SycleRange=2   |  SycleRange=2   |      Cik skaitļus jūs gribat ievadīt?      |
| 2     |      2 == 0      |   SycleRange=2  |  Nosacījums aplams    |  SycleRange=2   |                                            |
| 3     |       2 < 0      |   SycleRange=2  |  Nosacījums aplams    |  SycleRange=2   |                                            |
| 4     |        else      |   SycleRange=2  |  Inicializē min/max   |  minNumber=None,|                                            |
|       |                  |                 |                       |  maxNumber=None |                                            |
| 5     |      for i=0     |    min/max=None |Cikls 1 solis,ievada 5 |i=0,UserNumber=5 |          Ievadi savu 1 skaitli:            |
| 6     |None==None or 5<0 | min=None, User=5| Patiess, maina min    |   minNumber=5   |                                            |
| 7     |None==None or 5>0 |  maxNumber=None | Patiess, maina max    |   maxNumber=5   |                                            |
| 8     |      for i=1     |   min=5, max=5  |Cikla 2 solis,ievada 10|i=1,UserNumber=10|          Ievadi savu 2 skaitli:            |
| 9     | 5==None or 5>10  |  min=5, User=10 |  Nosacījums aplams    |   minNumber=5   |                                            |
| 10    | 5==None or 5<10  |  max=5, User=10 | Atjaunina maksimumu   |   maxNumber=10  |                                            |
| 11    |Cikla beigas      |  min=5, max=10  |   Izvada rezultātu    |  min=5, max=10  |Mazakais skaitlis: 5, lielākais skaitlis: 10|
```

## 3. Testa piemēri

Izveido vismaz četrus atšķirīgus testus.

```markdown
| Testa veids               | Ievade                          | Sagaidāmais rezultāts                  | Faktiskais rezultāts                   | Tests izturēts? |
|---------------------------|---------------------------------|----------------------------------------|----------------------------------------|-----------------|
| Tipisks                   | SycleRange=2; skaitļi: 5, 10    |     Min: 5, Max: 10                    |         Min: 5, Max: 10                |      Jā         |
| Robežgadījums             | SycleRange=0                    |Cikls ir pabeigts, jo skaitlis vienāds 0|Cikls ir pabeigts, jo skaitlis vienāds 0|      Jā         |
| Tukša vai nederīga ievade | SycleRange="a"                  |     Tas nav skaitlis                   |   Tas nav skaitlis                     |      Jā         |
| Papildu tests             | SycleRange=3; skaitļi: 5, 0, 10 |     Min: 0, Max: 10                    |         Min: 0, Max: 10                |      Jā         |
```

## 4. Kļūda, pretpiemērs vai uzlabojums

Tā kā pašreizējā koda versija visus testus iztur veiksmīgi, atskatāmies uz agrāko kļūdaino solīti:
Ievade: SycleRange=2; skaitļi = 5, 10 
Sagaidāmais rezultāts: Min: 5, Max: 10
Faktiskais rezultāts: TypeError: '>' not supported between instances of 'NoneType' and 'int'
Kļūdas cēlonis: Agrākajā versijā nosacījums bija uzrakstīts kā if (minNumber > UserNumber or minNumber == None):,
    Tā kā Python pārbauda izteiksmes no kreisās uz labo pusi, tas vispirms mēģināja salīdzināt None > 5, kas izraisīja sistēmas kļūdu (TypeError).   
Veiktais labojums: Jaunajā koda versijā pārbaudes tika samainītas vietām: if (minNumber == None or minNumber > UserNumber):, 
    Tā kā pirmais nosacījums minNumber == None ir patiess pirmajā iterācijā, Python izmanto saīsināto novērtēšanu (short-circuit evaluation) un otro daļu nemaz nemēģin rēķināt, tādējādi novēršot TypeError rašanos.
