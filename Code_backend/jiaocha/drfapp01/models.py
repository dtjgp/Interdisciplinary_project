from django.db import models

# Create your models here.
class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)

class LoginInfo(models.Model):
    user_id = models.CharField(primary_key=True,max_length=32)
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class auth_user(models.Model):
    id = models.CharField(primary_key=True,max_length=32)
    password = models.CharField(max_length=32)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class cust_cons_type_comb(models.Model):
    user_id = models.IntegerField(primary_key=True)
    timestamp0 = models.CharField(max_length=32)
    timestamp1 = models.CharField(max_length=32)
    timestamp2 = models.CharField(max_length=32)
    timestamp3 = models.CharField(max_length=32)
    timestamp4 = models.CharField(max_length=32)
    timestamp5 = models.CharField(max_length=32)
    timestamp6 = models.CharField(max_length=32)
    timestamp7 = models.CharField(max_length=32)
    timestamp8 = models.CharField(max_length=32)
    timestamp9 = models.CharField(max_length=32)
    timestamp10 = models.CharField(max_length=32)
    timestamp11 = models.CharField(max_length=32)
    timestamp12 = models.CharField(max_length=32)
    timestamp13 = models.CharField(max_length=32)
    timestamp14 = models.CharField(max_length=32)
    timestamp15 = models.CharField(max_length=32)
    timestamp16 = models.CharField(max_length=32)
    timestamp17 = models.CharField(max_length=32)
    timestamp18 = models.CharField(max_length=32)
    timestamp19 = models.CharField(max_length=32)
    timestamp20 = models.CharField(max_length=32)
    timestamp21 = models.CharField(max_length=32)
    timestamp22 = models.CharField(max_length=32)
    timestamp23 = models.CharField(max_length=32)
    timestamp24 = models.CharField(max_length=32)
    timestamp25 = models.CharField(max_length=32)
    timestamp26 = models.CharField(max_length=32)
    timestamp27 = models.CharField(max_length=32)
    timestamp28 = models.CharField(max_length=32)
    timestamp29 = models.CharField(max_length=32)
    timestamp30 = models.CharField(max_length=32)
    timestamp31 = models.CharField(max_length=32)
    timestamp32 = models.CharField(max_length=32)
    timestamp33 = models.CharField(max_length=32)
    timestamp34 = models.CharField(max_length=32)
    timestamp35 = models.CharField(max_length=32)
    timestamp36 = models.CharField(max_length=32)
    timestamp37 = models.CharField(max_length=32)
    timestamp38 = models.CharField(max_length=32)
    timestamp39 = models.CharField(max_length=32)
    timestamp40 = models.CharField(max_length=32)
    timestamp41 = models.CharField(max_length=32)
    timestamp42 = models.CharField(max_length=32)
    timestamp43 = models.CharField(max_length=32)
    timestamp44 = models.CharField(max_length=32)
    timestamp45 = models.CharField(max_length=32)
    timestamp46 = models.CharField(max_length=32)
    timestamp47 = models.CharField(max_length=32)
    customer_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = '1customer_consumption_type_combine'
        # fields = '__all__'
        # __all__ = True

class cust_cons_total(models.Model):
    user_id = models.IntegerField(primary_key=True)
    timestamp0 = models.CharField(max_length=32)
    timestamp1 = models.CharField(max_length=32)
    timestamp2 = models.CharField(max_length=32)
    timestamp3 = models.CharField(max_length=32)
    timestamp4 = models.CharField(max_length=32)
    timestamp5 = models.CharField(max_length=32)
    timestamp6 = models.CharField(max_length=32)
    timestamp7 = models.CharField(max_length=32)
    timestamp8 = models.CharField(max_length=32)
    timestamp9 = models.CharField(max_length=32)
    timestamp10 = models.CharField(max_length=32)
    timestamp11 = models.CharField(max_length=32)
    timestamp12 = models.CharField(max_length=32)
    timestamp13 = models.CharField(max_length=32)
    timestamp14 = models.CharField(max_length=32)
    timestamp15 = models.CharField(max_length=32)
    timestamp16 = models.CharField(max_length=32)
    timestamp17 = models.CharField(max_length=32)
    timestamp18 = models.CharField(max_length=32)
    timestamp19 = models.CharField(max_length=32)
    timestamp20 = models.CharField(max_length=32)
    timestamp21 = models.CharField(max_length=32)
    timestamp22 = models.CharField(max_length=32)
    timestamp23 = models.CharField(max_length=32)
    timestamp24 = models.CharField(max_length=32)
    timestamp25 = models.CharField(max_length=32)
    timestamp26 = models.CharField(max_length=32)
    timestamp27 = models.CharField(max_length=32)
    timestamp28 = models.CharField(max_length=32)
    timestamp29 = models.CharField(max_length=32)
    timestamp30 = models.CharField(max_length=32)
    timestamp31 = models.CharField(max_length=32)
    timestamp32 = models.CharField(max_length=32)
    timestamp33 = models.CharField(max_length=32)
    timestamp34 = models.CharField(max_length=32)
    timestamp35 = models.CharField(max_length=32)
    timestamp36 = models.CharField(max_length=32)
    timestamp37 = models.CharField(max_length=32)
    timestamp38 = models.CharField(max_length=32)
    timestamp39 = models.CharField(max_length=32)
    timestamp40 = models.CharField(max_length=32)
    timestamp41 = models.CharField(max_length=32)
    timestamp42 = models.CharField(max_length=32)
    timestamp43 = models.CharField(max_length=32)
    timestamp44 = models.CharField(max_length=32)
    timestamp45 = models.CharField(max_length=32)
    timestamp46 = models.CharField(max_length=32)
    timestamp47 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1customer_consumption_total'
        # fields = '__all__'
        # __all__ = True

class contract_market_num(models.Model):
    contract_id = models.IntegerField(primary_key=True)
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)
    ite_time7 = models.CharField(max_length=32)
    ite_time8 = models.CharField(max_length=32)
    ite_time9 = models.CharField(max_length=32)
    ite_time10 = models.CharField(max_length=32)
    ite_time11 = models.CharField(max_length=32)
    ite_time12 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1contract_market_number_12iterations'
        # fields = '__all__'
        # __all__ = True

class contract_market_share(models.Model):
    contract_id = models.IntegerField(primary_key=True)
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)
    ite_time7 = models.CharField(max_length=32)
    ite_time8 = models.CharField(max_length=32)
    ite_time9 = models.CharField(max_length=32)
    ite_time10 = models.CharField(max_length=32)
    ite_time11 = models.CharField(max_length=32)
    ite_time12 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1contract_market_share_12iterations'
        # fields = '__all__'
        # __all__ = True

class contract_ms_withself(models.Model):
    contract_id = models.IntegerField(primary_key=True)
    timestamp0 = models.CharField(max_length=32)
    timestamp1 = models.CharField(max_length=32)
    timestamp2 = models.CharField(max_length=32)
    timestamp3 = models.CharField(max_length=32)
    timestamp4 = models.CharField(max_length=32)
    timestamp5 = models.CharField(max_length=32)
    timestamp6 = models.CharField(max_length=32)
    timestamp7 = models.CharField(max_length=32)
    timestamp8 = models.CharField(max_length=32)
    timestamp9 = models.CharField(max_length=32)
    timestamp10 = models.CharField(max_length=32)
    timestamp11 = models.CharField(max_length=32)
    timestamp12 = models.CharField(max_length=32)
    timestamp13 = models.CharField(max_length=32)
    timestamp14 = models.CharField(max_length=32)
    timestamp15 = models.CharField(max_length=32)
    timestamp16 = models.CharField(max_length=32)
    timestamp17 = models.CharField(max_length=32)
    timestamp18 = models.CharField(max_length=32)
    timestamp19 = models.CharField(max_length=32)
    timestamp20 = models.CharField(max_length=32)
    timestamp21 = models.CharField(max_length=32)
    timestamp22 = models.CharField(max_length=32)
    timestamp23 = models.CharField(max_length=32)
    timestamp24 = models.CharField(max_length=32)
    timestamp25 = models.CharField(max_length=32)
    timestamp26 = models.CharField(max_length=32)
    timestamp27 = models.CharField(max_length=32)
    timestamp28 = models.CharField(max_length=32)
    timestamp29 = models.CharField(max_length=32)
    timestamp30 = models.CharField(max_length=32)
    timestamp31 = models.CharField(max_length=32)
    timestamp32 = models.CharField(max_length=32)
    timestamp33 = models.CharField(max_length=32)
    timestamp34 = models.CharField(max_length=32)
    timestamp35 = models.CharField(max_length=32)
    timestamp36 = models.CharField(max_length=32)
    timestamp37 = models.CharField(max_length=32)
    timestamp38 = models.CharField(max_length=32)
    timestamp39 = models.CharField(max_length=32)
    timestamp40 = models.CharField(max_length=32)
    timestamp41 = models.CharField(max_length=32)
    timestamp42 = models.CharField(max_length=32)
    timestamp43 = models.CharField(max_length=32)
    timestamp44 = models.CharField(max_length=32)
    timestamp45 = models.CharField(max_length=32)
    timestamp46 = models.CharField(max_length=32)
    timestamp47 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1contract_market_share_withself'

class contract_ms_withoutself(models.Model):
    contract_id = models.IntegerField(primary_key=True)
    timestamp0 = models.CharField(max_length=32)
    timestamp1 = models.CharField(max_length=32)
    timestamp2 = models.CharField(max_length=32)
    timestamp3 = models.CharField(max_length=32)
    timestamp4 = models.CharField(max_length=32)
    timestamp5 = models.CharField(max_length=32)
    timestamp6 = models.CharField(max_length=32)
    timestamp7 = models.CharField(max_length=32)
    timestamp8 = models.CharField(max_length=32)
    timestamp9 = models.CharField(max_length=32)
    timestamp10 = models.CharField(max_length=32)
    timestamp11 = models.CharField(max_length=32)
    timestamp12 = models.CharField(max_length=32)
    timestamp13 = models.CharField(max_length=32)
    timestamp14 = models.CharField(max_length=32)
    timestamp15 = models.CharField(max_length=32)
    timestamp16 = models.CharField(max_length=32)
    timestamp17 = models.CharField(max_length=32)
    timestamp18 = models.CharField(max_length=32)
    timestamp19 = models.CharField(max_length=32)
    timestamp20 = models.CharField(max_length=32)
    timestamp21 = models.CharField(max_length=32)
    timestamp22 = models.CharField(max_length=32)
    timestamp23 = models.CharField(max_length=32)
    timestamp24 = models.CharField(max_length=32)
    timestamp25 = models.CharField(max_length=32)
    timestamp26 = models.CharField(max_length=32)
    timestamp27 = models.CharField(max_length=32)
    timestamp28 = models.CharField(max_length=32)
    timestamp29 = models.CharField(max_length=32)
    timestamp30 = models.CharField(max_length=32)
    timestamp31 = models.CharField(max_length=32)
    timestamp32 = models.CharField(max_length=32)
    timestamp33 = models.CharField(max_length=32)
    timestamp34 = models.CharField(max_length=32)
    timestamp35 = models.CharField(max_length=32)
    timestamp36 = models.CharField(max_length=32)
    timestamp37 = models.CharField(max_length=32)
    timestamp38 = models.CharField(max_length=32)
    timestamp39 = models.CharField(max_length=32)
    timestamp40 = models.CharField(max_length=32)
    timestamp41 = models.CharField(max_length=32)
    timestamp42 = models.CharField(max_length=32)
    timestamp43 = models.CharField(max_length=32)
    timestamp44 = models.CharField(max_length=32)
    timestamp45 = models.CharField(max_length=32)
    timestamp46 = models.CharField(max_length=32)
    timestamp47 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1contract_market_share_withoutself'

class profit_withself(models.Model):
    contract_id = models.IntegerField(primary_key=True)
    timestamp0 = models.CharField(max_length=32)
    timestamp1 = models.CharField(max_length=32)
    timestamp2 = models.CharField(max_length=32)
    timestamp3 = models.CharField(max_length=32)
    timestamp4 = models.CharField(max_length=32)
    timestamp5 = models.CharField(max_length=32)
    timestamp6 = models.CharField(max_length=32)
    timestamp7 = models.CharField(max_length=32)
    timestamp8 = models.CharField(max_length=32)
    timestamp9 = models.CharField(max_length=32)
    timestamp10 = models.CharField(max_length=32)
    timestamp11 = models.CharField(max_length=32)
    timestamp12 = models.CharField(max_length=32)
    timestamp13 = models.CharField(max_length=32)
    timestamp14 = models.CharField(max_length=32)
    timestamp15 = models.CharField(max_length=32)
    timestamp16 = models.CharField(max_length=32)
    timestamp17 = models.CharField(max_length=32)
    timestamp18 = models.CharField(max_length=32)
    timestamp19 = models.CharField(max_length=32)
    timestamp20 = models.CharField(max_length=32)
    timestamp21 = models.CharField(max_length=32)
    timestamp22 = models.CharField(max_length=32)
    timestamp23 = models.CharField(max_length=32)
    timestamp24 = models.CharField(max_length=32)
    timestamp25 = models.CharField(max_length=32)
    timestamp26 = models.CharField(max_length=32)
    timestamp27 = models.CharField(max_length=32)
    timestamp28 = models.CharField(max_length=32)
    timestamp29 = models.CharField(max_length=32)
    timestamp30 = models.CharField(max_length=32)
    timestamp31 = models.CharField(max_length=32)
    timestamp32 = models.CharField(max_length=32)
    timestamp33 = models.CharField(max_length=32)
    timestamp34 = models.CharField(max_length=32)
    timestamp35 = models.CharField(max_length=32)
    timestamp36 = models.CharField(max_length=32)
    timestamp37 = models.CharField(max_length=32)
    timestamp38 = models.CharField(max_length=32)
    timestamp39 = models.CharField(max_length=32)
    timestamp40 = models.CharField(max_length=32)
    timestamp41 = models.CharField(max_length=32)
    timestamp42 = models.CharField(max_length=32)
    timestamp43 = models.CharField(max_length=32)
    timestamp44 = models.CharField(max_length=32)
    timestamp45 = models.CharField(max_length=32)
    timestamp46 = models.CharField(max_length=32)
    timestamp47 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1profit_list_withself'

class profit_withoutself(models.Model):
    contract_id = models.IntegerField(primary_key=True)
    timestamp0 = models.CharField(max_length=32)
    timestamp1 = models.CharField(max_length=32)
    timestamp2 = models.CharField(max_length=32)
    timestamp3 = models.CharField(max_length=32)
    timestamp4 = models.CharField(max_length=32)
    timestamp5 = models.CharField(max_length=32)
    timestamp6 = models.CharField(max_length=32)
    timestamp7 = models.CharField(max_length=32)
    timestamp8 = models.CharField(max_length=32)
    timestamp9 = models.CharField(max_length=32)
    timestamp10 = models.CharField(max_length=32)
    timestamp11 = models.CharField(max_length=32)
    timestamp12 = models.CharField(max_length=32)
    timestamp13 = models.CharField(max_length=32)
    timestamp14 = models.CharField(max_length=32)
    timestamp15 = models.CharField(max_length=32)
    timestamp16 = models.CharField(max_length=32)
    timestamp17 = models.CharField(max_length=32)
    timestamp18 = models.CharField(max_length=32)
    timestamp19 = models.CharField(max_length=32)
    timestamp20 = models.CharField(max_length=32)
    timestamp21 = models.CharField(max_length=32)
    timestamp22 = models.CharField(max_length=32)
    timestamp23 = models.CharField(max_length=32)
    timestamp24 = models.CharField(max_length=32)
    timestamp25 = models.CharField(max_length=32)
    timestamp26 = models.CharField(max_length=32)
    timestamp27 = models.CharField(max_length=32)
    timestamp28 = models.CharField(max_length=32)
    timestamp29 = models.CharField(max_length=32)
    timestamp30 = models.CharField(max_length=32)
    timestamp31 = models.CharField(max_length=32)
    timestamp32 = models.CharField(max_length=32)
    timestamp33 = models.CharField(max_length=32)
    timestamp34 = models.CharField(max_length=32)
    timestamp35 = models.CharField(max_length=32)
    timestamp36 = models.CharField(max_length=32)
    timestamp37 = models.CharField(max_length=32)
    timestamp38 = models.CharField(max_length=32)
    timestamp39 = models.CharField(max_length=32)
    timestamp40 = models.CharField(max_length=32)
    timestamp41 = models.CharField(max_length=32)
    timestamp42 = models.CharField(max_length=32)
    timestamp43 = models.CharField(max_length=32)
    timestamp44 = models.CharField(max_length=32)
    timestamp45 = models.CharField(max_length=32)
    timestamp46 = models.CharField(max_length=32)
    timestamp47 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1profit_list_withoutself'

class contract1_usertype_share(models.Model):
    user_type = models.IntegerField(primary_key=True)
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)
    ite_time7 = models.CharField(max_length=32)
    ite_time8 = models.CharField(max_length=32)
    ite_time9 = models.CharField(max_length=32)
    ite_time10 = models.CharField(max_length=32)
    ite_time11 = models.CharField(max_length=32)
    ite_time12 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1contract1_usertype_share'

class contract2_usertype_share(models.Model):
    user_type = models.IntegerField(primary_key=True)
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)
    ite_time7 = models.CharField(max_length=32)
    ite_time8 = models.CharField(max_length=32)
    ite_time9 = models.CharField(max_length=32)
    ite_time10 = models.CharField(max_length=32)
    ite_time11 = models.CharField(max_length=32)
    ite_time12 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1contract2_usertype_share'

class contract3_usertype_share(models.Model):
    user_type = models.IntegerField(primary_key=True)
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)
    ite_time7 = models.CharField(max_length=32)
    ite_time8 = models.CharField(max_length=32)
    ite_time9 = models.CharField(max_length=32)
    ite_time10 = models.CharField(max_length=32)
    ite_time11 = models.CharField(max_length=32)
    ite_time12 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1contract3_usertype_share'

class contract4_usertype_share(models.Model):
    user_type = models.IntegerField(primary_key=True)
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)
    ite_time7 = models.CharField(max_length=32)
    ite_time8 = models.CharField(max_length=32)
    ite_time9 = models.CharField(max_length=32)
    ite_time10 = models.CharField(max_length=32)
    ite_time11 = models.CharField(max_length=32)
    ite_time12 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1contract4_usertype_share'

class contract5_usertype_share(models.Model):
    user_type = models.IntegerField(primary_key=True)
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)
    ite_time7 = models.CharField(max_length=32)
    ite_time8 = models.CharField(max_length=32)
    ite_time9 = models.CharField(max_length=32)
    ite_time10 = models.CharField(max_length=32)
    ite_time11 = models.CharField(max_length=32)
    ite_time12 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1contract5_usertype_share'

class specific_c1_number(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.IntegerField()
    F2 = models.IntegerField()
    F3 = models.IntegerField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1specific_contract1_number'   

class specific_c2_number(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.IntegerField()
    F2 = models.IntegerField()
    F3 = models.IntegerField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1specific_contract2_number'

class specific_c3_number(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.IntegerField()
    F2 = models.IntegerField()
    F3 = models.IntegerField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1specific_contract3_number'

class specific_c4_number(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.IntegerField()
    F2 = models.IntegerField()
    F3 = models.IntegerField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1specific_contract4_number'

class specific_c5_number(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.IntegerField()
    F2 = models.IntegerField()
    F3 = models.IntegerField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1specific_contract5_number'

class specific_c1_profit(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.FloatField()
    F2 = models.FloatField()
    F3 = models.FloatField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1specific_contract1_profit'

class specific_c2_profit(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.FloatField()
    F2 = models.FloatField()
    F3 = models.FloatField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1specific_contract2_profit'

class specific_c3_profit(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.FloatField()
    F2 = models.FloatField()
    F3 = models.FloatField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1specific_contract3_profit'

class specific_c4_profit(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.FloatField()
    F2 = models.FloatField()
    F3 = models.FloatField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)
    
    class Meta:
        managed = False
        db_table = '1specific_contract4_profit'

class specific_c5_profit(models.Model):
    dynamic_set_num = models.IntegerField(primary_key=True)
    F1 = models.FloatField()
    F2 = models.FloatField()
    F3 = models.FloatField()
    ite_time1 = models.CharField(max_length=32)
    ite_time2 = models.CharField(max_length=32)
    ite_time3 = models.CharField(max_length=32)
    ite_time4 = models.CharField(max_length=32)
    ite_time5 = models.CharField(max_length=32)
    ite_time6 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = '1specific_contract5_profit'

class test_test(models.Model):
    month = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=32)
    user_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test_data'