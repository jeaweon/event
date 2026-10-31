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

# [1단계] 인사 화면
if st.session_state.step == 1:
    st.title("👋 Xin chào!")
    st.write("Đây là một trang web sự kiện nho nhỏ tôi chuẩn bị dành cho bạn. Bạn có muốn bấm thử vào nút bên dưới không?")
    
    st.write("") # 여백
    
    if st.button("Bấm vào đây ➡️", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# [2단계] 질문 및 2가지 선택지 화면
elif st.session_state.step == 2:
    st.title("1283 câu hỏi đơn giản")
    st.subheader("Hôm nay ngày của bạn thế nào?")
    
    st.write("") # 여백
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🍕 피자 먹으러 가기", use_container_width=True):
            st.session_state.choice = "피자"
            st.session_state.step = 3
            st.rerun()
            
    with col2:
        if st.button("🍣 초밥 먹으러 가기", use_container_width=True):
            st.session_state.choice = "초밥"
            st.session_state.step = 3
            st.rerun()

# [3단계] 선택 결과 및 이벤트 마무리
elif st.session_state.step == 3:
    st.balloons() # 축하 폭죽 효과
    st.title("🎉 탁월한 선택이야!")
    st.success(f"좋아! 오늘은 **{st.session_state.get('choice')}**(으)로 결정됐어!")
    
    st.write("너랑 같이 먹으러 갈 생각에 벌써 설렌다 😆")
    
    st.write("")
    if st.button("다시 하기 🔄"):
        st.session_state.step = 1
        st.rerun()
