from django.shortcuts import render	
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda user: user.userprofile.role == 'Librarians')
def librarian_view(request):
    return render(request, 'librarian.html')
