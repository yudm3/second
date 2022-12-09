import streamlit as st

st.header("Yugay Dmitriy:sunglasses:")

st.header("21900844")

st.title("Order")

st.image("mcdonalds-menu.png", width=300)

choice = st.radio(
    "What would you like?", ["Sandwich Only", "Set (Sandwich + Fries + Coke)"]
)

price = 0.0

if choice == "Sandwich Only":
    price = 5.92
elif choice == "Set (Sandwich + Fries + Coke)":
    price = 8.32


col1, col2 = st.columns(2)

with col1:
    quantity = st.slider("How many?", min_value=0, max_value=10, value=1)

with col2:
    ketchup = st.number_input("How many ketchup(s)?", min_value=0, max_value=3, value=0)


sec_b_col1, sec_b_col2, sec_b_col3 = st.columns(3)

with sec_b_col1:
    st.header("Item Price")
    st.write("$" + str(price))

with sec_b_col2:
    st.header("Tax")
    sales_tax_rate = 0.08875
    st.write("Sale Tax Rate:", sales_tax_rate)
    tax = price * quantity * sales_tax_rate
    st.write(f"Tax Amount: ${tax:.2f}")

with sec_b_col3:
    st.header("Total")
    total = price * quantity + tax
    st.write(f"You Owe: ${total:.2f}")

st.button("Place Order")