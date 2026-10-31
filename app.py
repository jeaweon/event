import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="너만을 위한 특별한 이벤트 🎁",
    page_icon="🎉",
    layout="centered"
)

# 세션 상태(페이지 번호) 초기화
if "step" not in st.session_state:
    st.session_state.step = 1

# [1단계] 메인 화면 (인사 + 대표 사진)
if st.session_state.step == 1:
    st.title("👋 Xin chào!")
    
    # 이미지 파일 넣는 곳 (저장소 폴더에 main_photo.jpg를 올리거나 이미지 URL 주소 작성)
    try:
        st.image("main_photo.jpg", use_container_width=True)
    except:
        st.info("💡 GitHub 저장소에 'main_photo.jpg' 파일이 없으면 안내 문구가 표시됩니다.")
        
    st.write("Đây là một trang web sự kiện nho nhỏ tôi chuẩn bị dành cho bạn. Bạn có muốn bấm thử vào nút bên dưới không?")
    
    st.write("")
    if st.button("Bấm vào đây ➡️", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# [2단계] 첫 번째 질문
elif st.session_state.step == 2:
    st.title("❓ Q1. 오늘 하루가 어땠어?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("좋아! 😊", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("별로... 🥺", use_container_width=True):
            st.session_state.step = 3
            st.rerun()

# [3단계] 두 번째 질문
elif st.session_state.step == 3:
    st.title("❓ Q2. 더 좋아하는 것은?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("붕어빵 🐟", use_container_width=True):
            st.session_state.step = "retry_q2"
            st.rerun()
    with col2:
        if st.button("재원 💖", use_container_width=True):
            st.session_state.step = 4
            st.rerun()

# [3-1단계] 붕어빵 선택 시 나오는 화면
elif st.session_state.step == "retry_q2":
    st.error("😤 실망이야 다시해")
    st.write("")
    if st.button("두 번째 질문으로 돌아가기 🔄", use_container_width=True):
        st.session_state.step = 3
        st.rerun()

# [4단계] 세 번째 질문
elif st.session_state.step == 4:
    st.title("❓ Q3. 저라는 사람의 첫인상, 솔직히 몇 점이었습니까?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("100점 💯", use_container_width=True):
            st.session_state.step = 5
            st.rerun()
    with col2:
        if st.button("1000점 💥", use_container_width=True):
            st.session_state.step = 5
            st.rerun()

# [5단계] 네 번째 질문
elif st.session_state.step == 5:
    st.title("❓ Q4. 어디를 좋아해?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("경복궁 🏯", use_container_width=True):
            st.session_state.step = 6
            st.rerun()
    with col2:
        if st.button("차이나 타운 🥟", use_container_width=True):
            st.session_state.step = 6
            st.rerun()

# [6단계] 마지막 결과 화면
elif st.session_state.step == 6:
    st.balloons() # 축하 효과
    st.success("✨ 축하합니다! ✨")
    
    st.subheader("첫인상이 좋고 붕어빵보다 좋아하는 사람이 특별히 너랑 데이트 해줄게 🥰")
    
    # 마지막 이미지 파일 넣는 곳
    try:
        st.image("final_photo.jpg", use_container_width=True)
    except:
        st.info("💡 GitHub 저장소에 'final_photo.jpg' 파일이 없으면 안내 문구가 표시됩니다.")
        
    st.write("")
    if st.button("처음부터 다시 하기 🔄", use_container_width=True):
        st.session_state.step = 1
        st.rerun()
