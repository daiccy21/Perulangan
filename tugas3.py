def hitung_ips():
    jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))
    total_nilai = 0

    for i in range(jumlah_mata_kuliah):
        nilai = input(f"Masukkan nilai untuk mata kuliah {i + 1} (A/B/C/D): ").upper()
        bobot = 4 if nilai == 'A' else 3 if nilai == 'B' else 2 if nilai == 'C' else 1 if nilai == 'D' else 0
        total_nilai += bobot * 3

    ips = total_nilai / (jumlah_mata_kuliah * 3) if jumlah_mata_kuliah > 0 else 0
    print(f"Indeks Prestasi Semester (IPS) Anda adalah: {ips:.2f}")

hitung_ips()