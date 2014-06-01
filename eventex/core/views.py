from django.views.generic import TemplateView

from apps.subscriptions.forms import SubscriptionForm

class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        try:
            context['form'] = SubscriptionForm()
        except:
            context['form'] = None

        return context