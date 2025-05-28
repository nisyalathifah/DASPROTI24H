# Gabungkan semua isi modul menjadi satu file Python utuh (tanpa folder modul)
all_in_one_py = '''# Sistem E-Voting Organisasi Mahasiswa

# Data Awal
pemilih_list = []
calon_list = []

# Fungsi Tambah Pemilih
def tambah_pemilih(pemilih_list, id, nama, jurusan):
    for p in pemilih_list:
        if p["id"] == id:
            print("❌ ID pemilih sudah terdaftar!")
            return
    pemilih_list.append({
        "id": id,
        "nama": nama,
        "jurusan": jurusan,
        "sudah_memilih": False
    })
    print("✅ Pemilih berhasil ditambahkan.")

# Fungsi Tambah Calon
def tambah_calon(calon_list, id, nama, visi):
    for c in calon_list:
        if c["id"] == id:
            print("❌ ID calon sudah terdaftar!")
            return
    calon_list.append({
        "id": id,
        "nama": nama,
        "visi": visi,
        "jumlah_suara": 0
    })
    print("✅ Calon berhasil ditambahkan.")

# Fungsi Voting
def voting(pemilih_list, calon_list, id_pemilih, id_calon):
    pemilih = next((p for p in pemilih_list if p["id"] == id_pemilih), None)
    if not pemilih:
        print("❌ ID pemilih tidak ditemukan.")
        return
    if pemilih["sudah_memilih"]:
        print("⚠️ Pemilih sudah menggunakan hak suaranya.")
        return

    calon = next((c for c in calon_list if c["id"] == id_calon), None)
    if not calon:
        print("❌ ID calon tidak ditemukan.")
        return

    calon["jumlah_suara"] += 1
    pemilih["sudah_memilih"] = True
    print("🗳️ Voting berhasil.")

# Fungsi Tampilkan Hasil
def tampilkan_hasil(calon_list):
    if not calon_list:
        print("Belum ada calon.")
        return
    print("\\n📊 Hasil Sementara:")
    for c in calon_list:
        print(f"{c['nama']} ({c['id']}): {c['jumlah_suara']} suara")

# Fungsi Statistik
def tampilkan_statistik(pemilih_list, calon_list):
    total = len(pemilih_list)
    sudah = sum(1 for p in pemilih_list if p["sudah_memilih"])
    persen = (sudah / total * 100) if total > 0 else 0

    print("\\n📈 Statistik Pemilu:")
    print(f"Total pemilih       : {total}")
    print(f"Sudah memilih       : {sudah}")
    print(f"Persentase partisipasi : {persen:.2f}%")

    if calon_list:
        calon_teratas = max(calon_list, key=lambda c: c["jumlah_suara"])
        print(f"Pemenang sementara  : {calon_teratas['nama']} ({calon_teratas['jumlah_suara']} suara)")

# Menu Utama
def menu():
    while True:
        print("\\n===== MENU E-VOTING =====")
        print("1. Tambah Pemilih")
        print("2. Tambah Calon")
        print("3. Voting")
        print("4. Lihat Hasil Sementara")
        print("5. Statistik Pemilu")
        print("6. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            id = input("ID Pemilih: ")
            nama = input("Nama: ")
            jurusan = input("Jurusan: ")
            tambah_pemilih(pemilih_list, id, nama, jurusan)

        elif pilih == "2":
            id = input("ID Calon: ")
            nama = input("Nama: ")
            visi = input("Visi Misi: ")
            tambah_calon(calon_list, id, nama, visi)

        elif pilih == "3":
            id_pemilih = input("ID Pemilih: ")
            id_calon = input("ID Calon: ")
            voting(pemilih_list, calon_list, id_pemilih, id_calon)

        elif pilih == "4":
            tampilkan_hasil(calon_list)

        elif pilih == "5":
            tampilkan_statistik(pemilih_list, calon_list)

        elif pilih == "6":
            print("Terima kasih!")
            break

        else:
            print("❌ Pilihan tidak valid.")

menu()
'''

# Simpan ke satu file Python
all_in_one_path = "/mnt/data/e_voting.py"
with open(all_in_one_path, "w") as f:
    f.write(all_in_one_py)

all_in_one_path
