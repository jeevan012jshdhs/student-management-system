from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentForm


def student_list(request):
    query = request.GET.get('q', '')

    if query:
        student_list = Student.objects.filter(name__icontains=query) | Student.objects.filter(usn__icontains=query)
        student_list = student_list.order_by('-created_at')
    else:
        student_list = Student.objects.all().order_by('-created_at')

    paginator = Paginator(student_list, 5)   # 5 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    context = {
        'students': students,
        'query': query
    }
    return render(request, 'students/student_list.html', context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Add Student'
    })


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Student updated successfully.')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Edit Student'
    })


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        messages.error(request, 'Student deleted successfully.')
        return redirect('student_list')

    return render(request, 'students/student_delete.html', {
        'student': student
    })