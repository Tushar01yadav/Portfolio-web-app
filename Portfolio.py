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
    col1, col2 = st.columns([5, 2])
    with col1:
        st.markdown('<div class="nav-title">Tushar Yadav\'s Portfolio 🌟</div>', unsafe_allow_html=True)
        with open("Tushar Yadav Resume.pdf", "rb") as pdf_file:
         PDFbyte = pdf_file.read()

        st.download_button(label="📄 Resume",
                   data=PDFbyte,
                   file_name="Tushar Yadav Resume.pdf",
                   mime="application/pdf")

        
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
    col1, col2 = st.columns([0.9,2.1])

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

    st.markdown(
     """
     <style>
     .hover-box-interest {
        background-color: rgba(240, 242, 246, 0.6);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ccc;
        transition: all 0.3s ease-in-out;
     }

     .hover-box-interest:hover {
        background-color: rgba(240, 242, 246, 0.9);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transform: scale(1.01);
     }
     </style>

     <div class="hover-box-interest">
        <h4>💡 <b>Interests</b></h4>
        <ul style="font-size: 16px; color: #31333f; list-style-type: none; padding-left: 1em;">
            <li>🤖 <b>Machine / Deep Learning</b></li>
            <li>🧠 <b>Natural Language Processing (NLP)</b></li>
            <li>🔁 <b>Transformer Models / LLMs</b></li>
            <li>🕹️ <b>Agentic AI</b></li>
            <li>🧩 <b>Multimodal AI Agents</b></li>
        </ul>
     </div>
     """, unsafe_allow_html=True)
    st.markdown("---")   
    st.header("Projects 🚀")
    st.write("")
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
            {
                "title": "Review Sentient Analysis on Products / Movies",
                "image": encode_image_to_base64("r1.png"),
                "description": "Review Sentiment Analyzer is a user-friendly web application that analyzes the sentiment of product or movie reviews. It leverages two powerful models — a state-of-the-art Hugging Face transformer and a classic Scikit-Learn classifier — to predict whether a review is positive or negative, providing confidence scores for better insights. Built with Streamlit, the app offers a sleek interface for quick and accurate sentiment analysis. ",
                "details": " Review Sentiment Analyzer is a user-friendly web application that analyzes the sentiment of product or movie reviews. It leverages two powerful models — a state-of-the-art Hugging Face transformer and a classic Scikit-Learn classifier — to predict whether a review is positive or negative, providing confidence scores for better insights. Built with Streamlit, the app offers a sleek interface for quick and accurate sentiment analysis.",
                "link": "https://github.com/Tushar01yadav/Sentiment-analysis-Product-Movie-.git"
            }
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
        for i in [1,3]:
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
    st.header("🛠️ **Skills / 🧰 Tech Stack**")
    st.write("")
    st.markdown(
    """
    <style>
    .grid-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 20px;
    }

    .hover-box {
        background-color: rgba(240, 242, 246, 0.6);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ccc;
        transition: all 0.3s ease-in-out;
        width: 48%;
        box-sizing: border-box;
    }

    .hover-box:hover {
        background-color: rgba(240, 242, 246, 0.9);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transform: scale(1.01);
    }

    .hover-box h4 {
        margin-top: 0;
        color: #31333f;
    }

    .hover-box p {
        margin: 0;
        font-size: 15px;
        color: #444;
    }

    @media (max-width: 768px) {
        .hover-box {
            width: 100%;
        }
    }
    </style>

    <div class="grid-container">
        <div class="hover-box">
            <h4>🤖 Machine Learning</h4>
            <p>Builds regression and classification models, from data preprocessing to deployment-ready pipelines.</p>
        </div>
        <div class="hover-box">
            <h4>🧠 Deep Learning</h4>
            <p>Trained CNNs for image tasks like crop disease detection with real-world datasets. Using neural networks for advanced tasks like image and speech recognition.</p>
        </div>
        <div class="hover-box">
            <h4>🔍 SQL</h4>
            <p>Intermediate SQL skills for querying and analyzing structured data in data science workflows.</p>
        </div>
        <div class="hover-box">
            <h4>🧮 Data Science</h4>
            <p>Applies end-to-end workflows — from raw data to predictive insights and model deployment.</p>
        </div>
        <div class="hover-box">
            <h4>🌐 Streamlit</h4>
            <p> Builds interactive dashboards and ML-powered web apps with user input and real-time predictions.</p>
        </div>
        <div class="hover-box">
            <h4>⚙️ Python Programming</h4>
            <p>Writes clean, modular, and functional code for AI, data science, and automation projects.</p>
        </div>
        <div class="hover-box">
            <h4>📊 Data Visualization</h4>
            <p>Performs exploratory data analysis using Pandas, Matplotlib, and Seaborn to extract key insights. Turning complex data into beautiful, meaningful visuals with insights.</p>
        </div>
        <div class="hover-box">
            <h4>📦 TensorFlow & Scikit-learn</h4>
            <p> Trains models using TF for deep learning and scikit-learn for traditional ML tasks.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True )
        
    st.write("")
    st.markdown("---")
    st.markdown(
     """
     <style>
     .experience-box {
        background-color:  transparent;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ccc;
        margin-bottom: 20px;
     }

     .experience-box p {
        font-size: 16px;
        color: #ffffff;
        margin-bottom: 10px;
     }

     .experience-box b {
        color: #ffffff;
     }
     </style>

     <h2>💼 Experience</h2>
 
     <div class="experience-box">
        <p><b>MACHINE LEARNING TRAINEE</b> | July - Aug 2023<br>
        Intrainz Innovation Pvt. Ltd. | Jul - Aug 2024</p>

        <p>
        Developed an online payment fraud detection system using machine learning. Analyzed transaction patterns to identify fraudulent behavior in real time, enhancing financial security and reducing risk for digital payment platforms.<br>
        <b>Project:</b> Online Payment Fraud Detection
        </p>
        <br>

        <p><b>AI & ML Intern – Microsoft Azure Platform</b> | June - July 2024<br>
        The NorthCap University</p>

        <p>
        Completed the Microsoft Certified: Azure AI Fundamentals (AI-900) exam, gaining a strong foundation in AI concepts, and Azure services.<br>
        Worked on real-time use cases using Azure Machine Learning, Cognitive Services, and Conversational AI tools.<br>
        <b>Project:</b> Chatbot using MS Azure Cognitive Services
        </p>
     </div>
     """,
    unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
     """
     <style>
     .hover-box-edu {
        background-color: rgba(200, 230, 255, 0.4);  /* light bluish transparent */
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #99ccff;
        transition: all 0.3s ease-in-out;
        margin-bottom: 20px;
     }

     .hover-box-edu:hover {
        background-color: rgba(200, 230, 255, 0.9);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transform: scale(1.01);
     }

     .hover-box-edu p {
        margin: 0 0 10px 0;
        font-size: 16px;
        color: #1a1a1a;
     }

     .hover-box-edu strong {
        font-size: 17px;
        color: #003366;
     }
     </style>
 
     <h2>🎓 Education</h2>

     <div class="hover-box-edu">
        <p><strong>The NorthCap University</strong><br>
        B.Tech (2021–2025)<br>
        Learnt core concepts of SQL, AI & ML, DSA, and database management.</p>

        <p><strong>Suraj School, Mahendargarh</strong><br>
        12th (2018–2020)<br>
        Achieved 96% in 12th Science (PCM), demonstrating strong academic excellence.</p>
      </div>
     """,
    unsafe_allow_html=True )



def about():
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
    st.write("")
    st.markdown("---")  
    st.header("🛠️ **Skills / 🧰 Tech Stack**")
    st.write("")
    st.markdown(
    """
    <style>
    .grid-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 20px;
    }

    .hover-box {
        background-color: rgba(240, 242, 246, 0.6);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ccc;
        transition: all 0.3s ease-in-out;
        width: 48%;
        box-sizing: border-box;
    }

    .hover-box:hover {
        background-color: rgba(240, 242, 246, 0.9);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transform: scale(1.01);
    }

    .hover-box h4 {
        margin-top: 0;
        color: #31333f;
    }

    .hover-box p {
        margin: 0;
        font-size: 15px;
        color: #444;
    }

    @media (max-width: 768px) {
        .hover-box {
            width: 100%;
        }
    }
    </style>

    <div class="grid-container">
        <div class="hover-box">
            <h4>🤖 Machine Learning</h4>
            <p>Builds regression and classification models, from data preprocessing to deployment-ready pipelines.</p>
        </div>
        <div class="hover-box">
            <h4>🧠 Deep Learning</h4>
            <p>Trained CNNs for image tasks like crop disease detection with real-world datasets. Using neural networks for advanced tasks like image and speech recognition.</p>
        </div>
        <div class="hover-box">
            <h4>🔍 SQL</h4>
            <p>Intermediate SQL skills for querying and analyzing structured data in data science workflows.</p>
        </div>
        <div class="hover-box">
            <h4>🧮 Data Science</h4>
            <p>Applies end-to-end workflows — from raw data to predictive insights and model deployment.</p>
        </div>
        <div class="hover-box">
            <h4>🌐 Streamlit</h4>
            <p> Builds interactive dashboards and ML-powered web apps with user input and real-time predictions.</p>
        </div>
        <div class="hover-box">
            <h4>⚙️ Python Programming</h4>
            <p>Writes clean, modular, and functional code for AI, data science, and automation projects.</p>
        </div>
        <div class="hover-box">
            <h4>📊 Data Visualization</h4>
            <p>Performs exploratory data analysis using Pandas, Matplotlib, and Seaborn to extract key insights. Turning complex data into beautiful, meaningful visuals with insights.</p>
        </div>
        <div class="hover-box">
            <h4>📦 TensorFlow & Scikit-learn</h4>
            <p> Trains models using TF for deep learning and scikit-learn for traditional ML tasks.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True )
        
    st.write("")
    st.markdown("---")
    st.markdown(
     """
     <style>
     .experience-box {
        background-color:  transparent;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ccc;
        margin-bottom: 20px;
     }

     .experience-box p {
        font-size: 16px;
        color: #ffffff;
        margin-bottom: 10px;
     }

     .experience-box b {
        color: #ffffff;
     }
     </style>

     <h2>💼 Experience</h2>
 
     <div class="experience-box">
        <p><b>MACHINE LEARNING TRAINEE</b> | July - Aug 2023<br>
        Intrainz Innovation Pvt. Ltd. | Jul - Aug 2024</p>

        <p>
        Developed an online payment fraud detection system using machine learning. Analyzed transaction patterns to identify fraudulent behavior in real time, enhancing financial security and reducing risk for digital payment platforms.<br>
        <b>Project:</b> Online Payment Fraud Detection
        </p>
        <br>

        <p><b>AI & ML Intern – Microsoft Azure Platform</b> | June - July 2024<br>
        The NorthCap University</p>

        <p>
        Completed the Microsoft Certified: Azure AI Fundamentals (AI-900) exam, gaining a strong foundation in AI concepts, and Azure services.<br>
        Worked on real-time use cases using Azure Machine Learning, Cognitive Services, and Conversational AI tools.<br>
        <b>Project:</b> Chatbot using MS Azure Cognitive Services
        </p>
     </div>
     """,
    unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
     """
     <style>
     .hover-box-edu {
        background-color: rgba(200, 230, 255, 0.4);  /* light bluish transparent */
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #99ccff;
        transition: all 0.3s ease-in-out;
        margin-bottom: 20px;
     }

     .hover-box-edu:hover {
        background-color: rgba(200, 230, 255, 0.9);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transform: scale(1.01);
     }

     .hover-box-edu p {
        margin: 0 0 10px 0;
        font-size: 16px;
        color: #1a1a1a;
     }

     .hover-box-edu strong {
        font-size: 17px;
        color: #003366;
     }
     </style>
 
     <h2>🎓 Education</h2>

     <div class="hover-box-edu">
        <p><strong>The NorthCap University</strong><br>
        B.Tech (2021–2025)<br>
        Learnt core concepts of SQL, AI & ML, DSA, and database management.</p>

        <p><strong>Suraj School, Mahendargarh</strong><br>
        12th (2018–2020)<br>
        Achieved 96% in 12th Science (PCM), demonstrating strong academic excellence.</p>
      </div>
     """,
    unsafe_allow_html=True )
   
def contact():
        
        st.header("Contact")
        st.write("Feel free to reach out to me!")
        st.write("📧 Email: tusharyadav61900@gamil.com") 
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
