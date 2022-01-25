teksts = input ("Ievadi tekstu: ")
def reverseSentence(text):
  sar1 = text.split(";") 
  if len(sar1)>2:
    sar1.reverse()
    teksts = ""
    for elements in sar1:
      teksts += elements + ";"
    print (teksts)
  else: 
    teksts = "Pārāk īss teikums!"
    print(teksts)
  return teksts 
reverseSentence(teksts)