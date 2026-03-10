import streamlit as st
import random

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Incredible India Travel",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Lato:wght@300;400;700&display=swap');

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
}
.stApp {
    background: #fdf6ec;
}

/* ── Hero ── */
.hero-section {
    background: linear-gradient(135deg, #c0392b 0%, #e67e22 50%, #f39c12 100%);
    border-radius: 20px;
    padding: 60px 40px;
    text-align: center;
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(192,57,43,0.3);
}
.hero-section::before {
    content: "🕌 🌸 🐘 🌺 🕌";
    font-size: 28px;
    display: block;
    opacity: 0.25;
    position: absolute;
    top: 10px; left: 0; right: 0;
    letter-spacing: 20px;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.2em;
    font-weight: 900;
    color: #fff;
    text-shadow: 2px 4px 12px rgba(0,0,0,0.3);
    margin: 0 0 10px 0;
}
.hero-sub {
    font-size: 1.25em;
    color: rgba(255,255,255,0.92);
    font-weight: 300;
    letter-spacing: 2px;
}

/* ── Section Heading ── */
.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 1.9em;
    font-weight: 700;
    color: #c0392b;
    border-left: 5px solid #e67e22;
    padding-left: 14px;
    margin: 30px 0 18px 0;
}

/* ── Destination Card ── */
.dest-card {
    background: #fff;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    transition: transform .2s, box-shadow .2s;
    border-top: 4px solid #e67e22;
    height: 100%;
}
.dest-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.14);
}
.dest-emoji { font-size: 2.6em; margin-bottom: 8px; }
.dest-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.3em;
    font-weight: 700;
    color: #2c2c2c;
    margin-bottom: 6px;
}
.dest-state { font-size: 0.82em; color: #e67e22; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; }
.dest-desc { font-size: 0.9em; color: #666; line-height: 1.5; margin: 8px 0; }
.dest-tag {
    display: inline-block;
    background: #fdf0e0;
    color: #c0392b;
    border-radius: 20px;
    padding: 2px 10px;
    font-size: 0.75em;
    font-weight: 700;
    margin: 2px 2px 0 0;
}
.dest-rating { color: #f39c12; font-size: 1em; margin-top: 6px; }

/* ── Package Card ── */
.pkg-card {
    background: linear-gradient(145deg, #fff 0%, #fdf6ec 100%);
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.09);
    border: 1px solid #f0dfc0;
    margin-bottom: 14px;
}
.pkg-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.2em;
    font-weight: 700;
    color: #c0392b;
}
.pkg-price {
    font-size: 1.4em;
    font-weight: 700;
    color: #27ae60;
}
.pkg-detail { font-size: 0.88em; color: #555; }

/* ── Info Box ── */
.info-box {
    background: #fff;
    border-radius: 14px;
    padding: 18px 20px;
    box-shadow: 0 3px 15px rgba(0,0,0,0.07);
    border-left: 4px solid #3498db;
    margin-bottom: 14px;
}
.info-box h4 { color: #3498db; margin: 0 0 8px 0; font-size: 1em; }
.info-box p  { color: #555; margin: 0; font-size: 0.9em; line-height: 1.5; }

/* ── Tip Card ── */
.tip-card {
    background: linear-gradient(135deg, #2c3e50, #3498db);
    border-radius: 14px;
    padding: 16px 20px;
    color: #fff;
    margin-bottom: 12px;
}
.tip-card h4 { margin: 0 0 6px 0; font-size: 1em; }
.tip-card p  { margin: 0; font-size: 0.88em; opacity: 0.9; line-height: 1.4; }

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 30px;
    color: #999;
    font-size: 0.85em;
    border-top: 1px solid #e8d5b0;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ─── Data (unchanged) ─────────────────────────────────────────────────────────
DESTINATIONS = [
    {"name": "Taj Mahal", "state": "Uttar Pradesh", "emoji": "🕌",
     "desc": "Symbol of eternal love. Marvel at the ivory-white marble masterpiece built by Mughal emperor Shah Jahan.", 
     "tags": ["Heritage", "UNESCO", "Romantic"], "rating": 5, "best_time": "Oct–Mar", "budget": "₹2,000–₹5,000/day"},
    {"name": "Jaipur", "state": "Rajasthan", "emoji": "🏯",
     "desc": "The Pink City dazzles with palaces, forts, and bustling bazaars filled with handicrafts and gems.", 
     "tags": ["Culture", "Heritage", "Shopping"], "rating": 5, "best_time": "Nov–Feb", "budget": "₹1,500–₹4,000/day"},
    {"name": "Kerala Backwaters", "state": "Kerala", "emoji": "🚣",
     "desc": "Drift through serene palm-lined canals on a houseboat. Nature, Ayurveda, and tranquillity combined.", 
     "tags": ["Nature", "Relaxation", "Houseboat"], "rating": 5, "best_time": "Sep–Mar", "budget": "₹3,000–₹8,000/day"},
    {"name": "Goa Beaches", "state": "Goa", "emoji": "🏖️",
     "desc": "Golden sands, turquoise waters, vibrant nightlife, and a unique Indo-Portuguese culture.", 
     "tags": ["Beach", "Nightlife", "Adventure"], "rating": 4, "best_time": "Nov–Feb", "budget": "₹2,000–₹6,000/day"},
]

PACKAGES = [
    {"name": "Golden Triangle Classic", "days": 7, "cities": "Delhi → Agra → Jaipur",
     "price": "₹25,000", "includes": "Hotels, Transport, Guide", "type": "Heritage"},
    {"name": "Kerala God's Own Country", "days": 6, "cities": "Kochi → Munnar → Alleppey",
     "price": "₹22,000", "includes": "Houseboat, Hotels, Meals", "type": "Nature"},
]

TIPS = [
    {"icon": "🚆", "title": "Book Trains Early", "tip": "Indian Railways is vast and cheap. Book on IRCTC at least 2–3 months ahead for popular routes."},
    {"icon": "💊", "title": "Health & Safety", "tip": "Carry oral rehydration salts, mosquito repellent, and a basic first-aid kit. Drink only bottled water."},
]

FESTIVALS = [
    {"name": "Diwali", "month": "Oct/Nov", "emoji": "🪔", "desc": "Festival of Lights celebrated across India with diyas, fireworks, and sweets."},
    {"name": "Holi", "month": "Mar", "emoji": "🌈", "desc": "Festival of Colors. Join the celebration in Mathura & Vrindavan for the most vibrant experience."},
]

CUISINES = {
    "North India 🫓": ["Butter Chicken", "Dal Makhani", "Naan"],
    "South India 🍛": ["Masala Dosa", "Idli Sambar", "Filter Coffee"],
}

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">🇮🇳 Incredible India</div>', unsafe_allow_html=True)
    page = st.selectbox("📍 Navigate", ["🏠 Home", "🗺️ Destinations", "📦 Tour Packages", "💡 Travel Tips"])
    
    st.markdown("---")
    st.markdown("**🌡️ Quick Weather Guide**")
    season_info = {"Jan–Mar": "🌤️ Cool & Pleasant", "Oct–Dec": "🍂 Best Season"}
    for period, desc in season_info.items():
        st.markdown(f"**{period}**: {desc}")

# ─── FIXED PAGES ──────────────────────────────────────────────────────────────
if page == "🏠 Home":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🇮🇳 Incredible India</div>
        <div class="hero-sub">Where every journey becomes a story worth telling</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🏛️ UNESCO Sites", "42")
    col2.metric("🌊 Coastline", "7,517 km")
    col3.metric("🗣️ Languages", "1,600+")
    col4.metric("🎭 Festivals", "365+")

    st.markdown('<div class="section-heading">🌟 Top Destinations</div>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, dest in enumerate(DESTINATIONS[:4]):
        with cols[i]:
            st.markdown(f"""
            <div class="dest-card">
                <div class="dest-emoji">{dest['emoji']}</div>
                <div class="dest-name">{dest['name']}</div>
                <div class="dest-state">{dest['state']}</div>
                <div class="dest-desc">{dest['desc']}</div>
                <div class="dest-rating">⭐⭐⭐⭐⭐</div>
            </div>
            """, unsafe_allow_html=True)

elif page == "🗺️ Destinations":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🗺️ Explore Destinations</div>
        <div class="hero-sub">Discover India's most captivating places</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"**Showing {len(DESTINATIONS)} destinations**")
    cols = st.columns(3)
    for i, dest in enumerate(DESTINATIONS):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="dest-card">
                <div class="dest-emoji">{dest['emoji']}</div>
                <div class="dest-name">{dest['name']}</div>
                <div class="dest-state">{dest['state']}</div>
                <div class="dest-desc">{dest['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

elif page == "📦 Tour Packages":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">📦 Tour Packages</div>
        <div class="hero-sub">Curated journeys for every kind of traveller</div>
    </div>
    """, unsafe_allow_html=True)

    for pkg in PACKAGES:
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(f"""
            <div class="pkg-card">
                <div class="pkg-title">{pkg['name']}</div>
                <div class="pkg-detail">🗓️ {pkg['days']} Days | 📍 {pkg['cities']}</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="pkg-price">{pkg["price"]}</div>', unsafe_allow_html=True)

elif page == "💡 Travel Tips":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">💡 Travel Tips</div>
        <div class="hero-sub">Expert advice for a smooth Indian adventure</div>
    </div>
    """, unsafe_allow_html=True)

    for tip in TIPS:
        st.markdown(f"""
        <div class="tip-card">
            <h4>{tip['icon']} {tip['title']}</h4>
            <p>{tip['tip']}</p>
        </div>
        """, unsafe_allow_html=True)

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    🇮🇳 <strong>Incredible India Travel</strong> — Crafted with ❤️ for wanderers
</div>
""", unsafe_allow_html=True)
