import streamlit as st
import pandas as pd
import random
from io import BytesIO

st.set_page_config(page_title="Jadwal Piket Kelas", page_icon="📅", layout="centered")

st.title("📅 Jadwal Piket Kelas TKJ")
st.markdown("Selamat datang di aplikasi **Jadwal Piket Kelas TKJ**! 🎓")

# --- Input Data ---
st.subheader("👩‍🏫 Input Data Siswa")
nama_siswa = st.text_area(
    "Masukkan nama siswa (pisahkan dengan koma):",
    "Andi, Budi, Citra, Deni, Eka, Fajar, Gita"
)

jumlah_piket = st.number_input("Jumlah siswa per hari", 1, 10, 2)

kelas = st.text_input("Nama Kelas", "XII TKJ 1")

if st.button("🚀 Buat Jadwal Piket"):
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

    st.success(f"✅ Jadwal piket untuk {kelas} berhasil dibuat!")
    st.dataframe(df, use_container_width=True)

    # --- Download ke Excel ---
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Jadwal Piket')
    st.download_button(
        label="📥 Download Jadwal (Excel)",
        data=output.getvalue(),
        file_name=f"Jadwal_Piket_{kelas.replace(' ', '_')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

st.markdown("---")
st.caption("Dibuat dengan ❤️ oleh kelas TKJ menggunakan Streamlit")
