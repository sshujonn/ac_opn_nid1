from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Customer(models.Model):
    class OccupationChoices(models.TextChoices):
        Farmer = 'FAR', _('কৃষক')

    b_name = models.TextField(max_length=100, blank=True)
    e_name = models.TextField(max_length=100, blank=True)
    dob = models.TextField(max_length=100, blank=True)
    f_name = models.TextField(max_length=100, blank=True)
    m_name = models.TextField(max_length=100, blank=True)
    s_name = models.TextField(max_length=100, blank=True)
    occupation = models.CharField(max_length=6, choices=OccupationChoices.choices, default='')
    occupation_nid = models.TextField(max_length=100, blank=True)
    pre_division = models.TextField(max_length=100, blank=True)
    pre_district = models.TextField(max_length=100, blank=True)
    pre_rmo = models.TextField(max_length=100, blank=True)
    pre_citycorp = models.TextField(max_length=100, blank=True)
    pre_upozila = models.TextField(max_length=100, blank=True)
    pre_union_ward = models.TextField(max_length=100, blank=True)
    pre_mouza_moholla = models.TextField(max_length=100, blank=True)
    pre_additional_mouza_moholla = models.TextField(max_length=100, blank=True)
    pre_ward_for_union_porishod = models.TextField(max_length=100, blank=True)
    pre_village_road = models.TextField(max_length=100, blank=True)
    pre_additional_village_road = models.TextField(max_length=100, blank=True)
    pre_home_holding_no = models.TextField(max_length=100, blank=True)
    pre_post_office = models.TextField(max_length=100, blank=True)
    pre_postal_code = models.TextField(max_length=100, blank=True)
    pre_region = models.TextField(max_length=100, blank=True)
    per_division = models.TextField(max_length=100, blank=True)
    per_district = models.TextField(max_length=100, blank=True)
    per_rmo = models.TextField(max_length=100, blank=True)
    per_city_corporation_or_municipality = models.TextField(max_length=100, blank=True)
    per_upozila = models.TextField(max_length=100, blank=True)
    per_union_ward = models.TextField(max_length=100, blank=True)
    per_mouza_moholla = models.TextField(max_length=100, blank=True)
    per_additional_mouza_moholla = models.TextField(max_length=100, blank=True)
    per_ward_for_union_porishod = models.TextField(max_length=100, blank=True)
    per_village_road = models.TextField(max_length=100, blank=True)
    per_additional_village_road = models.TextField(max_length=100, blank=True)
    per_home_holding_no = models.TextField(max_length=100, blank=True)
    per_post_office = models.TextField(max_length=100, blank=True)
    per_postal_code = models.TextField(max_length=100, blank=True)
    per_region = models.TextField(max_length=100, blank=True)
    blood_group = models.TextField(max_length=100, blank=True)
    national_id = models.TextField(max_length=100, blank=True)
    pin = models.TextField(max_length=100, blank=True)
    nationality = models.TextField(max_length=100, blank=True)
    income = models.TextField(max_length=100, blank=True)
    source = models.TextField(max_length=500, blank=True)
    tp_depo_cash_txn = models.TextField(max_length=3, blank=True)
    tp_depo_cash_txn_amt = models.TextField(max_length=500, blank=True)
    tp_depo_trans_txn = models.TextField(max_length=3, blank=True)
    tp_depo_trans_txn_amt = models.TextField(max_length=500, blank=True)
    tp_wd_cash_txn = models.TextField(max_length=3, blank=True)
    tp_wd_cash_txn_amt = models.TextField(max_length=500, blank=True)
    tp_wd_trans_txn = models.TextField(max_length=3, blank=True)
    tp_wd_trans_txn_amt = models.TextField(max_length=500, blank=True)




# Create your models here.
class Account(models.Model):
    e_name = models.TextField(max_length=100, blank=True)
    b_name = models.TextField(max_length=100, blank=True)
    ac_number = models.TextField(max_length=100, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    nominee = models.TextField(max_length=100, blank=True)
    init_depo = models.TextField(max_length=100, blank=True)
    init_depo_word = models.TextField(max_length=100, blank=True)


class SporceOfIncome(models.Model):
    name = models.TextField(max_length=1000, blank=True)