from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from jobs.models import Jobs
from education.models import Education


def index(request):
    profile = UserProfile.objects.all()
    jobs = Jobs.objects.order_by('-hire_date')
    education = Education.objects.order_by('-start_date')
    context = {
        "users": profile[0],
        "jobs": jobs,
        "schools": education
    }
    return render(request, 'pages/index.html', context)
