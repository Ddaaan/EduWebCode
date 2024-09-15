function validateForm() {
    // 문항 개수 확인
    const questionCount = 21;
    let allAnswered = true;

    //각 질문에 응답 확인
    for (let i = 1; i <= questionCount; i++) {
        const options = document.getElementsByName('question${i}');
        let answered = false;

        //옵션이 체크된지 확인
        for (let option of options) {
            if (option.checked) {
                answered = true;
                break;
            }
        }
        
        // 응답안된 질문 있으면 false
        if (!answered) {
            allAnswered = false;
            break;
        }           
    }

    // 문항에 답변하지 않았으면 경고창 (false일 때)
    if (!allAnswered) {
        alert('모든 문항에 답해주세요');
        return false;
    }

    return true;
    
}