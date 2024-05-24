from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
