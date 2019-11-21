from django.shortcuts import render
from .forms import SearchForm
from .models import Phone_number


def index(request):
    result = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            full_phone_number = form.cleaned_data['full_phone_number']
            code = full_phone_number[:3]
            phone_number = full_phone_number[3:]
            print(code, phone_number)
            result = Phone_number.objects.filter(
                code=code,
                start_number__lte=phone_number,
                end_number__gte=phone_number
            )
            print(len(result))

    else:
        form = SearchForm()
    return render(request, 'caller_id/index.html', {'form': form, 'result': result})
