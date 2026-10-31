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
    st.title("❓ Q1. Hôm nay ngày của bạn thế nào?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Thích! 😊", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("Bình thường... ", use_container_width=True):
            st.session_state.step = 3
            st.rerun()

# [3단계] 두 번째 질문
elif st.session_state.step == 3:
    st.title("❓ Q2. Thích cái nào hơn?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Bánh cá 🐟", use_container_width=True):
            st.session_state.step = "retry_q2"
            st.rerun()
    with col2:
        if st.button("재원 ", use_container_width=True):
            st.session_state.step = 4
            st.rerun()

# [3-1단계] 붕어빵 선택 시 나오는 화면
elif st.session_state.step == "retry_q2":
    st.error("😤 Thất vọng quá, làm lại đi!")
    st.write("")
    if st.button("Quay lại câu hỏi thứ hai 🔄", use_container_width=True):
        st.session_state.step = 3
        st.rerun()

# [4단계] 세 번째 질문
elif st.session_state.step == 4:
    st.title("❓ Q3. Nói thật thì ấn tượng đầu tiên của tôi trong mắt bạn được mấy điểm?")
    
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
    st.title("❓ Q4. Bạn thích đâu?")
    
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
    st.success("✨ Xin chúc mừng! ✨")
    
    st.subheader("Ấn tượng đầu tiên tốt, lại còn thích hơn cả bánh cá nữa, nên người đặc biệt như em sẽ hẹn hò với anh đấy. 🥰")
    
    # 마지막 이미지 파일 넣는 곳
    try:
        st.image("final_photo.jpg", use_container_width=True)
    except:
        st.info("💡 GitHub 저장소에 'final_photo.jpg' 파일이 없으면 안내 문구가 표시됩니다.")
        
    st.write("")
    if st.button("처음부터 다시 하기 🔄", use_container_width=True):
        st.session_state.step = 1
        st.rerun()
