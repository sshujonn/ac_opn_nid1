
from rest_framework import renderers
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages

from ac_openning.service import process_data, handle_uploaded_file, update_or_insert_customer, fill_up_form


# Create your views here.


class NIDCardScriptLand(APIView):
    permission_classes = ()
    template_name = 'ac_openning/ac_openning.html'
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def get(self, request):
        return Response({}, template_name=self.template_name)

    def post(self, request):
        card_script = request.FILES.get('card_script')
        n_card_script = request.FILES.get('card_script')

        form_fillup = request.POST.get('form_fillup')

        handle_uploaded_file(card_script, 'nid.htm')
        handle_uploaded_file(n_card_script,'n_nid.htm')

        data = process_data("nid.htm")
        n_data = process_data("n_nid.htm")

        data = {"customer": data, "nominee": n_data}

        message = update_or_insert_customer(data.get("customer"))
        n_message = update_or_insert_customer(data.get("nominee"))

        messages.warning(request, message)
        messages.warning(request, n_message)

        if form_fillup:
            file_link = fill_up_form(data)
        Response().set_cookie(key="c_nid", value='1234')
        Response().set_cookie(key="n_nid", value='16841')
        return Response({}, template_name=self.template_name)



