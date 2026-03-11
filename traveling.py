# -*- coding: utf-8 -*-
import streamlit as st
import random

st.set_page_config(
    page_title="Incredible India Travel",
    page_icon="IN",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Lato:wght@300;400;700&display=swap');
html, body, [class*="css"] { font-family: 'Lato', sans-serif; }
.stApp { background: #fdf6ec; }
.hero-section {
    background: linear-gradient(135deg, #c0392b 0%, #e67e22 50%, #f39c12 100%);
    border-radius: 20px; padding: 60px 40px; text-align: center;
    margin-bottom: 30px; box-shadow: 0 10px 40px rgba(192,57,43,0.3);
}
.hero-title {
    font-family: 'Playfair Display', serif; font-size: 3.2em;
    font-weight: 900; color: #fff; text-shadow: 2px 4px 12px rgba(0,0,0,0.3); margin: 0 0 10px 0;
}
.hero-sub { font-size: 1.25em; color: rgba(255,255,255,0.92); font-weight: 300; letter-spacing: 2px; }
.section-heading {
    font-family: 'Playfair Display', serif; font-size: 1.9em; font-weight: 700;
    color: #c0392b; border-left: 5px solid #e67e22; padding-left: 14px; margin: 30px 0 18px 0;
}
.dest-card {
    background: #fff; border-radius: 16px; padding: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-top: 4px solid #e67e22;
    margin-bottom: 16px; height: 100%;
}
.dest-emoji { font-size: 2.6em; margin-bottom: 8px; }
.dest-name { font-family: 'Playfair Display', serif; font-size: 1.3em; font-weight: 700; color: #2c2c2c; margin-bottom: 6px; }
.dest-state { font-size: 0.82em; color: #e67e22; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; }
.dest-desc { font-size: 0.9em; color: #666; line-height: 1.5; margin: 8px 0; }
.dest-tag {
    display: inline-block; background: #fdf0e0; color: #c0392b;
    border-radius: 20px; padding: 2px 10px; font-size: 0.75em; font-weight: 700; margin: 2px 2px 0 0;
}
.dest-rating { color: #f39c12; font-size: 1em; margin-top: 6px; }
.pkg-card {
    background: linear-gradient(145deg, #fff 0%, #fdf6ec 100%);
    border-radius: 16px; padding: 22px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.09); border: 1px solid #f0dfc0; margin-bottom: 14px;
}
.pkg-title { font-family: 'Playfair Display', serif; font-size: 1.2em; font-weight: 700; color: #c0392b; }
.pkg-price { font-size: 1.4em; font-weight: 700; color: #27ae60; }
.pkg-detail { font-size: 0.88em; color: #555; }
.info-box {
    background: #fff; border-radius: 14px; padding: 18px 20px;
    box-shadow: 0 3px 15px rgba(0,0,0,0.07); border-left: 4px solid #3498db; margin-bottom: 14px;
}
.info-box h4 { color: #3498db; margin: 0 0 8px 0; font-size: 1em; }
.info-box p { color: #555; margin: 0; font-size: 0.9em; line-height: 1.5; }
.tip-card {
    background: linear-gradient(135deg, #2c3e50, #3498db);
    border-radius: 14px; padding: 16px 20px; color: #fff; margin-bottom: 12px;
}
.tip-card h4 { margin: 0 0 6px 0; font-size: 1em; }
.tip-card p { margin: 0; font-size: 0.88em; opacity: 0.9; line-height: 1.4; }
.footer {
    text-align: center; padding: 30px; color: #999; font-size: 0.85em;
    border-top: 1px solid #e8d5b0; margin-top: 40px;
}
.sidebar-logo {
    font-family: 'Playfair Display', serif; font-size: 1.4em; color: #c0392b;
    text-align: center; padding: 10px 0 20px 0;
    border-bottom: 2px solid #f0dfc0; margin-bottom: 16px;
}
.stButton > button {
    background: linear-gradient(135deg, #c0392b, #e67e22) !important;
    color: white !important; border: none !important; border-radius: 25px !important;
    padding: 10px 28px !important; font-weight: 700 !important;
    font-size: 1em !important; letter-spacing: 1px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------
DESTINATIONS = [
    {"name": "Taj Mahal",         "state": "Uttar Pradesh",       "emoji": "\U0001f54c",
     "desc": "Symbol of eternal love. Marvel at the ivory-white marble masterpiece built by Mughal emperor Shah Jahan.",
     "tags": ["Heritage", "UNESCO", "Romantic"], "rating": 5, "best_time": "Oct-Mar", "budget": "Rs 2,000-5,000/day"},
    {"name": "Jaipur",            "state": "Rajasthan",           "emoji": "\U0001f3ef",
     "desc": "The Pink City dazzles with palaces, forts, and bustling bazaars filled with handicrafts and gems.",
     "tags": ["Culture", "Heritage", "Shopping"], "rating": 5, "best_time": "Nov-Feb", "budget": "Rs 1,500-4,000/day"},
    {"name": "Kerala Backwaters", "state": "Kerala",              "emoji": "\U0001f6a3",
     "desc": "Drift through serene palm-lined canals on a houseboat. Nature, Ayurveda, and tranquillity combined.",
     "tags": ["Nature", "Relaxation", "Houseboat"], "rating": 5, "best_time": "Sep-Mar", "budget": "Rs 3,000-8,000/day"},
    {"name": "Goa Beaches",       "state": "Goa",                 "emoji": "\U0001f3d6",
     "desc": "Golden sands, turquoise waters, vibrant nightlife, and a unique Indo-Portuguese culture.",
     "tags": ["Beach", "Nightlife", "Adventure"], "rating": 4, "best_time": "Nov-Feb", "budget": "Rs 2,000-6,000/day"},
    {"name": "Varanasi",          "state": "Uttar Pradesh",       "emoji": "\U0001fa94",
     "desc": "One of the worlds oldest cities. Witness the spiritual Ganga Aarti and ancient ghats at dawn.",
     "tags": ["Spiritual", "Culture", "Heritage"], "rating": 5, "best_time": "Oct-Mar", "budget": "Rs 1,000-3,000/day"},
    {"name": "Leh-Ladakh",        "state": "Jammu & Kashmir",     "emoji": "\U0001f3d4",
     "desc": "Otherworldly landscapes, high-altitude lakes, Buddhist monasteries, and thrilling mountain passes.",
     "tags": ["Adventure", "Nature", "Trekking"], "rating": 5, "best_time": "Jun-Sep", "budget": "Rs 3,500-9,000/day"},
    {"name": "Hampi",             "state": "Karnataka",           "emoji": "\U0001f5ff",
     "desc": "A UNESCO World Heritage Site with magnificent ruins of the Vijayanagara Empire set amid boulders.",
     "tags": ["UNESCO", "Heritage", "Trekking"], "rating": 4, "best_time": "Oct-Feb", "budget": "Rs 1,000-2,500/day"},
    {"name": "Ranthambore",       "state": "Rajasthan",           "emoji": "\U0001f42f",
     "desc": "One of India's best tiger reserves. Spot Bengal tigers in their natural fortress-like habitat.",
     "tags": ["Wildlife", "Safari", "Nature"], "rating": 4, "best_time": "Oct-Jun", "budget": "Rs 4,000-10,000/day"},
    {"name": "Andaman Islands",   "state": "Andaman & Nicobar",   "emoji": "\U0001f420",
     "desc": "Crystal-clear waters, vibrant coral reefs, pristine beaches and rich WWII history.",
     "tags": ["Beach", "Diving", "Nature"], "rating": 5, "best_time": "Nov-Apr", "budget": "Rs 4,000-12,000/day"},
    {"name": "Mysuru",            "state": "Karnataka",           "emoji": "\U0001f451",
     "desc": "City of Palaces. The magnificent Mysore Palace illuminated during Dasara is a sight to behold.",
     "tags": ["Culture", "Heritage", "Festival"], "rating": 4, "best_time": "Oct-Mar", "budget": "Rs 1,500-4,000/day"},
    {"name": "Rishikesh",         "state": "Uttarakhand",         "emoji": "\U0001f9d8",
     "desc": "Yoga capital of the world. Rafting on the Ganges, ashrams, and gateway to the Himalayas.",
     "tags": ["Adventure", "Spiritual", "Yoga"], "rating": 4, "best_time": "Sep-Jun", "budget": "Rs 1,000-3,500/day"},
    {"name": "Munnar",            "state": "Kerala",              "emoji": "\U0001f375",
     "desc": "Misty hills blanketed in emerald tea plantations. Colonial bungalows and cool mountain air.",
     "tags": ["Nature", "Trekking", "Relaxation"], "rating": 4, "best_time": "Sep-May", "budget": "Rs 2,000-5,000/day"},
]

PACKAGES = [
    {"name": "Golden Triangle Classic",       "days": 7,  "cities": "Delhi - Agra - Jaipur",
     "price": "Rs 25,000", "includes": "Hotels, Transport, Guide",           "type": "Heritage"},
    {"name": "Kerala Gods Own Country",        "days": 6,  "cities": "Kochi - Munnar - Alleppey",
     "price": "Rs 22,000", "includes": "Houseboat, Hotels, Meals",           "type": "Nature"},
    {"name": "Goa Beach Retreat",             "days": 5,  "cities": "North Goa - South Goa",
     "price": "Rs 18,000", "includes": "Resort, Breakfast, Transfers",       "type": "Beach"},
    {"name": "Ladakh Adventure Expedition",   "days": 9,  "cities": "Leh - Nubra - Pangong",
     "price": "Rs 45,000", "includes": "Camps, Jeep Safari, Permits",        "type": "Adventure"},
    {"name": "Rajasthan Royal Trail",         "days": 10, "cities": "Jaipur - Jodhpur - Udaipur - Jaisalmer",
     "price": "Rs 38,000", "includes": "Heritage Hotels, Camel Safari",      "type": "Heritage"},
    {"name": "Spiritual Varanasi & Bodh Gaya","days": 5,  "cities": "Varanasi - Sarnath - Bodh Gaya",
     "price": "Rs 15,000", "includes": "Hotels, Boat Ride, Guide",           "type": "Spiritual"},
]

TIPS = [
    {"icon": "Train",    "title": "Book Trains Early",
     "tip": "Indian Railways is vast and cheap. Book on IRCTC at least 2-3 months ahead for popular routes."},
    {"icon": "Health",   "title": "Health & Safety",
     "tip": "Carry oral rehydration salts, mosquito repellent, and a basic first-aid kit. Drink only bottled water."},
    {"icon": "Dress",    "title": "Dress Respectfully",
     "tip": "Cover shoulders and knees when visiting temples, mosques, and gurudwaras. Remove shoes at religious sites."},
    {"icon": "Money",    "title": "Currency & Payments",
     "tip": "Carry some cash (INR) for local markets. UPI (GPay, PhonePe) is widely accepted even in small towns."},
    {"icon": "Weather",  "title": "Best Time to Visit",
     "tip": "October to March is ideal for most of India. Monsoon (Jun-Sep) is great for Kerala & hill stations."},
    {"icon": "Market",   "title": "Bargain at Markets",
     "tip": "Bargaining is expected at local bazaars. Start at 40-50% of the quoted price and meet in the middle."},
]

FESTIVALS = [
    {"name": "Diwali",       "month": "Oct/Nov", "emoji": "\U0001fa94",
     "desc": "Festival of Lights celebrated across India with diyas, fireworks, and sweets."},
    {"name": "Holi",         "month": "Mar",     "emoji": "\U0001f308",
     "desc": "Festival of Colors. Join the celebration in Mathura & Vrindavan for the most vibrant experience."},
    {"name": "Durga Puja",   "month": "Sep/Oct", "emoji": "\U0001f64f",
     "desc": "10-day celebration in Kolkata with elaborate pandals and cultural performances."},
    {"name": "Pushkar Fair", "month": "Nov",     "emoji": "\U0001f42a",
     "desc": "Worlds largest camel fair in Rajasthan with folk music and desert festivities."},
    {"name": "Onam",         "month": "Aug/Sep", "emoji": "\U0001f338",
     "desc": "Kerala harvest festival with boat races, flower rangoli, and a grand 26-course feast."},
    {"name": "Navratri",     "month": "Sep/Oct", "emoji": "\U0001f483",
     "desc": "Nine nights of Garba dance in Gujarat. The most colorful folk dance festival in India."},
]

CUISINES = {
    "North India": ["Butter Chicken", "Dal Makhani", "Naan", "Chole Bhature", "Biryani", "Lassi"],
    "South India": ["Masala Dosa", "Idli Sambar", "Rasam", "Appam with Stew", "Chettinad Curry", "Filter Coffee"],
    "West India":  ["Pav Bhaji", "Vada Pav", "Dhokla", "Laal Maas", "Dal Baati Churma", "Modak"],
    "East India":  ["Rasgulla", "Macher Jhol", "Sandesh", "Litti Chokha", "Pakhala Bhata", "Momos"],
}

# ---------------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-logo">Incredible India</div>', unsafe_allow_html=True)

    page = st.selectbox("Navigate", [
        "Home",
        "Destinations",
        "Tour Packages",
        "Festivals & Culture",
        "Food & Cuisine",
        "Plan My Trip",
        "Travel Tips",
    ])

    st.markdown("---")
    st.markdown("**Quick Weather Guide**")
    for period, desc in [("Jan-Mar","Cool & Pleasant"),("Apr-Jun","Hot & Dry"),
                         ("Jul-Sep","Monsoon Season"),("Oct-Dec","Best Season")]:
        st.markdown(f"**{period}**: {desc}")

    st.markdown("---")
    st.markdown("**Emergency Numbers**")
    st.markdown("Police: **100**  \nAmbulance: **108**  \nFire: **101**  \nTourist Helpline: **1800-111-363**")

# ---------------------------------------------------------------------------
# HELPER
# ---------------------------------------------------------------------------
def dest_card_html(dest):
    stars = "\u2B50" * dest["rating"]
    tags_html = "".join(
        '<span class="dest-tag">{}</span>'.format(t) for t in dest["tags"]
    )
    return (
        '<div class="dest-card">'
        '<div class="dest-emoji">{emoji}</div>'
        '<div class="dest-name">{name}</div>'
        '<div class="dest-state">{state}</div>'
        '<div class="dest-desc">{desc}</div>'
        '{tags}'
        '<div class="dest-rating">{stars}</div>'
        '<div style="font-size:0.82em;color:#888;margin-top:6px;">Best: {bt} | {budget}</div>'
        '</div>'
    ).format(
        emoji=dest["emoji"], name=dest["name"], state=dest["state"],
        desc=dest["desc"], tags=tags_html, stars=stars,
        bt=dest["best_time"], budget=dest["budget"]
    )

# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
if page == "Home":
    st.markdown(
        '<div class="hero-section">'
        '<div class="hero-title">Incredible India</div>'
        '<div class="hero-sub">Where every journey becomes a story worth telling</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("UNESCO Sites",  "42",    "World Heritage Sites")
    c2.metric("Coastline",     "7,517 km", "Beaches & shores")
    c3.metric("Languages",     "1,600+","Spoken across India")
    c4.metric("Festivals",     "365+",  "Celebrated yearly")

    st.markdown('<div class="section-heading">Top Destinations</div>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, dest in enumerate(DESTINATIONS[:8]):
        with cols[i % 4]:
            st.markdown(dest_card_html(dest), unsafe_allow_html=True)

    st.markdown('<div class="section-heading">Upcoming Festivals</div>', unsafe_allow_html=True)
    fcols = st.columns(3)
    for i, f in enumerate(FESTIVALS[:3]):
        with fcols[i]:
            st.markdown(
                '<div class="pkg-card">'
                '<div style="font-size:2em">{emoji}</div>'
                '<div class="pkg-title">{name}</div>'
                '<div style="color:#e67e22;font-weight:700;font-size:0.85em;">{month}</div>'
                '<div class="pkg-detail" style="margin-top:6px;">{desc}</div>'
                '</div>'.format(**f),
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------------------------
# DESTINATIONS
# ---------------------------------------------------------------------------
elif page == "Destinations":
    st.markdown(
        '<div class="hero-section">'
        '<div class="hero-title">Explore Destinations</div>'
        '<div class="hero-sub">Discover India\'s most captivating places</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    f1, f2 = st.columns(2)
    with f1:
        tag_filter = st.selectbox("Filter by Category",
            ["All","Heritage","Nature","Beach","Adventure","Spiritual","Wildlife","UNESCO"])
    with f2:
        rating_filter = st.selectbox("Minimum Rating",
            ["Any","5 stars only","4 stars and above"])

    filtered = DESTINATIONS
    if tag_filter != "All":
        filtered = [d for d in filtered if tag_filter in d["tags"]]
    if rating_filter == "5 stars only":
        filtered = [d for d in filtered if d["rating"] == 5]
    elif rating_filter == "4 stars and above":
        filtered = [d for d in filtered if d["rating"] >= 4]

    st.markdown("**Showing {} destinations**".format(len(filtered)))
    cols = st.columns(3)
    for i, dest in enumerate(filtered):
        with cols[i % 3]:
            st.markdown(dest_card_html(dest), unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# PACKAGES
# ---------------------------------------------------------------------------
elif page == "Tour Packages":
    st.markdown(
        '<div class="hero-section">'
        '<div class="hero-title">Tour Packages</div>'
        '<div class="hero-sub">Curated journeys for every kind of traveller</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    type_filter = st.selectbox("Package Type",
        ["All","Heritage","Nature","Beach","Adventure","Spiritual"])
    pkgs = PACKAGES if type_filter == "All" else [p for p in PACKAGES if p["type"] == type_filter]

    for pkg in pkgs:
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(
                '<div class="pkg-card">'
                '<div class="pkg-title">{name}</div>'
                '<div class="pkg-detail" style="margin:6px 0;">'
                '{days} Days &nbsp;|&nbsp; {cities}'
                '</div>'
                '<div class="pkg-detail">Includes: {includes}</div>'
                '<div style="margin-top:10px;"><span class="dest-tag">{type}</span></div>'
                '</div>'.format(**pkg),
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                '<div class="pkg-card" style="text-align:center;">'
                '<div class="pkg-price">{price}</div>'
                '<div class="pkg-detail">per person</div>'
                '</div>'.format(**pkg),
                unsafe_allow_html=True,
            )
            if st.button("Book Now", key="book_" + pkg["name"]):
                st.success("Booking request for **{}** sent! We will contact you shortly.".format(pkg["name"]))

# ---------------------------------------------------------------------------
# FESTIVALS
# ---------------------------------------------------------------------------
elif page == "Festivals & Culture":
    st.markdown(
        '<div class="hero-section">'
        '<div class="hero-title">Festivals &amp; Culture</div>'
        '<div class="hero-sub">Celebrate the colours and traditions of India</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-heading">Major Festivals</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, f in enumerate(FESTIVALS):
        with cols[i % 3]:
            st.markdown(
                '<div class="dest-card" style="text-align:center;">'
                '<div style="font-size:3em;">{emoji}</div>'
                '<div class="dest-name">{name}</div>'
                '<div class="dest-state">{month}</div>'
                '<div class="dest-desc">{desc}</div>'
                '</div>'.format(**f),
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-heading">Art Forms of India</div>', unsafe_allow_html=True)
    arts = [
        ("Bharatanatyam",   "Tamil Nadu",  "Classical dance form with expressive hand gestures and footwork."),
        ("Madhubani",       "Bihar",       "Folk art with vibrant natural colours depicting mythology."),
        ("Kathak",          "North India", "Classical dance narrating stories through rhythmic footwork."),
        ("Pashmina Weaving","Kashmir",     "Fine wool woven into luxurious shawls by skilled artisans."),
        ("Chhau Dance",     "Bengal/Odisha","Martial arts based folk dance with elaborate masks."),
        ("Warli Art",       "Maharashtra", "Tribal art using simple geometric shapes depicting village life."),
    ]
    acols = st.columns(3)
    for i, (name, region, desc) in enumerate(arts):
        with acols[i % 3]:
            st.markdown(
                '<div class="info-box">'
                '<h4>{name} — {region}</h4>'
                '<p>{desc}</p>'
                '</div>'.format(name=name, region=region, desc=desc),
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------------------------
# FOOD
# ---------------------------------------------------------------------------
elif page == "Food & Cuisine":
    st.markdown(
        '<div class="hero-section">'
        '<div class="hero-title">Food &amp; Cuisine</div>'
        '<div class="hero-sub">A culinary journey across India\'s diverse flavours</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    for region, dishes in CUISINES.items():
        st.markdown('<div class="section-heading">{}</div>'.format(region), unsafe_allow_html=True)
        dcols = st.columns(6)
        for j, dish in enumerate(dishes):
            with dcols[j % 6]:
                st.markdown(
                    '<div style="background:#fff;border-radius:12px;padding:12px 8px;text-align:center;'
                    'box-shadow:0 3px 12px rgba(0,0,0,0.07);border-top:3px solid #e67e22;margin-bottom:8px;">'
                    '<div style="font-size:0.9em;font-weight:700;color:#2c2c2c;">{}</div>'
                    '</div>'.format(dish),
                    unsafe_allow_html=True,
                )

    st.markdown('<div class="section-heading">Must-Try Drinks</div>', unsafe_allow_html=True)
    drinks = [
        ("Masala Chai",    "Spiced milk tea — India's favourite drink, enjoyed everywhere."),
        ("Lassi",          "Cooling yoghurt-based drink, sweet or salted. Best in Punjab."),
        ("Tender Coconut", "Fresh coconut water straight from the shell, especially in South India."),
        ("Feni",           "Goa's local cashew or coconut spirit — a unique regional specialty."),
        ("Thandai",        "Milk infused with nuts and spices, especially popular during Holi."),
        ("Filter Coffee",  "South Indian coffee brewed in a traditional metal filter — rich and aromatic."),
    ]
    drcols = st.columns(3)
    for i, (name, desc) in enumerate(drinks):
        with drcols[i % 3]:
            st.markdown(
                '<div class="pkg-card">'
                '<div class="pkg-title">{name}</div>'
                '<div class="pkg-detail" style="margin-top:6px;">{desc}</div>'
                '</div>'.format(name=name, desc=desc),
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------------------------
# PLAN MY TRIP
# ---------------------------------------------------------------------------
elif page == "Plan My Trip":
    st.markdown(
        '<div class="hero-section">'
        '<div class="hero-title">Plan My Trip</div>'
        '<div class="hero-sub">Tell us your preferences and we\'ll craft your perfect journey</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    with st.form("trip_planner"):
        col1, col2 = st.columns(2)
        with col1:
            name        = st.text_input("Your Name")
            from_city   = st.text_input("Departing From")
            travel_date = st.date_input("Travel Date")
            duration    = st.slider("Trip Duration (days)", 2, 21, 7)
        with col2:
            num_people  = st.number_input("Number of Travellers", 1, 20, 2)
            budget_pp   = st.selectbox("Budget per Person",
                ["Under Rs 10,000", "Rs 10,000-25,000", "Rs 25,000-50,000", "Rs 50,000+"])
            interest    = st.multiselect("Travel Interests",
                ["Heritage","Nature","Beach","Adventure","Spiritual","Wildlife","Food","Yoga"])
            accomm      = st.selectbox("Accommodation Preference",
                ["Budget Hostel","Mid-range Hotel","Heritage Property","Luxury Resort"])

        special_req = st.text_area("Special Requirements (optional)",
            placeholder="Vegetarian meals, wheelchair access, travelling with kids...")
        submitted = st.form_submit_button("Generate My Itinerary")

    if submitted and name:
        st.balloons()
        st.success("Great, {}! Here is a customised itinerary for you.".format(name))

        recommended = [d for d in DESTINATIONS if any(t in d["tags"] for t in interest)] if interest else DESTINATIONS
        random.shuffle(recommended)
        recommended = recommended[:min(duration, len(recommended))]

        st.markdown('<div class="section-heading">Your Suggested Itinerary</div>', unsafe_allow_html=True)
        for day, dest in enumerate(recommended, 1):
            with st.expander("Day {}: {} {}, {}".format(day, dest["emoji"], dest["name"], dest["state"])):
                st.markdown("**About:** " + dest["desc"])
                st.markdown("**Best Activities:** " + ", ".join(dest["tags"]))
                st.markdown("**Estimated Daily Cost:** " + dest["budget"])
                st.markdown("**Best Season:** " + dest["best_time"])

        st.markdown('<div class="section-heading">Trip Summary</div>', unsafe_allow_html=True)
        sc1, sc2, sc3, sc4 = st.columns(4)
        sc1.metric("Travellers", num_people)
        sc2.metric("Duration",   "{} days".format(duration))
        sc3.metric("Stay",       accomm)
        sc4.metric("Budget",     budget_pp)

# ---------------------------------------------------------------------------
# TIPS
# ---------------------------------------------------------------------------
elif page == "Travel Tips":
    st.markdown(
        '<div class="hero-section">'
        '<div class="hero-title">Travel Tips</div>'
        '<div class="hero-sub">Expert advice for a smooth and memorable Indian adventure</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    for tip in TIPS:
        st.markdown(
            '<div class="tip-card">'
            '<h4>{icon}: {title}</h4>'
            '<p>{tip}</p>'
            '</div>'.format(**tip),
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-heading">Useful Apps for India Travel</div>', unsafe_allow_html=True)
    apps = [
        ("IRCTC Rail Connect",  "Book train tickets online"),
        ("MakeMyTrip / Yatra",  "Flights, hotels, and holiday packages"),
        ("Google Maps",         "Works offline; essential for navigation"),
        ("Ola / Uber",          "Cab booking in all major cities"),
        ("GPay / PhonePe",      "UPI payments accepted everywhere"),
        ("Google Translate",    "Translate 22+ Indian languages"),
    ]
    acols = st.columns(3)
    for i, (app, desc) in enumerate(apps):
        with acols[i % 3]:
            st.markdown(
                '<div class="info-box">'
                '<h4>{app}</h4>'
                '<p>{desc}</p>'
                '</div>'.format(app=app, desc=desc),
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="footer">'
    '<strong>Incredible India Travel</strong> — Crafted with love for wanderers who seek culture, colour &amp; adventure<br>'
    '<span style="color:#e67e22">© 2025 Incredible India Travel. All rights reserved.</span>'
    '</div>',
    unsafe_allow_html=True,
)
