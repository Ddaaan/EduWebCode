from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render
from main.models import School

# Create your views here.
def main_index(request):
    return render(request, "mainpage.html")

def post(request):
    return render(request, 'post.html')

def about1(request):
    return render(request, 'about1.html')

def about2(request):
    return render(request, 'about2.html')

def file(request):
    return render(request, 'file.html')

def admin(request):
    return render(request, 'admin.html')


# 지역명 선택
def info_page(request):
    role = request.GET.get('role', 'default')
    regions = School.objects.values_list('district', flat=True).distinct().order_by('district')

    role_messages = {
        'student' : '학생 정보를 선택하세요',
        'parent' : '학부모 정보를 선택하세요',
        'teacher' : '교원 정보를 선택하세요'
    }
    message = role_messages.get(role, '본인 정보를 선택하세요')
    
    if request.method == "POST":
        region = request.POST.get('region')
        school_level = request.POST.get('school-level')
        school_name = request.POST.get('school-name')
        school_id = request.POST.get('school-id')
        
        try:
            school = School.objects.get(district = region, school_level=school_level, school_name=school_name, school_id=school_id)
            
            if school is None:
                messages.error(request, "입력한 정보와 일치하는 학교가 없습니다.")
                return render(request, 'infopage.html', {'regions': regions, 'message': message})

            # 학교 정보가 일치하면 role에 따라 페이지 리디렉션
            if role == 'student':
                if school_level in ['초등학교', '각종학교(초)']:
                    return redirect('ele-student-s')
                elif school_level in ['중학교', '고등학교', '각종학교(중)', '각종학교(고)']:
                    return redirect('midhigh-student-s')
            elif role == 'parent':
                if school_level == '유치원':
                    return redirect('kinder-parents-s')
                elif school_level in ['초등학교', '중학교', '고등학교', '각종학교(초)', '각종학교(중)', '각종학교(고)']:
                    return redirect('school-parents-s')
            elif role == 'teacher':
                if school_level == '유치원':
                    return redirect('kinder-teacher-s')
                elif school_level in ['초등학교', '중학교', '고등학교', '각종학교(초)', '각종학교(중)', '각종학교(고)']:
                    return redirect('school-teacher-s')
            else:
                messages.error(request, "유효하지 않은 접근입니다.")
        except School.DoesNotExist:
            messages.error(request, "입력한 정보와 일치하는 학교가 없습니다.")
            return render(request, 'infopage.html', {'regions': regions, 'message': message})

    return render(request, 'infopage.html', {'regions': regions, 'message': message})

# 학교명 정렬
def get_school_names(request):
    region = request.GET.get('region')
    school_level = request.GET.get('school_level')
    
    schools = School.objects.filter(district=region, school_level=school_level).values('school_name')
    school_list = list(schools)
        
    return JsonResponse({'schools' : school_list})


# 로그인 화면 
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})






########################################### 설문 질문 리스트 ####################################################
#초등학생용 설문
def ele_stuSur_question(request):
    questions = [
        {'id' : 1, 'text': '우리 학교 학생들은 학급 규칙과 약속을 잘 지키는 편이다.'},
        {'id' : 2, 'text': '나는 내 생각과 느낌을 친구나 선생님에게 잘 표현하고 친구나 선생님의 생각과 느낌도 잘 이해하려고 노력한다.'},
        {'id' : 3, 'text': '우리 학교 학생들은 친구 또는 학급 일에 서로 도와준다.'},
        {'id' : 4, 'text': '우리 학교 학생들은 의사소통을 위한 바른 언어습관과 태도를 가지고 있다.'},
        {'id' : 5, 'text': '우리 학교 학생들은 서로 다투더라도 대화와 양보를 통해 해결한다.'},
        {'id' : 6, 'text': '우리 학교 학생들은 친구를 따돌리거나 괴롭히지 않는다.'},
        {'id' : 7, 'text': '우리 학교 학생들은 선생님을 존중한다.'},
        {'id' : 8, 'text': '(자기평가) 나는 친구들을 존중하며 친구들의 마음을 아프게 하는 말이나 행동을 하지 않는다.'},
        {'id' : 9, 'text': '우리 학교는 학생회와 동아리가 잘 될 수 있도록 지원한다.'},
        {'id' : 10, 'text': '나는 학교에서 내가 할 일과 책임져야 할 일을 잘 알고 있다.'},
        {'id' : 11, 'text': '우리 학교 선생님들은 학생들의 의견을 잘 들어주며 존중한다.'},
        {'id' : 12, 'text': '우리 학교는 학생들의 의견을 모을 수 있는 회의가 잘 운영된다.'},
        {'id' : 13, 'text': '우리 학교는 친구들끼리 갈등이 발생했을 때 대화와 타협을 통해 해결한다.'},
        {'id' : 14, 'text': '(자기 평가) 나는 학교활동(학급회, 학생회, 동아리활동, 학교 행사 등)에 적극적으로 참여한다.'},
        {'id' : 15, 'text': '우리 학교는 교육활동을 통해 민주시민교육을 실시한다. *민주주의, 평화통일, 인권(노동), 생태환경, 양성평등 등'},
        {'id' : 16, 'text': '우리 학교는 수업과 그 밖의 시간에 소통과 협력하며 공부할 기회가 많다.'},
        {'id' : 17, 'text': '우리 학교는 민주시민교육을 실천하고 경험할 수 있도록 학급회, 학생회 활동 등 다양한 교내외 참여 활동을 할 수 있도록 지원한다.'},
        {'id' : 18, 'text': '우리 학교는 학교폭력이나 학생인권 보호 및 학교민주주의에 대한 설문 조사 등이 적절하게 이루어진다.'},
        {'id' : 19, 'text': '우리 학교는 가정통신문이나 학교 홈페이지 등을 통해 다양한 교육활동 소식을 알려준다.'},
        {'id' : 20, 'text': '우리 학교 학생들은 학교와 사회에서 일어나는 문제에 관심을 가지고 해결하기 위해 노력한다.'},
        {'id' : 21, 'text': '(자기 평가) 나는 수업시간이나 학교 활동 중에 토의․토론, 체험활동, 행사 활동 등에 적극적으로 참여한다.'}
    ]
    options = range(1, 6)
    return render(request, 'survey_ele_student.html', {'questions' : questions, 'options' : options})

#중고등학생용 설문
def midHigh_stuSur_question(request):
    questions = [
        {'id' : 1, 'text': '우리 학교는 규칙이나 약속을 정할 때 학생들의 의견이나 생각을 반영한다.'},
        {'id' : 2, 'text': '우리 학교는 학급규칙이나 학교 규칙 등을 민주적인 절차에 따라 바꿀 수 있다.'},
        {'id' : 3, 'text': '나는 다른 사람들과 잘 어울리며 친구나 선생님의 생각도 잘 헤아린다.'},
        {'id' : 4, 'text': '우리 학교 학생들은 의사소통을 위한 바른 언어습관과 태도를 가지고 있다.'},
        {'id' : 5, 'text': '우리 학교 학생들은 대화와 타협을 통해 문제 상황을 해결한다.'},
        {'id' : 6, 'text': '우리 학교 학생들은 모든 형태의 폭력과 차별을 없애기 위해 노력한다.'},
        {'id' : 7, 'text': '우리 학교 학생들은 선생님을 존중한다.'},
        {'id' : 8, 'text': '(자기평가) 나는 따돌리거나 괴롭히는 행동으로 친구의 인권을 침해하지 않는다.'},
        {'id' : 9, 'text': '우리 학교는 학생회와 동아리를 만들고 활동할 수 있도록 시간과 공간 확보 등의 도움을 제공한다.'},
        {'id' : 10, 'text': '나는 학교에서 내가 할 일과 책임져야 할 일을 잘 알고 있다.'},
        {'id' : 11, 'text': '우리 학교는 선생님들과 학생들이 결정한 내용을 존중한다.'},
        {'id' : 12, 'text': '우리는 학교 교육과정 운영에 대하여 스스로 참여하여 의견을 낼 수 있다.'},
        {'id' : 13, 'text': '우리 학교는 학생들의 의견을 모을 수 있는 회의가 필요할 때마다 열린다.'},
        {'id' : 14, 'text': '우리 학교는 학생들끼리 갈등상황이 발생했을 때 중재․조정․화해를 위해 노력한다.'},
        {'id' : 15, 'text': '(자기 평가) 나는 학교활동(학급회, 학생회, 동아리활동, 학교 행사 등)에 적극적으로 참여한다.'},
        {'id' : 16, 'text': '우리 학교는 교육활동을 통해 민주시민교육을 실시한다. *민주주의, 평화통일, 인권(노동), 생태환경, 양성평등 등'},
        {'id' : 17, 'text': '우리 학교는 수업 및 그 밖의 시간에 토의·토론, 프로젝트 학습, 논쟁형 수업, 협력학습 등을 할 기회가 많다.'},
        {'id' : 18, 'text': '우리 학교는 민주시민교육을 실천하고 경험할 수 있도록 학급회, 학생회 활동 등 다양한 교내외 참여 활동을 할 수 있도록 지원한다.'},
        {'id' : 19, 'text': '우리 학교는 학교폭력이나 학생인권 보호 및 학교민주주의에 대한 설문 조사 등이 적절하게 이루어진다.'},
        {'id' : 20, 'text': '우리 학교는 가정통신문이나 학교 홈페이지 등을 통해 다양한 교육활동 소식을 알려준다.'},
        {'id' : 21, 'text': '우리 학교 학생들은 학교와 사회에서 일어나는 문제에 관심을 가지고 해결하기 위해 노력한다.'},
        {'id' : 22, 'text': '(자기 평가) 나는 수업시간이나 학교 활동 중에 친구들과 협력하여 토의․토론, 체험활동, 캠페인, 행사 활동 등에 적극적으로 참여한다.'}
    ]

    options = range(1, 6)
    return render(request, 'survey_midHigh_student.html', {'questions' : questions, 'options' : options})


#유치원 학부모용 설문
def kinder_parSur_question(request):
    questions = [
        {'id' : 1, 'text': '우리 유치원은 교육 목표와 규칙을 결정할 때 학부모가 참여할 기회를 충분히 제공한다. *가정통신문, 설문조사, 협의회, 간담회, 홈페이지 등'},
        {'id' : 2, 'text': '우리 유치원의 교육 목표와 규칙은 유아를 존중한다.'},
        {'id' : 3, 'text': '우리 유치원은 학부모를 교육공동체의 주체로 생각한다.'},
        {'id' : 4, 'text': '우리 유치원은 학부모의 다양한 의견을 수렴한다.'},
        {'id' : 5, 'text': '우리 유치원의 구성원(유아, 교직원, 학부모)은 갈등문제를 대화와 타협을 통해 해결한다.'},
        {'id' : 6, 'text': '우리 유치원의 구성원은 모든 형태의 폭력과 차별을 없애기 위해 노력한다.'},
        {'id' : 7, 'text': '우리 유치원의 구성원은 사회적 소수자의 권리를 존중하기 위해 노력한다.'},
        {'id' : 8, 'text': '우리 유치원의 유아, 학부모들은 선생님을 존중한다.'},
        {'id' : 9, 'text': '우리 유치원은 구성원들 간에 상대방의 권리를 서로 존중한다.'},
        {'id' : 10, 'text': '(자기평가) 나는 우리 유치원의 구성원을 대할 때 존중하는 태도와 언어를 사용한다.'},
        {'id' : 11, 'text': '우리 유치원은 교육과정과 교육활동을 통해 유아들에게 민주시민교육을 실시한다. *민주주의, 평화통일, 인권(노동), 생태환경, 양성평등 등'},
        {'id' : 12, 'text': '우리 유치원은 학부모회에 행정적․재정적 지원을 하고 있다.'},
        {'id' : 13, 'text': '우리 유치원의 학부모로서의 권한과 책임에 대해 알고 있다.'},
        {'id' : 14, 'text': '우리 유치원은 학부모회의 대표를 민주적으로 선출하여 학부모의 의견을 수렴한다.'},
        {'id' : 15, 'text': '우리 유치원은 갈등해결을 위한 중재․조정․화해가 실질적으로 운영된다. '},
        {'id' : 16, 'text': '(자기평가) 나는 우리 유치원의 교육활동을 위한 의견수렴 과정(가정통신문, 설문조사, 간담회 등)에 적극 참여한다.'},
        {'id' : 17, 'text': '우리 유치원은 민주주의 가치들을 내면화할 수 있도록 교육과정과 수업 방법을 활용한다.'},
        {'id' : 18, 'text': '우리 유치원은 유아의 교육적 요구사항을 유치원 교육활동에 적극 반영한다.'},
        {'id' : 19, 'text': '우리 유치원은 민주시민교육을 실천하고 참여하는 경험할 수 있도록 다양한 교내외 활동을 운영한다.'},
        {'id' : 20, 'text': '우리 유치원은 놀이 활동을 통해 유아들의 의사 표현과 민주적 결정 등을 경험하게 하는 교육활동이 점차 많아지고 있다.'},
        {'id' : 21, 'text': '우리 유치원은 유아들이 지역사회에 관심을 갖도록 지원한다.'},
        {'id' : 22, 'text': '우리 유치원은 학부모에게 학교교육활동 정보 및 참여 기회를 제공한다.'},
        {'id' : 23, 'text': '(자기평가) 나는 우리 유치원의 교육적 변화와 발전을 위해 다양한 활동에 참여한다. *학부모회 활동, 동아리활동, 토론회 참여, 학부모 연수 참여, 지역사회 활동 등'}
    ]
    
    options = range(1, 6)
    return render(request, 'survey_kinder_parents.html', {'questions' : questions, 'options' : options})


#초중고 학부모용 설문
def school_parSur_question(request):
    questions = [
        {'id' : 1, 'text': '우리 학교는 교육 목표와 규칙을 결정할 때 학부모가 참여할 기회를 충분히 제공한다. *가정통신문, 설문조사, 협의회, 간담회, 홈페이지 등'},
        {'id' : 2, 'text': '우리 학교의 교육 목표와 규칙은 학생을 존중한다.'},
        {'id' : 3, 'text': '우리 학교는 학부모를 교육공동체의 주체로 생각한다.'},
        {'id' : 4, 'text': '우리 학교는 학부모의 다양한 의견을 수렴한다.'},
        {'id' : 5, 'text': '우리 학교의 구성원(학생, 교직원, 학부모)은 갈등문제를 대화와 타협을 통해 해결한다.'},
        {'id' : 6, 'text': '우리 학교의 구성원은 모든 형태의 폭력과 차별을 없애기 위해 노력한다.'},
        {'id' : 7, 'text': '우리 학교의 구성원은 사회적 소수자의 권리를 존중하기 위해 노력한다.'},
        {'id' : 8, 'text': '우리 학교의 학생, 학부모들은 선생님을 존중한다.'},
        {'id' : 9, 'text': '우리 학교는 구성원들 간에 상대방의 권리를 서로 존중한다.'},
        {'id' : 10, 'text': '(자기평가) 나는 우리 학교의 구성원을 대할 때 존중하는 태도와 언어를 사용한다.'},
        {'id' : 11, 'text': '우리 학교는 교육과정과 교육활동을 통해 학생들에게 민주시민교육을 실시한다. *민주주의, 평화통일, 인권(노동), 생태환경, 양성평등 등'},
        {'id' : 12, 'text': '우리 학교는 학부모회에 행정적․재정적 지원을 하고 있다.'},
        {'id' : 13, 'text': '우리 학교에 대한 학부모로서의 권한과 책임에 대해 알고 있다.'},
        {'id' : 14, 'text': '우리 학교는 학부모회의 대표를 민주적으로 선출하여 학부모의 의견을 수렴한다.'},
        {'id' : 15, 'text': '우리 학교는 갈등해결을 위한 중재․조정․화해가 실질적으로 운영된다. '},
        {'id' : 16, 'text': '(자기평가) 나는 우리 학교의 교육활동을 위한 의견수렴 과정(가정통신문, 설문조사, 간담회 등)에 적극 참여한다.'},
        {'id' : 17, 'text': '우리 학교는 민주주의 가치들을 내면화할 수 있도록 교육과정과 수업 방법을 활용한다. *교육과정 편성, 토의․토론, 프로젝트학습, 사회참여활동 등'},
        {'id' : 18, 'text': '우리 학교는 학생들의 의견이나 건의사항을 학교교육활동과 수업, 학급 운영 등에 적극 반영한다.'},
        {'id' : 19, 'text': '우리 학교는 민주시민교육을 실천(참여)하고 경험할 수 있도록 학생회 활동 등 다양한 교내외 활동을 실질적으로 보장하고 지원한다.'},
        {'id' : 20, 'text': '우리 학교는 학교폭력이나 학생인권 보호 및 학교민주주의에 대한 설문 조사 등이 적절하게 이루어진다.'},
        {'id' : 21, 'text': '우리 학교는 학생들이 지역의 다양한 사회참여활동을 할 수 있도록 지원한다.'},
        {'id' : 22, 'text': '우리 학교는 학부모에게 학교교육활동 정보 및 참여 기회를 제공한다.'},
        {'id' : 23, 'text': '(자기평가) 나는 우리 학교의 교육적 변화와 발전을 위해 다양한 활동에 참여하고 있다.*학부모회 활동, 동아리활동, 토론회 참여, 학부모 연수 참여, 지역사회 활동 등'}
    ]

    options = range(1, 6)
    return render(request, 'survey_school_parents.html', {'questions' : questions, 'options' : options})


#유치원 교직원용 설문
def kinder_teaSur_question(request):
    questions = [
        {'id' : 1, 'text': '우리 유치원은 유치원의 비전과 목표 등을 결정할 때 구성원(유아, 교직원, 학부모)의 생각과 의견을 충분하게 반영한다.'},
        {'id' : 2, 'text': '우리 유치원은 교육과정 운영계획을 수립할 때 구성원이 함께 소통하여 정한다.'},
        {'id' : 3, 'text': '우리 유치원은 교육과정 운영을 위해 안건과 토의가 있는 민주적 협의회를 운영한다.'},
        {'id' : 4, 'text': '우리 유치원 구성원은 서로 수평적인 관계를 유지하면서 협력한다.'},
        {'id' : 5, 'text': '우리 유치원 구성원은 민주적인 의사소통을 위한 언어습관과 태도를 가지고 있다.'},
        {'id' : 6, 'text': '우리 유치원 구성원은 모든 형태의 폭력과 차별을 없애기 위해 노력한다.'},
        {'id' : 7, 'text': '우리 유치원 구성원은 사회적 소수자의 권리를 존중하기 위해 노력한다.'},
        {'id' : 8, 'text': '우리 유치원 선생님들은 구성원들로부터 교권을 존중받고 있다.'},
        {'id' : 9, 'text': '우리 유치원의 주요 사안은 민주적인 과정을 통해 결정하고 그 내용은 특별한 사유가 없는 한 존중하고 실행한다.'},
        {'id' : 10, 'text': '(자기평가) 나는 유치원 구성원으로서 책임감을 갖고 의사결정 과정에 적극 참여한다.'},
        {'id' : 11, 'text': '우리 유치원 교직원은 민주적 가치를 중요시하고 절차를 준수하며 전문성 신장을 위해 노력한다.'},
        {'id' : 12, 'text': '우리 유치원은 구성원의 협의를 통해 예산을 편성하고 교육목적에 따라 집행한다.'},
        {'id' : 13, 'text': '우리 유치원은 학교 운영에 필요한 권한이 학교 구성원에게 적절하게 배분되어 민주적인 절차에 따라 발휘된다.'},
        {'id' : 14, 'text': '우리 유치원은 교직원들이 학교 의사결정 과정에 자유롭게 참여한다.'},
        {'id' : 15, 'text': '우리 유치원은 교직원의 업무에 대해 이해하며 협력적으로 지원한다.'},
        {'id' : 16, 'text': '우리 유치원은 갈등해결을 위한 중재․조정․화해가 실질적으로 운영된다.'},
        {'id' : 17, 'text': '(자기평가) 나는 우리 유치원 구성원의 권리를 존중하면서 민주적으로 업무를 처리한다.'},
        {'id' : 18, 'text': '우리 유치원은 교육과정과 연계한 교육활동을 통해 민주시민교육을 한다. *민주주의, 평화통일, 인권(노동), 생태환경, 양성평등 등'},
        {'id' : 19, 'text': '우리 유치원은 민주주의 가치에 관심을 가질 수 있도록 교육과정을 편성하고 토의․토론 등의 수업방법을 활용한다.'},
        {'id' : 20, 'text': '우리 유치원은 유아의 교육적 요구사항을 유치원 교육활동에 적극 반영한다.'},
        {'id' : 21, 'text': '우리 유치원은 유치원 운영에 대한 사안을 정할 때 학급별 또는 개별 의사를 존중하여 결정하는 경험을 준다.'},
        {'id' : 22, 'text': '우리 유치원은 놀이하는 동안 자유로운 의사 표현과 민주적 결정 등을 경험하게 하는 교육활동이 점차 많아지고 있다.'},
        {'id' : 23, 'text': '학부모가 유치원의 교육활동에 참여할 수 있도록 다양한 교육활동 소식을 알려준다.'},
        {'id' : 24, 'text': '우리 유치원 구성원은 학교와 사회․공동체 문제 해결을 위한 활동에 참여한다.'},
        {'id' : 25, 'text': '(자기평가) 나는 민주시민교육과 학교민주주의 실현을 위한 활동에 적극적으로 참여한다.'}
    ]

    options = range(1, 6)
    return render(request, 'survey_kinder_teacher.html', {'questions' : questions, 'options' : options})


#초중고 교직원용 설문
def school_teaSur_question(request):
    questions = [
        {'id' : 1, 'text': '우리 학교는 학교의 비전과 목표 등을 결정할 때 구성원(학생, 교직원, 학부모)의 생각과 의견을 충분하게 반영한다.'},
        {'id' : 2, 'text': '우리 학교는 교육과정 운영계획을 수립할 때 구성원이 함께 소통하여 정한다.'},
        {'id' : 3, 'text': '우리 학교는 교육과정 운영을 위해 안건과 토의가 있는 민주적 협의회를 운영한다.'},
        {'id' : 4, 'text': '우리 학교 구성원은 서로 수평적인 관계를 유지하면서 협력한다.'},
        {'id' : 5, 'text': '우리 학교 구성원은 민주적인 의사소통을 위한 언어습관과 태도를 가지고 있다.'},
        {'id' : 6, 'text': '우리 학교 구성원은 모든 형태의 폭력과 차별을 없애기 위해 노력한다.'},
        {'id' : 7, 'text': '우리 학교 구성원은 사회적 소수자의 권리를 존중하기 위해 노력한다.'},
        {'id' : 8, 'text': '우리 학교 선생님들은 구성원들로부터 교권을 존중받고 있다.'},
        {'id' : 9, 'text': '우리 학교의 주요 사안은 민주적인 과정을 통해 결정하고 그 내용은 특별한 사유가 없는 한 존중하고 실행한다.'},
        {'id' : 10, 'text': '(자기평가) 나는 학교 구성원으로서 책임감을 갖고 의사결정 과정에 적극 참여한다.'},
        {'id' : 11, 'text': '우리 학교 교직원은 민주적 가치를 중요시하고 절차를 준수하며 전문성 신장을 위해 노력한다.'},
        {'id' : 12, 'text': '우리 학교는 구성원의 협의를 통해 예산을 편성하고 교육목적에 따라 집행한다.'},
        {'id' : 13, 'text': '우리 학교는 학교 운영에 필요한 권한이 학교 구성원에게 적절하게 배분되어 민주적인 절차에 따라 발휘된다.'},
        {'id' : 14, 'text': '우리 학교는 교직원들이 학교 의사결정 과정에 자유롭게 참여한다.'},
        {'id' : 15, 'text': '우리 학교는 교직원의 업무에 대해 이해하며 협력적으로 지원한다.'},
        {'id' : 16, 'text': '우리 학교는 갈등해결을 위한 중재․조정․화해가 실질적으로 운영된다.'},
        {'id' : 17, 'text': '(자기평가) 나는 우리 학교 구성원의 권리를 존중하면서 민주적으로 업무를 처리한다.'},
        {'id' : 18, 'text': '우리 학교는 교육과정과 연계한 교육활동을 통해 민주시민교육을 한다. *민주주의, 평화통일, 인권(노동), 생태환경, 양성평등 등'},
        {'id' : 19, 'text': '우리 학교는 민주주의 가치를 내면화할 수 있도록 교육과정을 편성하고 다양한 수업방법(토의․토론, 프로젝트학습, 사회참여활동 등)을 활용한다.'},
        {'id' : 20, 'text': '우리 학교는 학생들의 교육적 요구 사항을 학교 교육활동에 적극 반영한다.'},
        {'id' : 21, 'text': '우리 학교는 민주시민교육을 실천하거나 경험할 수 있도록 학급회, 학생회 활동 등 다양한 교내외 활동을 실질적으로 보장하고 지원한다.'},
        {'id' : 22, 'text': '우리 학교는 학생들이 자율적이고 주도적인 교육활동이 이루어지고 있다.'},
        {'id' : 23, 'text': '우리 학교는 지역사회 유관기관과 연계하여 학생들이 다양한 프로그램에 참여할 수 있도록 지원한다.'},
        {'id' : 24, 'text': '우리 학교 구성원은 학교와 사회․공동체 문제를 해결하기 위한 활동에 참여한다.'},
        {'id' : 25, 'text': '(자기평가) 나는 민주시민교육과 학교민주주의 실현을 위한 활동에 적극적으로 참여한다.'}
    ]

    options = range(1, 6)
    return render(request, 'survey_school_teacher.html', {'questions' : questions, 'options' : options})


