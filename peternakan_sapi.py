
import streamlit as st

st.set_page_config(page_title="Peternakan Sapi", page_icon="🐮", layout="centered")

st.title("🐮 Game Peternakan Sapi")
st.markdown("Selamat datang di peternakan sapi kamu! Rawat sapimu dan jadikan peternakanmu sukses.")

if "sapi" not in st.session_state:
    st.session_state.sapi = 1
    st.session_state.makanan = 10
    st.session_state.susu = 0

col1, col2, col3 = st.columns(3)
col1.metric("Jumlah Sapi", st.session_state.sapi)
col2.metric("Stok Makanan", st.session_state.makanan)
col3.metric("Susu Terkumpul", st.session_state.susu)

st.divider()

st.subheader("🍼 Beri Makan Sapi")
if st.button("Beri Makan"):
    if st.session_state.makanan >= st.session_state.sapi:
        st.session_state.makanan -= st.session_state.sapi
        st.success("Semua sapi kenyang dan bahagia!")
    else:
        st.warning("Makanan tidak cukup!")

st.subheader("🐄 Perah Sapi")
if st.button("Perah Susu"):
    st.session_state.susu += st.session_state.sapi
    st.success(f"Berhasil memerah {st.session_state.sapi} susu.")

st.subheader("🌾 Tambah Makanan")
if st.button("Beli 10 makanan (2 susu)"):
    if st.session_state.susu >= 2:
        st.session_state.susu -= 2
        st.session_state.makanan += 10
        st.success("Kamu membeli 10 makanan.")
    else:
        st.warning("Susu tidak cukup untuk membeli makanan.")

st.subheader("🐮 Tambah Sapi")
if st.button("Beli 1 sapi (10 susu)"):
    if st.session_state.susu >= 10:
        st.session_state.susu -= 10
        st.session_state.sapi += 1
        st.success("Kamu membeli 1 sapi baru!")
    else:
        st.warning("Susu tidak cukup untuk membeli sapi.")
