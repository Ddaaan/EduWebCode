function drawCharts(average_response, average_section_response, average_total_response) {
    // 첫 번째 그래프 (문항별 평균 점수)
    var labels = Array.from({length: average_response.length}, (v, k) => "문항 "+ (k+1));
    var ctx = document.getElementById('student_question_canvas').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: '문항별 평균 점수',
                data: average_response,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 5
                }
            }
        }
    });

    // 두 번째 그래프 (영역별 평균 점수)
    var sectionLabels = ["학교문화", "학교구조", "민주시민교육"];
    var ctx2 = document.getElementById('student_section_canvas').getContext('2d');
    new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: sectionLabels,
            datasets: [{
                label: '영역별 평균 점수',
                data: average_section_response,
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 5
                }
            }
        }
    });

    // 세 번째 그래프 (총 평균 점수)
    var totalLabels = ["총 평균 점수"];
    var ctx3 = document.getElementById('student_total_canvas').getContext('2d');
    new Chart(ctx3, {
        type: 'bar',
        data: {
            labels: totalLabels,
            datasets: [{
                label: '총 평균 점수',
                data: average_total_response,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 5
                }
            }
        }
    });
}