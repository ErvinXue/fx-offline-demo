from app.user.model import Student


from app.course.model import Course
from datetime import datetime

from email.policy import default
from flask_mongoengine import Document
from flask_jwt_extended import current_user
from mongoengine import (
    StringField,
    ReferenceField,
    CASCADE,
    DateTimeField,
    BooleanField,
    FloatField,
)


class Order(Document):
    student = ReferenceField(Student, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    created_time = DateTimeField(default=datetime.now)
    original_price = FloatField()
    paid = BooleanField(default=False)
    paid_time = DateTimeField()
    paid_comment = StringField(default="No comment")
    paid_price = FloatField()

    def to_dict(self):
        return {
            "id": str(self.id),
            "student": {
                "id": str(self.student.id),
                "username": self.student.username,
                "display_name": self.student.display_name,
            },
            "course": {
                "id": str(self.course.id),
                "name": self.course.name,
                "uni_course_code": self.course.uni_course_code,
            },
            "campus": {
                "id": str(self.course.campus.id),
                "name": self.course.campus.name
            },
            "created_time": self.created_time.isoformat(),
            "original_price": self.original_price,
            "paid": self.paid,
            "paid_time": self.paid_time and self.paid_time.isoformat() or None,
            "paid_comment": self.paid_comment,
            "paid_price": self.paid_price,
        }
