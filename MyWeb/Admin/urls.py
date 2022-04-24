from django.urls import path
from . import views

urlpatterns = [
    # todo 管理员
    # 添加超级管理员
    path('superuser/create/', views.SuperUser_create.as_view()),
    # 修改超级管理员信息
    path('superuser/edit/<str:user_id>', views.SuperUser_edit.as_view()),
    # 条件查询超级管理员用户
    path('superuser/search/', views.SuperUser_search.as_view()),

    # todo 学生
    # 添加学生信息
    path('student/create/', views.Student_create.as_view()),
    # 修改学生信息
    path('student/edit/<str:student_id>', views.Student_edit.as_view()),
    # 条件搜索学生信息
    path('student/search/', views.Student_search.as_view()),

    # todo 教师
    # 添加教师信息
    path('teacher/create/', views.Teacher_create.as_view()),
    # 修改教师信息
    path('teacher/edit/<str:teacher_id>', views.Teacher_edit.as_view()),
    # 条件搜索教师信息
    path('teacher/search/', views.Teacher_search.as_view()),

    # todo 院系列表
    # 添加院系信息
    path('college/create/', views.College_create.as_view()),
    # 修改院系信息
    path('college/edit/<str:college_id>', views.College_edit.as_view()),
    # 条件搜索院系信息
    path('college/search/', views.College_search.as_view()),

    # todo 课程列表
    # 添加课程信息
    path('course/create/', views.Course_create.as_view()),
    # 修改课程信息
    path('course/edit/<str:course_id>', views.Course_edit.as_view()),
    # 条件搜索课程信息
    path('course/search/', views.Course_search.as_view()),

    # todo 开课列表
    # 添加开课列表
    path('open/create/', views.Open_create.as_view()),
    # 修改开课列表
    path('open/edit/<str:open_id>', views.Open_edit.as_view()),
    # 修改时搜索开课列表
    path('open/search/', views.Open_search.as_view()),
    # 条件搜索开课列表
    path('open/search_detail/', views.Open_search_detail.as_view()),

    # 添加选课
    path('score/create/', views.Score_create.as_view()),
    # 暂时不用
    path('score/search/', views.Score_search.as_view()),
    # 选课管理-查询选课
    path('score/search_detail/', views.Score_search_detail.as_view()),
    # 选课管理-删除学生选课
    path('score/delete/', views.Score_delete.as_view()),
    # 成绩管理-编辑学生成绩信息
    path('score/edit/', views.Score_edit.as_view()),

    # 成绩分析
    path('score/analysis/<str:semester>', views.Score_Analysis.as_view()),
]
