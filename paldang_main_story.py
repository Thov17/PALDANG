import streamlit as st

# Page Setting
st.set_page_config(
    layout="centered",
    page_title="Dacon Competition | Team_PaldangPaldang",
    page_icon="🌊",
)

st.title("Dacon Competition")
st.header('Team 팔당팔당')
st.image('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/adbc4cd6-e590-404a-9b8e-1c1c7f1a4f70/FQxGhN4VgAIx0rz.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220818T153837Z&X-Amz-Expires=86400&X-Amz-Signature=d0784ea5a578bffe28b6a87046d797fa5ca9a77fb93f549db160264f4d11f312&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22FQxGhN4VgAIx0rz.jpg%22&x-id=GetObject')

st.markdown('---')
st.subheader('프로젝트 주제')

text_1 = '2012-2022년 5-10월 팔당댐/한강/강수량 데이터를 기반으로 한 한강의 <span style="color:red">4대교 수위 예측</span>'
st.markdown(text_1, unsafe_allow_html=True)

st.markdown('---')
st.subheader("About the Backgrounds")

st.markdown('''
**전세계적으로 발생하고 있는 기상 이변 현상**과 관련해 **공공 안전**에 도움이 되는 프로젝트를 진행

*  최근 기후변화로 인해 홍수 피해를 최소화하는 댐의 역할은 매우 중요해지고 있음.

    * 팔당댐은 서울 및 수도권의 홍수 방어에 있어 최후의 보루 역할을 하고 있음.
''')
st.image('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4ec4aefe-3a63-490c-9eb4-d321193097e3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220819T015528Z&X-Amz-Expires=86400&X-Amz-Signature=45f7289e443b8ee751f04ab629e1bb9463d192f9853e0a6a2f0e13d9d6d642ea&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject')
st.markdown('''
* 팔당댐의 홍수 안전운영에 따라 서울시내 한강 주요지점(청담, 잠수교, 한강, 행주대교)의 수위를 예측,

    * 홍수재해로 인한 피해를 방지 및 최소화 하고자 함.
''')

st.markdown('---')
st.subheader('전체 흐름도')
st.image('https://velog.velcdn.com/images/thov1017/post/f32dbf17-4567-4c57-a41f-bda5695d4f11/image.png', width = 700)
text_2 = ('우측 팔당댐에서 시작된 물은<br>1. <span style="color:DarkViolet">진관교 강수량</span>과 <span style="color:DarkViolet">대곡교 강수량</span>이 합쳐진 후 <span style="color:Magenta">청담대교</span>에 수위와 유량이 기록된다.<br>2. 이후 <span style="color:DarkViolet">송정동의 강수량</span>이 합쳐진 후에 <span style="color:Magenta">잠수교</span>를 지난다.<br>3. <span style="color:Magenta">한강대교</span>, <span style="color:Magenta">행주대교</span> 순으로 물이 쭉 흘러가는 흐름')
st.markdown(text_2, unsafe_allow_html=True)
