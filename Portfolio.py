import streamlit as st
import os
# --- Page Config ---
st.set_page_config(page_title="Tushar Yadav's Portfolio", layout="wide")

# --- Session Initialization ---
if "page" not in st.session_state:
    st.session_state["page"] = "Home"
if "show_project" not in st.session_state:
    st.session_state["show_project"] = None
import base64
def encode_image_to_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    file_ext = os.path.splitext(path)[-1][1:]  # jpg, png etc.
    return f"data:image/{file_ext};base64,{encoded}"
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call it with your file:
set_background("portfoliobg.jpg")

# --- Navbar ---
def navbar():
    st.markdown(
        """
        <style>
        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #000000;
            padding: 0.1rem 0.8rem;
            border-radius: 4px;
            margin-bottom: 0.1rem;
        }
        .nav-title {
            color: #ffffff;
            font-size: 1.3rem;
            font-weight: bold;
            letter-spacing: 1px;
        }
        .nav-buttons button {
            background-color: transparent;
            color: #ffffff;
            font-size: 1rem;
            font-weight: 500;
            border: none;
            padding: 0.5rem 1rem;
            margin-left: 1rem;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .nav-buttons button:hover {
            background-color: #222;
            border-radius: 5px;
            transform: scale(1.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns([4, 2])
    with col1:
        st.markdown('<div class="nav-title">Tushar Yadav\'s Portfolio 🌟</div>', unsafe_allow_html=True)
    with col2:
        btn_home, btn_about, btn_contact = st.columns(3)
        with btn_home:
            if st.button("Home"):
                st.session_state["page"] = "Home"
        with btn_about:
            if st.button("About"):
                st.session_state["page"] = "About"
        with btn_contact:
            if st.button("Contact"):
                st.session_state["page"] = "Contact"
    st.markdown("------")
# --- Project Card Style ---
st.markdown("""
    <style>
    .project-card {
        position: relative;
        overflow: hidden;
        border-radius: 12px;
        transition: transform 0.3s ease;
        cursor: pointer;
        margin-bottom: 1rem;
    }
    .project-card img {
        width: 100%;
        border-radius: 12px;
        transition: transform 0.3s ease;
    }
    .project-card:hover img {
        transform: scale(1.05);
    }
    .project-title {
        margin-top: 0.5rem;
        font-size: 1.1rem;
        font-weight: bold;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# --- Pages ---
def home():
    # Create two columns
    col1, col2 = st.columns([1,2])

    with col2:
        st.header("🌈About Me")
        st.write("""
        A dedicated and aspiring Machine Learning Engineer with a strong passion for building intelligent systems that solve real-world problems. 
        I aim to contribute to an organization that values innovation and supports both technical advancement and personal development. 
        My expertise lies in Machine Learning, Deep Learning, SQL, Streamlit, and Database Management.
        """)
        st.write("""
        I enjoy transforming data into actionable insights and deploying user-friendly applications that make complex models accessible. 
        With a growth mindset and a commitment to continuous learning, I strive to stay at the forefront of AI advancements and contribute meaningfully 
        to impactful projects and collaborative teams.
        """)
    with col1:
        st.header("Contact")
        st.write("Feel free to reach out to me!")
        st.write("📧 Email: tusharyadav61900@gamil.com") 
        st.write("🐙 GitHub: [Tushar Yadav](https://github.com/Tushar01yadav?tab=repositories)")
        st.write("🔗 LinkedIn: [Tushar Yadav](https://www.linkedin.com/in/tushar-yadav-5829bb353/)")
        st.write("📞 Phone: +91-8826610864")
    

    st.markdown("---")   
    st.header("Projects 🚀")

    projects = [
            {
                "title": "Cancer Diagnosis Assistant",
                "image":  encode_image_to_base64("cancer.png"),
                "description": "A smart diagnostic tool using ML models, A smart, self-learning web application for breast cancer prediction built with Streamlit.The app automatically retrains itself after every 5 new inputs by learning from stored input/output data.",
                "details": "This project is a smart, self-learning web application for breast cancer prediction built with Streamlit. The app automatically retrains itself after every 5 new inputs by learning from stored input/output data. It uses machine learning models to predict the likelihood of breast cancer based on user inputs.",
                "link": "https://github.com/Tushar01yadav/Cancer-Diagnosis-Assistant-Self-Learning-"
            },
            {
                "title": "Smart Farming Assistant",
                "image": encode_image_to_base64("crop.png"),
                "description": "Crop Recommender + Disease Detector, An AI tool to assist farmers with crop planning and disease management,an AI-powered web app that helps farmers make data-driven decisions!",
                "details": "An AI tool to assist farmers with crop planning and disease management,an AI-powered web app that helps farmers make data-driven decisions! This system recommends the most suitable crop based on environmental conditions and detects plant diseases using image classification (CNN).",
                "link": "https://github.com/Tushar01yadav/Smart-Farming-Assistant-Crop-Recommender-Disease-Detector"
            },
            {
                "title": "Satellite Land Use Classification",
                "image": encode_image_to_base64("sat1.png"),
                "description": "Classify land use from satellite images, A CNN-powered deep learning project that classifies satellite images into different land use categories such as urban, forest, water, and agriculture. Built with an interactive Streamlit frontend for real-time inference and visualization.",
                "details": "A deep learning pipeline that analyzes satellite imagery for land classification.",
                "link": "https://github.com/Tushar01yadav/Satellite-Image-Land-Use-Classification"
            },
        ]

    cols = st.columns(2)

    with cols[0]:
            for i in [0, 2]:
                project = projects[i]
                st.markdown(f"""
                    <a href="{project['link']}" target="_blank" style="text-decoration: none;">
                        <div class="project-card" onclick="this.parentNode.submit();">
                            <img src="{project['image']}" />
                            <div class="project-title">{project['title']}</div>
                            <p style='color:#ccc;font-size:0.9rem;'>{project['description']}</p>
                        </div>
                    </form>
                """, unsafe_allow_html=True)

    with cols[1]:
            i = 1
            project = projects[i]
            st.markdown(f"""
                 <a href="{project['link']}" target="_blank" style="text-decoration: none;">
                    <div class="project-card" onclick="this.parentNode.submit();">
                        <img src="{project['image']}" />
                        <div class="project-title">{project['title']}</div>
                        <p style='color:#ccc;font-size:0.9rem;'>{project['description']}</p>
                    </div>
                </form>
            """, unsafe_allow_html=True)

        # Handle query param click
    query = st.query_params
    if "proj" in query:
            idx = int(query["proj"][0])
            st.session_state["show_project"] = idx

    if st.session_state["show_project"] is not None:
            project = projects[st.session_state["show_project"]]
            st.markdown("---")
            st.subheader(project["title"])
            st.image(project["image"], width=600)
            st.write(project["details"])
    st.markdown("------")

        
    st.write("""
    ### 🛠️ **Skills / 🧰 Tech Stack**

    -  **Machine Learning**/n
     Builds regression and classification models, from data preprocessing to deployment-ready pipelines.
                 
    -  **Python**, 🧹 Data Preprocessing, 📊 Data Visualization
    - 🎯 **Supervised Learning algorithms**, 🌀 **Unsupervised Learning algorithms**, 🧠 Artificial Neural Networks (ANN), 🖼️ Convolutional Neural Networks (CNN)
    -  **Java**,  Python
    - 📚 **Scikit-Learn**,  TensorFlow,  Keras,  Pandas, ➗ NumPy
    - 🌐 **Streamlit UI** development
    -  **SQLite database**,  SQL
    - 📈 **Data Analysis** – insights extraction, business impact
    """)
    st.markdown("---")
    st.header("Education 🎓")
    st.write("""
    **The Northcap University**  
    B.Tech (2021–2025)  
    Learnt core concepts of SQL, AI & ML, DSA, and database management.  

    **Suraj School, Mahendargarh**  
    12th (2018–2020)  
    Achieved 96% in 12th Science (PCM), demonstrating strong academic excellence.
    """)
    st.markdown("---")
    st.header("Contact")
    st.write("Feel free to reach out to me!")
    st.write("📧 Email : tusharyadav61900@gamil.com") 
    st.write("🐙 GitHub: [Tushar Yadav](https://github.com/Tushar01yadav?tab=repositories)")
    st.write("🔗 LinkedIn: [Tushar Yadav](https://www.linkedin.com/in/tushar-yadav-5829bb353/)")
    st.write("📞 Phone: +91-8826610864")


def about():
    st.header("About Me")
    st.write("""
        Hi, I'm Tushar Yadav, a software developer with a passion for building impactful solutions.
        I specialize in Python, web development, and data science. I love learning new technologies and collaborating on exciting projects.
    """)
    st.write(" I am a dedicated and aspiring Machine Learning Engineer with a strong passion for building intelligent systems that solve real-world problems. I aim to contribute to an organization that values innovation and supports both technical advancement and personal development. My expertise lies in Machine Learning, Deep Learning, SQL, Streamlit, and Database Management. ")
    st.write(" I enjoy transforming data into actionable insights and deploying user-friendly applications that make complex models accessible. With a growth mindset and a commitment to continuous learning, I strive to stay at the forefront of AI advancements and contribute meaningfully to impactful projects and collaborative teams.")    
    st.markdown("------")
    
    
    st.write("""
### 🛠️ **Skills / 🧰 Tech Stack**

-  **Machine Learning**
-  **Python**, 🧹 Data Preprocessing, 📊 Data Visualization
- 🎯 **Supervised Learning algorithms**, 🌀 **Unsupervised Learning algorithms**, 🧠 Artificial Neural Networks (ANN), 🖼️ Convolutional Neural Networks (CNN)
-  **Java**,  Python
- 📚 **Scikit-Learn**,  TensorFlow,  Keras,  Pandas, ➗ NumPy
- 🌐 **Streamlit UI** development
-  **SQLite database**,  SQL
- 📈 **Data Analysis** – insights extraction, business impact
""")
    st.markdown("------")

    st.header("Education ")
    st.write("""
**The Northcap University**  
B.Tech (2021–2025)  
Learnt core concepts of SQL, AI & ML, DSA, and database management.  

**Suraj School, Mahendargarh**  
12th (2018–2020)  
Achieved 96% in 12th Science (PCM), demonstrating strong academic excellence.
""")


def contact():
    st.header("Contact")
    st.write("Feel free to reach out to me!")
    st.write("📧 Email : tusharyadav61900@gamil.com") 
    st.write("🐙 GitHub: [Tushar Yadav](https://github.com/Tushar01yadav?tab=repositories)")
    st.write("🔗 LinkedIn: [Tushar Yadav](https://www.linkedin.com/in/tushar-yadav-5829bb353/)")
    st.write("📞 Phone: +91-8826610864")

# --- Main App ---
def main():
    navbar()
    page = st.session_state["page"]
    if page == "Home":
        home()
    elif page == "About":
        about()
    elif page == "Contact":
        contact()

main()
