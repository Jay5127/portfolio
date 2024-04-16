import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image




st.set_page_config(page_title= 'My web page' , page_icon= ':tada:' , layout= 'wide')

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use local css
def local_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading CSS file: {e}")

# Call the local_css() function with the file path
local_css('style.css')

# Load Assets
lottie = load_lottie_url('https://lottie.host/e241daf1-63cb-418d-b8a1-4070ea4986d7/OOldqGn7qv.json')
harry = Image.open('images/harry.png')
# py = Image.open('D:\VS code\Streamlit\Website Coding is fun\images\py.png')




# Header 
with st.container():
    st.header('Hello I am Jay K. Chakole :wave:')
    st.title('I am 3rd year AI & DS engineering student')
    st.write('As a third-year AI&DS (Artificial Intelligence and Data Science) student, Im immersed in the captivating realm of cutting-edge technology and data-driven insights. With each algorithm mastered and dataset analyzed, I m honing my skills in machine learning, natural language processing, and data visualization, poised to tackle complex real-world challenges. From crafting predictive models to unraveling patterns in vast data sets, my journey involves constant exploration, innovation, and collaboration with peers and mentors. With a passion for harnessing the power of data to drive meaningful change, I eagerly anticipate the opportunities ahead to make a tangible impact in industries ranging from healthcare to finance and beyond.')
    st.write('[Here is my youtube channel >]  (https://www.youtube.com/@guitarist_jay)')





#What I do 
with st.container():
    st.write('---')
    left_column , right_column = st.columns(2)
    
    with left_column:
        st.header('What I do')
        st.write('###')
        st.write('As someone who balances the rhythmic melodies of guitar strings with the structured syntax of coding, I find solace in the harmonious blend of creativity and logic. Whether Im strumming chords to unwind or delving into Python scripts to solve intricate problems, my passion for both music and programming fuels my curiosity and drive for continuous learning. From crafting soulful melodies to crafting efficient algorithms, I thrive on the process of creation and the satisfaction of seeing projects come to life. Python, with its elegant simplicity and versatility, serves as my gateway to exploring the endless possibilities of software development and data manipulation. As I navigate the intricate rhythms of both guitar and code, I find fulfillment in the art of expression and the pursuit of mastery in these interconnected realms.')
        st.write('[Learn more >](https://www.instagram.com/jay/)')

    with right_column:
        st_lottie(lottie , height= 300 , key = 'guitar')





# My Projects
with st.container():
    st.write('---')
    st.header('Projects')
    image_column , text_column = st.columns((1,2))

    with image_column:
        st.image(harry)

    with text_column:
        st.subheader('Chatbot in laptop')
        st.write('Embarking on a Python chatbot project opens up a world of creativity and innovation, where I can seamlessly merge my coding skills with the intricacies of natural language processing. From inception to deployment, each stage of the project presents a unique challenge to overcome, whether its designing conversational flows, implementing machine learning algorithms for context understanding, or refining the bots responses for a more human-like interaction. Through meticulous iteration and testing, I strive to create a chatbot that not only provides accurate and relevant information but also fosters genuine engagement and satisfaction for its users. With every line of code written, I am not just building a program; I am crafting a digital companion that can enrich and streamline communication, ultimately paving the way for more intuitive and accessible human-computer interactions.')
        st.markdown('[Learn more>] (https://youtu.be/PGaiZfjJZi0?si=qmTgd3XjWZI7GwL3)')



#Contact Form
with st.container():
    st.write('---')
    st.header('Contact')
    st.write('##')

    contact_form = '''<form action="https://formsubmit.co/jaychakole123@gmail.com" method="POST">
     <input type = 'hidden' name = '_captcha' value = 'false'>
     <input type="text" name="name" placeholder = 'Your name' required>
     <input type="email" name="email" placeholder = 'Your email' required>
     <textarea name = 'Message' placeholder = 'Enter your message' required></textarea> 
     <button type="submit">Send</button>
     </form>
     '''

    left_column , right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form , unsafe_allow_html= True)
    with right_column:
        st.empty()
