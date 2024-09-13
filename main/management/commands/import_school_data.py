import pandas as pd
from django.core.management.base import BaseCommand
from main.models import School  # School 모델이 정의된 파일 경로에 맞춰 수정

class Command(BaseCommand):
    help = '엑셀 파일에서 학교 데이터를 불러와 School 모델에 저장'

    def add_arguments(self, parser):
        # 명령어 인자로 엑셀 파일 경로를 받음
        parser.add_argument('excel_file', type=str, help='불러올 엑셀 파일 경로')

    def handle(self, *args, **kwargs):
        # 명령어 인자로부터 엑셀 파일 경로 받기
        excel_file = kwargs['excel_file']

        # 엑셀 파일에서 1399번째 줄부터 데이터를 읽음 (index는 0부터 시작하므로 1398을 사용)
        df = pd.read_excel(excel_file)

        # 열 이름 정리 (공백 제거)
        df.columns = df.columns.str.strip()

        # 각 열에 해당하는 데이터를 School 모델에 저장
        for index, row in df.iterrows():
            # 데이터가 이미 존재하는지 확인 후 추가
            if not School.objects.filter(school_id=row['아이디']).exists():
                School.objects.create(
                    education_office=row['시도교육청'],
                    school_level=row['학교급'],
                    establishment_type=row['설립구분'],
                    school_name=row['학교명'],
                    district=row['자치구'],
                    postal_code=row['우편번호'],
                    address=row['주소'],
                    school_id=row['아이디'],
                    school_pw=row['비밀번호']
                )

        self.stdout.write(self.style.SUCCESS('학교 데이터를 성공적으로 추가 저장했습니다.'))
