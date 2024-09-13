from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from opd.models import Doctor, Appointment
from opd.utils import (
    get_total_appointment_count,
    get_total_bed_count,
    get_total_doctor_count,
)
from django.db import models
from user.utils import (
    custom_authenticate,
    check_user,
    search_by_opd,
    search_specialist_doctor,
    getResponse,
)
# TODO: remove the message after a time


def user_login(request):
    if request.method == "POST":
        is_user = custom_authenticate(request)
        if is_user:
            login(request, is_user)
            messages.success(request, "Welcome back")
            return redirect("user:home_page")
        messages.error(request, "something wrong with user or password")
        return redirect("user:login")
    context = {}
    return render(request, "user/user_login.html", context)


def user_logout(request):
    logout(request)
    messages.success(request, "you have been logout")
    return redirect("user:home_page")


def home_page(request):
    # check if the home page is for user or not
    is_user = check_user(request)
    if is_user:
        context = {
            "user": is_user,
            "total_beds_count": get_total_bed_count,
            "total_doctor_count": get_total_doctor_count,
            "total_appointment_count": get_total_appointment_count,
        }
        return render(request, "user/logged/profile.html", context)
    context = {
        "total_beds_count": get_total_bed_count,
        "total_doctor_count": get_total_doctor_count,
        "total_appointment_count": get_total_appointment_count,
    }
    return render(request, "user/index.html", context)


def profile(request):
    context = {}
    return render(request, "user/profile.html", context)


def bed_list(request):
    is_user = check_user(request)
    if is_user:
        base_template = "user/logged/index.html"
    else:
        base_template = "base.html"
    doctors = Doctor.objects.all()
    context = {"doctors": doctors, "base_template": base_template}
    return render(request, "user/bed_list.html", context)


def opd_list(request):
    is_user = check_user(request)
    if is_user:
        base_template = "user/logged/index.html"
    else:
        base_template = "base.html"
    search_query = request.GET.get("search_query", "")
    if search_query:
        doctors = search_by_opd(request, search_query)
    else:
        doctors = Doctor.objects.all()
    context = {"doctors": doctors, "base_template": base_template}
    return render(request, "user/opd_list.html", context)


def hospital_detail(request):
    context = {}
    return render(request, "user/hospital_detail.html", context)


def search_specialist(request):
    is_user = check_user(request)
    if is_user:
        base_template = "user/logged/index.html"
    else:
        base_template = "base.html"
    search_query = request.GET.get("search_query", "")
    if search_query:
        doctors = search_specialist_doctor(request, search_query)
    else:
        doctors = Doctor.objects.all()
    context = {"doctors": doctors, "base_template": base_template}
    return render(request, "user/search_specialist.html", context)


def chatbot(request):
    user_message = request.GET.get("message", "")
    if user_message:
        print("inside the if statement")
        bot_response = getResponse(user_message)  # Assuming you have this function
    else:
        bot_response = ""

    context = {"bot_response": bot_response, "user_message": user_message}
    return render(request, "user/chatbot.html", context)


def appointment(request, pk):
    doctor = Doctor.objects.get(id=pk)
    search_query = request.GET.get("search_query")
    if search_query == "booking":
        is_user = check_user(request)
        if is_user:
            try:
                Appointment.objects.create(
                    opd=doctor.opd,  # type: ignore
                    online_patient=request.user.profile,
                    appointment_type="offline",
                    status="not_seen",
                )
                doctor.opd.save()
                messages.success(
                    request, "You appoinment request has been send successfully"
                )
                return redirect("user:home_page")
            except Exception as e:
                messages.error(request, f"Error creating appointment: {str(e)}")
                return redirect("user:appointment", pk=doctor.id)
        return redirect("user:login")
    total_bed_count = doctor.opd.no_of_beds  # type: ignore
    total_appointment_count = doctor.opd.no_of_appointment  # type: ignore
    context = {
        "doctor": doctor,
        "total_appointment_count": total_appointment_count,
        "total_bed_count": total_bed_count,
    }
    return render(request, "user/appointment.html", context)


def doctor_profile(request, pk):
    doctor = Doctor.objects.get(id=pk)
    context = {"doctor": doctor}
    return render(request, "user/doctor_profile.html", context)


# NOTE: All the method after this are related to the logged in user
def medical_history(request):
    context = {}
    return render(request, "user/logged/medical_history.html", context)


def message(request):
    context = {}
    return render(request, "user/logged/message.html", context)


def user_profile(request):
    is_user = check_user(request)
    context = {"user": is_user.profile}  # type: ignore
    return render(request, "user/logged/user_profile.html", context)
