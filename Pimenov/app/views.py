from django.shortcuts import render
from .models import Grade, Lesson, Student
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# Create your views here.


def index(request):
    students = Student.objects.all()
    return render(request, 'app/index.html', {'students':students})

def create_objects():
    if Lesson.objects.all()==0:
        Lesson.objects.create(lesson='algebra')
        Lesson.objects.create(lesson='english')
        Lesson.objects.create(lesson='PE')
        Lesson.objects.create(lesson='geometry')
    if Grade.objects.all() == 0:
        Grade.objects.create(grade=2)
        Grade.objects.create(grade=3)
        Grade.objects.create(grade=4)
        Grade.objects.create(grade=5)


def create(request):
    if request.method == 'POST':
        # create_objects()
        student = Student()

        student.name = request.POST.get('name')
        student.surname = request.POST.get('surname')
        student.lesson_id = request.POST.get('lesson')
        student.grade_id = request.POST.get('grade')

        student.save()
        return HttpResponseRedirect('/student')

    grades = Grade.objects.all()
    lessons = Lesson.objects.all()
    return render(request, 'app/create.html', {'grades':grades, 'lessons':lessons})
