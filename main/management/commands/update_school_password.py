from django.core.management.base import BaseCommand
import openpyxl
from main.models import School

class Command(BaseCommand):
    help = '학교 비밀번호를 엑셀 파일을 통해 업데이트합니다.'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help="D:\Daeun\eduWeb\surveySite\main\surveydata\data.xlsx")

    def handle(self, *args, **kwargs):
        excel_file = kwargs['excel_file']
        wb = openpyxl.load_workbook(excel_file)
        ws = wb.active

        for row in ws.iter_rows(min_row=2, values_only=True):
            school_id = row[7]  # 아이디가 8번째 열에 있다고 가정
            password = row[8]   # 비밀번호가 9번째 열에 있다고 가정
            try:
                school = School.objects.get(school_id=school_id)
                school.school_pw = password
                school.save()
                self.stdout.write(self.style.SUCCESS(f'{school_id}의 비밀번호가 성공적으로 업데이트되었습니다.'))
            except School.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'{school_id}에 해당하는 학교를 찾을 수 없습니다.'))
