import streamlit as st
import os

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

def main():
    """Trang tính giai thừa"""
    st.title("Factorial Calculator")
    
    # Chức năng tính giai thừa
    number = st.number_input("Nhập vào một số:", 
                              min_value=0, 
                              max_value=900)
    
    if st.button("Tính giai thừa"):
        result = fact(number)
        st.write(f"Giai thừa của {number} là {result}")

if __name__ == "__main__":
    main()
