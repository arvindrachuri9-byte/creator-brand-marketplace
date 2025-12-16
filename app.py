import streamlit as st

st.set_page_config(
    page_title="Creator ↔ Brand Marketplace",
    layout="wide"
)

st.title("🤝 Creator ↔ Brand Direct Marketplace")
st.subheader("Brands connect directly with creators. No agencies.")

st.markdown("---")

# -------------------------------
# BRAND INPUT SECTION
# -------------------------------

st.markdown("## 🏷️ Brand Campaign Details")

brand_name = st.text_input("Brand Name")
category = st.selectbox(
    "Category",
    ["Fashion", "Beauty", "Fitness", "Tech", "Food", "Finance", "Other"]
)

budget = st.number_input(
    "Campaign Budget (INR)",
    min_value=5000,
    step=5000
)

country = st.selectbox(
    "Country Focus",
    ["India", "USA", "UK", "UAE"]
)

submit_campaign = st.button("🔍 Find Creators")

# -------------------------------
# MOCK CREATOR DATABASE
# -------------------------------

creators = [
    {"name": "Aarav Sharma", "followers": "75K", "category": "Fashion"},
    {"name": "Neha Verma", "followers": "150K", "category": "Beauty"},
    {"name": "Rohit Singh", "followers": "320K", "category": "Fitness"},
    {"name": "Ananya Kapoor", "followers": "1.2M", "category": "Fashion"},
]

# -------------------------------
# RESULTS
# -------------------------------

if submit_campaign and brand_name:
    st.markdown("---")
    st.markdown("## 📢 Available Creators")

    for creator in creators:
        with st.container():
            st.markdown(
                f"""
                **{creator['name']}**  
                Followers: {creator['followers']}  
                Category: {creator['category']}
                """
            )

            col1, col2 = st.columns(2)
            with col1:
                st.button("✅ Send Collaboration Request", key=f"send_{creator['name']}")
            with col2:
                st.button("ℹ️ View Profile", key=f"profile_{creator['name']}")

            st.markdown("---")

elif submit_campaign:
    st.warning("Please enter a brand name to continue.")
