import streamlit as st

st.title("👤 About Me")

col1, col2 = st.columns([1, 2])

with col1:
    # Use a placeholder or your own image path
    st.image("https://scontent.fhan4-1.fna.fbcdn.net/v/t39.30808-1/621183628_122204337632365475_2456610163545570808_n.jpg?stp=c95.95.834.834a_dst-jpg_s200x200_tt6&_nc_cat=105&ccb=1-7&_nc_sid=e99d92&_nc_eui2=AeFzJv4EHIotsvjgELyA4SJNzzobGhN2GBrPOhsaE3YYGq2gTEdnRvIf7hu6Gxfh3GMPxt0_orqR0yWB7jcuU8tk&_nc_ohc=NwQ8TW551QoQ7kNvwE-hBH_&_nc_oc=Adld-wiVCLrguy1BIszCHAdzDdUCsk6W2dN2PJYBqgjvtQpmS44c4ONf1O39S0rXx0U&_nc_zt=24&_nc_ht=scontent.fhan4-1.fna&_nc_gid=WjNBZlt6k0FI8_rUoal4Zg&oh=00_AfsT2g_XEcNJbXB03CO4TEPN5xm3Lc1NuMwySUPkg2u2IA&oe=69878689", caption="Tran Quoc Thanh")

with col2:
    st.markdown("""
    ### Hello! I'm [Thanh]
    I am passionate about physics and interactive simulations. 
    This suite was built to help students and engineers visualize complex phenomena.
    
    **Find me on:**
    * [Facebook](https://www.facebook.com/tran.quoc.thanh.154157)
    * [GitHub](https://github.com/thanhtq2701-alt)
    """)