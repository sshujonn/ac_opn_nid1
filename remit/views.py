from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from rest_framework import renderers
from rest_framework.views import APIView

from remit.form import CustomCustomerForm
from remit.models import CustomCustomer


class CustEntryLand(APIView):
    permission_classes = ()
    template_name = 'ac_openning/cust_entry.html'
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def get(self, request):
        form = CustomCustomerForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CustomCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, "Data uploaded")
            return redirect('cust_entry')
        else:
            messages.warning(request, str(form.errors))
            return redirect('cust_entry')


class ShowAllCustLand(APIView):
    permission_classes = ()
    template_name = 'ac_openning/show_all_cust.html'
    renderer_classes = [renderers.TemplateHTMLRenderer]
    def get(self, request):
        all_cust = CustomCustomer.objects.all()
        return render(request, self.template_name, {"data": all_cust})