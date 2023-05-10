
from rest_framework import renderers
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from ac_openning.service import process_data, handle_uploaded_file, update_or_insert_customer, fill_up_form, \
    process_for_show_data, process_for_form_fillup, update_db


# Create your views here.


class NIDCardScriptLand(APIView):
    permission_classes = ()
    template_name = 'ac_openning/ac_openning.html'
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def get(self, request):
        return Response({}, template_name=self.template_name)

    def post(self, request):
        card_script = request.FILES.get('card_script')
        n_card_script = request.FILES.get('n_card_script')

        form_fillup = request.POST.get('form_fillup')

        handle_uploaded_file(card_script, 'nid.htm')
        data = process_data("nid.htm")
        data = {"customer": data}
        message = update_or_insert_customer(data.get("customer"))
        messages.warning(request, message)
        request.session['c_nid'] = data.get("customer").get("national_id")
        if n_card_script:
            handle_uploaded_file(n_card_script,'n_nid.htm')
            n_data = process_data("n_nid.htm")
            data["nominee"] = n_data
            n_message = update_or_insert_customer(data.get("nominee"))
            messages.warning(request, n_message)
            request.session['n_nid'] = data.get("nominee").get("national_id")

        return HttpResponseRedirect(reverse('show_data'))


class ShowAllData(APIView):
    permission_classes = ()
    template_name = 'ac_openning/show_data.html'
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def get(self, request):
        nid =request.session['c_nid']
        nnid =request.session.get('n_nid')

        data = process_for_show_data(nid, nnid)
        return Response({"data": data}, template_name=self.template_name)


class FormFillup(APIView):
    permission_classes = ()
    template_name = 'ac_openning/show_data.html'
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def post(self, request):
        acc_dict, cust_dict, nom_dict, tp_dict = process_for_form_fillup(request.data)

        acc_id, cust_id, nom_id, tp_id = update_db(acc_dict, cust_dict, nom_dict, tp_dict)

        file_link = fill_up_form(acc_id, cust_id, tp_id, nom_id)
        request.session.clear()
        return JsonResponse({"file_link": file_link}, safe=False)



