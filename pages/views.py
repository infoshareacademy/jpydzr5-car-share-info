from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse

from .forms import ContactForm, RentalForm
from .models import Cars, Rental


class HomePageView(ListView):
    model = Cars
    template_name = "pages/home.html"
    context_object_name = "cars"
    paginate_by = 6

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context


class RentView(CreateView):
    model = Rental
    form_class = RentalForm
    template_name = "pages/rent.html"
    success_url = reverse_lazy("rental_success")

    def get_initial(self):
        initial = super().get_initial()
        car_id = self.kwargs.get("car_id")
        if car_id:
            initial["car"] = car_id
        if self.request.user.is_authenticated:
            initial["user"] = self.request.user
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RentalViewSuccess(TemplateView):
    template_name = "pages/rental_success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            pass
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["form_data"] = request.POST
        return self.render_to_response(context)


class SendView(TemplateView):
    template_name = "pages/send.html"


class ContactView(FormView):
    form_class = ContactForm
    template_name = "pages/contact.html"
    success_url = reverse_lazy("send")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs["initial"] = {
                "email": self.request.user.email,  # type: ignore
                "first_name": self.request.user.first_name,  # type: ignore
                "last_name": self.request.user.last_name,  # type: ignore
                "phone_number": self.request.user.phone_number,  # type: ignore
            }
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def car_detail_api(request, pk):
    car = Cars.objects.get(pk=pk)
    data = {
        "brand": car.brand,
        "model": car.model,
        "year": car.year,
        "category": car.category,
        "mileage": car.mileage,
        "engine_size": car.engine_size,
        "fuel": car.fuel,
        "gearbox": car.gearbox,
        "air_contidion": car.air_contidion,
        "number_of_seats": car.number_of_seats,
        "number_of_doors": car.number_of_doors,
        "color": car.color,
        "body_style": car.body_style,
        "availability": car.availability,
        "image": car.image.url if car.image else None,
    }
    return JsonResponse(data)
