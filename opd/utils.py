from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate
from opd.models import Appointment, Opd, Doctor


def add_user_to_doctor_group(user):
    doctor_group = Group.objects.get(name="Doctor")
    user.groups.add(doctor_group)


def create_doctor_user(username, password, email):
    user = User.objects.create_user(username=username, password=password, email=email)
    add_user_to_doctor_group(user)
    return user


def is_doctor(user):
    return user.groups.filter(name="Doctor").exists()


def get_processed_data(patients):
    return [
        patient.offline_patient if patient.type == "offline" else patient.online_patient
        for patient in patients
    ]


def get_product_count(products):
    return [sum(product.quantity for product in products)]


def get_total_bed_count():
    opds = Opd.objects.all()
    total_beds = 0
    for opd in opds:
        total_beds += opd.no_of_beds
    return total_beds


def get_total_doctor_count():
    return Doctor.objects.count()


def get_total_appointment_count():
    return Appointment.objects.count()


def custom_authenticate(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None and user.groups.filter(name="Doctor").exists():
        return user

    return None
