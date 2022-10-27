from django.contrib import messages
from django.shortcuts import render

from my_app.models import Car
from my_app.forms import CarForm


def create_cars(request):
    if request.method == "POST":
        car_form = CarForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if car_form.is_valid():
            data = car_form.cleaned_data
            actual_objects = Car.objects.filter(
                brand=data["brand"], model=data["model"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El coche {data['brand']} - {data['model']} ya está creado",
                )
            else:
                car = Car(brand=data["brand"], model=data["model"])
                car.save()
                messages.success(
                    request,
                    f"Coche {data['brand']} - {data['model']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"cars": Car.objects.all()},
                template_name="my_app/car_list.html",
            )

    car_form = CarForm(request.POST)
    context_dict = {"form": car_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/car_form.html",
    )


def cars(request):
    return render(
        request=request,
        context={"cars": Car.objects.all()},
        template_name="my_app/car_list.html",
    )
