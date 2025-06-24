import streamlit as st

# Streamlit 페이지 설정
st.set_page_config(page_title="MBTI 퀴즈 & 직업 추천", page_icon="🎯")

# MBTI 및 직업 데이터
mbti_jobs = {
    'ISTJ': {'desc': '✔️ 신중하고 책임감이 강한 현실주의자', 'jobs': [
        {'name': '🧮 회계사', 'detail': '숫자와 데이터 분석에 강하며, 체계적인 업무를 선호합니다.', 'image': 'https://cdn-icons-png.flaticon.com/512/2920/2920065.png'}
    ]},
    'ENFP': {'desc': '✨ 열정적이고 창의적인 아이디어 뱅크', 'jobs': [
        {'name': '🎨 광고 기획자', 'detail': '자유롭게 아이디어를 내며 사람들과 협업하는 것을 즐깁니다.', 'image': 'https://cdn-icons-png.flaticon.com/512/3135/3135715.png'}
    ]},
    'INFJ': {'desc': '🌟 깊은 통찰력을 가진 조언자', 'jobs': [
        {'name': '🗣️ 상담사', 'detail': '타인의 고민을 들어주고 깊이 있는 해결책을 제시하는 것을 좋아합니다.', 'image': 'https://cdn-icons-png.flaticon.com/512/2922/2922522.png'}
    ]},
    'ESTP': {'desc': '🔥 도전적이고 에너지가 넘치는 활동가', 'jobs': [
        {'name': '⚽ 운동선수', 'detail': '움직이고 경쟁하며 즉각적인 결과를 얻는 환경을 선호합니다.', 'image': 'https://cdn-icons-png.flaticon.com/512/2972/2972219.png'}
    ]}
}

# MBTI 퀴즈 질문
questions = [
    {"question": "Q1. 새로운 사람을 만날 때 나는?", "options": ["에너지가 생긴다", "조금 부담스럽다"], "dimension": "E/I"},
    {"question": "Q2. 주로 정보를 처리할 때 나는?", "options": ["현재 사실을 중시한다", "미래 가능성을 본다"], "dimension": "S/N"},
    {"question": "Q3. 결정을 내릴 때 나는?", "options": ["논리적으로 생각한다", "사람의 감정을 고려한다"], "dimension": "T/F"},
    {"question": "Q4. 일하는 스타일은?", "options": ["계획을 세워 착착 진행한다", "즉흥적으로 유연하게 한다"], "dimension": "J/P"}
]

# --- 상태 저장 ---
if 'answers' not in st.session_state:
    st.session_state.answers = []

# --- 타이틀 ---
st.title("🎯 나의 MBTI 찾기 & 직업 추천")

# --- 퀴즈 진행 ---
current_q = len(st.session_state.answers)

if current_q < len(questions):
    q = questions[current_q]
    st.subheader(q["question"])
    choice = st.radio("선택하세요:", q["options"])

    if st.button("다음"):
        st.session_state.answers.append(choice)
        st.experimental_rerun()
else:
    # MBTI 결과 계산
    mbti_result = ""

    # E/I
    mbti_result += 'E' if st.session_state.answers[0] == "에너지가 생긴다" else 'I'
    # S/N
    mbti_result += 'S' if st.session_state.answers[1] == "현재 사실을 중시한다" else 'N'
    # T/F
    mbti_result += 'T' if st.session_state.answers[2] == "논리적으로 생각한다" else 'F'
    # J/P
    mbti_result += 'J' if st.session_state.answers[3] == "계획을 세워 착착 진행한다" else 'P'

    # MBTI 중 준비된 결과만 추출 (없으면 기본 ENFP 제공)
    if mbti_result not in mbti_jobs:
        mbti_result = 'ENFP'

    st.success(f"🎉 당신의 MBTI는 **{mbti_result}** 입니다!")
    st.subheader(f"✅ {mbti_jobs[mbti_result]['desc']}")

    # 직업 추천 출력
    st.subheader("💼 추천 직업")
    for job in mbti_jobs[mbti_result]['jobs']:
        st.write(f"### {job['name']}")
        st.image(job['image'], width=200)
        st.write(f"📌 {job['detail']}")
        st.markdown("---")

    # 풍선 효과
    st.balloons()

    # 다시 하기 버튼
    if st.button("🔄 다시 하기"):
        st.session_state.answers = []
        st.experimental_rerun()
