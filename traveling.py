import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

 
# Page configuration
st.set_page_config(
    page_title="India Travel Hub 🇮🇳",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better visuals
st.markdown("""
    <style>
    .main-header {
        font-size: 4rem !important;
        color: #d32f2f;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .travel-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 15px;
        color: white;
        transition: transform 0.3s;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .travel-card:hover {
        transform: translateY(-5px);
    }
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .official-link {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        color: white !important;
        padding: 8px 16px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Updated destinations with REAL images & OFFICIAL links
destinations_data = {
    "North India": {
        "Delhi": {
            "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400&h=300&fit=crop",
            "desc": "Historical capital with Red Fort, India Gate, Qutub Minar",
            "cost": "₹5000-15000",
            "link": "http://www.delhitourism.gov.in"
        },
        "Agra": {
            "image": "https://images.unsplash.com/photo-1574456780999-0fd922ac5d4e?w=400&h=300&fit=crop",
            "desc": "Home to Taj Mahal - Wonder of the World",
            "cost": "₹4000-12000",
            "link": "http://www.uptourism.gov.in"
        },
        "Jaipur": {
            "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop",
            "desc": "Pink City with Amber Fort, Hawa Mahal, City Palace",
            "cost": "₹4500-13000",
            "link": "http://www.tourism.rajasthan.gov.in"
        },
        "Manali": {
            "image": "https://images.unsplash.com/photo-1580411050990-85788898b74a?w=400&h=300&fit=crop",
            "desc": "Hill station with adventure sports & scenic beauty",
            "cost": "₹6000-18000",
            "link": "https://himachaltourism.gov.in"
        }
    },
    "South India": {
        "Goa": {
            "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400&h=300&fit=crop",
            "desc": "Beaches, nightlife, Portuguese heritage",
            "cost": "₹7000-20000",
            "link": "https://goa-tourism.com"
        },
        "Munnar": {
            "image": "https://images.unsplash.com/photo-1578287006259-0333c0a036c0?w=400&h=300&fit=crop",
            "desc": "Tea plantations and misty hills",
            "cost": "₹5000-15000",
            "link": "http://www.keralatourism.org"
        },
        "Ooty": {
            "image": "https://images.unsplash.com/photo-1545565340-764f28128502?w=400&h=300&fit=crop",
            "desc": "Nilgiri Mountain Railway & scenic lakes",
            "cost": "₹4000-12000",
            "link": "http://www.tamilnadutourism.org"
        },
        "Kerala": {
            "image": "https://images.unsplash.com/photo-1600433792800-9e52d3c664b1?w=400&h=300&fit=crop",
            "desc": "Houseboats, backwaters & Ayurvedic retreats",
            "cost": "₹8000-25000",
            "link": "http://www.keralatourism.org"
        }
    },
    "East India": {
        "Darjeeling": {
            "image": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=400&h=300&fit=crop",
            "desc": "Tea gardens & Kanchenjunga views",
            "cost": "₹6000-18000",
            "link": "https://www.wbtourism.gov.in"
        },
        "Gangtok": {
            "image": "https://images.unsplash.com/photo-1615568489508-89f3dd0a9b46?w=400&h=300&fit=crop",
            "desc": "Himalayan beauty & monasteries",
            "cost": "₹7000-20000",
            "link": "http://www.sikkimtourism.gov.in"
        }
    },
    "West India": {
        "Udaipur": {
            "image": "https://images.unsplash.com/photo-1585814134696-b509cd80d340?w=400&h=300&fit=crop",
            "desc": "City of Lakes & romantic palaces",
            "cost": "₹5500-16000",
            "link": "http://www.tourism.rajasthan.gov.in"
        },
        "Ahmedabad": {
            "image": "https://images.unsplash.com/photo-1591076482168-20e844f9a6b3?w=400&h=300&fit=crop",
            "desc": "Sabarmati Ashram & UNESCO heritage",
            "cost": "₹3500-10000",
            "link": "https://www.gujarattourism.com"
        }
    }
}

# Main App
def main():
    st.markdown('<h1 class="main-header">🇮🇳 India Travel Hub</h1>', unsafe_allow_html=True)
    
    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2 style='color:white; font-size:2rem;'>50K+</h2>
            <p>Happy Travelers</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2 style='color:white; font-size:2rem;'>100+</h2>
            <p>Destinations</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2 style='color:white; font-size:2rem;'>24/7</h2>
            <p>Support</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h2 style='color:white; font-size:2rem;'>₹2999</h2>
            <p>Starting @</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("🚀 Quick Plan")
    from_city = st.sidebar.selectbox("From:", ["Mumbai", "Delhi", "Bangalore", "Pune", "Chennai", "Kolkata"])
    travelers = st.sidebar.slider("Travelers", 1, 6, 2)
    budget = st.sidebar.selectbox("Budget per person", ["Economy (₹3k-8k)", "Comfort (₹8k-15k)", "Luxury (₹15k+)"])
    
    # Main tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🏔️ Destinations", "🗺️ Itinerary", "✈️ Bookings", "📊 Stats"])
    
    with tab1:
        display_destinations()
    
    with tab2:
        create_itinerary(from_city, travelers)
    
    with tab3:
        booking_interface()
    
    with tab4:
        display_stats()

def display_destinations():
    st.subheader("✨ Popular Indian Destinations")
    
    for region, cities in destinations_data.items():
        with st.expander(f"🌟 {region}", expanded=(region=="North India")):
            cols = st.columns(min(4, len(cities)))
            for i, (city, info) in enumerate(cities.items()):
                col_idx = i % 4
                with cols[col_idx]:
                    # Image
                    st.image(info['image'], use_column_width=True)
                    
                    # Card content
                    st.markdown(f"""
                    <div class="travel-card">
                        <h3 style='margin:0;'>{city} 🌟</h3>
                        <p style='margin:5px 0;'>{info['desc']}</p>
                        <p><strong>💰 {info['cost']}</strong></p>
                        <a href="{info['link']}" target="_blank" class="official-link">
                            🏛️ Official Tourism Site
                        </a>
                    </div>
                    """, unsafe_allow_html=True)

def create_itinerary(from_city, travelers):
    st.subheader("🗺️ Smart Itinerary Generator")
    
    destination = st.selectbox("Choose Destination", 
                             ["Delhi-Agra-Jaipur", "Goa", "Manali", "Kerala Backwaters", "Darjeeling"])
    
    days = st.slider("Trip Duration", 3, 10, 5)
    
    if st.button("✨ Generate Itinerary", type="primary"):
        st.balloons()
        show_sample_itinerary(destination, days)

def show_sample_itinerary(dest, days):
    itineraries = {
        "Delhi-Agra-Jaipur": [
            "Day 1: Delhi - Red Fort, India Gate, Qutub Minar",
            "Day 2: Agra - Taj Mahal Sunrise, Agra Fort", 
            "Day 3: Fatehpur Sikri, drive to Jaipur",
            "Day 4: Jaipur - Amber Fort, Hawa Mahal, Shopping",
            "Day 5: City Palace, Jantar Mantar, Return"
        ],
        "Goa": [
            "Day 1: North Goa - Baga Beach, Fort Aguada",
            "Day 2: South Goa - Colva Beach, Churches",
            "Day 3: Water sports & Party night",
            "Day 4: Dudhsagar Falls & Spice Plantation"
        ]
    }
    
    st.success(f"✅ Perfect {days}-day itinerary for {dest}!")
    
    for day in itineraries.get(dest, ["Custom itinerary generated"])[0:days]:
        st.info(day)

def booking_interface():
    st.subheader("✈️ Instant Booking")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Flight Deals")
        flights = pd.DataFrame({
            'Route': ['DEL-BOM', 'BLR-DEL', 'PNQ-GOI', 'CCU-IXB'],
            'Price': ['₹2999', '₹3899', '₹1999', '₹4499'],
            'Date': ['Mar 15', 'Mar 20', 'Mar 25', 'Apr 1']
        })
        st.dataframe(flights, use_container_width=True)
    
    with col2:
        st.subheader("Hotels")
        hotels = pd.DataFrame({
            'Hotel': ['Taj Gateway', 'ITC Grand', 'Lemon Tree', 'FabHotel'],
            'Price/Night': ['₹5999', '₹8999', '₹2999', '₹1999'],
            'Location': ['Delhi', 'Agra', 'Goa', 'Manali']
        })
        st.dataframe(hotels, use_container_width=True)
    
    if st.button("💳 Book Now", type="primary"):
        st.success("🎉 Booking confirmed! Check your email.")

def display_stats():
    st.subheader("📊 Travel Trends 2026")
    
    months = ['Jan', 'Feb', 'Mar', 'Apr']
    north = [1200, 1500, 1800, 2200]
    south = [800, 1000, 1400, 1900]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='North India', x=months, y=north))
    fig.add_trace(go.Bar(name='South India', x=months, y=south))
    fig.update_layout(title="Booking Trends", barmode='group')
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
