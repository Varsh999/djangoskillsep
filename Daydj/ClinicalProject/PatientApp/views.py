from django.shortcuts import render, redirect
from .models import Patient

# List all doctors
def patient_list(request):
    patient = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patient})

# Create a new doctor
def patient_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        disease = request.POST['disease']
        age= request.POST['age']
        Patient.objects.create(name=name, disease=disease, age=age)
        return redirect('patient_list')
    return render(request, 'patient_form.html')

# Update an existing doctor
def patient_update(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.disease = request.POST['disease']
        patient.age = request.POST['age']
        patient.save()
        return redirect('patient_list')
    return render(request, 'patient_form.html', {'patient': patient})

# Delete a doctor
def patient_delete(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patient_list')

