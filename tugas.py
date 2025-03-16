def perkalian(a, b):
    hasil = b * a
    langkah = " + ".join([str(b)] * a)  
    print(f"{a} x {b} = {langkah} = {hasil}")

perkalian(6, 5)   
perkalian(7, 10)  