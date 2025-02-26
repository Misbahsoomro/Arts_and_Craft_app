import streamlit as st
import sqlite3
from PIL import Image
import time
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

# Set page configuration
st.set_page_config(
    page_title="Arts and Craft Challenge",
    page_icon="🌱",
    layout="centered",
)


# Custom CSS for animations
st.markdown(
    """
    <style>
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .animated {
            animation: fadeInUp 1s ease-in-out;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize SQLite database
conn = sqlite3.connect("growth_mindset.db")
c = conn.cursor()

# Create tables if they don't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"""
)
c.execute(
    """CREATE TABLE IF NOT EXISTS progress
             (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, progress INTEGER, date TEXT)"""
)
c.execute(
    """CREATE TABLE IF NOT EXISTS reflections
             (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, reflection TEXT, date TEXT)"""
)
c.execute(
    """CREATE TABLE IF NOT EXISTS habits
             (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, habit TEXT, date TEXT)"""
)
conn.commit()

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Boost Your Creativity",
        "Progress Monitor",
        "Sign Up",
        "Login",
    ],
)
# User Authentication
def login(username, password):
    c.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?", (username, password)
    )
    return c.fetchone()


def sign_up(username, password):
    c.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
    )
    conn.commit()
# User Authentication
def login(username, password):
    c.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?", (username, password)
    )
    return c.fetchone()


def sign_up(username, password):
    c.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
    )
    conn.commit()
# Home Page
if page == "Home":
    st.markdown(
        "<h1 class='animated' style='color: green;'>Welcome to the Arts and Craft Challenge! 🎨🖌️</h1>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])

    # Load text first
    with col1:
        st.markdown(
            """
        <div class='animated'>
            <h3>What is Arts and Craft?</h3>
            <p>Arts and Craft is a creative activity where you make things using your hands, such as painting, drawing, sculpture, or other handmade works. 
            It allows you to express your creativity and improve your skills. Whether you are an expert or a beginner, the process of creating can be incredibly rewarding.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
    <div class='animated'>
        <h3>Why Engage in Arts and Craft?</h3>
        <ul>
            <li><b>Unleash Your Creativity:</b> Arts and craft activities encourage you to think outside the box and express your ideas.</li>
            <li><b>Improve Fine Motor Skills:</b> Working with your hands helps improve coordination and dexterity.</li>
            <li><b>Relax and De-stress:</b> Crafting can be a therapeutic activity, helping you unwind and focus on the present moment.</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class='animated'>
        <h3>How Can You Get Started with Arts and Craft?</h3>
        <ul>
            <li><b>Choose Your Medium:</b> Whether it's painting, knitting, or paper crafting, pick a craft that excites you.</li>
            <li><b>Learn the Basics:</b> Take time to learn the foundational skills for your chosen craft.</li>
            <li><b>Practice Regularly:</b> The more you practice, the better you'll become. Don't be afraid to make mistakes!</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class='animated'>
        <p>Engaging in arts and craft not only helps you relax and develop new skills but also connects you to a community of creative individuals. 
        No matter what craft you choose, remember that the joy is in the process and the creative expression it brings.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    # Show spinner and load image separately
    with col2:
        with st.spinner("Loading image..."):
            time.sleep(1)
            try:
                image = Image.open("images.jpg")
                st.image(
                    image,
                    caption="Embrace the power of Creativity!",
                    use_container_width=True,
                )
            except FileNotFoundError:
                st.error("Image file not found. Please check the path.")





import random
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import streamlit as st

# Boost Your Creativity Page
if page == "Boost Your Creativity":
    # Custom CSS to ensure the heading stays visible
    st.markdown(
        """
        <style>
        .stHeadingContainer {
            position: sticky;
            top: 0;
            background-color: white;
            z-index: 1000;
            padding: 10px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    # Add content to the first column
    with col1:
        st.markdown(
            "<h1 style='color: green;'>🎨 Arts and Craft Creativity Booster</h1>",
            unsafe_allow_html=True,
        )

    # Motivational Quotes for Artists
    quotes = [
        "🌱 Creativity blooms when you try something new!",
        "💡 Every project is an opportunity to express yourself!",
        "🔥 Your hands create what your mind imagines!",
        "🚀 Every brushstroke brings you closer to your masterpiece!",
        "🌟 No matter how small the progress, you're always creating!",
    ]

    # Add content to the second column
    with col2:
        st.subheader("💭 Your Daily Artistic Inspiration")
        st.info(random.choice(quotes))

    # Artistic Goal
    goal = st.text_area("Set Your Artistic Goal:") 

    # Achieved Goal Date
    achieved_date = st.date_input("When did you finish your project?")
    if achieved_date:
        st.success(
            f"🎉 Bravo! You finished your project on **{achieved_date}**. Keep going and create more! 🏆"
        )

    # Arts and Craft Tips
    tips = st.radio(
        "Pick a tip to boost your creativity:",
        [
            "🎨 Experiment with new materials and techniques!",
            "🔄 Mistakes are just happy accidents – embrace them!",
            "💬 Feedback helps you improve, don't hesitate to ask for it.",
            "🏋️ Push your limits – try something you've never done before!",
            "🧠 Creativity thrives with practice – the more you create, the better you get!",
        ],
    )
    st.success(f"**Tip Selected:** {tips}")

    # Feedback on Progress
    feedback = st.selectbox(
        "How do you feel about your creative journey?",
        ["Feeling Inspired!", "Still Exploring", "Need More Motivation"],
    )
    st.write(f"💬 **Your Response:** {feedback}")

    # Celebration Button
    celebrate = st.button("🚀 Celebrate Your Creativity!")
    if celebrate:
        st.snow()
    st.success("Every piece of art you create is a step forward. Keep up the great work! 🎉")

    # Function to generate PDF
    def generate_pdf(goal, achieved_date, tips, feedback):
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)
        pdf.setTitle("Arts and Craft Creativity Progress")

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(200, 750, "🎨 Arts and Craft Creativity Progress 🎨")

        pdf.setFont("Helvetica", 12)
        pdf.drawString(100, 700, f"Artistic Goal: {goal}")
        pdf.drawString(100, 670, f"Achieved Date: {achieved_date}")
        pdf.drawString(100, 640, f"Selected Tip: {tips}")
        pdf.drawString(100, 610, f"Journey Feedback: {feedback}")

        pdf.drawString(100, 570, "🎉 Keep creating and push your artistic boundaries! 🚀")

        pdf.save()
        buffer.seek(0)
        return buffer

    # Download PDF Button
    if st.button("📥 Download Your Progress as PDF"):
        if goal and achieved_date:
            pdf_file = generate_pdf(goal, achieved_date, tips, feedback)
            st.download_button(
                label="📥 Click to Download PDF",
                data=pdf_file,
                file_name="arts_and_craft_creativity_progress.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("⚠️ Please fill in all fields before downloading.")


# Progress Monitor
elif page == "Progress Monitor":
    st.markdown(
        "<h1 style='color: green;'>Progress Monitor 📊</h1>",
        unsafe_allow_html=True,
    )
    
    st.write("### Track your artistic progress and stay motivated! 🚀")
    
    progress = st.slider("📈 How much progress have you made today?", 0, 100, 50)
    
    if st.button("💾 Save Progress"):
        if "user_id" in st.session_state:
            c.execute(
                'INSERT INTO progress (user_id, progress, date) VALUES (?, ?, DATE("now"))',
                (st.session_state["user_id"], progress),
            )
            conn.commit()
            
            st.success(f"✅ Progress saved successfully: {progress}%")
            
            # Display motivational message
            if progress < 30:
                st.warning("Keep pushing! 💪 Small steps lead to big achievements.")
            elif progress < 70:
                st.info("You're doing great! Stay consistent. ✨")
            else:
                st.success("Amazing progress! Keep up the fantastic work! 🎉")
        else:
            st.error("🚨 Please log in to save your progress.")


# Sign Up Page
elif page == "Sign Up":
    st.markdown(
        "<h1 style='color: green;'>Sign Up</h1>",
        unsafe_allow_html=True,
    )
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        sign_up(username, password)
        st.success("You have successfully signed up! Please log in.")


# Login Page
elif page == "Login":
    st.markdown(
        "<h1 style='color: green;'>Log in</h1>",
        unsafe_allow_html=True,
    )
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login(username, password)
        if user:
            st.session_state["user_id"] = user[0]
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password.")
