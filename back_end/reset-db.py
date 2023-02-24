print("Loading...")

from app import create_app
from app.campus.model import Campus
from app.user.model import Student, Admin, User, Teacher,get_hashed_password

create_app()

# Campus.objects().delete()
# User.objects().delete()

c= Campus(name="monash")
c.save()

admin = Admin(
    username="admin",
    password=get_hashed_password("password"),
    telephone="987654321",
    permissions =["systm_owner","campus_admin","user_admin","lecture_admin","order_admin"],
    campus=c

)
admin.save()

student = Student(
    username="student_1",
    display_name="Jerry",
    password=get_hashed_password("password"),
    telephone="987654321",
    wx="wxid_123",
    campus=c,
)
student.save()

teacher = Teacher(
    username="teacher_1",
    display_name="Teacher",
    password= get_hashed_password("password"),
    telephone="987654321",
    abn="xxxxxxxxxxxxxxxxx",
    campus=c
)
teacher.save()