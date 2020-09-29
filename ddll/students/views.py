from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from students.models import StudentInfo, MoneyInfo, StudentClassInfo, ClassDetailInfo, UserInfo


def index(request):
    return render(request, 'students/index.html')


def login(request):
    u_name = request.COOKIES.get("u_name", '')
    context = {'u_name':u_name, 'error_name':0, 'error_pwd':0}
    return render(request, 'students/login.html',context)


def login_handle(request):
    u_name = request.POST.get('username')
    u_pwd = request.POST.get('pwd')
    jizhu = request.POST.get('jizhu',0)
    user = UserInfo.objects.filter(u_name = u_name)
    print(u_name)
    if len(user)==1:
        print('用户名验证成功！')
        if user[0].u_pwd == u_pwd:
            red = HttpResponseRedirect('/students/student_into/')
            if jizhu != 0:
                red.set_cookie('u_name', u_name)
            else:
                red.set_cookie('u_name', '', max_age=-1)
            request.session['u_id'] = user[0].u_id
            request.session['u_name'] = user[0].u_name
            return red
        else:
            context ={'u_name':u_name,'error_name':0,'error_pwd':1}
            return render(request,'students/login.html',context)
    else:
        context = {'u_name':u_name,'error_name':1,'error_pwd':0}
        return render(request, 'students/login.html', context)
def student_into(request):
    return render(request, 'students/student_into.html')


def student_list(request):
    student_info = StudentInfo.objects.all()
    query_type = 0
    num_dic = {}
    for i in student_info:
        s_id = i.id
        # sid = int(float(sid))
        over_course_num = MoneyInfo.objects.filter(m_id_id=s_id)
        # over_course_num = MoneyInfo.objects.filter(m_id_id=s_id)
        use_course_num = ClassDetailInfo.objects.filter(s_id_id=s_id).count()
        num = 0
        for m_info in over_course_num:
            num += m_info.m_regular_time
            num1 = num - use_course_num
            num_dic[i.s_id] = num1

    # context = {"student_info": student_info}
    # return render(request, "students/student_list.html", context)

    context = {"student_info": student_info, "over_num": num_dic, "query_type": query_type}
    return render(request, "students/student_list.html", context)


def student_list_handle(request):
    q_method = request.GET.get("query_method")
    query_info = request.GET.get("query_info")
    query_type = 1
    num_dic = {}
    if q_method == "1":
        student_info = StudentInfo.objects.filter(s_id__contains=query_info)
        for i in student_info:
            s_id = i.id
            over_course_num = MoneyInfo.objects.filter(m_id_id=s_id)
            use_course_num = ClassDetailInfo.objects.filter(s_id_id=s_id).count()
            num = 0
            for m_info in over_course_num:
                num += m_info.m_regular_time
                num1 = num - use_course_num
                num_dic[i.s_id] = num1

    elif q_method == "2":
        student_info = StudentInfo.objects.filter(s_name__contains=query_info)
        for i in student_info:
            s_id = i.id
            over_course_num = MoneyInfo.objects.filter(m_id_id=s_id)
            use_course_num = ClassDetailInfo.objects.filter(s_id_id=s_id).count()
            num = 0
            for m_info in over_course_num:
                num += m_info.m_regular_time
                num1 = num - use_course_num
                num_dic[i.s_id] = num1

    elif q_method == "3":
        student_info = StudentInfo.objects.filter(s_into__contains=query_info)
        for i in student_info:
            s_id = i.id
            over_course_num = MoneyInfo.objects.filter(m_id_id=s_id)
            use_course_num = ClassDetailInfo.objects.filter(s_id_id=s_id).count()
            num = 0
            for m_info in over_course_num:
                num += m_info.m_regular_time
                num1 = num - use_course_num
                num_dic[i.s_id] = num1
    else:
        return HttpResponse("没有找到！")

    context = {"student_info": student_info, "over_num": num_dic, "query_type": query_type}
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
    context = {'s_id': s_id,'s_name': s_name, 's_gender': s_gender, 's_into': s_into, 's_phone': s_phone, 's_status': s_status, 's_note':s_note}
    # return render(request, 'students/student_show.html',context)
    return HttpResponse("新增成功！<a href= 'http://localhost:8002/students/student_show/'>查询</a>")


def student_view(request):
    return render(request, 'students/student_view.html')


def student_view_handle(request):
    s_id = request.GET.get('s_id')
    id = request.GET.get('id')
    # if s_id == "":
    #     return HttpResponse('您查找的内容不存在！')
    # 查找学生信息表中对应学生的信息
    s_info = StudentInfo.objects.get(id=id)
    # 查找财务表中对应学生的所有信息
    s_money = MoneyInfo.objects.filter(m_id_id=id)

    s_class_detail = ClassDetailInfo.objects.filter(s_id_id=id)

    cl_info = []
    sk_info = []
    for s in s_class_detail:
        kc_id = s.c_id_id
        s_class = StudentClassInfo.objects.filter(id=kc_id)
        sk_info.append(s_class)
        cl_info.append(s)
        # test.append(kc_id)

    context = {'s_info': s_info, 's_money': s_money, 'classinfo': sk_info, 'classdetail': cl_info}
    # context = {'test': test, 'test1': test1, 's_info': s_info, 's_money': s_money, 'classinfo': sk_info, 'classdetail': cl_info}
    return render(request, 'students/student_view.html', context)


def student_add(request):
    return render(request,"students/student_add.html")


def student_alter(request):
    return render(request, 'students/student_alter.html')


def student_add_handle(request):
    s_name = request.POST.get('s_name')
    s_gender = request.POST.get('s_gender')
    s_phone = request.POST.get('s_phone')
    s_birthday = request.POST.get('s_birthday')
    s_into = request.POST.get('s_into')
    s_note = request.POST.get('s_note')
    student = StudentInfo()
    student1 = StudentInfo.objects.create(s_name, s_gender, s_phone, s_birthday, s_into, s_note)

    m_money = request.POST.get('m_money')
    m_pay_date = request.POST.get('m_pay_date')
    m_usually = request.POST.get('m_usually')
    m_special = request.POST.get('m_special')
    m_discount = request.POST.get('m_discount')
    m_note = request.POST.get('m_note')
    if m_money != "" and m_pay_date != "" and m_usually != "":
        s_info = StudentInfo.objects.get(s_id=student1)
        MoneyInfo.objects.create(s_info.id, m_money, m_pay_date, m_usually, m_special, m_discount, m_note)

    context = {'s_name': s_name, "s_gender": s_gender, "s_phone": s_phone, "s_birthday": s_birthday, "s_into":s_into, "s_note":s_note}
    return render(request,'students/student_add.html', context)

    context = {'s_name':s_name,"s_gender":s_gender,"s_phone":s_phone,"s_birthday":s_birthday,"s_into":s_into,"s_note":s_note}
    return render(request,'students/student_add.html', context)


def student_info_alter(request):
    if request.method == 'POST':
        post = request.POST
        s_id = post.get('s_id')
        print(s_id)
        s_info = StudentInfo.objects.get(s_id=s_id)
        # s_info = StudentInfo.objects.get(s_id='DDLL0001')
        s_info.s_name = post.get('s_name')
        s_info.s_gender = post.get('s_gender')
        s_info.s_birthday = post.get("s_birthday")
        s_info.s_phone = post.get("s_phone")
        s_info.s_status = post.get("s_status")
        s_info.s_into = post.get("s_into")
        s_info.s_note = post.get("s_note")
        s_info.save()
        print('学生基本信息保存成功！')
        print('开始保存收入信息！')
        # m_info = MoneyInfo.objects.filter(m_id=s_info.id)
        # for minfo in m_info:
        #     minfo.m_money =
        return HttpResponse('保存成功！')
    else:
        request_info = request.GET
        s_id = request_info.get('s_id')
        s_info = StudentInfo.objects.get(s_id=s_id)
        id = s_info.id
        s_name = s_info.s_name
        s_gender = s_info.s_gender
        if s_gender:
            s_gender = '男'
        else:
            s_gender = "女"
        s_birthday = s_info.s_birthday
        s_phone = s_info.s_phone
        s_status = s_info.s_status
        s_into = s_info.s_into
        s_note = s_info.s_note
        # 接下来是获取该对象所有的缴费记录
        m_info = MoneyInfo.objects.filter(m_id_id=id)
        context = {'s_name': s_name, 's_id':s_id, 's_gender': s_gender,
                   's_birthday': s_birthday, 's_phone': s_phone,
                   's_status': s_status, 's_into': s_into, 's_note': s_note,
                   'm_info': m_info,
                   }
        return render(request, 'students/student_info_alter.html/', context)

