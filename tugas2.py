def ganjil(bawah, atas):
    bilangan_ganjil = []
    
    if bawah < atas:
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                bilangan_ganjil.append(i)
    else:
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                bilangan_ganjil.append(i)
    
    return ', '.join(map(str, bilangan_ganjil))

print(ganjil(10, 30))
print(ganjil(97, 82))
