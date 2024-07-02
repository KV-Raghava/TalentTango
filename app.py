import streamlit as st;
from streamlit_option_menu import option_menu
import asyncio
from src.components.ats import atsMain
from src.components.jdGeneration import jdGenMain
from src.components.questions import questionsMain
from src.components.intFeed import intFeedMain
# from src.components.sentAna import sentAnaMain
# state variables
if 'selected' not in st.session_state:
    st.session_state.selected = "ATS"
if 'jdGenSubmit' not in st.session_state:
    st.session_state.jdGenSubmit = False
if 'isEnrichClicked' not in st.session_state:
    st.session_state.isEnrichClicked = False
if 'enrichContent' not in st.session_state:
    st.session_state.enrichContent=None
if 'jd' not in st.session_state:
    st.session_state.jd=None
if 'updatedJd' not in st.session_state:
    st.session_state.updatedJd=""
if 'intFeed' not in st.session_state:
    st.session_state.intFeed = None
if 'role' not in st.session_state:
    st.session_state.role=None
if 'min_exp' not in st.session_state:
    st.session_state.min_exp=None
if 'max_exp' not in st.session_state:
    st.session_state.max_exp=None
if 'requirements' not in st.session_state:
    st.session_state.requirements=None
if 'transcript' not in st.session_state:
    st.session_state.transcript=None
if 'jdTokenCount' not in st.session_state:
    st.session_state.jdTokenCount=0
if 'atsTokenCount' not in st.session_state:
    st.session_state.atsTokenCount=0
if 'intFeedTokenCount' not in st.session_state:
    st.session_state.intFeedTokenCount=0
if 'questionsTokenCount' not in st.session_state:
    st.session_state.questionsTokenCount=0

async def initialize():
    with st.sidebar:  
        st.session_state.selected = option_menu(
            menu_title="Talent Tango",
            options=[
                "Talent Craft",
                "Talent Tracking",
                "Talent Screening",
                "Talent Recap",
                "Talent Sense"              
            ],
            menu_icon="none",
        )
    if st.session_state.selected == "Talent Tracking":
        await atsMain()
    if st.session_state.selected == "Talent Craft":
        await jdGenMain()
    if st.session_state.selected == "Talent Screening":
        await questionsMain()
    if st.session_state.selected ==  "Talent Recap":
        await intFeedMain()    
    if st.session_state.selected == "Talent Sense":
        # await sentAnaMain()
        st.write("nltk Issue")
if  __name__ == '__main__':
    # st.session_state.account = authenticate()
    asyncio.run(initialize())