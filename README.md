# Quine-McCluskey
[![Build Status](https://travis-ci.org/codecentric/springboot-sample-app.svg?branch=master)](https://travis-ci.org/codecentric/springboot-sample-app)

==========Risolutore reti logiche==========
1) Karnaugh
2) Quine-McCluskey
0) Exit
Enter a number: 

Selezionando la prima opzione bisognerà inserire i mintermini ed eventuali dont'care separati da spazi
-- in caso di assenza di DC lasciare vuoto e premere invio:

Esempio karnaugh:
f(a,b,c,d) = ON(1,2,6,8,9,10,14) DC(7,13,15)

    risolutore di mappe di karnaugh 4 x 4 
    prima si avra' una semplificazione con karnaugh, poi copiare il risultato di Quine-McCluskey
    Mintermini: 1 2 6 8 9 10 14 
    DC: 7 13 15

    0 1 0 1 
    0 0 - 1 
    0 - - 1 
    1 1 0 1 


    f(A,B,C,D) = A'B+BC+B'C'D+AB'C'+A'C'D+AB'D
    minimizzazione di QuineMcCluskey:  F = AB'C' + B'C'D + CD'
    
Esempio Quine-McCluskey
f(a,b,c,d) = ON(1,2,6,8,9,10,14) DC(7,13,15)

    -!-!-!---inserire i valori separandoli con lo spazio---!-!-!-
    - Caso 1 funzione:
       inserire prima gli implicanti
       successivamente inserire i dc
    - Caso 2 funzioni:
       inserire prima gli implicanti primi della PRIMA funzione 
       inserire gli implicanti primi della SECONDA funzione, ripetendo eventuali implicanti
       successivamente inserire i dc della prima funzione e poi quelli della seconda, ripetendo i duplicati
    _________________________________________________________________________________________________________________________________
    non vengono gestite le etichette, quindi quando copiate le variabili e le trovate duplicate, associate manualmente l'etichetta 11
    Mintermini: 1 2 6 8 9 10 14
    DC: 7 13 15


    
            Mintermini		Binary Mintermini
    ==================================================
    |    1:
    |		    1                   0001
    |		    2                   0010
    |		    8                   1000
    --------------------------------------------------
    |    2:
    |		    6                   0110
    |		    9                   1001
    |		    10                  1010
    --------------------------------------------------
    |    3:
    |		    7                   0111
    |		    13                  1101
    |		    14                  1110
    --------------------------------------------------
    |    4:
    |		    15                  1111
    --------------------------------------------------
    Implicanti primi di questa tabella: None




            Mintermini		Binary Mintermini
    ==================================================
    |    0:
    |		1,9                     -001
    |		2,6                     0-10
    |		2,10                    -010
    |		8,9                     100-
    |		8,10                    10-0
    --------------------------------------------------
    |    1:
    |		6,7                     011-
    |		6,14                    -110
    |		9,13                    1-01
    |		10,14                   1-10
    --------------------------------------------------
    |    2:
    |		7,15                    -111
    |		13,15                   11-1
    |		14,15                   111-
    --------------------------------------------------
    Implicanti primi di questa tabella: -001, 11-1, 10-0, 100-, 1-01




            Mintermini		Binary Mintermini
    ==================================================
    |    0:
    |		2,6,10,14               --10
    --------------------------------------------------
    |    1:
    |		6,7,14,15               -11-
    --------------------------------------------------
    Implicanti primi di questa tabella: -11-, --10


    tutti gli implicanti primi:  -001, 11-1, 100-, -11-, 10-0, 1-01, --10



    Implicanti primi (caratteri):

        Minterms    | 1  2  6  8  9 10 14
    =====================================
    1,9             | X           X
    -------------------------------------
    13,15           |
    -------------------------------------
    8,9             |          X  X
    -------------------------------------
    6,7,14,15       |       X           X
    -------------------------------------
    8,10            |          X     X
    -------------------------------------
    9,13            |             X
    -------------------------------------
    2,6,10,14       |    X  X        X  X
    -------------------------------------

    Implicanti primi essenziali: -001, --10


     Soluzione: F = AB'C' + B'C'D + CD'
