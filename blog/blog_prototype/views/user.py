from django.shortcuts import get_object_or_404, redirect, render

from blog_prototype.forms import SignUpForm


def register(request):

    form = SignUpForm(request.POST or None)

    print(form.is_valid())
    print(form.errors)

    if form.is_valid():
        form.save()

        return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)
