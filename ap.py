import streamlit as st
import pandas as pd
import random

st.title("📅 Jadwal Piket Kelas")

st.write("Masukkan daftar nama siswa (pisahkan dengan koma):")
nama_siswa = st.text_area("Nama siswa", "Andi, Budi, Citra, Deni, Eka")

jumlah_piket = st.number_input("Jumlah siswa per hari", 1, 10, 2)

if st.button("Buat Jadwal"):
    nama_list = [n.strip() for n in nama_siswa.split(",") if n.strip()]
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    jadwal = {h: [] for h in hari}

    random.shuffle(nama_list)
    i = 0
    for h in hari:
        for _ in range(jumlah_piket):
            jadwal[h].append(nama_list[i % len(nama_list)])
            i += 1

    df = pd.DataFrame(
        [(h, ", ".join(s)) for h, s in jadwal.items()],
        columns=["Hari", "Petugas Piket"]
    )
    st.success("✅ Jadwal berhasil dibuat!")
    st.dataframe(df)
