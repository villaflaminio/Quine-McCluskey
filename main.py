import KM
import QuineMcCluskey

if __name__ == '__main__':
   print("==========Risolutore reti logiche==========")
   print("1) Karnaugh")
   print("2) Quine-McCluskey")
   print("0) Exit")

   x = int(input("Enter a number: "))
   if(x == 1):
      print("risolutore di mappe di karnaugh 4 x 4 ")
      print("prima si avra' una semplificazione con karnaugh, poi copiare il risultato di Quine-McCluskey")

      mt = [int(i) for i in input("Mintermini: ").strip().split()]
      dc = [int(i) for i in input("DC: ").strip().split()]
      KM.karnaugh(mt,dc)
      QuineMcCluskey.blockPrint()
      minimization = QuineMcCluskey.quineMcCluskey(mt,dc)
      QuineMcCluskey.enablePrint()
      print("minimizzazione di QuineMcCluskey: " + minimization)

   if (x == 2):
      print("-!-!-!---inserire i valori separandoli con lo spazio---!-!-!-")

      print("- Caso 1 funzione:")
      print("   inserire prima gli implicanti")
      print("   successivamente inserire i dc")
      print("- Caso 2 funzioni:")
      print("   inserire prima gli implicanti primi della PRIMA funzione ")
      print("   inserire gli implicanti primi della SECONDA funzione, ripetendo eventuali implicanti")
      print("   successivamente inserire i dc della prima funzione e poi quelli della seconda, ripetendo i duplicati")
      print("_________")
      print("non vengono gestite le etichette, quindi quando copiate le variabili e le trovate duplicate, associate manualmente l'etichetta 11")
      mt = [int(i) for i in input("Mintermini: ").strip().split()]
      dc = [int(i) for i in input("DC: ").strip().split()]
      QuineMcCluskey.quineMcCluskey(mt,dc)
      print("end")