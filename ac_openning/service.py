import datetime

from django.contrib import messages

import os

from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from docx import Document

from ac_openning.models import Customer
from ac_opn_nid.settings import NID_DIRECTORY, N_NID_DIRECTORY


def process_basic_info(item):
    basic_info = {"Name(Bangla)": "b_name",
                  "Name(English)": "e_name",
                  "Date of Birth": "dob",
                  "Father Name": "f_name",
                  "Mother Name": "m_name",
                  "Spouse Name": "s_name",
                  "Occupation": "occupation"}
    processed_info = {}

    for itm in basic_info.items():
        val_div = item[0].find_all('div', string=itm[0])
        val = val_div[0].find_next_sibling()

        processed_info[itm[1]] = val.text
    return processed_info


def process_pre_address(pre_div):
    pre_info = {"Division": "pre_division",
                "District": "pre_district",
                "RMO": "pre_rmo",
                "City Corporation Or Municipality": "pre_citycorp",
                "Upozila": "pre_upozila",
                "Union/Ward": "pre_union_ward",
                "mouza/Moholla": "pre_mouza_moholla",
                "Additional Mouza/Moholla": "pre_additional_mouza_moholla",
                "Ward For Union Porishod": "pre_ward_for_union_porishod",
                "village/Road": "pre_village_road",
                "Additional Village/Road": "pre_additional_village_road",
                "Home/Holding No": "pre_home_holding_no",
                "Post Office": "pre_post_office",
                "Postal Code": "pre_postal_code",
                "Region": "pre_region"}
    processed_info = {}

    # import pdb;pdb.set_trace()
    for itm in pre_info.items():
        val_div = pre_div.find_all('div', string=itm[0])
        val = val_div[0].find_next_sibling()

        processed_info[itm[1]] = val.text
    return processed_info


def process_per_address(per_div):
    per_info = {"Division": "per_division",
                "District": "per_district",
                "RMO": "per_rmo",
                "City Corporation Or Municipality": "per_city_corporation_or_municipality",
                "Upozila": "per_upozila",
                "Union/Ward": "per_union_ward",
                "mouza/Moholla": "per_mouza_moholla",
                "Additional Mouza/Moholla": "per_additional_mouza_moholla",
                "Ward For Union Porishod": "per_ward_for_union_porishod",
                "village/Road": "per_village_road",
                "Additional Village/Road": "per_additional_village_road",
                "Home/Holding No": "per_home_holding_no",
                "Post Office": "per_post_office",
                "Postal Code": "per_postal_code",
                "Region": "per_region"}
    processed_info = {}

    for itm in per_info.items():
        val_div = per_div.find_all('div', string=itm[0])
        val = val_div[0].find_next_sibling()

        processed_info[itm[1]] = val.text
    return processed_info


def process_other_info(item):
    basic_info = {"Blood Group": "blood_group",
                  "National ID": "national_id",
                  "Pin": "pin"}
    processed_info = {}

    for itm in basic_info.items():
        val_div = item[0].find_all('div', string=itm[0])
        val = val_div[0].find_next_sibling()

        processed_info[itm[1]] = val.text
    return processed_info


def process_data(file_name):
    with open(NID_DIRECTORY+file_name, encoding="utf8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        item = soup.find_all('div', {'class': 'row border'})
        processed_info = process_basic_info(item)

        per_div = item[0].find_all('div', string='Permanent Address')
        per_div = per_div[0].find_next_sibling()
        processed_info = {**processed_info, **process_per_address(per_div)}

        pre_div = item[0].find_all('div', string='Present Address')
        pre_div = pre_div[0].find_next_sibling()
        processed_info = {**processed_info, **process_pre_address(pre_div)}
        processed_info = {**processed_info, **process_other_info(item)}
        return processed_info

def update_or_insert_customer(data):
    customer = Customer.objects.filter(national_id=data.get("national_id"))
    if customer.exists():
        customer = Customer.objects.get(national_id=data.get("national_id"))
        for item in data.items():
            if item[0] is not "national_id":
                setattr(customer, item[0], item[1])
        message = "Updated customer successfully"

    else:
        customer = Customer(**data)
        message = "Created customer successfully"
    customer.save()

    return message


def handle_uploaded_file(fl, name):
    dir = NID_DIRECTORY

    if os.path.exists(dir+name):
        os.remove(dir+name)

    try:
        with open(NID_DIRECTORY+name, "wb+") as destination:
            for chunk in fl.chunks():
                destination.write(chunk)
            destination.close()
    except Exception as ex:
        print(str(ex))
        # import pdb;pdb.set_trace()




def fill_up_form(all_data):

    import docx
    from docx.shared import Pt
    from docx.enum.style import WD_STYLE_TYPE

    doc = Document('test.docx')

    # parag = doc.add_paragraph("Hello!")

    font_styles = doc.styles
    # font_charstyle = font_styles.add_style()
    # font_charstyle = font_styles
    # font_object = font_charstyle.font
    # font_object.size = Pt(20)
    # font_object.name = 'Nirmala UI'

    # parag.add_run(data.get('b_name'), style='CommentsStyle').bold = True
    # parag.add_run("Python", style='CommentsStyle').italic = True
    # doc.save("test.docx")

    # import pdb;pdb.set_trace()
    data = all_data.get("customer")
    n_data = all_data.get("nominee")
    for paragraph in doc.paragraphs:
        if '__b_name__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__b_name__", data.get('b_name'))
        if '__e_name__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__e_name__", data.get('e_name'))
        if '__f_name__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__f_name__", data.get('f_name'))
        if '__m_name__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__m_name__", data.get('m_name'))
        if '__s_name__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__s_name__", data.get('s_name'))
        if '__dob__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__dob__", data.get('dob'))
        if '__vill__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__vill__", data.get('pre_village_road','pre_additional_village_road'))
        if '__post__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__post__", data.get('pre_post_office'))
        if '__thana__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__thana__", data.get('pre_upozila'))
        if '__dist__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__dist__", data.get('pre_district'))
        if '__pvill__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__pvill__", data.get('per_village_road','per_additional_village_road'))
        if '__ppost__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__ppost__", data.get('per_post_office'))
        if '__pthana__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__pthana__", data.get('per_upozila'))
        if '__pdist__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__pdist__", data.get('per_district'))
        if '__date__' in paragraph.text:
            paragraph.text = paragraph.text.replace("__date__", str(datetime.datetime.today()))
            # import pdb;pdb.set_trace()
    doc.save(data.get("national_id")+".docx")



def process_for_show_data(nid,nnid=None):
    customer = Customer.objects.get(national_id=nid)
    from django.forms.models import model_to_dict
    cust_dict = model_to_dict(customer)
    nom_dict ={}
    if nnid is not None:
        nominee = Customer.objects.get(national_id=nnid)
        nom_dict = model_to_dict(nominee)

    return {"customer": cust_dict, "nominee": nom_dict}
