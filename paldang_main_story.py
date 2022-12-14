import streamlit as st

# Page Setting
st.set_page_config(
    layout="centered",
    page_title="Dacon Competition | Team_PaldangPaldang",
    page_icon="π",
)

st.title("Dacon Competition")
st.header('Team νλΉνλΉ')
st.image('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/adbc4cd6-e590-404a-9b8e-1c1c7f1a4f70/FQxGhN4VgAIx0rz.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220818T153837Z&X-Amz-Expires=86400&X-Amz-Signature=d0784ea5a578bffe28b6a87046d797fa5ca9a77fb93f549db160264f4d11f312&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22FQxGhN4VgAIx0rz.jpg%22&x-id=GetObject')

st.markdown('---')
st.subheader('νλ‘μ νΈ μ£Όμ ')

text_1 = '2012-2022λ 5-10μ νλΉλ/νκ°/κ°μλ λ°μ΄ν°λ₯Ό κΈ°λ°μΌλ‘ ν νκ°μ <span style="color:red">4λκ΅ μμ μμΈ‘</span>'
st.markdown(text_1, unsafe_allow_html=True)

st.markdown('---')
st.subheader("About the Backgrounds")

st.markdown('''
**μ μΈκ³μ μΌλ‘ λ°μνκ³  μλ κΈ°μ μ΄λ³ νμ**κ³Ό κ΄λ ¨ν΄ **κ³΅κ³΅ μμ **μ λμμ΄ λλ νλ‘μ νΈλ₯Ό μ§ν

*  μ΅κ·Ό κΈ°νλ³νλ‘ μΈν΄ νμ νΌν΄λ₯Ό μ΅μννλ λμ μ­ν μ λ§€μ° μ€μν΄μ§κ³  μμ.

    * νλΉλμ μμΈ λ° μλκΆμ νμ λ°©μ΄μ μμ΄ μ΅νμ λ³΄λ£¨ μ­ν μ νκ³  μμ.
''')
st.image('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4ec4aefe-3a63-490c-9eb4-d321193097e3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220819T015528Z&X-Amz-Expires=86400&X-Amz-Signature=45f7289e443b8ee751f04ab629e1bb9463d192f9853e0a6a2f0e13d9d6d642ea&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject')
st.markdown('''
* νλΉλμ νμ μμ μ΄μμ λ°λΌ μμΈμλ΄ νκ° μ£Όμμ§μ (μ²­λ΄, μ μκ΅, νκ°, νμ£Όλκ΅)μ μμλ₯Ό μμΈ‘,

    * νμμ¬ν΄λ‘ μΈν νΌν΄λ₯Ό λ°©μ§ λ° μ΅μν νκ³ μ ν¨.
''')

st.markdown('---')
st.subheader('μ μ²΄ νλ¦λ')
st.image('https://velog.velcdn.com/images/thov1017/post/f32dbf17-4567-4c57-a41f-bda5695d4f11/image.png', width = 700)
text_2 = ('μ°μΈ‘ νλΉλμμ μμλ λ¬Όμ<br>1. <span style="color:DarkViolet">μ§κ΄κ΅ κ°μλ</span>κ³Ό <span style="color:DarkViolet">λκ³‘κ΅ κ°μλ</span>μ΄ ν©μ³μ§ ν <span style="color:Magenta">μ²­λ΄λκ΅</span>μ μμμ μ λμ΄ κΈ°λ‘λλ€.<br>2. μ΄ν <span style="color:DarkViolet">μ‘μ λμ κ°μλ</span>μ΄ ν©μ³μ§ νμ <span style="color:Magenta">μ μκ΅</span>λ₯Ό μ§λλ€.<br>3. <span style="color:Magenta">νκ°λκ΅</span>, <span style="color:Magenta">νμ£Όλκ΅</span> μμΌλ‘ λ¬Όμ΄ μ­ νλ¬κ°λ νλ¦')
st.markdown(text_2, unsafe_allow_html=True)
