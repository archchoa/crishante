from django.contrib import messages
from django.urls import reverse_lazy

from contact_form.views import ContactFormView

from .forms import CustomContactForm


class CustomContactFormView(ContactFormView):
    form_class = CustomContactForm
    success_url = reverse_lazy('contact_form')

    def form_valid(self, form):
        form = super(CustomContactFormView, self).form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS, 'Message sent successfully.')
        return form
