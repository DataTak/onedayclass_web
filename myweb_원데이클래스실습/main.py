import streamlit as st

#스트림릿의 단점은.. 폰트 설정 등 세부적으로 조정하고 싶은 것들이 안된다.


# button = st.button("버튼")
# if button:
#     st.write("버튼을 눌렀습니다")
# button2 = st.button("버튼2")
# if button2:
#     st.write("버튼을 눌렀습니다")

# check = st.checkbox("선택")
# if check:
#     st.write("선택되었습니다")


# st.title("😍Title")
# st.header("Header")
# st.subheader("Subheader")
# st.write("가장 작은 글자")
# st.markdown(" # 제목 \n ## :red[부제목]입니다.  \n ### 소제목")



# ## 음식 메뉴판 만들기 실습

# check_짜장면 = st.checkbox("짜장면(5000원)")
# check_짬뽕 = st.checkbox("짬뽕(7000원)")
# check_탕수육 = st.checkbox("탕수육(15000원)")   
# 가격 = 0


# if check_짜장면:
#     가격 += 5000
    
# if check_짬뽕:
#     가격 += 7000

# if check_탕수육:
#     가격 += 15000
    
# st.subheader(f"가격은 {가격}원 입니다.")



메뉴 = st.sidebar.selectbox("메뉴", ["로그인", "회원가입", "비밀번호 찾기"])


if 메뉴 == "로그인":
    db_id = "test"
    db_pw = "123"

    st.title("🏀로그인")
    id=st.text_input("아이디", placeholder="아이디를 입력해주세요")
    pw=st.text_input("비밀번호", type="password")
    login = st.button("로그인")

    if login:
        if db_id == id and db_pw == pw:
            st.success("로그인 성공")
            st.balloons()
        else:
            st.error("로그인 실패")
            st.snow()
            

elif 메뉴 == "회원가입":
    st.title("🏀회원가입")
    
elif 메뉴 == "비밀번호 찾기":
    st.video("https://www.youtube.com/watch?v=ekr2nIex040")