import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def can_edit_question(self, user):
        if user.is_superuser:
            return True
        
        if self.author:
            return self.author == user
        return True
    
    class Meta:
        permissions = [
            ('can_view_results', 'User can access results page'),
            ('can_view_results_w_score', 'User can access page and check votes count'),
        ]
    
    # def can_view(self, user):
    #     return user.is_authenticated and user.is_active


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def vote(self):
        self.votes+=1
        self.save()


class ChoiceRate(models.Model):
    choice_rate = models.IntegerField(default=1)


class Student(models.Model):
    name = models.CharField(max_length=70)
    

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, through='Enrollment')


class Enrollment(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_date = models.DateField(auto_now=True)

    def __repr__(self):
        return f'Student: {self.students}, courses: {self.courses}'
    def __str__(self):
        return f'Student: {self.students}, courses: {self.courses}'


class TimeStampModel(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_edit_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self):
        self.last_edit_datetime = datetime.datetime.now()
        super().save()


class Books(TimeStampModel):
    author = models.TextField(max_length=100)
    genre = models.TextField(max_length=100)
    in_use_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)

class Dvd(TimeStampModel):
    name = models.CharField(max_length=50)
    in_use_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)

class UserDocuments(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='user_documents/')
