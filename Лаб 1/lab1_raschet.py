
Disk = 1.44
Stanica = 100
Strok = 50
Simvol = 25
Kod = 4

Size_book = Kod*Simvol*Strok*Stanica
Size_book_kb = Size_book / 1024
Size_book_mb = Size_book_kb / 1024

kol_vo = round(1.44/Size_book_mb, )



print("Количество книг, помещающихся на дискету:", kol_vo)
