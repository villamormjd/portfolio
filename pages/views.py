from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import resolve
from user_profile.models import UserProfile
from jobs.models import Jobs
from education.models import Education
from .skills import skills


def index(request):
    profile = UserProfile.objects.all()
    jobs = Jobs.objects.order_by('-hire_date')
    education = Education.objects.order_by('-start_date')

    context = {
        "users": profile[0],
        "jobs": jobs,
        "schools": education,
        "skills": skills,

    }
    return render(request, 'pages/index.html', context)
