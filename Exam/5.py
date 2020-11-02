def MysteryWrite(n):
  if (n > 0):
     print(n)
     MysteryWrite(n-2)
  print(n + 1)

MysteryWrite(4)