def addressVal(Address):
  dot = Address.find(".")
  at = Address.find("@")
  email = Address.find("email")
  if (dot == -1):
    print("missing . ")
  elif (at == -1):
    print("missing @")
  elif (email == -1):
    print("missing word email ")
  else:
    print("valid")
    
  print("program ini akan mengecek apakah input yang anda berikan adalah alamat email atau bukan")
  while(True):
    print("alamat email yang benar membutuhkan simbol '@','.', dan 'email' ")
    x = input ("silahkan isi alamat email anda:")
    addressVal(x)