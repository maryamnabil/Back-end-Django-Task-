
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login
from django.core.urlresolvers import reverse_lazy
from .models import Album
from .forms import  UserForm

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name ='music/detail.html'

	
class AlbumCreate(CreateView):
	model=Album
	fields = ['artist' , 'album_title' , 'genre' , 'album_logo']
				
class AlbumUpdate(UpdateView):
	model=Album
	fields = ['artist' , 'album_title' , 'genre' , 'album_logo']

class AlbumDelete(DeleteView):
	model=Album			
	success_url= reverse_lazy('music:index')

class UserFormView(View):
	form_class =UserForm
	template_name = 'music/registeration_form.html'
	def get(self , request):
		form = self.form_class(None)
		return render(request, self.template_name , {'form' : form})
	def post(self , request):	
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			# clean data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			# returns user object if credential are correct
			user= authenticate(username=username ,password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('music:index')
		return render(request ,self.template_name , {'form':form})









# -*- coding: utf-8 -*-
'''from __future__ import unicode_literals

from django.shortcuts import render , get_object_or_404
#from django.http import HttpResponse
#from django.http import Http404
from django.shortcuts import render
#from django.template import loader
from .models import Album 
# Create your views here.

def index(request):
	all_albums=Album.objects.all()
	#template=loader.get_template('music/index.html')
	return render(request, 'music/index.html', {'all_albums': all_albums}) #HttpResponse(template.render(context, request))


def detail(request, album_id):
	#try:
		#album = Album.objects.get(pk=album_id)
	#except Album.DoesNotExist:
		#raise Http404("Album Does Not Exist")
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', {'album': album})
	#return HttpResponse("<h2>details for album id:" + str(album_id)+"</h2>")

def favourite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError, song.DoesNotExistD):
		return render(request, 'music/detail.html', 
			{'album': album, 'error_message':"you didn't select a valid song"} )
	else:
		selected_song.is_fav=True
		selected_song.save()
		return render(request, 'music/detail.html', {'album': album})'''#
