from django.shortcuts import render
from first_app.models import Reciter, Album
from first_app import forms



# Create your views here.
#  Show the listings
def index(request):
    reciter_list = Reciter.objects.order_by('first_name')
    album_list = Album.objects.order_by('num_stars')
    diction = {'title' : 'Home Page', 'reciter_list':reciter_list, 'album_list':album_list}
    return render(request, "first_app/index.html", context=diction)

# Show single Artist page
def album_list(request, artist_id):
    artist_info = Reciter.objects.get(pk = artist_id)
    album_list = Album.objects.filter(artist = artist_id).order_by('release_date')
    diction = {'title': 'list of Album', 'artist_info':artist_info, 'album_list':album_list}
    return render(request, 'first_app/album_list.html', context=diction)

def reciter_form(request):
    form = forms.ReciterForm()
    
    if request.method == 'POST':
        form = forms.ReciterForm(request.POST)
        
        if form.is_valid():
            form.save(commit = True)
            return index(request)
            
    diction = {'title': 'Add Reciter', 'reciter_form': form }
    return render(request,  'first_app/reciter_form.html', context=diction)

def album_form(request):
    form = forms.AlbumForm()
    
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        
    diction = {'title': 'Add Album', 'album_form':form}
    return render(request, 'first_app/album_form.html', context=diction)

def edit_artist(request, artist_id):
    artist_info = Reciter.objects.get(pk = artist_id)
    form=forms.ReciterForm(instance=artist_info)
    
    if request.method == 'POST':
        form=forms.ReciterForm(request.POST, instance=artist_info)

        if form.is_valid():
            form.save(commit = True)
            return album_list(request, artist_id)
        
    diction={"title": "Update Artist", 'edit_form': form}
    return render(request, "first_app/edit_artist.html", context=diction)

def edit_album(request, album_id):
    album_info = Album.objects.get(pk = album_id)
    form = forms.AlbumForm(instance=album_info)
    diction = {}

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)
        
        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id=album_info.artist_id)
    diction.update({'edit_form':form, 'album_id':album_id})
    diction.update({'album_id':album_id})
    
    return render(request, 'first_app/edit_album.html', context=diction) 

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'delete_success':'Album Deleted Successfully!'}
    return render(request, "first_app/delete.html", context=diction) 

def delete_artist(request, artist_id):
    artist = Reciter.objects.get(pk=artist_id).delete()
    diction = {'delete_success':'Album Deleted Successfully!'}
    return render(request, "first_app/delete.html", context=diction)