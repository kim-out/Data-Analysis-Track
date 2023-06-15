from django.urls import path

from . import views

app_name = 'board' # 네임스페이스 설정

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), # name으로 url별칭 지정
    # /(숫자)/ 페이지 요청 시 question_id에 int로 숫자를 저장하고 views.detail 함수 실행
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete')
]