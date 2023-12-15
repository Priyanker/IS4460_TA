from django.views import View
from django.shortcuts import render
from . import my_functions, my_objects

class HomePageView(View):
    def get(self, request):
        orig_name = "jACOB"
        name = fix_name(orig_name)

        names = ['LUis', 'GaBriela', 'MaRy']
        fixed_names = my_functions.fix_names_list(names)

        context = {
            'hi': 'hello world!',
            'name': name,
            'orig_name': orig_name,
            'names': names,
            'fixed_names': fixed_names,
            'car1': my_objects.Car("Honda", "Fit", 2023, "blue", "honk honk"),
            'car2': my_objects.Car("Tesla", "Y", 2023, "green", "beep beep"),
            'motorcycle1': my_objects.Motorcycle("BMW", "K12", 2023, "blue", "beep!")
        }

        return render(request, 'lab4/index.html', context)

def fix_name(name: str):
    return name.title()