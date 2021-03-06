from django.db import models
from django.db.models import Max
from django.contrib.auth.models import AbstractUser, UserManager as _UserManager

from django.db import models
import re


class UserInfo(models.Model):
    u_id = models.CharField(u'用户ID', max_length=10)
    u_name = models.CharField(u'用户名', max_length=10)
    u_pwd = models.CharField(u"密码", max_length=10)
    u_nickname = models.CharField(u'昵称', max_length=10)
    # 用户类型：1表示管理员，2表示普通老师：3表示财务人员
    u_type = models.IntegerField(u'用户类型', default='1')


    class Meta:
        verbose_name = u"用户表"
        verbose_name_plural = u"用户表"

    def __str__(self):
        return self.u_name


class StudentManager(models.Manager):

    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

    def create(self, s_name, s_gender, s_phone, s_birthday, s_into, s_note):
        stu = StudentInfo()
        stu.s_name = s_name
        s_info = StudentInfo.objects.latest('id')
        last_sid = s_info.s_id
        num = int(re.sub(r"\D", "", last_sid))
        num += 1
        num = str(num)
        stu.s_id = "DDLL" + num.zfill(4)
        stu.s_gender = s_gender
        stu.s_birthday = s_birthday
        stu.s_phone = s_phone
        stu.s_status = 1
        stu.s_into = s_into
        stu.s_note = s_note
        stu.isDelete = False
        stu.save()
        print('保存成功！')
        return stu


class StudentInfo(models.Model):
    s_name = models.CharField(u'姓名', max_length=6, default='')
    s_id = models.CharField(u'学号', max_length=10)
    s_gender = models.BooleanField(u'性别（打勾表示男）', default=False)
    s_birthday = models.DateField(u'出生日期', default="1900-01-01")
    s_phone = models.CharField(u'手机号码', max_length=20, default='')
    s_status = models.BooleanField(u'是否在读（打勾表示在读）', default=True)
    s_into = models.DateField(u'报名日期', default="1900-01-01")
    s_note = models.TextField(u'备注', default="", null=True, blank=True)
    isDelete = models.BooleanField(u'是否删除', default=False)
    # stu_manager1 = models.Manager()
    objects = StudentManager()

    def classinfo(self):
        return self.s_name

    class Meta:
        verbose_name = u"学生表"
        verbose_name_plural = u"学生表"

    def __str__(self):
        return self.s_id + " " + self.s_name

    def gender(self):
        if self.s_gender:
            return '男'
        else:
            return '女'

    gender.short_description = '性别'


class MoneyInfoManager(models.Manager):
    def get_queryset(self):
        return super(MoneyInfoManager, self).get_queryset().filter(isDelete=False)

    def create(self, s_id, m_money, m_pay_date, m_usually, m_special, m_discount, m_note):
        moneyinfo = MoneyInfo()
        moneyinfo.m_id = s_id
        moneyinfo.m_money = m_money
        moneyinfo.m_into_date = m_pay_date
        moneyinfo.m_regular_time = m_usually
        moneyinfo.m_special_time = m_special
        moneyinfo.m_note = m_note
        moneyinfo.m_discount_from = m_discount
        moneyinfo.isDelete = False
        moneyinfo.save()
        return moneyinfo


class MoneyInfo(models.Model):
    m_id = models.ForeignKey(StudentInfo, default='', verbose_name='学生学号', on_delete=models.CASCADE)
    m_money = models.IntegerField(u'金额', default="")
    m_into_date = models.DateField(u'入账时间', default="1900-01-01")
    m_regular_time = models.IntegerField(u'购买常规课数量', default="")
    m_special_time = models.IntegerField(u'购买特殊课数量', default="", null=True)
    m_note = models.TextField(u'备注', max_length=1000, default="", null=True, blank=True)
    m_discount_from = models.CharField(u'优惠情况', max_length=500, null=True, blank=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    objects = MoneyInfoManager()

    # def __str__(self):
    #     return self.m_id

    class Meta:
        verbose_name = u"财务表"
        verbose_name_plural = u"财务表"


class TeacherInfoManager(models.Manager):
    def get_queryset(self):
        return super(TeacherInfoManager, self).get_queryset().filter(isDelete=False)


class TeacherInfo(models.Model):
    t_name = models.CharField(u'姓名', max_length=10, default=None)
    t_age = models.IntegerField(u'年龄', )
    t_gender = models.BooleanField(u'性别（打勾表示男）', default=1)
    t_professional = models.CharField(u'专业', max_length=100, null=True)
    t_school = models.CharField(u'毕业学校', max_length=200, null=True, blank=True)
    t_work_goal = models.CharField(u'工作方向', max_length=100,null=True, blank=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    class Meta:
        verbose_name = u"教师表"
        verbose_name_plural = u"教师表"

    def __str__(self):
        return self.t_name


class ClassInfoManager(models.Manager):
    def get_queryset(self):
        return super(ClassInfoManager, self).get_queryset().filter(isDelete=False)


class ClassInfo(models.Model):
    cl_id = models.CharField(u'班级ID', max_length=20)
    cl_name = models.CharField(u'班级名称', max_length=50)
    cl_teacher = models.ForeignKey(TeacherInfo, default='', verbose_name='教师姓名',on_delete=models.CASCADE)
    cl_class_place = models.CharField(u'上课地点', max_length=100)
    cl_class_data = models.CharField(u'上课日期', max_length=20)
    cl_class_start_time = models.CharField(u'上课开始时间', max_length=20)
    cl_class_end_time = models.CharField(u'上课结束时间', max_length=20)
    cl_note = models.TextField(u'备注', max_length=1000, null=True, blank=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    class Meta:
        verbose_name = u"班级表"
        verbose_name_plural = u"班级表"

    def __str__(self):
        return self.cl_class_place +" "+ self.cl_name


class CourseTypeInfoManager(models.Manager):
    def get_queryset(self):
        return super(CourseTypeInfoManager, self).get_queryset().filter(isDelete=False)


class CourseTypeInfo(models.Model):
    ct_course_id = models.CharField(u'课程ID', max_length=20, default='' )
    ct_course_name = models.CharField(u'课程名称', max_length=50, default='')
    ct_study_age = models.CharField(u'推荐学习年龄', max_length=20, default="")
    ct_equipment = models.CharField(u'器材', max_length=50, default='')
    ct_note = models.CharField(u'备注', max_length=2000, default='',null=True, blank=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    class Meta:
        verbose_name = u"课程总表"
        verbose_name_plural = u"课程总表"

    def __str__(self):
        return self.ct_course_id + " " + self.ct_course_name


class CourseInfoManager(models.Manager):
    def get_queryset(self):
        return super(CourseInfoManager, self).get_queryset().filter(isDelete=False)


class CourseInfo(models.Model):
    c_course_id = models.CharField(u'课程ID', max_length=20, default='')
    c_section_theme = models.CharField(u'小节主题', max_length=1000)
    c_level = models.CharField(u'难度', max_length=10)
    c_program_design = models.CharField(u'程序设计', max_length=1000, null=True, blank=True)
    c_mechanical = models.CharField(u'机械原理', max_length=1000, null=True, blank=True)
    c_content_theme = models.CharField(u'内容主题', max_length=500)
    c_scientific = models.CharField(u'科学原理', max_length=500, null=True, blank=True)
    c_teacher_experience = models.CharField(u'教学经验', max_length=1000, null=True, blank=True)
    c_classroom = models.CharField(u'教室', max_length=30)
    c_child_five_theme = models.CharField(u'幼儿五大主题', max_length=50, null=True, blank=True)
    c_course_from = models.CharField(u'课程来源', max_length=1000, null=True, blank=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    class Meta:
        verbose_name = u"课程详细表"
        verbose_name_plural = u"课程详细表"

    def __str__(self):
        return str(self.c_course_id) + self.c_section_theme


class StudentClassInfoManager(models.Manager):
    def get_queryset(self):
        return super(StudentClassInfoManager, self).get_queryset().filter(isDelete=False)


class StudentClassInfo(models.Model):
    # sc_id = models.ForeignKey(CourseInfo, default='', verbose_name='课程ID', on_delete=models.CASCADE)
    sc_id = models.ForeignKey(CourseTypeInfo, default='', verbose_name='课程ID', on_delete=models.CASCADE)
    sc_teacher_name = models.ForeignKey(TeacherInfo, verbose_name='任课老师', on_delete=models.CASCADE)
    # sc_section_theme = models.CharField(u'课程小节主题', max_length=1000)
    sc_section_theme = models.ForeignKey(CourseInfo, verbose_name="课程小节主题", on_delete=models.CASCADE)
    sc_date = models.DateField(u'上课时间')
    sc_use_time = models.IntegerField(u'消耗课时', default=1)
    sc_place = models.CharField(u'上课地点', max_length=50)
    sc_bj_id = models.ForeignKey(ClassInfo, default='', verbose_name='上课班级ID', null=True, on_delete=models.CASCADE)
    sc_note = models.CharField(u"备注",max_length=500, null=True, blank=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    class Meta:
        verbose_name = u"教师上课流水"
        verbose_name_plural = u"教师上课流水"

    def __str__(self):
        return  str(self.sc_id) + "+" + str(self.sc_section_theme)


class ClassDetailInfoManager(models.Manager):
    def get_queryset(self):
        return super(ClassDetailInfoManager, self).get_queryset().filter(isDelete=False)


class ClassDetailInfo(models.Model):
    # c_id = models.ForeignKey(StudentClassInfo, verbose_name='课程流水ID')
    # s_id = models.ForeignKey(StudentInfo, verbose_name='上课学生')
    # t_name = models.ForeignKey(TeacherInfo, verbose_name='老师信息')
    c_id = models.ForeignKey(StudentClassInfo, verbose_name='课程名称', on_delete=models.CASCADE)
    s_id = models.ForeignKey(StudentInfo, verbose_name='上课学生', on_delete=models.CASCADE)
    t_name = models.ForeignKey(TeacherInfo, verbose_name='老师信息', on_delete=models.CASCADE)
    cd_note = models.CharField(u'备注', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = u"学生上课流水表"
        verbose_name_plural = u"学生上课流水表"

    def __str__(self):
        return str(self.s_id)


# Create your models here.
