from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from jobs.models import Jobs


def index(request):
    profile = UserProfile.objects.all()
    jobs = Jobs.objects.order_by('-hire_date')
    context = {
        "users": profile[0],
        "jobs": jobs
    }
    return render(request, 'pages/index.html', context)
