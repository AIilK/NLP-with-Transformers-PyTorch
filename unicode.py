import unicodedata

c_with_cedilla = "\u00C7"
print(c_with_cedilla)

c_plus_cedilaa = "\u0043\u0327"
print(c_plus_cedilaa)

print(c_plus_cedilaa == c_with_cedilla)
#nfd tajzie mikonim 
print(unicodedata.normalize('NFD' , c_with_cedilla))
print(unicodedata.normalize('NFD' , c_with_cedilla) == c_plus_cedilaa)

#nfc miad michasbone beham 
print(unicodedata.normalize('NFC' , c_plus_cedilaa))
print( c_with_cedilla == unicodedata.normalize('NFC' , c_plus_cedilaa))

      
#compatibility 
fancy_h_with_cedilla = "\u210B\u0327"
print(fancy_h_with_cedilla)

h_with_cedilla = "\u1e28"
print(h_with_cedilla)

unicodedata.normalize('NFKC', fancy_h_with_cedilla) == h_with_cedilla