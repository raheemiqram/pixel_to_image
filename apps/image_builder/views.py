from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from apps.image_builder.models import OriginalImage


class CSVList(ListView):
    model = OriginalImage
    template_name = 'dashboard/image_builder/list.html'
    context_object_name = 'csv_list'
    paginate_by = 10


class UploadCSV(CreateView):
    model = OriginalImage
    template_name = 'dashboard/image_builder/upload_csv.html'
    fields = ['csv_file']
    success_url = reverse_lazy('csv_list')

    def form_valid(self, form):
        # Save the form and get the created object
        self.object = form.save()

        # convert csv(pixels) to image
        self.object.data_process(commit=True)

        return super().form_valid(form)


class ImageBuilder(TemplateView):
    template_name = 'dashboard/image_builder/image_builder.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            object = OriginalImage.objects.get(id=kwargs.get('pk'))
        except ObjectDoesNotExist:
            raise Http404("Matching query does not exist.")
        ctx['object'] = object
        return ctx
