from django.shortcuts import render
def page_not_found_view(request, exception):
    context = {
        'is_auth':request.user.is_authenticated,
    } 
    return render(request, '404.html', status=404,context=context)