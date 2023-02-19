
from django.http import HttpResponse
from django.shortcuts import render, redirect
from diploma_work.forms import ContactForm
from django.views.generic import TemplateView
# Create your views here.


def index(request):

    return render(request, 'main/index.html')


def price(request):

    return render(request, 'main/price.html')


# def my_form_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             name = form.cleaned_data['name']
#             float_val = form.cleaned_data['float_val']
#             class_val = form.cleaned_data['class_val']
#             safety = form.cleaned_data['safety']

#             # Save the form data to a database, send an email, etc.

#             # Redirect to a success page

#     else:
#         form = ContactForm()

#     return render(request, 'my_form.html', {'form': form})


# def my_form_view(request):
#     if request.method == 'POST':
#         # get the form data from the request object
#         name = request.POST.get('name')
#         float_value = request.POST.get('exampleInputFloat')
#         class_value = request.POST.get('exampleInputClass')
#         safety_option_1 = request.POST.get('safety1')
#         safety_option_2 = request.POST.get('safety2')
#         # do something with the form data
#         # for example, you can save it to a database or send it via email
#         # then redirect the user to a thank you page
#         return render("good")

#     else:
#         return render(request, 'index.html')
class ContactView(TemplateView):
    template_name = 'main/index.html'


def func1():
    return 50


def index(request):

    form = ContactForm(request.POST or None)

    total_area = None

    year = None
    pledge = None
    levels = None

    type_of_building = None
    status = None

    ceilings = None
    telephone_lines = None

    parking = None
    all_day_security = None

    fire_alarm = None

    signaling = None
    video_surveillance = None

    window_bars = None
    TV_cable = None
    ADSL = None
    optics = None
    wired = None
    price = 0

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            total_area = form.cleaned_data['total_area']
            year = form.cleaned_data['year']
            pledge = form.cleaned_data['pledge']
            levels = form.cleaned_data['levels']
            type_of_building = form.cleaned_data['type_of_building']
            status = form.cleaned_data['status']
            ceilings = form.cleaned_data['ceilings']
            telephone_lines = form.cleaned_data['telephone_lines']

            parking = form.cleaned_data['parking']

            all_day_security = form.cleaned_data['all_day_security']

            fire_alarm = form.cleaned_data['fire_alarm']

            signaling = form.cleaned_data['signaling']
            video_surveillance = form.cleaned_data['video_surveillance']
            window_bars = form.cleaned_data['window_bars']
            TV_cable = form.cleaned_data['TV_cable']
            ADSL = form.cleaned_data['ADSL']
            optics = form.cleaned_data['optics']
            wired = form.cleaned_data['wired']

    print(total_area, year, pledge, levels, type_of_building,
          status, ceilings, telephone_lines, parking, all_day_security,  fire_alarm, signaling, video_surveillance, window_bars, TV_cable, ADSL, optics, wired)

    context = {
        "form": form,
        "price": price,
    }

    return render(request, 'main/index.html', context)
