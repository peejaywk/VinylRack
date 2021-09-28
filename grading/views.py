from django.shortcuts import render


def grading(request):
    """
    Display information on how the records sold on the site are graded
    """

    context = {}
    template = "grading/grading.html"
    return render(request, template, context)
