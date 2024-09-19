function validateForm() {
    // 모든 질문을 가져옴
    const questions = document.querySelectorAll('.question');
    let allAnswered = true;

    // 각 질문에 대한 응답 확인
    questions.forEach((question) => {
        const options = question.querySelectorAll('input[type="radio"]');
        let answered = false;

        // 각 질문의 옵션들 중에서 체크된 것이 있는지 확인
        options.forEach((option) => {
            if (option.checked) {
                answered = true;
            }
        });

        // 응답되지 않은 질문이 있으면 경고 처리
        if (!answered) {
            allAnswered = false;
            question.querySelector('h4').style.color = "red"; // 응답하지 않은 질문의 제목을 빨간색으로 표시
        } else {
            question.querySelector('h4').style.color = ""; // 응답된 질문은 원래 색상으로
        }
    });

    // 문항에 답변하지 않았으면 경고창 표시
    if (!allAnswered) {
        alert('모든 문항에 답해주세요');
        return false;
    }

    return true; // 모든 질문에 응답했으면 폼 제출 허용
}
