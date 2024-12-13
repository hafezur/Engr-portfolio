from django.shortcuts import render
from django import views
from django.views import generic


from . forms import ContactForm
from django.contrib import messages
from . models import UserProfile,MySkill,Certificate,Project,Blog,Testimonial,ContactProfile
# Create your views here.
def baseFunc(request):
    return render(request,'home.html')

def first(request):
    hafiz=UserProfile.objects.all()
    my_skill=MySkill.objects.all()
    all_certificate=Certificate.objects.all()
    all_project=Project.objects.all()
    testimonial=Testimonial.objects.all()
    
    context={
        'hafiz': hafiz,
        'my_skill':my_skill,
        'certificate':all_certificate,
        'project':all_project,
        'testimonial':testimonial
    }
    return render(request, 'index.html',context)


def Contact(request):
    return render(request, 'contact.html')

def NewProject(request):
    get_id=Project.objects.all()
    find_length=len(get_id)
    #print(find_length)
    letest_project=Project.objects.filter(id=find_length)
    #print(letest_project)
    context={
        'letest_project':letest_project,
    }
    return render(request, 'letest_project-detail.html',context)

def only_Blog(request):
    my_blog=Blog.objects.all()
    context={
        'blog1':my_blog,
    }
    return render(request, 'blog.html',context)

def Hello_Blog(request):
    block_detail=Blog.objects.all()
    context={
        'blog2':block_detail,
    }
    return render(request, 'blog-detail.html',context)

def project_detail(request):
    my_project=Project.objects.all()
    context={
        'detail_project':my_project,
    }
    return render (request, 'project-detail.html',context)


class ContactView(generic.FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


