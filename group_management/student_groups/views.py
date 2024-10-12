from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from .models import Student




def index(request):
    return render(request, "student_groups/index.html", {
        "message": messages.get_messages(request)  
    })


def change(request):
    if request.method == "POST":
        Fmatricule = request.POST['matricule']
        Fnom = request.POST['nom']
        Fprenom = request.POST['prenom']
        Fgroupe = request.POST['Fgroup']
        Ftogroupe = request.POST['Ftogroup']

        Smatricule = request.POST['Smatricule']
        Snom = request.POST['Snom']
        Sprenom = request.POST['Sprenom']
        Sgroupe = request.POST['Sgroup']

        # Retrieve first student
        first_student = Student.objects.filter(
            matricule=Fmatricule,
            group_actual=Fgroupe,
            nom=Fnom,
            prenom=Fprenom
        ).first()

        # Retrieve second student
        second_student = Student.objects.filter(
            matricule=Smatricule,
            group_actual=Sgroupe,
            nom=Snom,
            prenom=Sprenom
        ).first()

        if first_student and second_student and Sgroupe == Ftogroupe:
            # Proceed with the swap
            first_student.group_actual = Ftogroupe
            second_student.group_actual = Fgroupe
            first_student.save()
            second_student.save()

            messages.success(request, "Your request has benn successfully saved!")
        else:
            messages.error(request, "One or both students not found or group details do not match. REQUEST FAILED")

        return redirect('index') 
     
    messages.error(request, "Somthing went wrong try again")

    return redirect('index')
