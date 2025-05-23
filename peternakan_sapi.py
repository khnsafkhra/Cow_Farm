import streamlit as st

# Inisialisasi state dengan session_state agar data tetap ada saat refresh tombol
if 'money' not in st.session_state:
    st.session_state.money = 100
if 'cows' not in st.session_state:
    st.session_state.cows = 1
if 'milk' not in st.session_state:
    st.session_state.milk = 0
if 'food' not in st.session_state:
    st.session_state.food = 5
if 'barn_level' not in st.session_state:
    st.session_state.barn_level = 1
if 'day' not in st.session_state:
    st.session_state.day = 1

st.title("🐄 Game Peternakan Sapi (Streamlit Edition)")

st.write(f"**Hari:** {st.session_state.day}")
st.write(f"**Uang:** ${st.session_state.money}")
st.write(f"**Jumlah Sapi:** {st.session_state.cows}")
st.write(f"**Jumlah Susu:** {st.session_state.milk}")
st.write(f"**Jumlah Makanan:** {st.session_state.food}")
st.write(f"**Level Kandang:** {st.session_state.barn_level}")

def produce_milk():
    needed_food = st.session_state.cows
    if st.session_state.food >= needed_food:
        st.session_state.milk += st.session_state.cows * 2
        st.session_state.food -= needed_food
        st.success(f"Sapi memproduksi susu sebanyak {st.session_state.cows * 2} liter!")
    else:
        st.warning("Makanan sapi tidak cukup untuk produksi susu.")

def sell_milk():
    if st.session_state.milk > 0:
        income = st.session_state.milk * 5
        st.session_state.money += income
        st.session_state.milk = 0
        st.success(f"Kamu menjual susu dan mendapatkan ${income}.")
    else:
        st.info("Tidak ada susu untuk dijual.")

def buy_food():
    cost = 10
    amount = 5
    if st.session_state.money >= cost:
        st.session_state.money -= cost
        st.session_state.food += amount
        st.success(f"Kamu membeli {amount} makanan seharga ${cost}.")
    else:
        st.warning("Uang tidak cukup untuk membeli makanan.")

def buy_cow():
    cost = 50
    if st.session_state.money >= cost:
        st.session_state.money -= cost
        st.session_state.cows += 1
        st.success("Kamu membeli seekor sapi baru!")
    else:
        st.warning("Uang tidak cukup untuk membeli sapi.")

def upgrade_barn():
    cost = 100
    if st.session_state.money >= cost:
        st.session_state.money -= cost
        st.session_state.barn_level += 1
        st.success("Kandang berhasil diupgrade!")
    else:
        st.warning("Uang tidak cukup untuk upgrade kandang.")

def next_day():
    st.session_state.day += 1
    st.info(f"Hari {st.session_state.day} dimulai!")

# Tombol aksi
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🍼 Beri Makan Sapi (Produksi Susu)"):
        produce_milk()
    if st.button("💰 Jual Susu"):
        sell_milk()

with col2:
    if st.button("🍎 Beli Makanan ($10)"):
        buy_food()
    if st.button("🐄 Beli Sapi ($50)"):
        buy_cow()

with col3:
    if st.button("🏠 Upgrade Kandang ($100)"):
        upgrade_barn()
    if st.button("⏭ Next Day"):
        next_day()
