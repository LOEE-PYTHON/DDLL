from django.shortcuts import render, HttpResponse
from students.models import StudentInfo, MoneyInfo, StudentClassInfo, ClassDetailInfo


def index(request):
    return render(request, 'students/index.html')


def login(request):
    return render(request, 'students/login.html')


def student_into(request):
    return render(request, 'students/student_into.html')


def student_list(request):
    student_info = StudentInfo.objects.all()
    context = {"student_info": student_info}
    return render(request, "students/student_list.html", context)


def student_list_handle(request):
    q_method = request.GET.get("query_method")
    query_info = request.GET.get("query_info")
    if q_method == "1":
        student_info = StudentInfo.objects.filter(s_id=query_info)
    elif q_method == "2":
        student_info = StudentInfo.objects.filter(s_name=query_info)
    elif q_method == "3":
        student_info = StudentInfo.objects.filter(s_into=query_info)
    else:
        return HttpResponse("没有找到！")
    context = {"student_info": student_info}
    return render(request, "students/student_list.html", context)


def student_handle(request):
    s_id = request.POST.get('s_id')
    s_name = request.POST.get('s_name')
    s_gender = request.POST.get('s_gender')
    s_gender = int(s_gender)
    if s_gender == 0:
        s_gender = '女'
    else:
        s_gender = '男'
    s_into = request.POST.get('s_into')
    s_phone = request.POST.get('s_phone')
    s_status = request.POST.get('s_status')
    if s_status:
        s_status = "在读"
    else:
        s_status = '停课'
    s_note = request.POST.get('s_note')
    context = {'s_id': s_id,'s_name': s_name, 's_gender': s_gender, 's_into': s_into, 's_phone': s_phone, 's_status':s_status, 's_note':s_note}
    # return render(request, 'students/student_show.html',context)
    return HttpResponse("新增成功！<a href= 'http://localhost:8002/students/student_show/'>查询</a>")


def student_view(request):
    return render(request, 'students/student_view.html')


def student_view_handle(request):
    s_id = request.GET.get('s_id')
    id = request.GET.get('id')
    if s_id == "":
        return HttpResponse('您查找的内容不存在！')
    s_info = StudentInfo.objects.get(s_id=s_id)
    s_money = MoneyInfo.objects.filter(m_id_id=id)
    s_class_detail = ClassDetailInfo.objects.get(s_id_id=id)
    kc_id = s_class_detail.kcls_id_id
    test = type(s_class_detail)
    s_class = StudentClassInfo.objects.get(id = kc_id)

    context = {'s_info': s_info, 's_money': s_money, 'classinfo': s_class, 'classdetail': s_class_detail}
    # context = {'test': s_class, 's_info': s_info, 's_money': s_money, 'classinfo': s_class, 'classdetail': s_class_detail}
    return render(request, 'students/student_view.html', context)


def student_alter(request):
    return render(request, 'students/student_alter.html')

