from django.db import models

from django.db import models


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=1)

    def create(self, s_name, s_sid):
        stu = StudentInfo()
        stu.s_name = s_name
        stu.s_id = s_sid
        stu.s_gender = 0
        stu.s_birthday = '2010-05-21'
        stu.s_phone = '12322222222'
        stu.s_status = 1
        stu.s_into = '2024-3-2'
        stu.isDelete = False
        return stu


class StudentInfo(models.Model):
    s_name = models.CharField(u'姓名', max_length=6, default='')
    s_id = models.CharField(u'学号', max_length=10)
    s_gender = models.BooleanField(u'性别', default=False)
    s_birthday = models.DateField(u'出生日期', )
    s_phone = models.CharField(u'手机号码', max_length=20, default='')
    s_status = models.BooleanField(u'在读状态', default=True)
    s_into = models.DateField(u'报名日期', )
    s_note = models.TextField(u'备注', default="", null=True)
    isDelete = models.BooleanField(u'是否删除', default=False)
    # stu_manager1 = models.Manager()
    # stu_manager2 = StudentManager()

    def classinfo(self):
        return self.s_name

    class Meta:
        verbose_name = u"学生表"
        verbose_name_plural = u"学生表"

    def __str__(self):
        return self.s_name

    def gender(self):
        if self.s_gender:
            return '男'
        else:
            return '女'

    gender.short_description = '性别'


class TeacherInfo(models.Model):
    t_name = models.CharField(u'姓名', max_length=10, default=None)
    t_age = models.IntegerField(u'年龄', )
    t_gender = models.BooleanField(u'性别', default=1)
    t_professional = models.CharField(u'专业', max_length=100, null=True)
    t_school = models.CharField(u'毕业学校', max_length=200, null=True)
    # t_work_goal = models.CharField(u'工作方向',max_length=100)
    isDelete = models.BooleanField(u'是否删除', default=False)

    class Meta:
        verbose_name = u"教师表"
        verbose_name_plural = u"教师表"

    def __str__(self):
        return self.t_name


class MoneyInfo(models.Model):
    m_id = models.ForeignKey(StudentInfo, default='', verbose_name='学生学号')
    m_money = models.IntegerField(u'金额', default="")
    m_into_date = models.DateField(u'入账时间', default="1900-01-01")
    m_regular_time = models.IntegerField(u'购买常规课数量', default="")
    m_special_time = models.IntegerField(u'购买特殊课数量', default="", null=True)
    m_note = models.TextField(u'备注', max_length=1000, default="", null=True)
    m_discount_from = models.CharField(u'优惠情况', max_length=500, null=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    # def __str__(self):
    #     return self.m_id

    class Meta:
        verbose_name = u"财务表"
        verbose_name_plural = u"财务表"


class ClassInfo(models.Model):
    cl_id = models.CharField(u'班级ID', max_length=20)
    cl_name = models.CharField(u'班级名称', max_length=50)
    cl_teacher = models.ForeignKey(TeacherInfo, default='', verbose_name='教师姓名')
    cl_class_place = models.CharField(u'上课地点', max_length=100)
    cl_class_data = models.CharField(u'上课日期', max_length=20)
    cl_class_start_time = models.CharField(u'上课开始时间', max_length=20)
    cl_class_end_time = models.CharField(u'上课结束时间', max_length=20)
    cl_note = models.TextField(u'备注', max_length=1000, null=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    class Meta:
        verbose_name = u"班级表"
        verbose_name_plural = u"班级表"

    def __str__(self):
        return self.cl_name


class CourseTypeInfo(models.Model):
    ct_course_id = models.CharField(u'课程ID', max_length=20, default='')
    ct_course_name = models.CharField(u'课程名称', max_length=50, default='')
    ct_study_age = models.CharField(u'推荐学习年龄', max_length=20, default="")
    ct_equipment = models.CharField(u'器材', max_length=50, default='')
    ct_note = models.CharField(u'备注', max_length=2000, default='')


class CourseInfo(models.Model):
    c_course_id = models.CharField(u'课程ID', max_length=20, default='')
    c_section_theme = models.CharField(u'小节主题', max_length=1000)
    c_level = models.CharField(u'难度', max_length=10)
    c_program_design = models.CharField(u'程序设计', max_length=1000, null=True)
    c_mechanical = models.CharField(u'物理结构', max_length=1000, null=True)
    c_content_theme = models.CharField(u'内容主题', max_length=500)
    c_scientific = models.CharField(u'科学原理', max_length=500, null=True)
    c_teacher_experience = models.CharField(u'教学经验', max_length=1000, null=True)
    c_classroom = models.CharField(u'教室', max_length=30)
    c_course_from = models.CharField(u'课程来源', max_length=1000, null=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    class Meta:
        verbose_name = u"课程详细表"
        verbose_name_plural = u"课程详细表"

    def __str__(self):
        return self.c_course_id


class StudentClassInfo(models.Model):
    sc_id = models.ForeignKey(CourseInfo, default='', verbose_name='课程ID')
    sc_teacher_name = models.ForeignKey(TeacherInfo, verbose_name='任课老师')
    sc_section_theme = models.CharField(u'课程小节主题', max_length=1000)
    sc_date = models.DateField(u'上课时间')
    sc_use_time = models.IntegerField(u'消耗课时', )
    sc_place = models.CharField(u'上课地点', max_length=50)
    sc_bj_id = models.ForeignKey(ClassInfo, default='', verbose_name='上课班级ID', null=True)
    isDelete = models.BooleanField(u'是否删除', default=False)

    class Meta:
        verbose_name = u"学生上课表"
        verbose_name_plural = u"学生上课表"

    def __str__(self):
        return str(self.kc_id_id)


class ClassDetailInfo(models.Model):
    c_id = models.ForeignKey(StudentClassInfo, verbose_name='课程流水ID')
    s_id = models.ForeignKey(StudentInfo, verbose_name='上课学生')
    cd_note = models.CharField(u'备注', max_length=1000, null=True)

    class Meta:
        verbose_name = u"学生上课详细表"
        verbose_name_plural = u"学生上课详细表"
# Create your models here.
