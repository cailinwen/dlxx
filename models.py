# -*- coding: utf-8 -*-
#import codecs
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.forms import ModelForm
from django.db import models

class AdImg(models.Model):
    ad_img_id = models.BigIntegerField(db_column='AD_IMG_ID', primary_key=True)  # Field name made lowercase.
    ad_img_type = models.BigIntegerField(db_column='AD_IMG_TYPE', blank=True, null=True)  # Field name made lowercase.
    ad_img_name = models.CharField(db_column='AD_IMG_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ad_img_path = models.CharField(db_column='AD_IMG_PATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ad_img_url = models.CharField(db_column='AD_IMG_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ad_img_remark = models.CharField(db_column='AD_IMG_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ad_img_stat = models.BigIntegerField(db_column='AD_IMG_STAT', blank=True, null=True)  # Field name made lowercase.
    ad_img_create_user_id = models.BigIntegerField(db_column='AD_IMG_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    ad_img_create_time = models.DateTimeField(db_column='AD_IMG_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    ad_img_modify_user_id = models.BigIntegerField(db_column='AD_IMG_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    ad_img_modify_time = models.DateTimeField(db_column='AD_IMG_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ad_img_rec'


class Address(models.Model):
    address_id = models.BigIntegerField(db_column='ADDRESS_ID', primary_key=True)  # Field name made lowercase.
    address_member = models.ForeignKey('Member', db_column='ADDRESS_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    address_parea_id = models.BigIntegerField(db_column='ADDRESS_PAREA_ID', blank=True, null=True)  # Field name made lowercase.
    address_carea_id = models.BigIntegerField(db_column='ADDRESS_CAREA_ID', blank=True, null=True)  # Field name made lowercase.
    address_rarea_id = models.BigIntegerField(db_column='ADDRESS_RAREA_ID', blank=True, null=True)  # Field name made lowercase.
    address_no = models.CharField(db_column='ADDRESS_NO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    address_user = models.CharField(db_column='ADDRESS_USER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address_mobile = models.CharField(db_column='ADDRESS_MOBILE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address_post = models.CharField(db_column='ADDRESS_POST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address_type = models.IntegerField(db_column='ADDRESS_TYPE', blank=True, null=True)  # Field name made lowercase.
    address_create_member_id = models.BigIntegerField(db_column='ADDRESS_CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    address_create_time = models.DateTimeField(db_column='ADDRESS_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    address_modify_member_id = models.BigIntegerField(db_column='ADDRESS_MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    address_modify_time = models.DateTimeField(db_column='ADDRESS_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    address_user_cid = models.CharField(db_column='ADDRESS_USER_CID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'address_rec'


class Adtmn(models.Model):
    adtmn_id = models.BigIntegerField(db_column='ADTMN_ID', primary_key=True)  # Field name made lowercase.
    adtmn_tmn_id = models.BigIntegerField(db_column='ADTMN_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    adtmn_store = models.ForeignKey('Store', db_column='ADTMN_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    adtmn_member = models.ForeignKey('Member', db_column='ADTMN_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    adtmn_ad_id = models.BigIntegerField(db_column='ADTMN_AD_ID', blank=True, null=True)  # Field name made lowercase.
    adtmn_sort = models.SmallIntegerField(db_column='ADTMN_SORT', blank=True, null=True)  # Field name made lowercase.
    adtmn_create_member_id = models.BigIntegerField(db_column='ADTMN_CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    adtmn_create_time = models.DateTimeField(db_column='ADTMN_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    adtmn_modify_member_id = models.BigIntegerField(db_column='ADTMN_MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    adtmn_modify_time = models.DateTimeField(db_column='ADTMN_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'adtmn_rec'


class Append(models.Model):
    append_id = models.BigIntegerField(db_column='APPEND_ID', primary_key=True)  # Field name made lowercase.
    append_msg = models.ForeignKey('Msg', db_column='APPEND_MSG_ID', blank=True, null=True)  # Field name made lowercase.
    append_url = models.CharField(db_column='APPEND_URL', max_length=512, blank=True, null=True)  # Field name made lowercase.
    append_file_name = models.CharField(db_column='APPEND_FILE_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    append_file_fix = models.CharField(db_column='APPEND_FILE_FIX', max_length=20, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'append_rec'


class Area(models.Model):
    area_id = models.BigIntegerField(db_column='AREA_ID', primary_key=True)  # Field name made lowercase.
    area_code = models.CharField(db_column='AREA_CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    area_name = models.CharField(db_column='AREA_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    area_parent_id = models.BigIntegerField(db_column='AREA_PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    area_laycount = models.IntegerField(db_column='AREA_LAYCOUNT', blank=True, null=True)  # Field name made lowercase.
    area_sortstep = models.BigIntegerField(db_column='AREA_SORTSTEP', blank=True, null=True)  # Field name made lowercase.
    area_remark = models.CharField(db_column='AREA_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    area_create_user_id = models.BigIntegerField(db_column='AREA_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    area_create_time = models.DateTimeField(db_column='AREA_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    area_modify_user_id = models.BigIntegerField(db_column='AREA_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    area_modify_time = models.DateTimeField(db_column='AREA_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'area_rec'


class Brand(models.Model):
    brand_id = models.BigIntegerField(db_column='BRAND_ID', primary_key=True)  # Field name made lowercase.
    brand_code = models.CharField(db_column='BRAND_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    brand_name = models.CharField(db_column='BRAND_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    brand_url = models.CharField(db_column='BRAND_URL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    brand_create_user_id = models.BigIntegerField(db_column='BRAND_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    brand_create_time = models.DateTimeField(db_column='BRAND_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    brand_modify_user_id = models.BigIntegerField(db_column='BRAND_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    brand_modify_time = models.DateTimeField(db_column='BRAND_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    brand_remark = models.CharField(db_column='BRAND_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'brand_rec'


class Cart(models.Model):
    cart_id = models.BigIntegerField(db_column='CART_ID', primary_key=True)  # Field name made lowercase.
    cart_tmn_id = models.BigIntegerField(db_column='CART_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    cart_member = models.ForeignKey('Member', db_column='CART_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    cart_le_id = models.BigIntegerField(db_column='CART_LE_ID', blank=True, null=True)  # Field name made lowercase.
    cart_qty = models.DecimalField(db_column='CART_QTY', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cart_remark = models.CharField(db_column='CART_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cart_create_member_id = models.BigIntegerField(db_column='CART_CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    cart_create_time = models.DateTimeField(db_column='CART_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    cart_modify_member_id = models.BigIntegerField(db_column='CART_MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    cart_modify_time = models.DateTimeField(db_column='CART_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'cart_rec'


class CashItem(models.Model):
    cash_item_id = models.BigIntegerField(db_column='CASH_ITEM_ID', primary_key=True)  # Field name made lowercase.
    cash_item_cash = models.ForeignKey('Cash', db_column='CASH_ITEM_CASH_ID', blank=True, null=True)  # Field name made lowercase.
    cash_itme_sod_income = models.ForeignKey('SodIncome', db_column='CASH_ITME_SOD_INCOME_ID', blank=True, null=True)  # Field name made lowercase.
    cash_item_user = models.ForeignKey('User', db_column='CASH_ITEM_USER_ID', blank=True, null=True)  # Field name made lowercase.
    cash_item_date = models.DateTimeField(db_column='CASH_ITEM_DATE', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'cash_item_rec'


class Cash(models.Model):
    cash_id = models.BigIntegerField(db_column='CASH_ID', primary_key=True)  # Field name made lowercase.
    cash_member = models.ForeignKey('Member', db_column='CASH_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    cash_date = models.DateTimeField(db_column='CASH_DATE', blank=True, null=True)  # Field name made lowercase.
    cash_apply_amt = models.DecimalField(db_column='CASH_APPLY_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cash_account_type = models.IntegerField(db_column='CASH_ACCOUNT_TYPE', blank=True, null=True)  # Field name made lowercase.
    cash_brank = models.CharField(db_column='CASH_BRANK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cash_account_no = models.CharField(db_column='CASH_ACCOUNT_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cash_account_name = models.CharField(db_column='CASH_ACCOUNT_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cash_stat = models.IntegerField(db_column='CASH_STAT', blank=True, null=True)  # Field name made lowercase.
    cash_check_user = models.ForeignKey('User', db_column='CASH_CHECK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    cash_check_date = models.DateTimeField(db_column='CASH_CHECK_DATE', blank=True, null=True)  # Field name made lowercase.
    cash_check_amt = models.DecimalField(db_column='CASH_CHECK_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'cash_rec'


class Color(models.Model):
    color_id = models.BigIntegerField(db_column='COLOR_ID', primary_key=True)  # Field name made lowercase.
    color_code = models.CharField(db_column='COLOR_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    color_name = models.CharField(db_column='COLOR_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    color_stat = models.BigIntegerField(db_column='COLOR_STAT', blank=True, null=True)  # Field name made lowercase.
    color_create_user_id = models.BigIntegerField(db_column='COLOR_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    color_create_time = models.DateTimeField(db_column='COLOR_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    color_modify_user_id = models.BigIntegerField(db_column='COLOR_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    color_modify_time = models.DateTimeField(db_column='COLOR_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'color_rec'


class Company(models.Model):
    company_id = models.BigIntegerField(db_column='COMPANY_ID', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='COMPANY_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_short_name = models.CharField(db_column='COMPANY_SHORT_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_full_name = models.CharField(db_column='COMPANY_FULL_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    company_contacts = models.CharField(db_column='COMPANY_CONTACTS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_tel = models.CharField(db_column='COMPANY_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_mobil = models.CharField(db_column='COMPANY_MOBIL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_email = models.CharField(db_column='COMPANY_EMAIL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    company_addr = models.CharField(db_column='COMPANY_ADDR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_home_page = models.CharField(db_column='COMPANY_HOME_PAGE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    company_logo_pic = models.CharField(db_column='COMPANY_LOGO_PIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_fmon = models.CharField(db_column='COMPANY_FMON', max_length=6, blank=True, null=True)  # Field name made lowercase.
    company_gl_fmon = models.CharField(db_column='COMPANY_GL_FMON', max_length=6, blank=True, null=True)  # Field name made lowercase.
    company_currency_id = models.BigIntegerField(db_column='COMPANY_CURRENCY_ID', blank=True, null=True)  # Field name made lowercase.
    company_c_fmon = models.CharField(db_column='COMPANY_C_FMON', max_length=6, blank=True, null=True)  # Field name made lowercase.
    company_remark = models.CharField(db_column='COMPANY_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_create_user_id = models.BigIntegerField(db_column='COMPANY_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    company_create_time = models.DateTimeField(db_column='COMPANY_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    company_modify_user_id = models.BigIntegerField(db_column='COMPANY_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    company_modify_time = models.DateTimeField(db_column='COMPANY_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'company_rec'


class Country(models.Model):
    country_id = models.BigIntegerField(db_column='COUNTRY_ID', primary_key=True)  # Field name made lowercase.
    country_code = models.CharField(db_column='COUNTRY_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    country_name = models.CharField(db_column='COUNTRY_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    country_stat = models.SmallIntegerField(db_column='COUNTRY_STAT', blank=True, null=True)  # Field name made lowercase.
    country_create_user_id = models.BigIntegerField(db_column='COUNTRY_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    country_create_time = models.DateTimeField(db_column='COUNTRY_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    country_modify_user_id = models.BigIntegerField(db_column='COUNTRY_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    country_modify_time = models.DateTimeField(db_column='COUNTRY_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'country_rec'


class Department(models.Model):
    department_id = models.BigIntegerField(db_column='DEPARTMENT_ID', primary_key=True)  # Field name made lowercase.
    department_code = models.CharField(db_column='DEPARTMENT_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    department_name = models.CharField(db_column='DEPARTMENT_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    department_parent_id = models.BigIntegerField(db_column='DEPARTMENT_PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    department_laycount = models.SmallIntegerField(db_column='DEPARTMENT_LAYCOUNT', blank=True, null=True)  # Field name made lowercase.
    department_sort_step = models.SmallIntegerField(db_column='DEPARTMENT_SORT_STEP', blank=True, null=True)  # Field name made lowercase.
    department_remark = models.CharField(db_column='DEPARTMENT_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    department_company = models.ForeignKey(Company, db_column='DEPARTMENT_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    department_create_user_id = models.BigIntegerField(db_column='DEPARTMENT_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    department_create_time = models.DateTimeField(db_column='DEPARTMENT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    department_modify_user_id = models.BigIntegerField(db_column='DEPARTMENT_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    department_modify_time = models.DateTimeField(db_column='DEPARTMENT_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'department_rec'


class DimSumIncome(models.Model):
    summary_income_id = models.BigIntegerField(db_column='SUMMARY_INCOME_ID', primary_key=True)  # Field name made lowercase.
    summary_income_member_id = models.BigIntegerField(db_column='SUMMARY_INCOME_MEMBER_ID')  # Field name made lowercase.
    summary_income_type = models.IntegerField(db_column='SUMMARY_INCOME_TYPE')  # Field name made lowercase.
    summary_income_sum = models.DecimalField(db_column='SUMMARY_INCOME_SUM', max_digits=12, decimal_places=2)  # Field name made lowercase.
    summary_income_tmn_id = models.BigIntegerField(db_column='SUMMARY_INCOME_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    summary_income_tmn_type = models.IntegerField(db_column='SUMMARY_INCOME_TMN_TYPE', blank=True, null=True)  # Field name made lowercase.
    summary_income_date = models.DateField(db_column='SUMMARY_INCOME_DATE')  # Field name made lowercase.
    summary_income_created = models.DateTimeField(db_column='SUMMARY_INCOME_CREATED')  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'dim_sum_income'


class DocGen(models.Model):
    doc_gen_id = models.BigIntegerField(db_column='DOC_GEN_ID', primary_key=True)  # Field name made lowercase.
    doc_gen_code = models.CharField(db_column='DOC_GEN_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doc_gen_method = models.SmallIntegerField(db_column='DOC_GEN_METHOD', blank=True, null=True)  # Field name made lowercase.
    doc_gen_type = models.SmallIntegerField(db_column='DOC_GEN_TYPE', blank=True, null=True)  # Field name made lowercase.
    doc_gen_doc_len = models.SmallIntegerField(db_column='DOC_GEN_DOC_LEN', blank=True, null=True)  # Field name made lowercase.
    doc_gen_tag = models.CharField(db_column='DOC_GEN_TAG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    doc_gen_reuse_flg = models.SmallIntegerField(db_column='DOC_GEN_REUSE_FLG', blank=True, null=True)  # Field name made lowercase.
    doc_gen_number_len = models.SmallIntegerField(db_column='DOC_GEN_NUMBER_LEN', blank=True, null=True)  # Field name made lowercase.
    doc_gen_max_no = models.SmallIntegerField(db_column='DOC_GEN_MAX_NO', blank=True, null=True)  # Field name made lowercase.
    doc_gen_fix_part = models.CharField(db_column='DOC_GEN_FIX_PART', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doc_gen_company_id = models.BigIntegerField(db_column='DOC_GEN_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    doc_gen_create_user_id = models.BigIntegerField(db_column='DOC_GEN_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    doc_gen_create_time = models.DateTimeField(db_column='DOC_GEN_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    doc_gen_modify_user_id = models.BigIntegerField(db_column='DOC_GEN_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    doc_gen_modify_time = models.DateTimeField(db_column='DOC_GEN_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'doc_gen_rec'


class DocLinkGen(models.Model):
    doc_link_gen_id = models.BigIntegerField(db_column='DOC_LINK_GEN_ID', primary_key=True)  # Field name made lowercase.
    doc_link_gen_type = models.SmallIntegerField(db_column='DOC_LINK_GEN_TYPE', blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_doct = models.ForeignKey('Doct', db_column='DOC_LINK_GEN_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_f_doct = models.ForeignKey('Doct', db_column='DOC_LINK_GEN_F_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_s_doc_link_gen = models.ForeignKey('SysDocLinkGen', db_column='DOC_LINK_GEN_S_DOC_LINK_GEN_ID', blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_out_put_expr = models.CharField(db_column='DOC_LINK_GEN_OUT_PUT_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_from_expr = models.CharField(db_column='DOC_LINK_GEN_FROM_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_where_expr = models.CharField(db_column='DOC_LINK_GEN_WHERE_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_fix_where = models.CharField(db_column='DOC_LINK_GEN_FIX_WHERE', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_order_expr = models.CharField(db_column='DOC_LINK_GEN_ORDER_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_company_id = models.BigIntegerField(db_column='DOC_LINK_GEN_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_create_u_id = models.BigIntegerField(db_column='DOC_LINK_GEN_CREATE_U_ID', blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_create_time = models.DateTimeField(db_column='DOC_LINK_GEN_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_modify_u_id = models.BigIntegerField(db_column='DOC_LINK_GEN_MODIFY_U_ID', blank=True, null=True)  # Field name made lowercase.
    doc_link_gen_modify_time = models.DateTimeField(db_column='DOC_LINK_GEN_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'doc_link_gen_rec'


class DocMsg(models.Model):
    doc_msg_id = models.BigIntegerField(db_column='DOC_MSG_ID', primary_key=True)  # Field name made lowercase.
    doc_msg_msg = models.ForeignKey('Msg', db_column='DOC_MSG_MSG_ID', blank=True, null=True)  # Field name made lowercase.
    doc_msg_from_flg = models.SmallIntegerField(db_column='DOC_MSG_FROM_FLG', blank=True, null=True)  # Field name made lowercase.
    doc_msg_from_doc_id = models.BigIntegerField(db_column='DOC_MSG_FROM_DOC_ID', blank=True, null=True)  # Field name made lowercase.
    doc_msg_from_doct_id = models.BigIntegerField(db_column='DOC_MSG_FROM_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    doc_msg_sys_menu_id = models.BigIntegerField(db_column='DOC_MSG_SYS_MENU_ID', blank=True, null=True)  # Field name made lowercase.
    doc_msg_view_path = models.CharField(db_column='DOC_MSG_VIEW_PATH', max_length=500, blank=True, null=True)  # Field name made lowercase.
    doc_msg_input_seq = models.CharField(db_column='DOC_MSG_INPUT_SEQ', max_length=500, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'doc_msg_rec'


class DocStat(models.Model):
    doc_stat_id = models.BigIntegerField(db_column='DOC_STAT_ID', primary_key=True)  # Field name made lowercase.
    doc_stat_doct_id = models.BigIntegerField(db_column='DOC_STAT_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    doc_stat_doc_id = models.BigIntegerField(db_column='DOC_STAT_DOC_ID', blank=True, null=True)  # Field name made lowercase.
    doc_stat_check_val = models.SmallIntegerField(db_column='DOC_STAT_CHECK_VAL', blank=True, null=True)  # Field name made lowercase.
    doc_stat_post_val = models.SmallIntegerField(db_column='DOC_STAT_POST_VAL', blank=True, null=True)  # Field name made lowercase.
    doc_stat_post_user_id = models.BigIntegerField(db_column='DOC_STAT_POST_USER_ID', blank=True, null=True)  # Field name made lowercase.
    doc_stat_post_time = models.DateTimeField(db_column='DOC_STAT_POST_TIME', blank=True, null=True)  # Field name made lowercase.
    doc_stat_check_user_id = models.BigIntegerField(db_column='DOC_STAT_CHECK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    doc_stat_check_time = models.DateTimeField(db_column='DOC_STAT_CHECK_TIME', blank=True, null=True)  # Field name made lowercase.
    doc_stat_check_desc = models.CharField(db_column='DOC_STAT_CHECK_DESC', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    doc_stat_next_check_val = models.SmallIntegerField(db_column='DOC_STAT_NEXT_CHECK_VAL', blank=True, null=True)  # Field name made lowercase.
    doc_stat_next_check_user_id = models.BigIntegerField(db_column='DOC_STAT_NEXT_CHECK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    doc_stat_next_check_time = models.DateTimeField(db_column='DOC_STAT_NEXT_CHECK_TIME', blank=True, null=True)  # Field name made lowercase.
    doc_stat_fmon = models.CharField(db_column='DOC_STAT_FMON', max_length=6, blank=True, null=True)  # Field name made lowercase.
    doc_stat_company_id = models.BigIntegerField(db_column='DOC_STAT_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    doc_stat_create_user_id = models.BigIntegerField(db_column='DOC_STAT_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    doc_stat_create_time = models.DateTimeField(db_column='DOC_STAT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    doc_stat_modify_user_id = models.BigIntegerField(db_column='DOC_STAT_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    doc_stat_modify_time = models.DateTimeField(db_column='DOC_STAT_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'doc_stat_rec'


class Docflow(models.Model):
    docflow_id = models.BigIntegerField(db_column='DOCFLOW_ID', primary_key=True)  # Field name made lowercase.
    docflow_doct_id = models.BigIntegerField(db_column='DOCFLOW_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    docflow_doc_id = models.BigIntegerField(db_column='DOCFLOW_DOC_ID', blank=True, null=True)  # Field name made lowercase.
    docflow_flow = models.ForeignKey('Flow', db_column='DOCFLOW_FLOW_ID', blank=True, null=True)  # Field name made lowercase.
    docflow_seq = models.SmallIntegerField(db_column='DOCFLOW_SEQ', blank=True, null=True)  # Field name made lowercase.
    docflow_code = models.CharField(db_column='DOCFLOW_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    docflow_name = models.CharField(db_column='DOCFLOW_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    docflow_cancel_flg = models.SmallIntegerField(db_column='DOCFLOW_CANCEL_FLG', blank=True, null=True)  # Field name made lowercase.
    docflow_chg_flg = models.SmallIntegerField(db_column='DOCFLOW_CHG_FLG', blank=True, null=True)  # Field name made lowercase.
    docflow_role = models.ForeignKey('SysRole', db_column='DOCFLOW_ROLE_ID', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'docflow_rec'


class DoctLink(models.Model):
    doct_link_id = models.BigIntegerField(db_column='DOCT_LINK_ID', primary_key=True)  # Field name made lowercase.
    doct_link_doct = models.ForeignKey('Doct', db_column='DOCT_LINK_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    doct_link_from_doct = models.ForeignKey('Doct', db_column='DOCT_LINK_FROM_DOCT_ID', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'doct_link_rec'


class Doct(models.Model):
    doct_id = models.BigIntegerField(db_column='DOCT_ID', primary_key=True)  # Field name made lowercase.
    doct_sys_doct = models.ForeignKey('SysDoct', db_column='DOCT_SYS_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    doct_sys_menu_id = models.BigIntegerField(db_column='DOCT_SYS_MENU_ID', blank=True, null=True)  # Field name made lowercase.
    doct_from_flg = models.SmallIntegerField(db_column='DOCT_FROM_FLG', blank=True, null=True)  # Field name made lowercase.
    doct_name = models.CharField(db_column='DOCT_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doct_gen_flg = models.SmallIntegerField(db_column='DOCT_GEN_FLG', blank=True, null=True)  # Field name made lowercase.
    doct_doc_gen = models.ForeignKey(DocGen, db_column='DOCT_DOC_GEN_ID', blank=True, null=True)  # Field name made lowercase.
    doct_bu_flg = models.SmallIntegerField(db_column='DOCT_BU_FLG', blank=True, null=True)  # Field name made lowercase.
    doct_remark = models.CharField(db_column='DOCT_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doct_company_id = models.BigIntegerField(db_column='DOCT_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    doct_create_user_id = models.BigIntegerField(db_column='DOCT_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    doct_create_time = models.DateTimeField(db_column='DOCT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    doct_modify_user_id = models.BigIntegerField(db_column='DOCT_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    doct_modify_time = models.DateTimeField(db_column='DOCT_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'doct_rec'


class Docth(models.Model):
    docth_id = models.BigIntegerField(db_column='DOCTH_ID', primary_key=True)  # Field name made lowercase.
    docth_doct_id = models.BigIntegerField(db_column='DOCTH_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    docth_doc_id = models.BigIntegerField(db_column='DOCTH_DOC_ID', blank=True, null=True)  # Field name made lowercase.
    docth_from_check_val = models.SmallIntegerField(db_column='DOCTH_FROM_CHECK_VAL', blank=True, null=True)  # Field name made lowercase.
    docth_from_check_user_id = models.BigIntegerField(db_column='DOCTH_FROM_CHECK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    docth_from_check_time = models.DateTimeField(db_column='DOCTH_FROM_CHECK_TIME', blank=True, null=True)  # Field name made lowercase.
    docth_from_check_desc = models.CharField(db_column='DOCTH_FROM_CHECK_DESC', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    docth_from_docth_id = models.BigIntegerField(db_column='DOCTH_FROM_DOCTH_ID', blank=True, null=True)  # Field name made lowercase.
    docth_check_val = models.SmallIntegerField(db_column='DOCTH_CHECK_VAL', blank=True, null=True)  # Field name made lowercase.
    docth_check_user_id = models.BigIntegerField(db_column='DOCTH_CHECK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    docth_check_time = models.DateTimeField(db_column='DOCTH_CHECK_TIME', blank=True, null=True)  # Field name made lowercase.
    docth_check_desc = models.CharField(db_column='DOCTH_CHECK_DESC', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    docth_next_check_val = models.SmallIntegerField(db_column='DOCTH_NEXT_CHECK_VAL', blank=True, null=True)  # Field name made lowercase.
    docth_next_check_user_id = models.BigIntegerField(db_column='DOCTH_NEXT_CHECK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    docth_next_check_time = models.DateTimeField(db_column='DOCTH_NEXT_CHECK_TIME', blank=True, null=True)  # Field name made lowercase.
    docth_next_check_desc = models.CharField(db_column='DOCTH_NEXT_CHECK_DESC', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    docth_company_id = models.BigIntegerField(db_column='DOCTH_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    docth_create_user_id = models.BigIntegerField(db_column='DOCTH_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    docth_create_time = models.DateTimeField(db_column='DOCTH_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    docth_modify_uaer_id = models.BigIntegerField(db_column='DOCTH_MODIFY_UAER_ID', blank=True, null=True)  # Field name made lowercase.
    docth_modify_time = models.DateTimeField(db_column='DOCTH_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'docth_rec'


class DsField(models.Model):
    ds_field_id = models.BigIntegerField(db_column='DS_FIELD_ID', primary_key=True)  # Field name made lowercase.
    ds_field_ds = models.ForeignKey('Ds', db_column='DS_FIELD_DS_ID', blank=True, null=True)  # Field name made lowercase.
    ds_field_table_code = models.CharField(db_column='DS_FIELD_TABLE_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    ds_field_code = models.CharField(db_column='DS_FIELD_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ds_field_name = models.CharField(db_column='DS_FIELD_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ds_field_val_type = models.CharField(db_column='DS_FIELD_VAL_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ds_field_val_wid = models.SmallIntegerField(db_column='DS_FIELD_VAL_WID', blank=True, null=True)  # Field name made lowercase.
    ds_field_val_dig = models.SmallIntegerField(db_column='DS_FIELD_VAL_DIG', blank=True, null=True)  # Field name made lowercase.
    ds_field_is_group = models.SmallIntegerField(db_column='DS_FIELD_IS_GROUP', blank=True, null=True)  # Field name made lowercase.
    ds_field_is_sum = models.SmallIntegerField(db_column='DS_FIELD_IS_SUM', blank=True, null=True)  # Field name made lowercase.
    ds_field_expr = models.CharField(db_column='DS_FIELD_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ds_field_filter_type = models.SmallIntegerField(db_column='DS_FIELD_FILTER_TYPE', blank=True, null=True)  # Field name made lowercase.
    ds_field_filter_help = models.CharField(db_column='DS_FIELD_FILTER_HELP', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ds_field_create_user_id = models.BigIntegerField(db_column='DS_FIELD_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    ds_field_create_time = models.DateTimeField(db_column='DS_FIELD_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    ds_field_modify_user_id = models.BigIntegerField(db_column='DS_FIELD_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    ds_field_modify_time = models.DateTimeField(db_column='DS_FIELD_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ds_field_rec'


class Ds(models.Model):
    ds_id = models.BigIntegerField(db_column='DS_ID', primary_key=True)  # Field name made lowercase.
    ds_description = models.CharField(db_column='DS_DESCRIPTION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ds_type = models.SmallIntegerField(db_column='DS_TYPE', blank=True, null=True)  # Field name made lowercase.
    ds_company_id = models.BigIntegerField(db_column='DS_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    ds_create_user_id = models.BigIntegerField(db_column='DS_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    ds_create_time = models.DateTimeField(db_column='DS_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    ds_modify_user_id = models.BigIntegerField(db_column='DS_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    ds_modify_time = models.DateTimeField(db_column='DS_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ds_rec'


class DsTable(models.Model):
    ds_table_id = models.BigIntegerField(db_column='DS_TABLE_ID', primary_key=True)  # Field name made lowercase.
    ds_table_ds = models.ForeignKey(Ds, db_column='DS_TABLE_DS_ID', blank=True, null=True)  # Field name made lowercase.
    ds_table_code = models.CharField(db_column='DS_TABLE_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ds_table_name = models.CharField(db_column='DS_TABLE_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ds_table_second_code = models.CharField(db_column='DS_TABLE_SECOND_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ds_table_link_code = models.CharField(db_column='DS_TABLE_LINK_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ds_table_where_expr = models.CharField(db_column='DS_TABLE_WHERE_EXPR', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ds_table_create_user_id = models.BigIntegerField(db_column='DS_TABLE_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    ds_table_create_time = models.DateTimeField(db_column='DS_TABLE_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    ds_table_modify_user_id = models.BigIntegerField(db_column='DS_TABLE_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    ds_table_modify_time = models.DateTimeField(db_column='DS_TABLE_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ds_table_rec'


class Flag(models.Model):
    flag_id = models.BigIntegerField(db_column='FLAG_ID', primary_key=True)  # Field name made lowercase.
    flag_parent_id = models.BigIntegerField(db_column='FLAG_PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    flag_sys_flag = models.ForeignKey('SysFlag', db_column='FLAG_SYS_FLAG_ID', blank=True, null=True)  # Field name made lowercase.
    flag_code = models.CharField(db_column='FLAG_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flag_name = models.CharField(db_column='FLAG_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    flag_type = models.SmallIntegerField(db_column='FLAG_TYPE', blank=True, null=True)  # Field name made lowercase.
    flag_value = models.CharField(db_column='FLAG_VALUE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flag_desc = models.CharField(db_column='FLAG_DESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flag_laycount = models.SmallIntegerField(db_column='FLAG_LAYCOUNT', blank=True, null=True)  # Field name made lowercase.
    flag_sort_step = models.BigIntegerField(db_column='FLAG_SORT_STEP', blank=True, null=True)  # Field name made lowercase.
    flag_company_id = models.BigIntegerField(db_column='FLAG_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    flag_create_user_id = models.BigIntegerField(db_column='FLAG_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    flag_create_time = models.DateTimeField(db_column='FLAG_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    flag_modify_user_id = models.BigIntegerField(db_column='FLAG_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    flag_modify_time = models.DateTimeField(db_column='FLAG_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'flag_rec'


class FlowDoct(models.Model):
    flow_doct_id = models.BigIntegerField(db_column='FLOW_DOCT_ID', primary_key=True)  # Field name made lowercase.
    flow_doct_doct = models.ForeignKey(Doct, db_column='FLOW_DOCT_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    flow_doct_flow = models.ForeignKey('Flow', db_column='FLOW_DOCT_FLOW_ID', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'flow_doct_rec'


class Flow(models.Model):
    flow_id = models.BigIntegerField(db_column='FLOW_ID', primary_key=True)  # Field name made lowercase.
    flow_code = models.CharField(db_column='FLOW_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flow_name = models.CharField(db_column='FLOW_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    flow_return_flg = models.SmallIntegerField(db_column='FLOW_RETURN_FLG', blank=True, null=True)  # Field name made lowercase.
    flow_create_user_id = models.BigIntegerField(db_column='FLOW_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    flow_create_time = models.DateTimeField(db_column='FLOW_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    flow_modify_user_id = models.BigIntegerField(db_column='FLOW_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    flow_modify_time = models.DateTimeField(db_column='FLOW_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'flow_rec'


class FlowTcode(models.Model):
    flow_tcode_id = models.BigIntegerField(db_column='FLOW_TCODE_ID', primary_key=True)  # Field name made lowercase.
    flow_tcode_flow = models.ForeignKey(Flow, db_column='FLOW_TCODE_FLOW_ID', blank=True, null=True)  # Field name made lowercase.
    flow_tcode_tcode = models.ForeignKey('Tcode', db_column='FLOW_TCODE_TCODE_ID', blank=True, null=True)  # Field name made lowercase.
    flow_tcode_seq = models.SmallIntegerField(db_column='FLOW_TCODE_SEQ', blank=True, null=True)  # Field name made lowercase.
    flow_tcode_cancel_flg = models.SmallIntegerField(db_column='FLOW_TCODE_CANCEL_FLG', blank=True, null=True)  # Field name made lowercase.
    flow_tcode_chg_flg = models.SmallIntegerField(db_column='FLOW_TCODE_CHG_FLG', blank=True, null=True)  # Field name made lowercase.
    flow_tcode_role = models.ForeignKey('SysRole', db_column='FLOW_TCODE_ROLE_ID', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'flow_tcode_rec'


class ForeignLogistics(models.Model):
    foreign_id = models.BigIntegerField(db_column='FOREIGN_ID', primary_key=True)  # Field name made lowercase.
    foreign_node = models.IntegerField(db_column='FOREIGN_NODE', blank=True, null=True)  # Field name made lowercase.
    foreign_node_info = models.CharField(db_column='FOREIGN_NODE_INFO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    foreign_sod_no = models.CharField(db_column='FOREIGN_SOD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    foreign_create_time = models.DateTimeField(db_column='FOREIGN_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'foreign_logistics_rec'


class GenField(models.Model):
    gen_field_id = models.BigIntegerField(db_column='GEN_FIELD_ID', primary_key=True)  # Field name made lowercase.
    gen_field_doc_link = models.ForeignKey(DocLinkGen, db_column='GEN_FIELD_DOC_LINK_ID', blank=True, null=True)  # Field name made lowercase.
    gen_field_sys_gem_field = models.ForeignKey('SysGenField', db_column='GEN_FIELD_SYS_GEM_FIELD_ID', blank=True, null=True)  # Field name made lowercase.
    gen_field_f_page_iten = models.ForeignKey('PageItem', db_column='GEN_FIELD_F_PAGE_ITEN_ID', blank=True, null=True)  # Field name made lowercase.
    gen_field_page_iten = models.ForeignKey('PageItem', db_column='GEN_FIELD_PAGE_ITEN_ID', blank=True, null=True)  # Field name made lowercase.
    gen_field_is_visible_flg = models.SmallIntegerField(db_column='GEN_FIELD_IS_VISIBLE_FLG', blank=True, null=True)  # Field name made lowercase.
    gen_field_is_filter_flg = models.SmallIntegerField(db_column='GEN_FIELD_IS_FILTER_FLG', blank=True, null=True)  # Field name made lowercase.
    gen_field_is_order_flg = models.SmallIntegerField(db_column='GEN_FIELD_IS_ORDER_FLG', blank=True, null=True)  # Field name made lowercase.
    gen_field_company_id = models.BigIntegerField(db_column='GEN_FIELD_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    gen_field_create_user_id = models.BigIntegerField(db_column='GEN_FIELD_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    gen_field_create_time = models.DateTimeField(db_column='GEN_FIELD_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    gen_field_modify_user_id = models.BigIntegerField(db_column='GEN_FIELD_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    gen_field_modify_time = models.DateTimeField(db_column='GEN_FIELD_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'gen_field_rec'


class LeCprop(models.Model):
    le_cprop_id = models.BigIntegerField(db_column='LE_CPROP_ID', primary_key=True)  # Field name made lowercase.
    le_cprop_le = models.ForeignKey('Le', db_column='LE_CPROP_LE_ID', blank=True, null=True)  # Field name made lowercase.
    le_cprop_group_id = models.BigIntegerField(db_column='LE_CPROP_GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    le_cprop_name = models.CharField(db_column='LE_CPROP_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_cprop_value = models.CharField(db_column='LE_CPROP_VALUE', max_length=60, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'le_cprop_rec'


class LePic(models.Model):
    le_pic_id = models.BigIntegerField(db_column='LE_PIC_ID', primary_key=True)  # Field name made lowercase.
    le_pic_le = models.ForeignKey('Le', db_column='LE_PIC_LE_ID', blank=True, null=True)  # Field name made lowercase.
    le_pic_url = models.CharField(db_column='LE_PIC_URL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    le_pic_type = models.IntegerField(db_column='LE_PIC_TYPE', blank=True, null=True)  # Field name made lowercase.
    le_pic_sort = models.IntegerField(db_column='LE_PIC_SORT', blank=True, null=True)  # Field name made lowercase.
    le_pic_create_user_id = models.BigIntegerField(db_column='LE_PIC_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    le_pic_create_time = models.DateTimeField(db_column='LE_PIC_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    le_pic_modify_user_id = models.BigIntegerField(db_column='LE_PIC_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    le_pic_modify_time = models.DateTimeField(db_column='LE_PIC_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'le_pic_rec'


class LeProp(models.Model):
    le_prop_id = models.BigIntegerField(db_column='LE_PROP_ID', primary_key=True)  # Field name made lowercase.
    le_prop_le_id = models.BigIntegerField(db_column='LE_PROP_LE_ID', blank=True, null=True)  # Field name made lowercase.
    le_prop_group = models.ForeignKey('PropGroup', db_column='LE_PROP_GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    le_prop_prop = models.ForeignKey('Prop', db_column='LE_PROP_PROP_ID', blank=True, null=True)  # Field name made lowercase.
    le_prop_sort = models.SmallIntegerField(db_column='LE_PROP_SORT', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'le_prop_rec'


class LePropval(models.Model):
    le_propval_id = models.BigIntegerField(db_column='LE_PROPVAL_ID', primary_key=True)  # Field name made lowercase.
    le_propval_le = models.ForeignKey('Le', db_column='LE_PROPVAL_LE_ID', blank=True, null=True)  # Field name made lowercase.
    le_propval_prop = models.ForeignKey('Prop', db_column='LE_PROPVAL_PROP_ID', blank=True, null=True)  # Field name made lowercase.
    le_propval_propval = models.ForeignKey('Propval', db_column='LE_PROPVAL_PROPVAL_ID', blank=True, null=True)  # Field name made lowercase.
    le_propval_sort = models.SmallIntegerField(db_column='LE_PROPVAL_SORT', blank=True, null=True)  # Field name made lowercase.
    le_propval_alias = models.CharField(db_column='LE_PROPVAL_ALIAS', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    le_propval_pic = models.CharField(db_column='LE_PROPVAL_PIC', max_length=128, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'le_propval_rec'

class Lets(models.Model):
    let_id = models.BigIntegerField(db_column='LET_ID', primary_key=True)  # Field name made lowercase.
    let_code = models.CharField(db_column='LET_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_name = models.CharField(db_column='LET_NAME', max_length=512, blank=True, null=True)  # Field name made lowercase.
    let_full_name = models.CharField(db_column='LET_FULL_NAME', max_length=512, blank=True, null=True)  # Field name made lowercase.
    let_id1 = models.BigIntegerField(db_column='LET_ID1', blank=True, null=True)  # Field name made lowercase.
    let_code1 = models.CharField(db_column='LET_CODE1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    let_name1 = models.CharField(db_column='LET_NAME1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_id2 = models.BigIntegerField(db_column='LET_ID2', blank=True, null=True)  # Field name made lowercase.
    let_code2 = models.CharField(db_column='LET_CODE2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    let_name2 = models.CharField(db_column='LET_NAME2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_id3 = models.BigIntegerField(db_column='LET_ID3', blank=True, null=True)  # Field name made lowercase.
    let_code3 = models.CharField(db_column='LET_CODE3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    let_name3 = models.CharField(db_column='LET_NAME3', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_parent_id = models.BigIntegerField(db_column='LET_PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    let_laycount = models.SmallIntegerField(db_column='LET_LAYCOUNT', blank=True, null=True)  # Field name made lowercase.
    let_sort_step = models.SmallIntegerField(db_column='LET_SORT_STEP', blank=True, null=True)  # Field name made lowercase.
    let_is_end = models.SmallIntegerField(db_column='LET_IS_END', blank=True, null=True)  # Field name made lowercase.
    let_url = models.CharField(db_column='LET_URL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_stat = models.SmallIntegerField(db_column='LET_STAT', blank=True, null=True)  # Field name made lowercase.
    let_remark = models.CharField(db_column='LET_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    let_create_user_id = models.BigIntegerField(db_column='LET_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_create_time = models.DateTimeField(db_column='LET_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    let_modify_user_id = models.BigIntegerField(db_column='LET_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_modify_time = models.DateTimeField(db_column='LET_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    let_type = models.SmallIntegerField(db_column='LET_TYPE', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'let_rec'

class Le(models.Model):
    le_id = models.BigIntegerField(db_column='LE_ID', primary_key=True)  # Field name made lowercase.
    le_code = models.CharField(db_column='LE_CODE', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_name = models.CharField(db_column='LE_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    le_let = models.ForeignKey(Lets, db_column='LE_LET_ID', blank=True, null=True)  # Field name made lowercase.
    le_unit = models.ForeignKey('Unit', db_column='LE_UNIT_ID', blank=True, null=True)  # Field name made lowercase.
    le_brand = models.ForeignKey(Brand, db_column='LE_BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    le_country = models.ForeignKey(Country, db_column='LE_COUNTRY_ID', blank=True, null=True)  # Field name made lowercase.
    le_qty = models.DecimalField(db_column='LE_QTY', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    le_usp = models.CharField(db_column='LE_USP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    le_ad = models.CharField(db_column='LE_AD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    le_sg = models.CharField(db_column='LE_SG', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    le_lg_id = models.BigIntegerField(db_column='LE_LG_ID', blank=True, null=True)  # Field name made lowercase.
    le_heat = models.IntegerField(db_column='LE_HEAT', blank=True, null=True)  # Field name made lowercase.
    le_mobile_content = models.CharField(db_column='LE_MOBILE_CONTENT', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    le_pc_content = models.CharField(db_column='LE_PC_CONTENT', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    le_qcsiq = models.CharField(db_column='LE_QCSIQ', max_length=128, blank=True, null=True)  # Field name made lowercase.
    le_barcode = models.CharField(db_column='LE_BARCODE', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    le_sprice1 = models.DecimalField(db_column='LE_SPRICE1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_sprice2 = models.DecimalField(db_column='LE_SPRICE2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_sprice3 = models.DecimalField(db_column='LE_SPRICE3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_sprice = models.DecimalField(db_column='LE_SPRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_wg = models.DecimalField(db_column='DF_LE_REC_LE_WG', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_nw = models.DecimalField(db_column='DF_LE_REC_LE_NW', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_cost = models.DecimalField(db_column='DF_LE_REC_LE_COST', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_tax = models.DecimalField(db_column='DF_LE_REC_LE_TAX', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_tax_amt = models.DecimalField(db_column='DF_LE_REC_LE_TAX_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_fee1 = models.DecimalField(db_column='DF_LE_REC_LE_FEE1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_fee2 = models.DecimalField(db_column='DF_LE_REC_LE_FEE2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_fee3 = models.DecimalField(db_column='DF_LE_REC_LE_FEE3', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_ratio1 = models.DecimalField(db_column='DF_LE_REC_LE_RATIO1', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    df_le_rec_le_ratio2 = models.DecimalField(db_column='DF_LE_REC_LE_RATIO2', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    le_wg = models.DecimalField(db_column='LE_WG', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    le_nw = models.DecimalField(db_column='LE_NW', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    le_cost = models.DecimalField(db_column='LE_COST', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_tax = models.DecimalField(db_column='LE_TAX', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    le_tax_amt = models.DecimalField(db_column='LE_TAX_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_fee1 = models.DecimalField(db_column='LE_FEE1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_fee2 = models.DecimalField(db_column='LE_FEE2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_fee3 = models.DecimalField(db_column='LE_FEE3', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    le_ratio1 = models.DecimalField(db_column='LE_RATIO1', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    le_ratio2 = models.DecimalField(db_column='LE_RATIO2', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    le_ratio3 = models.DecimalField(db_column='LE_RATIO3', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    le_main_pic_url = models.CharField(db_column='LE_MAIN_PIC_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    le_homepage_pic_url = models.CharField(db_column='LE_HOMEPAGE_PIC_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    le_stat = models.IntegerField(db_column='LE_STAT', blank=True, null=True)  # Field name made lowercase.
    le_stat_user_id = models.BigIntegerField(db_column='LE_STAT_USER_ID', blank=True, null=True)  # Field name made lowercase.
    le_stat_time = models.DateTimeField(db_column='LE_STAT_TIME', blank=True, null=True)  # Field name made lowercase.
    le_end_user_id = models.BigIntegerField(db_column='LE_END_USER_ID', blank=True, null=True)  # Field name made lowercase.
    le_end_time = models.DateTimeField(db_column='LE_END_TIME', blank=True, null=True)  # Field name made lowercase.
    product_type = models.BigIntegerField(db_column='PRODUCT_TYPE', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'le_rec'


class Lehot(models.Model):
    lehot_id = models.BigIntegerField(db_column='LEHOT_ID', primary_key=True)  # Field name made lowercase.
    lehot_type = models.SmallIntegerField(db_column='LEHOT_TYPE', blank=True, null=True)  # Field name made lowercase.
    lehot_member_id = models.BigIntegerField(db_column='LEHOT_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    lehot_store = models.ForeignKey('Store', db_column='LEHOT_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    lehot_tmn_id = models.BigIntegerField(db_column='LEHOT_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    lehot_le = models.ForeignKey(Le, db_column='LEHOT_LE_ID', blank=True, null=True)  # Field name made lowercase.
    lehot_sort = models.SmallIntegerField(db_column='LEHOT_SORT', blank=True, null=True)  # Field name made lowercase.
    lehot_stat = models.SmallIntegerField(db_column='LEHOT_STAT', blank=True, null=True)  # Field name made lowercase.
    lehot_release_user_id = models.BigIntegerField(db_column='LEHOT_RELEASE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    lehot_modify_time = models.DateTimeField(db_column='LEHOT_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    lehot_create_user_id = models.BigIntegerField(db_column='LEHOT_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    lehot_create_time = models.DateTimeField(db_column='LEHOT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    lehot_modify_user_id = models.BigIntegerField(db_column='LEHOT_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    lehot_release_time = models.DateTimeField(db_column='LEHOT_RELEASE_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'lehot_rec'


class Lelink(models.Model):
    lelink_id = models.BigIntegerField(db_column='LELINK_ID', primary_key=True)  # Field name made lowercase.
    lelink_le = models.ForeignKey(Le, db_column='LELINK_LE_ID', blank=True, null=True)  # Field name made lowercase.
    lelink_link_le = models.ForeignKey(Le, db_column='LELINK_LINK_LE_ID', blank=True, null=True)  # Field name made lowercase.
    lelink_sort = models.SmallIntegerField(db_column='LELINK_SORT', blank=True, null=True)  # Field name made lowercase.
    lelink_create_user_id = models.BigIntegerField(db_column='LELINK_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    lelink_create_time = models.DateTimeField(db_column='LELINK_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    lelink_modify_user_id = models.BigIntegerField(db_column='LELINK_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    lelink_modify_time = models.DateTimeField(db_column='LELINK_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'lelink_rec'


class LetBrand(models.Model):
    let_brand_id = models.BigIntegerField(db_column='LET_BRAND_ID', primary_key=True)  # Field name made lowercase.
    let_brand_let_id = models.BigIntegerField(db_column='LET_BRAND_LET_ID', blank=True, null=True)  # Field name made lowercase.
    let_brand_brand_id = models.BigIntegerField(db_column='LET_BRAND_BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    let_brand_sort = models.SmallIntegerField(db_column='LET_BRAND_SORT', blank=True, null=True)  # Field name made lowercase.
    let_brand_create_user_id = models.BigIntegerField(db_column='LET_BRAND_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_brand_create_time = models.DateTimeField(db_column='LET_BRAND_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    let_brand_modify_user_id = models.BigIntegerField(db_column='LET_BRAND_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_brand_modify_time = models.DateTimeField(db_column='LET_BRAND_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'let_brand_rec'


class LetProp(models.Model):
    let_prop_id = models.BigIntegerField(db_column='LET_PROP_ID', primary_key=True)  # Field name made lowercase.
    let_prop_group = models.ForeignKey('PropGroup', db_column='LET_PROP_GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    let_prop_let = models.ForeignKey('Let', db_column='LET_PROP_LET_ID', blank=True, null=True)  # Field name made lowercase.
    let_prop_prop = models.ForeignKey('Prop', db_column='LET_PROP_PROP_ID', blank=True, null=True)  # Field name made lowercase.
    let_prop_sort = models.IntegerField(db_column='LET_PROP_SORT', blank=True, null=True)  # Field name made lowercase.
    let_prop_valid = models.IntegerField(db_column='LET_PROP_VALID', blank=True, null=True)  # Field name made lowercase.
    let_prop_create_user_id = models.BigIntegerField(db_column='LET_PROP_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_prop_create_time = models.DateTimeField(db_column='LET_PROP_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    let_prop_modify_user_id = models.BigIntegerField(db_column='LET_PROP_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_prop_modify_time = models.DateTimeField(db_column='LET_PROP_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'let_prop_rec'


class LetPropval(models.Model):
    let_propval_id = models.BigIntegerField(db_column='LET_PROPVAL_ID', primary_key=True)  # Field name made lowercase.
    let_propval_let = models.ForeignKey('Let', db_column='LET_PROPVAL_LET_ID', blank=True, null=True)  # Field name made lowercase.
    let_propval_let_prop_id = models.BigIntegerField(db_column='LET_PROPVAL_LET_PROP_ID', blank=True, null=True)  # Field name made lowercase.
    let_propval_prop_id = models.BigIntegerField(db_column='LET_PROPVAL_PROP_ID', blank=True, null=True)  # Field name made lowercase.
    let_propval_propval = models.ForeignKey('Propval', db_column='LET_PROPVAL_PROPVAL_ID', blank=True, null=True)  # Field name made lowercase.
    let_propval_sort = models.SmallIntegerField(db_column='LET_PROPVAL_SORT', blank=True, null=True)  # Field name made lowercase.
    let_propval_create_user_id = models.BigIntegerField(db_column='LET_PROPVAL_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_propval_create_time = models.DateTimeField(db_column='LET_PROPVAL_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    let_propval_modify_user_id = models.BigIntegerField(db_column='LET_PROPVAL_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_propval_modify_time = models.DateTimeField(db_column='LET_PROPVAL_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'let_propval_rec'


class Let(models.Model):
    let_id = models.BigIntegerField(db_column='LET_ID', primary_key=True)  # Field name made lowercase.
    let_code = models.CharField(db_column='LET_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_name = models.CharField(db_column='LET_NAME', max_length=512, blank=True, null=True)  # Field name made lowercase.
    let_full_name = models.CharField(db_column='LET_FULL_NAME', max_length=512, blank=True, null=True)  # Field name made lowercase.
    let_id1 = models.BigIntegerField(db_column='LET_ID1', blank=True, null=True)  # Field name made lowercase.
    let_code1 = models.CharField(db_column='LET_CODE1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    let_name1 = models.CharField(db_column='LET_NAME1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_id2 = models.BigIntegerField(db_column='LET_ID2', blank=True, null=True)  # Field name made lowercase.
    let_code2 = models.CharField(db_column='LET_CODE2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    let_name2 = models.CharField(db_column='LET_NAME2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_id3 = models.BigIntegerField(db_column='LET_ID3', blank=True, null=True)  # Field name made lowercase.
    let_code3 = models.CharField(db_column='LET_CODE3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    let_name3 = models.CharField(db_column='LET_NAME3', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_parent_id = models.BigIntegerField(db_column='LET_PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    let_laycount = models.SmallIntegerField(db_column='LET_LAYCOUNT', blank=True, null=True)  # Field name made lowercase.
    let_sort_step = models.SmallIntegerField(db_column='LET_SORT_STEP', blank=True, null=True)  # Field name made lowercase.
    let_is_end = models.SmallIntegerField(db_column='LET_IS_END', blank=True, null=True)  # Field name made lowercase.
    let_url = models.CharField(db_column='LET_URL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    let_stat = models.SmallIntegerField(db_column='LET_STAT', blank=True, null=True)  # Field name made lowercase.
    let_remark = models.CharField(db_column='LET_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    let_create_user_id = models.BigIntegerField(db_column='LET_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_create_time = models.DateTimeField(db_column='LET_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    let_modify_user_id = models.BigIntegerField(db_column='LET_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    let_modify_time = models.DateTimeField(db_column='LET_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    let_type = models.SmallIntegerField(db_column='LET_TYPE', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'let_rec'


class Lethot(models.Model):
    lethot_id = models.BigIntegerField(db_column='LETHOT_ID', primary_key=True)  # Field name made lowercase.
    lethot_flet_id = models.BigIntegerField(db_column='LETHOT_FLET_ID', blank=True, null=True)  # Field name made lowercase.
    lethot_slet_id = models.BigIntegerField(db_column='LETHOT_SLET_ID', blank=True, null=True)  # Field name made lowercase.
    lethot_le_id = models.BigIntegerField(db_column='LETHOT_LE_ID', blank=True, null=True)  # Field name made lowercase.
    lethot_sort = models.SmallIntegerField(db_column='LETHOT_SORT', blank=True, null=True)  # Field name made lowercase.
    lethot_create_user_id = models.BigIntegerField(db_column='LETHOT_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    lethot_create_time = models.DateTimeField(db_column='LETHOT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    lethot_modify_user_id = models.BigIntegerField(db_column='LETHOT_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    lethot_modify_time = models.DateTimeField(db_column='LETHOT_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'lethot_rec'


class Letmn(models.Model):
    letmn_id = models.BigIntegerField(db_column='LETMN_ID', primary_key=True)  # Field name made lowercase.
    letmn_tmn_id = models.BigIntegerField(db_column='LETMN_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    letmn_member = models.ForeignKey('Member', db_column='LETMN_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    letmn_store = models.ForeignKey('Store', db_column='LETMN_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    letmn_le = models.ForeignKey(Le, db_column='LETMN_LE_ID', blank=True, null=True)  # Field name made lowercase.
    letmn_create_user_id = models.BigIntegerField(db_column='LETMN_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    letmn_create_time = models.DateTimeField(db_column='LETMN_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'letmn_rec'


class Lg(models.Model):
    lg_id = models.BigIntegerField(db_column='LG_ID', primary_key=True)  # Field name made lowercase.
    lg_name = models.CharField(db_column='LG_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    lg_type = models.SmallIntegerField(db_column='LG_TYPE', blank=True, null=True)  # Field name made lowercase.
    lg_create_user_id = models.BigIntegerField(db_column='LG_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    lg_create_time = models.DateTimeField(db_column='LG_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    lg_modify_user_id = models.BigIntegerField(db_column='LG_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    lg_modify_time = models.DateTimeField(db_column='LG_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'lg_rec'


class Lgitem(models.Model):
    lgitem_id = models.BigIntegerField(db_column='LGITEM_ID', primary_key=True)  # Field name made lowercase.
    lgitem_lg = models.ForeignKey(Lg, db_column='LGITEM_LG_ID', blank=True, null=True)  # Field name made lowercase.
    lgitem_le = models.ForeignKey(Le, db_column='LGITEM_LE_ID', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'lgitem_rec'


class MemberBank(models.Model):
    member_bank_id = models.BigIntegerField(db_column='MEMBER_BANK_ID', primary_key=True)  # Field name made lowercase.
    member_bank_member_id = models.BigIntegerField(db_column='MEMBER_BANK_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    member_bank_type = models.BigIntegerField(db_column='MEMBER_BANK_TYPE', blank=True, null=True)  # Field name made lowercase.
    member_bank_no = models.CharField(db_column='MEMBER_BANK_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    member_bank_create_member_id = models.BigIntegerField(db_column='MEMBER_BANK_CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    member_bank_create_time = models.DateTimeField(db_column='MEMBER_BANK_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    member_bank_modify_member_id = models.BigIntegerField(db_column='MEMBER_BANK_MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    member_bank_modify_time = models.DateTimeField(db_column='MEMBER_BANK_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'member_bank_rec'

class Stores(models.Model):
    store_id = models.BigIntegerField(db_column='STORE_ID', primary_key=True)  # Field name made lowercase.
    #store_member = models.ForeignKey(Member, db_column='STORE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='STORE_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    store_full_name = models.CharField(db_column='STORE_FULL_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    store_logo = models.CharField(db_column='STORE_LOGO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    store_sarea = models.ForeignKey(Area, db_column='STORE_SAREA_ID', blank=True, null=True)  # Field name made lowercase.
    store_carea = models.ForeignKey(Area, db_column='STORE_CAREA_ID', blank=True, null=True)  # Field name made lowercase.
    store_xarea = models.ForeignKey(Area, db_column='STORE_XAREA_ID', blank=True, null=True)  # Field name made lowercase.
    store_address = models.CharField(db_column='STORE_ADDRESS', max_length=128, blank=True, null=True)  # Field name made lowercase.
    store_zipcode = models.CharField(db_column='STORE_ZIPCODE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    store_phone = models.CharField(db_column='STORE_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_fax = models.CharField(db_column='STORE_FAX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_contact = models.CharField(db_column='STORE_CONTACT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_contact_tel = models.CharField(db_column='STORE_CONTACT_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_contact_phone = models.CharField(db_column='STORE_CONTACT_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_type = models.SmallIntegerField(db_column='STORE_TYPE', blank=True, null=True)  # Field name made lowercase.
    store_flg = models.SmallIntegerField(db_column='STORE_FLG', blank=True, null=True)  # Field name made lowercase.
    store_check_user_id = models.BigIntegerField(db_column='STORE_CHECK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    store_check_desc = models.CharField(db_column='STORE_CHECK_DESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    store_check_time = models.DateTimeField(db_column='STORE_CHECK_TIME', blank=True, null=True)  # Field name made lowercase.
    store_create_user_id = models.BigIntegerField(db_column='STORE_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    store_create_time = models.DateTimeField(db_column='STORE_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    store_modify_user_id = models.BigIntegerField(db_column='STORE_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    store_modify_time = models.DateTimeField(db_column='STORE_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    store_is_broker = models.BigIntegerField(db_column='STORE_IS_BROKER', blank=True, null=True)  # Field name made lowercase.
    # class Meta:
    #     managed = False
    #     db_table = 'store_rec'

class Tmns(models.Model):
    tmn_id = models.BigIntegerField(db_column='TMN_ID', primary_key=True)  # Field name made lowercase.
    tmn_code = models.CharField(db_column='TMN_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmn_name = models.CharField(db_column='TMN_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tmn_first_member_id = models.BigIntegerField(db_column='TMN_FIRST_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_store = models.ForeignKey(Stores,db_column='TMN_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_type = models.SmallIntegerField(db_column='TMN_TYPE', blank=True, null=True)  # Field name made lowercase.
    tmn_url = models.CharField(db_column='TMN_URL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tmn_manager = models.CharField(db_column='TMN_MANAGER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmn_tel = models.CharField(db_column='TMN_TEL', max_length=120, blank=True, null=True)  # Field name made lowercase.
    tmn_address = models.CharField(db_column='TMN_ADDRESS', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tmn_stat = models.BigIntegerField(db_column='TMN_STAT', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'tmn_rec'

class Member(models.Model):
    member_id = models.BigIntegerField(db_column='MEMBER_ID', primary_key=True)  # Field name made lowercase.Tmn
    member_tmn = models.ForeignKey(Tmns, db_column='MEMBER_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    #member_tmn_id = models.BigIntegerField(db_column='MEMBER_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    member_parent_id = models.BigIntegerField(db_column='MEMBER_PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    member_code = models.CharField(db_column='MEMBER_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    member_password = models.CharField(db_column='MEMBER_PASSWORD', max_length=60, blank=True, null=True)  # Field name made lowercase.
    member_name = models.CharField(db_column='MEMBER_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    member_full_name = models.CharField(db_column='MEMBER_FULL_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    member_second_name = models.CharField(db_column='MEMBER_SECOND_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    member_head_url = models.CharField(db_column='MEMBER_HEAD_URL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    member_sarea = models.ForeignKey(Area, db_column='MEMBER_SAREA_ID', blank=True, null=True)  # Field name made lowercase.
    member_carea = models.ForeignKey(Area, db_column='MEMBER_CAREA_ID', blank=True, null=True)  # Field name made lowercase.
    member_xarea = models.ForeignKey(Area, db_column='MEMBER_XAREA_ID', blank=True, null=True)  # Field name made lowercase.
    member_address_no = models.CharField(db_column='MEMBER_ADDRESS_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    member_cid = models.CharField(db_column='MEMBER_CID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    member_phone = models.CharField(db_column='MEMBER_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    member_wxcode = models.CharField(db_column='MEMBER_WXCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    member_wbcode = models.CharField(db_column='MEMBER_WBCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    member_type = models.IntegerField(db_column='MEMBER_TYPE', blank=True, null=True)  # Field name made lowercase.
    user_create_member_id = models.BigIntegerField(db_column='USER_CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    user_create_time = models.DateTimeField(db_column='USER_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    user_modify_member_id = models.BigIntegerField(db_column='USER_MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    user_modify_time = models.DateTimeField(db_column='USER_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'member_rec'


class MemberTmn(models.Model):
    member_tmn_id = models.BigIntegerField(db_column='MEMBER_TMN_ID', primary_key=True)  # Field name made lowercase.
    member_tmn_member = models.ForeignKey(Member, db_column='MEMBER_TMN_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    member_tmn_tmn_id = models.BigIntegerField(db_column='MEMBER_TMN_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    member_tmn_begtime = models.DateTimeField(db_column='MEMBER_TMN_BEGTIME', blank=True, null=True)  # Field name made lowercase.
    member_tmn_endtime = models.DateTimeField(db_column='MEMBER_TMN_ENDTIME', blank=True, null=True)  # Field name made lowercase.
    member_tmn_url = models.CharField(db_column='MEMBER_TMN_URL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    member_tmn_manager = models.CharField(db_column='MEMBER_TMN_MANAGER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    member_tmn_tel = models.CharField(db_column='MEMBER_TMN_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    member_tmn_address = models.CharField(db_column='MEMBER_TMN_ADDRESS', max_length=128, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'member_tmn_rec'


class MsInvitation(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    store_name = models.CharField(max_length=100, blank=True, null=True)
    invite_people = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=4096, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'ms_invitation'


class Msg(models.Model):
    msg_id = models.BigIntegerField(db_column='MSG_ID', primary_key=True)  # Field name made lowercase.
    msg_type = models.SmallIntegerField(db_column='MSG_TYPE', blank=True, null=True)  # Field name made lowercase.
    msg_title = models.CharField(db_column='MSG_TITLE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    msg_contents = models.CharField(db_column='MSG_CONTENTS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    msg_mobile_flg = models.SmallIntegerField(db_column='MSG_MOBILE_FLG', blank=True, null=True)  # Field name made lowercase.
    msg_email_flg = models.SmallIntegerField(db_column='MSG_EMAIL_FLG', blank=True, null=True)  # Field name made lowercase.
    msg_from_id = models.BigIntegerField(db_column='MSG_FROM_ID', blank=True, null=True)  # Field name made lowercase.
    msg_close = models.SmallIntegerField(db_column='MSG_CLOSE', blank=True, null=True)  # Field name made lowercase.
    msg_company_id = models.BigIntegerField(db_column='MSG_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    msg_create_user_id = models.BigIntegerField(db_column='MSG_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    msg_create_time = models.DateTimeField(db_column='MSG_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    msg_modify_user_id = models.BigIntegerField(db_column='MSG_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    msg_modify_time = models.DateTimeField(db_column='MSG_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'msg_rec'


class Msgeive(models.Model):
    msg_receive_id = models.BigIntegerField(db_column='MSG_RECEIVE_ID', primary_key=True)  # Field name made lowercase.
    msg_receive_msg = models.ForeignKey(Msg, db_column='MSG_RECEIVE_MSG_ID', blank=True, null=True)  # Field name made lowercase.
    msg_receive_user_id = models.BigIntegerField(db_column='MSG_RECEIVE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    msg_receive_mobile = models.CharField(db_column='MSG_RECEIVE_MOBILE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    msg_receive_email = models.CharField(db_column='MSG_RECEIVE_EMAIL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    msg_receive_read_flg = models.BigIntegerField(db_column='MSG_RECEIVE_READ_FLG', blank=True, null=True)  # Field name made lowercase.
    msg_receive_read_time = models.DateTimeField(db_column='MSG_RECEIVE_READ_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'msg_receive_rec'


class Myatt(models.Model):
    myatt_id = models.BigIntegerField(db_column='MYATT_ID', primary_key=True)  # Field name made lowercase.
    myatt_tmn_id = models.BigIntegerField(db_column='MYATT_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    myatt_member = models.ForeignKey(Member, db_column='MYATT_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    myatt_le_id = models.BigIntegerField(db_column='MYATT_LE_ID', blank=True, null=True)  # Field name made lowercase.
    myatt_create_member_id = models.BigIntegerField(db_column='MYATT_CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    myatt_create_time = models.DateTimeField(db_column='MYATT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    myatt_modify_member_id = models.BigIntegerField(db_column='MYATT_MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    myatt_modify_time = models.DateTimeField(db_column='MYATT_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'myatt_rec'


class PageBlock(models.Model):
    page_block_id = models.BigIntegerField(db_column='PAGE_BLOCK_ID', primary_key=True)  # Field name made lowercase.
    page_block_page = models.ForeignKey('Page', db_column='PAGE_BLOCK_PAGE_ID', blank=True, null=True)  # Field name made lowercase.
    page_block_sys_page_block_id = models.BigIntegerField(db_column='PAGE_BLOCK_SYS_PAGE_BLOCK_ID', blank=True, null=True)  # Field name made lowercase.
    page_block_seq = models.SmallIntegerField(db_column='PAGE_BLOCK_SEQ', blank=True, null=True)  # Field name made lowercase.
    page_block_no = models.CharField(db_column='PAGE_BLOCK_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    page_block_code = models.CharField(db_column='PAGE_BLOCK_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    page_block_name = models.CharField(db_column='PAGE_BLOCK_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    page_block_table_type = models.SmallIntegerField(db_column='PAGE_BLOCK_TABLE_TYPE', blank=True, null=True)  # Field name made lowercase.
    page_block_table_code = models.CharField(db_column='PAGE_BLOCK_TABLE_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    page_block_table_name = models.CharField(db_column='PAGE_BLOCK_TABLE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    page_block_show_flg = models.SmallIntegerField(db_column='PAGE_BLOCK_SHOW_FLG', blank=True, null=True)  # Field name made lowercase.
    page_block_sum_flg = models.SmallIntegerField(db_column='PAGE_BLOCK_SUM_FLG', blank=True, null=True)  # Field name made lowercase.
    page_block_create_user_id = models.BigIntegerField(db_column='PAGE_BLOCK_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    page_block_create_time = models.DateTimeField(db_column='PAGE_BLOCK_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    page_block_modify_user_id = models.BigIntegerField(db_column='PAGE_BLOCK_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    page_block_modify_time = models.DateTimeField(db_column='PAGE_BLOCK_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'page_block_rec'


class PageItem(models.Model):
    page_item_id = models.BigIntegerField(db_column='PAGE_ITEM_ID', primary_key=True)  # Field name made lowercase.
    page_item_page_block = models.ForeignKey(PageBlock, db_column='PAGE_ITEM_PAGE_BLOCK_ID', blank=True, null=True)  # Field name made lowercase.
    page_item_seq = models.SmallIntegerField(db_column='PAGE_ITEM_SEQ', blank=True, null=True)  # Field name made lowercase.
    page_item_sys_page_item_id = models.BigIntegerField(db_column='PAGE_ITEM_SYS_PAGE_ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    page_item_field_code = models.CharField(db_column='PAGE_ITEM_FIELD_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    page_item_title = models.CharField(db_column='PAGE_ITEM_TITLE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    page_item_code = models.CharField(db_column='PAGE_ITEM_CODE', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    page_item_name = models.CharField(db_column='PAGE_ITEM_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    page_item_table = models.CharField(db_column='PAGE_ITEM_TABLE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    page_item_second_table = models.CharField(db_column='PAGE_ITEM_SECOND_TABLE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    page_item_type = models.CharField(db_column='PAGE_ITEM_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    page_item_wid = models.SmallIntegerField(db_column='PAGE_ITEM_WID', blank=True, null=True)  # Field name made lowercase.
    page_item_dig = models.SmallIntegerField(db_column='PAGE_ITEM_DIG', blank=True, null=True)  # Field name made lowercase.
    page_item_control = models.CharField(db_column='PAGE_ITEM_CONTROL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    page_item_val_flg = models.SmallIntegerField(db_column='PAGE_ITEM_VAL_FLG', blank=True, null=True)  # Field name made lowercase.
    page_item_val_str = models.CharField(db_column='PAGE_ITEM_VAL_STR', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    page_item_is_sum = models.SmallIntegerField(db_column='PAGE_ITEM_IS_SUM', blank=True, null=True)  # Field name made lowercase.
    page_item_is_visible = models.SmallIntegerField(db_column='PAGE_ITEM_IS_VISIBLE', blank=True, null=True)  # Field name made lowercase.
    page_item_is_edit = models.SmallIntegerField(db_column='PAGE_ITEM_IS_EDIT', blank=True, null=True)  # Field name made lowercase.
    page_item_where_str = models.CharField(db_column='PAGE_ITEM_WHERE_STR', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    page_item_tag = models.CharField(db_column='PAGE_ITEM_TAG', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    page_item_create_user_id = models.BigIntegerField(db_column='PAGE_ITEM_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    page_item_create_time = models.DateTimeField(db_column='PAGE_ITEM_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    page_item_modify_user_id = models.BigIntegerField(db_column='PAGE_ITEM_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    page_item_modify_time = models.DateTimeField(db_column='PAGE_ITEM_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'page_item_rec'


class Page(models.Model):
    page_id = models.BigIntegerField(db_column='PAGE_ID', primary_key=True)  # Field name made lowercase.
    page_sys_page_id = models.BigIntegerField(db_column='PAGE_SYS_PAGE_ID', blank=True, null=True)  # Field name made lowercase.
    page_sys_menu_id = models.BigIntegerField(db_column='PAGE_SYS_MENU_ID', blank=True, null=True)  # Field name made lowercase.
    page_type = models.SmallIntegerField(db_column='PAGE_TYPE', blank=True, null=True)  # Field name made lowercase.
    page_sys_doct_id = models.BigIntegerField(db_column='PAGE_SYS_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    page_doct = models.ForeignKey(Doct, db_column='PAGE_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    page_code = models.CharField(db_column='PAGE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    page_name = models.CharField(db_column='PAGE_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    page_remark = models.CharField(db_column='PAGE_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    page_create_user_id = models.BigIntegerField(db_column='PAGE_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    page_create_time = models.DateTimeField(db_column='PAGE_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    page_modify_user_id = models.BigIntegerField(db_column='PAGE_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    page_modify_time = models.DateTimeField(db_column='PAGE_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'page_rec'


class PropGroup(models.Model):
    prop_group_id = models.BigIntegerField(db_column='PROP_GROUP_ID', primary_key=True)  # Field name made lowercase.
    prop_group_let = models.ForeignKey(Let, db_column='PROP_GROUP_LET_ID', blank=True, null=True)  # Field name made lowercase.
    prop_group_name = models.CharField(db_column='PROP_GROUP_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    prop_group_pic = models.CharField(db_column='PROP_GROUP_PIC', max_length=128, blank=True, null=True)  # Field name made lowercase.
    prop_group_sort = models.SmallIntegerField(db_column='PROP_GROUP_SORT', blank=True, null=True)  # Field name made lowercase.
    prop_group_valid = models.SmallIntegerField(db_column='PROP_GROUP_VALID', blank=True, null=True)  # Field name made lowercase.
    prop_group_create_user_id = models.BigIntegerField(db_column='PROP_GROUP_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    prop_group_create_time = models.DateTimeField(db_column='PROP_GROUP_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    prop_group_modify_user_id = models.BigIntegerField(db_column='PROP_GROUP_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    prop_group_modify_time = models.DateTimeField(db_column='PROP_GROUP_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'prop_group_rec'


class Prop(models.Model):
    prop_id = models.BigIntegerField(db_column='PROP_ID', primary_key=True)  # Field name made lowercase.
    prop_code = models.CharField(db_column='PROP_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prop_name = models.CharField(db_column='PROP_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    prop_hint = models.CharField(db_column='PROP_HINT', max_length=60, blank=True, null=True)  # Field name made lowercase.
    prop_is_color = models.IntegerField(db_column='PROP_IS_COLOR', blank=True, null=True)  # Field name made lowercase.
    prop_is_key = models.IntegerField(db_column='PROP_IS_KEY', blank=True, null=True)  # Field name made lowercase.
    prop_is_sale = models.IntegerField(db_column='PROP_IS_SALE', blank=True, null=True)  # Field name made lowercase.
    prop_alias = models.CharField(db_column='PROP_ALIAS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prop_is_input = models.IntegerField(db_column='PROP_IS_INPUT', blank=True, null=True)  # Field name made lowercase.
    prop_is_multi = models.IntegerField(db_column='PROP_IS_MULTI', blank=True, null=True)  # Field name made lowercase.
    prop_is_must = models.IntegerField(db_column='PROP_IS_MUST', blank=True, null=True)  # Field name made lowercase.
    prop_sort = models.IntegerField(db_column='PROP_SORT', blank=True, null=True)  # Field name made lowercase.
    prop_valid = models.IntegerField(db_column='PROP_VALID', blank=True, null=True)  # Field name made lowercase.
    prop_is_show = models.IntegerField(db_column='PROP_IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    prop_create_user_id = models.BigIntegerField(db_column='PROP_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    prop_create_time = models.DateTimeField(db_column='PROP_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    prop_modify_user_id = models.BigIntegerField(db_column='PROP_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    prop_modify_time = models.DateTimeField(db_column='PROP_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'prop_rec'


class Propval(models.Model):
    propval_id = models.BigIntegerField(db_column='PROPVAL_ID', primary_key=True)  # Field name made lowercase.
    propval_prop = models.ForeignKey(Prop, db_column='PROPVAL_PROP_ID', blank=True, null=True)  # Field name made lowercase.
    propval_code = models.CharField(db_column='PROPVAL_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    propval_name = models.CharField(db_column='PROPVAL_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    propval_desc = models.CharField(db_column='PROPVAL_DESC', max_length=128, blank=True, null=True)  # Field name made lowercase.
    propval_pic = models.CharField(db_column='PROPVAL_PIC', max_length=128, blank=True, null=True)  # Field name made lowercase.
    propval_sort = models.SmallIntegerField(db_column='PROPVAL_SORT', blank=True, null=True)  # Field name made lowercase.
    propval_valid = models.CharField(db_column='PROPVAL_VALID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    propval_create_user_id = models.BigIntegerField(db_column='PROPVAL_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    propval_create_time = models.DateTimeField(db_column='PROPVAL_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    propval_modify_user_id = models.BigIntegerField(db_column='PROPVAL_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    propval_modify_time = models.DateTimeField(db_column='PROPVAL_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'propval_rec'


class RField(models.Model):
    r_field_id = models.BigIntegerField(db_column='R_FIELD_ID', primary_key=True)  # Field name made lowercase.
    r_field_report = models.ForeignKey('Report', db_column='R_FIELD_REPORT_ID', blank=True, null=True)  # Field name made lowercase.
    r_field_seq = models.BigIntegerField(db_column='R_FIELD_SEQ', blank=True, null=True)  # Field name made lowercase.
    r_field_code = models.CharField(db_column='R_FIELD_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    r_field_name = models.CharField(db_column='R_FIELD_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    r_field_val_type = models.CharField(db_column='R_FIELD_VAL_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    r_field_val_wid = models.SmallIntegerField(db_column='R_FIELD_VAL_WID', blank=True, null=True)  # Field name made lowercase.
    r_field_val_dig = models.SmallIntegerField(db_column='R_FIELD_VAL_DIG', blank=True, null=True)  # Field name made lowercase.
    r_field_table_code = models.CharField(db_column='R_FIELD_TABLE_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    r_field_expr = models.CharField(db_column='R_FIELD_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    r_field_default_val = models.CharField(db_column='R_FIELD_DEFAULT_VAL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    r_field_is_filter = models.SmallIntegerField(db_column='R_FIELD_IS_FILTER', blank=True, null=True)  # Field name made lowercase.
    r_field_is_output = models.SmallIntegerField(db_column='R_FIELD_IS_OUTPUT', blank=True, null=True)  # Field name made lowercase.
    r_field_is_group_flg = models.SmallIntegerField(db_column='R_FIELD_IS_GROUP_FLG', blank=True, null=True)  # Field name made lowercase.
    r_field_is_sum = models.SmallIntegerField(db_column='R_FIELD_IS_SUM', blank=True, null=True)  # Field name made lowercase.
    r_field_is_group = models.SmallIntegerField(db_column='R_FIELD_IS_GROUP', blank=True, null=True)  # Field name made lowercase.
    r_field_is_orderby = models.SmallIntegerField(db_column='R_FIELD_IS_ORDERBY', blank=True, null=True)  # Field name made lowercase.
    r_field_method = models.SmallIntegerField(db_column='R_FIELD_METHOD', blank=True, null=True)  # Field name made lowercase.
    r_field_table_name = models.CharField(db_column='R_FIELD_TABLE_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    r_field_re_name = models.CharField(db_column='R_FIELD_RE_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    r_field_where_order = models.CharField(db_column='R_FIELD_WHERE_ORDER', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    r_field_output_name = models.CharField(db_column='R_FIELD_OUTPUT_NAME', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    r_field_output_title = models.CharField(db_column='R_FIELD_OUTPUT_TITLE', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    r_field_connet_name = models.CharField(db_column='R_FIELD_CONNET_NAME', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    r_field_company_id = models.BigIntegerField(db_column='R_FIELD_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    r_field_create_user_id = models.BigIntegerField(db_column='R_FIELD_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    r_field_create_time = models.DateTimeField(db_column='R_FIELD_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    r_field_modify_user_id = models.BigIntegerField(db_column='R_FIELD_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    r_field_modify_time = models.DateTimeField(db_column='R_FIELD_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'r_field_rec'


class Report(models.Model):
    report_id = models.BigIntegerField(db_column='REPORT_ID', primary_key=True)  # Field name made lowercase.
    report_name = models.CharField(db_column='REPORT_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    report_type = models.SmallIntegerField(db_column='REPORT_TYPE', blank=True, null=True)  # Field name made lowercase.
    report_parent_id = models.BigIntegerField(db_column='REPORT_PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    report_laycount = models.SmallIntegerField(db_column='REPORT_LAYCOUNT', blank=True, null=True)  # Field name made lowercase.
    report_ds = models.ForeignKey(Ds, db_column='REPORT_DS_ID', blank=True, null=True)  # Field name made lowercase.
    report_remark = models.CharField(db_column='REPORT_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    report_output_expr = models.CharField(db_column='REPORT_OUTPUT_EXPR', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    report_sum_expr = models.CharField(db_column='REPORT_SUM_EXPR', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    report_group_expr = models.CharField(db_column='REPORT_GROUP_EXPR', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    report_from_expr = models.CharField(db_column='REPORT_FROM_EXPR', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    report_where_expr = models.CharField(db_column='REPORT_WHERE_EXPR', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    report_having_expr = models.CharField(db_column='REPORT_HAVING_EXPR', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    report_orderby_expr = models.CharField(db_column='REPORT_ORDERBY_EXPR', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    report_company_id = models.BigIntegerField(db_column='REPORT_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    report_create_user_id = models.BigIntegerField(db_column='REPORT_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    report_create_time = models.DateTimeField(db_column='REPORT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    report_modify_user_id = models.BigIntegerField(db_column='REPORT_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    report_modify_time = models.DateTimeField(db_column='REPORT_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'report_rec'


class SearchMethodField(models.Model):
    s_m_f_id = models.BigIntegerField(db_column='S_M_F_ID', primary_key=True)  # Field name made lowercase.
    s_m_f_search_method = models.ForeignKey('SearchMethod', db_column='S_M_F_SEARCH_METHOD_ID', blank=True, null=True)  # Field name made lowercase.
    s_m_f_page_item = models.ForeignKey(PageItem, db_column='S_M_F_PAGE_ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    s_m_f_is_visible_flg = models.SmallIntegerField(db_column='S_M_F_IS_VISIBLE_FLG', blank=True, null=True)  # Field name made lowercase.
    s_m_f_is_order_flg = models.SmallIntegerField(db_column='S_M_F_IS_ORDER_FLG', blank=True, null=True)  # Field name made lowercase.
    s_m_f_is_filter_flg = models.SmallIntegerField(db_column='S_M_F_IS_FILTER_FLG', blank=True, null=True)  # Field name made lowercase.
    s_m_f_control = models.CharField(db_column='S_M_F_CONTROL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s_m_f_filter_output_title = models.CharField(db_column='S_M_F_FILTER_OUTPUT_TITLE', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    s_m_f_filter_output_name = models.CharField(db_column='S_M_F_FILTER_OUTPUT_NAME', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    s_m_f_filter_name = models.CharField(db_column='S_M_F_FILTER_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s_m_f_filter_where_order = models.CharField(db_column='S_M_F_FILTER_WHERE_ORDER', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    s_m_f_filter_table_name = models.CharField(db_column='S_M_F_FILTER_TABLE_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s_m_f_filter_method = models.SmallIntegerField(db_column='S_M_F_FILTER_METHOD', blank=True, null=True)  # Field name made lowercase.
    s_m_f_is_output_flg = models.SmallIntegerField(db_column='S_M_F_IS_OUTPUT_FLG', blank=True, null=True)  # Field name made lowercase.
    s_m_f_filter_connet_name = models.CharField(db_column='S_M_F_FILTER_CONNET_NAME', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    s_m_f_company_id = models.BigIntegerField(db_column='S_M_F_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    s_m_f_create_user_id = models.BigIntegerField(db_column='S_M_F_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    s_m_f_create_user_time = models.DateTimeField(db_column='S_M_F_CREATE_USER_TIME', blank=True, null=True)  # Field name made lowercase.
    s_m_f_modify_user_id = models.BigIntegerField(db_column='S_M_F_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    s_m_f_modify_time = models.DateTimeField(db_column='S_M_F_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    s_m_f_default_value = models.CharField(db_column='S_M_F_DEFAULT_VALUE', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'search_method_field_rec'


class SearchMethod(models.Model):
    search_method_id = models.BigIntegerField(db_column='SEARCH_METHOD_ID', primary_key=True)  # Field name made lowercase.
    search_method_name = models.CharField(db_column='SEARCH_METHOD_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    search_method_sys_menu = models.ForeignKey('SysMenu', db_column='SEARCH_METHOD_SYS_MENU_ID', blank=True, null=True)  # Field name made lowercase.
    search_method_doct = models.ForeignKey(Doct, db_column='SEARCH_METHOD_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    search_method_default_flg = models.SmallIntegerField(db_column='SEARCH_METHOD_DEFAULT_FLG', blank=True, null=True)  # Field name made lowercase.
    search_method_out_put_expr = models.CharField(db_column='SEARCH_METHOD_OUT_PUT_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    search_method_out_put_field = models.CharField(db_column='SEARCH_METHOD_OUT_PUT_FIELD', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    search_method_from_expr = models.CharField(db_column='SEARCH_METHOD_FROM_EXPR', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    search_method_where_expr = models.CharField(db_column='SEARCH_METHOD_WHERE_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    search_method_order_by_expr = models.CharField(db_column='SEARCH_METHOD_ORDER_BY_EXPR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    search_method_company_id = models.BigIntegerField(db_column='SEARCH_METHOD_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    search_method_create_user_id = models.BigIntegerField(db_column='SEARCH_METHOD_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    search_method_create_time = models.DateTimeField(db_column='SEARCH_METHOD_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    search_method_modify_user_id = models.BigIntegerField(db_column='SEARCH_METHOD_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    search_method_modify_time = models.DateTimeField(db_column='SEARCH_METHOD_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'search_method_rec'

class Store(models.Model):
    store_id = models.BigIntegerField(db_column='STORE_ID', primary_key=True)  # Field name made lowercase.
    store_member = models.ForeignKey(Member, db_column='STORE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='STORE_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    store_full_name = models.CharField(db_column='STORE_FULL_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    store_logo = models.CharField(db_column='STORE_LOGO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    store_sarea = models.ForeignKey(Area, db_column='STORE_SAREA_ID', blank=True, null=True)  # Field name made lowercase.
    store_carea = models.ForeignKey(Area, db_column='STORE_CAREA_ID', blank=True, null=True)  # Field name made lowercase.
    store_xarea = models.ForeignKey(Area, db_column='STORE_XAREA_ID', blank=True, null=True)  # Field name made lowercase.
    store_address = models.CharField(db_column='STORE_ADDRESS', max_length=128, blank=True, null=True)  # Field name made lowercase.
    store_zipcode = models.CharField(db_column='STORE_ZIPCODE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    store_phone = models.CharField(db_column='STORE_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_fax = models.CharField(db_column='STORE_FAX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_contact = models.CharField(db_column='STORE_CONTACT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_contact_tel = models.CharField(db_column='STORE_CONTACT_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_contact_phone = models.CharField(db_column='STORE_CONTACT_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_type = models.SmallIntegerField(db_column='STORE_TYPE', blank=True, null=True)  # Field name made lowercase.
    store_flg = models.SmallIntegerField(db_column='STORE_FLG', blank=True, null=True)  # Field name made lowercase.
    store_check_user_id = models.BigIntegerField(db_column='STORE_CHECK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    store_check_desc = models.CharField(db_column='STORE_CHECK_DESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    store_check_time = models.DateTimeField(db_column='STORE_CHECK_TIME', blank=True, null=True)  # Field name made lowercase.
    store_create_user_id = models.BigIntegerField(db_column='STORE_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    store_create_time = models.DateTimeField(db_column='STORE_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    store_modify_user_id = models.BigIntegerField(db_column='STORE_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    store_modify_time = models.DateTimeField(db_column='STORE_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    store_is_broker = models.BigIntegerField(db_column='STORE_IS_BROKER', blank=True, null=True)  # Field name made lowercase.
    # class Meta:
    #     managed = False
    #     db_table = 'store_rec'


class SodAddress(models.Model):
    sod_address_id = models.BigIntegerField(db_column='SOD_ADDRESS_ID', primary_key=True)  # Field name made lowercase.
    sod_address_sod = models.ForeignKey('Sod', db_column='SOD_ADDRESS_SOD_ID', blank=True, null=True)  # Field name made lowercase.
    sod_address_user = models.CharField(db_column='SOD_ADDRESS_USER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sod_parea_id = models.BigIntegerField(db_column='SOD_PAREA_ID', blank=True, null=True)  # Field name made lowercase.
    sod_carea_id = models.BigIntegerField(db_column='SOD_CAREA_ID', blank=True, null=True)  # Field name made lowercase.
    sod_rarea_id = models.BigIntegerField(db_column='SOD_RAREA_ID', blank=True, null=True)  # Field name made lowercase.
    sod_address_no = models.CharField(db_column='SOD_ADDRESS_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sod_address_tel = models.CharField(db_column='SOD_ADDRESS_TEL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sod_address_post = models.CharField(db_column='SOD_ADDRESS_POST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sod_address_remark = models.CharField(db_column='SOD_ADDRESS_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sod_address_user_cid = models.CharField(db_column='SOD_ADDRESS_USER_CID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sod_address'


class SodIncome(models.Model):
    sod_income_id = models.BigIntegerField(db_column='SOD_INCOME_ID', primary_key=True)  # Field name made lowercase.
    sod_income_date = models.DateField(db_column='SOD_INCOME_DATE')  # Field name made lowercase.
    sod_income_sod_id = models.BigIntegerField(db_column='SOD_INCOME_SOD_ID')  # Field name made lowercase.
    sod_income_sod_item_id = models.BigIntegerField(db_column='SOD_INCOME_SOD_ITEM_ID')  # Field name made lowercase.
    sod_income_sod_type = models.BigIntegerField(db_column='SOD_INCOME_SOD_TYPE')  # Field name made lowercase.
    sod_income_type = models.IntegerField(db_column='SOD_INCOME_TYPE')  # Field name made lowercase.
    sod_income_member_id = models.BigIntegerField(db_column='SOD_INCOME_MEMBER_ID')  # Field name made lowercase.
    sod_income_tmn_id = models.BigIntegerField(db_column='SOD_INCOME_TMN_ID')  # Field name made lowercase.
    sod_income_iamt = models.DecimalField(db_column='SOD_INCOME_IAMT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    sod_income_oamt = models.DecimalField(db_column='SOD_INCOME_OAMT', max_digits=12, decimal_places=2)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sod_income_rec'

class Tmns(models.Model):
    tmn_id = models.BigIntegerField(db_column='TMN_ID', primary_key=True)  # Field name made lowercase.
    tmn_code = models.CharField(db_column='TMN_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmn_name = models.CharField(db_column='TMN_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tmn_member = models.ForeignKey(Member, db_column='TMN_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_first_member_id = models.BigIntegerField(db_column='TMN_FIRST_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_second_member = models.ForeignKey(Member, db_column='TMN_SECOND_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_store_id = models.BigIntegerField(db_column='TMN_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_type = models.SmallIntegerField(db_column='TMN_TYPE', blank=True, null=True)  # Field name made lowercase.
    tmn_url = models.CharField(db_column='TMN_URL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tmn_manager = models.CharField(db_column='TMN_MANAGER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmn_tel = models.CharField(db_column='TMN_TEL', max_length=120, blank=True, null=True)  # Field name made lowercase.
    tmn_address = models.CharField(db_column='TMN_ADDRESS', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tmn_stat = models.BigIntegerField(db_column='TMN_STAT', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'tmn_rec'

class Sods(models.Model):
    sod_id = models.BigIntegerField(db_column='SOD_ID', primary_key=True)  # Field name made lowercase.
    sod_doct = models.ForeignKey(Doct, db_column='SOD_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    sod_member = models.ForeignKey(Member, db_column='SOD_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_tmn = models.ForeignKey(Tmns, db_column='SOD_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    sod_no = models.CharField(db_column='SOD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sod_date = models.DateTimeField(db_column='SOD_DATE', blank=True, null=True)  # Field name made lowercase.
    sod_type = models.IntegerField(db_column='SOD_TYPE', blank=True, null=True)  # Field name made lowercase.
    sod_stat = models.IntegerField(db_column='SOD_STAT', blank=True, null=True)  # Field name made lowercase.
    sod_pay_type = models.IntegerField(db_column='SOD_PAY_TYPE', blank=True, null=True)  # Field name made lowercase.
    sod_pay_flg = models.IntegerField(db_column='SOD_PAY_FLG', blank=True, null=True)  # Field name made lowercase.
    sod_pay_no = models.CharField(db_column='SOD_PAY_NO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sod_qty = models.DecimalField(db_column='SOD_QTY', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_amt = models.DecimalField(db_column='SOD_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_pay_time = models.DateTimeField(db_column='SOD_PAY_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_tariff = models.DecimalField(db_column='SOD_TARIFF', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_ccf = models.DecimalField(db_column='SOD_CCF', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_uex = models.DecimalField(db_column='SOD_UEX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_ration1 = models.DecimalField(db_column='SOD_RATION1', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_ration2 = models.DecimalField(db_column='SOD_RATION2', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_ration3 = models.DecimalField(db_column='SOD_RATION3', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_rc_flg = models.IntegerField(db_column='SOD_RC_FLG', blank=True, null=True)  # Field name made lowercase.
    sod_sk_flg = models.IntegerField(db_column='SOD_SK_FLG', blank=True, null=True)  # Field name made lowercase.
    sod_sk_user_id = models.BigIntegerField(db_column='SOD_SK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_sk_time = models.DateTimeField(db_column='SOD_SK_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_close_flg = models.IntegerField(db_column='SOD_CLOSE_FLG', blank=True, null=True)  # Field name made lowercase.
    sod_close_time = models.DateTimeField(db_column='SOD_CLOSE_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_create_member_id = models.BigIntegerField(db_column='SOD_CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_create_time = models.DateTimeField(db_column='SOD_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_modify_member_id = models.BigIntegerField(db_column='SOD_MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_modify_time = models.DateTimeField(db_column='SOD_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    store = models.ForeignKey(Store, db_column='STORE_ID', blank=True, null=True)
    store_member = models.ForeignKey(Member, db_column='STORE_MEMBER_ID', blank=True, null=True)
    agent = models.ForeignKey(Member, db_column='AGENT_ID', blank=True, null=True)
    # class Meta:
    #     managed = False
    #     db_table = 'sod_rec'

class SodItem(models.Model):
    sod_item_id = models.BigIntegerField(db_column='SOD_ITEM_ID', primary_key=True)  # Field name made lowercase.
    sod = models.ForeignKey(Sods,db_column='SOD_ITEM_SOD_ID', blank=True, null=True)  # Field name made lowercase.
    #sod_item_le_id = models.BigIntegerField(db_column='SOD_ITEM_LE_ID', blank=True, null=True)  # Field name made lowercase.
    le = models.ForeignKey(Le,db_column='SOD_ITEM_LE_ID', blank=True, null=True)  # Field name made lowercase.
    sod_item_store = models.ForeignKey(Stores,db_column='SOD_ITEM_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    sod_item_member = models.ForeignKey(Member,db_column='SOD_ITEM_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_item_tmn_id = models.BigIntegerField(db_column='SOD_ITEM_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    sod_item_qty = models.DecimalField(db_column='SOD_ITEM_QTY', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_item_price = models.DecimalField(db_column='SOD_ITEM_PRICE', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    sod_item_amt = models.DecimalField(db_column='SOD_ITEM_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_item_from_id = models.BigIntegerField(db_column='SOD_ITEM_FROM_ID', blank=True, null=True)  # Field name made lowercase.
    sod_item_from_item_id = models.BigIntegerField(db_column='SOD_ITEM_FROM_ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    sod_item_remark = models.CharField(db_column='SOD_ITEM_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sod_item_rc_type = models.IntegerField(db_column='SOD_ITEM_RC_TYPE', blank=True, null=True)  # Field name made lowercase.
    sod_item_rc_no = models.IntegerField(db_column='SOD_ITEM_RC_NO', blank=True, null=True)  # Field name made lowercase.
    sod_item_rc_qty = models.DecimalField(db_column='SOD_ITEM_RC_QTY', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_item_rc_amt = models.DecimalField(db_column='SOD_ITEM_RC_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_item_no_type = models.IntegerField(db_column='SOD_ITEM_NO_TYPE', blank=True, null=True)  # Field name made lowercase.
    sod_item_pay_brank = models.CharField(db_column='SOD_ITEM_PAY_BRANK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sod_item_pay_no = models.CharField(db_column='SOD_ITEM_PAY_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sod_item_pay_name = models.CharField(db_column='SOD_ITEM_PAY_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sod_item_erp_no = models.CharField(db_column='SOD_ITEM_ERP_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sod_item_sh_no = models.CharField(db_column='SOD_ITEM_SH_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sod_rc_member_id = models.BigIntegerField(db_column='SOD_RC_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_item_rc_date = models.DateTimeField(db_column='SOD_ITEM_RC_DATE', blank=True, null=True)  # Field name made lowercase.
    sod_item_create_member_id = models.BigIntegerField(db_column='SOD_ITEM_CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_item_create_time = models.DateTimeField(db_column='SOD_ITEM_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_item_modify_member_id = models.BigIntegerField(db_column='SOD_ITEM_MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_item_modify_time = models.DateTimeField(db_column='SOD_ITEM_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_item_express_no = models.CharField(db_column='SOD_ITEM_EXPRESS_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sod_item_rec'

    def get_sold_sum(self):
         return sum([self.sod_item_qty])

class Sod(models.Model):
    sod_id = models.BigIntegerField(db_column='SOD_ID', primary_key=True)  # Field name made lowercase.
    sod_doct = models.ForeignKey(Doct, db_column='SOD_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    sod_member = models.ForeignKey(Member, db_column='SOD_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_tmn = models.ForeignKey(Tmns, db_column='SOD_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    sod_no = models.CharField(db_column='SOD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sod_date = models.DateTimeField(db_column='SOD_DATE', blank=True, null=True)  # Field name made lowercase.
    sod_type = models.IntegerField(db_column='SOD_TYPE', blank=True, null=True)  # Field name made lowercase.
    sod_stat = models.IntegerField(db_column='SOD_STAT', blank=True, null=True)  # Field name made lowercase.
    sod_pay_type = models.IntegerField(db_column='SOD_PAY_TYPE', blank=True, null=True)  # Field name made lowercase.
    sod_pay_flg = models.IntegerField(db_column='SOD_PAY_FLG', blank=True, null=True)  # Field name made lowercase.
    sod_pay_no = models.CharField(db_column='SOD_PAY_NO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sod_qty = models.DecimalField(db_column='SOD_QTY', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_amt = models.DecimalField(db_column='SOD_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_pay_time = models.DateTimeField(db_column='SOD_PAY_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_tariff = models.DecimalField(db_column='SOD_TARIFF', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_ccf = models.DecimalField(db_column='SOD_CCF', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_uex = models.DecimalField(db_column='SOD_UEX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_ration1 = models.DecimalField(db_column='SOD_RATION1', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_ration2 = models.DecimalField(db_column='SOD_RATION2', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_ration3 = models.DecimalField(db_column='SOD_RATION3', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sod_rc_flg = models.IntegerField(db_column='SOD_RC_FLG', blank=True, null=True)  # Field name made lowercase.
    sod_sk_flg = models.IntegerField(db_column='SOD_SK_FLG', blank=True, null=True)  # Field name made lowercase.
    sod_sk_user_id = models.BigIntegerField(db_column='SOD_SK_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_sk_time = models.DateTimeField(db_column='SOD_SK_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_close_flg = models.IntegerField(db_column='SOD_CLOSE_FLG', blank=True, null=True)  # Field name made lowercase.
    sod_close_time = models.DateTimeField(db_column='SOD_CLOSE_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_create_member_id = models.BigIntegerField(db_column='SOD_CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_create_time = models.DateTimeField(db_column='SOD_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sod_modify_member_id = models.BigIntegerField(db_column='SOD_MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    sod_modify_time = models.DateTimeField(db_column='SOD_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    store = models.ForeignKey(Store, db_column='STORE_ID', blank=True, null=True)
    store_member = models.ForeignKey(Member, db_column='STORE_MEMBER_ID', blank=True, null=True)
    agent = models.ForeignKey(Member, db_column='AGENT_ID', blank=True, null=True)
    tmn = models.ForeignKey(Tmns, db_column='SOD_TMN_ID', blank=True, null=True)
    sod_tmn_id = models.IntegerField(db_column='SOD_TMN_ID', blank=True, null=True)  # Field name made lowercase.
    sod_remark = models.TextField(db_column='SOD_REMARK', max_length=2220, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sod_rec'


class SysBtn(models.Model):
    sys_btn_id = models.BigIntegerField(db_column='SYS_BTN_ID', primary_key=True)  # Field name made lowercase.
    sys_btn_code = models.CharField(db_column='SYS_BTN_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_btn_name = models.CharField(db_column='SYS_BTN_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_btn_type = models.SmallIntegerField(db_column='SYS_BTN_TYPE', blank=True, null=True)  # Field name made lowercase.
    sys_btn_img_url = models.CharField(db_column='SYS_BTN_IMG_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_btn_sort_step = models.SmallIntegerField(db_column='SYS_BTN_SORT_STEP', blank=True, null=True)  # Field name made lowercase.
    sys_btn_remark = models.CharField(db_column='SYS_BTN_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_btn_create_user_id = models.BigIntegerField(db_column='SYS_BTN_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_btn_create_time = models.DateTimeField(db_column='SYS_BTN_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_btn_modify_user_id = models.BigIntegerField(db_column='SYS_BTN_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_btn_modify_time = models.DateTimeField(db_column='SYS_BTN_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_btn_rec'


class SysDocLinkGen(models.Model):
    sys_doc_link_gen_id = models.BigIntegerField(db_column='SYS_DOC_LINK_GEN_ID', primary_key=True)  # Field name made lowercase.
    sys_doc_link_gen_type = models.SmallIntegerField(db_column='SYS_DOC_LINK_GEN_TYPE', blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_out_put_expr = models.CharField(db_column='SYS_DOC_LINK_GEN_OUT_PUT_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_from_expr = models.CharField(db_column='SYS_DOC_LINK_GEN_FROM_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_where_expr = models.CharField(db_column='SYS_DOC_LINK_GEN_WHERE_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_fix_where = models.CharField(db_column='SYS_DOC_LINK_GEN_FIX_WHERE', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_order_expr = models.CharField(db_column='SYS_DOC_LINK_GEN_ORDER_EXPR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_company_id = models.BigIntegerField(db_column='SYS_DOC_LINK_GEN_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_create_u_id = models.BigIntegerField(db_column='SYS_DOC_LINK_GEN_CREATE_U_ID', blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_create_time = models.DateTimeField(db_column='SYS_DOC_LINK_GEN_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_modify_u_id = models.BigIntegerField(db_column='SYS_DOC_LINK_GEN_MODIFY_U_ID', blank=True, null=True)  # Field name made lowercase.
    sys_doc_link_gen_modify_time = models.DateTimeField(db_column='SYS_DOC_LINK_GEN_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_doc_link_gen_rec'


class SysDoctLink(models.Model):
    sys_doct_link_id = models.BigIntegerField(db_column='SYS_DOCT_LINK_ID', primary_key=True)  # Field name made lowercase.
    doct_link_from_doct_id = models.BigIntegerField(db_column='DOCT_LINK_FROM_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    doct_link_doct_id = models.BigIntegerField(db_column='DOCT_LINK_DOCT_ID', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_doct_link_rec'


class SysDoct(models.Model):
    sys_doct_id = models.BigIntegerField(db_column='SYS_DOCT_ID', primary_key=True)  # Field name made lowercase.
    sys_doct_doc_gen_id = models.BigIntegerField(db_column='SYS_DOCT_DOC_GEN_ID', blank=True, null=True)  # Field name made lowercase.
    sys_doct_sys_menu_id = models.BigIntegerField(db_column='SYS_DOCT_SYS_MENU_ID', blank=True, null=True)  # Field name made lowercase.
    sys_doct_name = models.CharField(db_column='SYS_DOCT_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_doct_gen_flg = models.SmallIntegerField(db_column='SYS_DOCT_GEN_FLG', blank=True, null=True)  # Field name made lowercase.
    sys_doct_remark = models.CharField(db_column='SYS_DOCT_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_doct_create_user_id = models.BigIntegerField(db_column='SYS_DOCT_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_doct_create_time = models.DateTimeField(db_column='SYS_DOCT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_doct_modify_user_id = models.BigIntegerField(db_column='SYS_DOCT_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_doct_modify_time = models.DateTimeField(db_column='SYS_DOCT_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_doct_rec'


class SysFlag(models.Model):
    sys_flag_id = models.BigIntegerField(db_column='SYS_FLAG_ID', primary_key=True)  # Field name made lowercase.
    sys_flag_parent_id = models.BigIntegerField(db_column='SYS_FLAG_PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    sys_flag_code = models.CharField(db_column='SYS_FLAG_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_flag_name = models.CharField(db_column='SYS_FLAG_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sys_flag_type = models.SmallIntegerField(db_column='SYS_FLAG_TYPE', blank=True, null=True)  # Field name made lowercase.
    sys_flag_value = models.CharField(db_column='SYS_FLAG_VALUE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sys_flag_desc = models.CharField(db_column='SYS_FLAG_DESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_flag_laycount = models.SmallIntegerField(db_column='SYS_FLAG_LAYCOUNT', blank=True, null=True)  # Field name made lowercase.
    sys_flag_sort_step = models.BigIntegerField(db_column='SYS_FLAG_SORT_STEP', blank=True, null=True)  # Field name made lowercase.
    sys_flag_create_user_id = models.BigIntegerField(db_column='SYS_FLAG_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_flag_create_time = models.DateTimeField(db_column='SYS_FLAG_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_flag_modify_user_id = models.BigIntegerField(db_column='SYS_FLAG_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_flag_modify_time = models.DateTimeField(db_column='SYS_FLAG_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_flag_rec'


class SysGenField(models.Model):
    sys_gen_field_id = models.BigIntegerField(db_column='SYS_GEN_FIELD_ID', primary_key=True)  # Field name made lowercase.
    sys_gen_field_sys_doc_link = models.ForeignKey(SysDocLinkGen, db_column='SYS_GEN_FIELD_SYS_DOC_LINK_ID', blank=True, null=True)  # Field name made lowercase.
    sys_gen_field_s_page_iten = models.ForeignKey('SysPageItem', db_column='SYS_GEN_FIELD_S_PAGE_ITEN_ID', blank=True, null=True)  # Field name made lowercase.
    sys_gen_field_is_visible_flg = models.SmallIntegerField(db_column='SYS_GEN_FIELD_IS_VISIBLE_FLG', blank=True, null=True)  # Field name made lowercase.
    sys_gen_field_is_filter_flg = models.SmallIntegerField(db_column='SYS_GEN_FIELD_IS_FILTER_FLG', blank=True, null=True)  # Field name made lowercase.
    sys_gen_field_is_order_flg = models.SmallIntegerField(db_column='SYS_GEN_FIELD_IS_ORDER_FLG', blank=True, null=True)  # Field name made lowercase.
    sys_gen_field_company_id = models.BigIntegerField(db_column='SYS_GEN_FIELD_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    sys_gen_field_create_user_id = models.BigIntegerField(db_column='SYS_GEN_FIELD_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_gen_field_create_time = models.DateTimeField(db_column='SYS_GEN_FIELD_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_gen_field_modify_user_id = models.BigIntegerField(db_column='SYS_GEN_FIELD_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_gen_field_modify_time = models.DateTimeField(db_column='SYS_GEN_FIELD_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_gen_field_rec'


class SysLog(models.Model):
    sys_log_id = models.BigIntegerField(db_column='SYS_LOG_ID', primary_key=True)  # Field name made lowercase.
    sys_log_sys_menu_id = models.BigIntegerField(db_column='SYS_LOG_SYS_MENU_ID', blank=True, null=True)  # Field name made lowercase.
    sys_log_doct_id = models.BigIntegerField(db_column='SYS_LOG_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    sys_log_doc_id = models.BigIntegerField(db_column='SYS_LOG_DOC_ID', blank=True, null=True)  # Field name made lowercase.
    sys_log_desc = models.CharField(db_column='SYS_LOG_DESC', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    sys_log_action = models.BigIntegerField(db_column='SYS_LOG_ACTION', blank=True, null=True)  # Field name made lowercase.
    sys_log_user_id = models.BigIntegerField(db_column='SYS_LOG_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_log_date_time = models.DateTimeField(db_column='SYS_LOG_DATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_log_company_id = models.BigIntegerField(db_column='SYS_LOG_COMPANY_ID', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_log_rec'


class SysMenuBtn(models.Model):
    sys_menu_btn_id = models.BigIntegerField(db_column='SYS_MENU_BTN_ID', primary_key=True)  # Field name made lowercase.
    sys_menu_btn_menu_id = models.BigIntegerField(db_column='SYS_MENU_BTN_MENU_ID', blank=True, null=True)  # Field name made lowercase.
    sys_menu_btn_btn = models.ForeignKey(SysBtn, db_column='SYS_MENU_BTN_BTN_ID', blank=True, null=True)  # Field name made lowercase.
    sys_menu_btn_sort_step = models.SmallIntegerField(db_column='SYS_MENU_BTN_SORT_STEP', blank=True, null=True)  # Field name made lowercase.
    sys_menu_btn_create_user_id = models.BigIntegerField(db_column='SYS_MENU_BTN_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_menu_btn_create_time = models.DateTimeField(db_column='SYS_MENU_BTN_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_menu_btn_modify_user_id = models.BigIntegerField(db_column='SYS_MENU_BTN_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_menu_btn_modify_time = models.DateTimeField(db_column='SYS_MENU_BTN_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_menu_btn_rec'


class SysMenu(models.Model):
    sys_menu_id = models.BigIntegerField(db_column='SYS_MENU_ID', primary_key=True)  # Field name made lowercase.
    sys_menu_code = models.CharField(db_column='SYS_MENU_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_menu_name = models.CharField(db_column='SYS_MENU_NAME', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.
    sys_menu_parent = models.ForeignKey('self', db_column='SYS_MENU_PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    sys_menu_type = models.SmallIntegerField(db_column='SYS_MENU_TYPE', blank=True, null=True)  # Field name made lowercase.
    sys_menu_flg = models.SmallIntegerField(db_column='SYS_MENU_FLG', blank=True, null=True)  # Field name made lowercase.
    sys_menu_url = models.CharField(db_column='SYS_MENU_URL', max_length=512, blank=True, null=True)  # Field name made lowercase.
    sys_menu_laycount = models.CharField(db_column='SYS_MENU_LAYCOUNT', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sys_menu_sort_step = models.SmallIntegerField(db_column='SYS_MENU_SORT_STEP', blank=True, null=True)  # Field name made lowercase.
    sys_menu_remark = models.SmallIntegerField(db_column='SYS_MENU_REMARK', blank=True, null=True)  # Field name made lowercase.
    sys_menu_create_user_id = models.BigIntegerField(db_column='SYS_MENU_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_menu_create_time = models.DateTimeField(db_column='SYS_MENU_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_menu_modify_user_id = models.BigIntegerField(db_column='SYS_MENU_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_menu_modify_time = models.DateTimeField(db_column='SYS_MENU_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_menu_rec'


class SysPageBlock(models.Model):
    sys_page_block_id = models.BigIntegerField(db_column='SYS_PAGE_BLOCK_ID', primary_key=True)  # Field name made lowercase.
    sys_page_block_sys_page = models.ForeignKey('SysPage', db_column='SYS_PAGE_BLOCK_SYS_PAGE_ID', blank=True, null=True)  # Field name made lowercase.
    sys_page_block_seq = models.SmallIntegerField(db_column='SYS_PAGE_BLOCK_SEQ', blank=True, null=True)  # Field name made lowercase.
    sys_page_block_table_type = models.SmallIntegerField(db_column='SYS_PAGE_BLOCK_TABLE_TYPE', blank=True, null=True)  # Field name made lowercase.
    sys_page_block_no = models.CharField(db_column='SYS_PAGE_BLOCK_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sys_page_block_code = models.CharField(db_column='SYS_PAGE_BLOCK_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sys_page_block_name = models.CharField(db_column='SYS_PAGE_BLOCK_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sys_page_block_table_code = models.CharField(db_column='SYS_PAGE_BLOCK_TABLE_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sys_page_block_table_name = models.CharField(db_column='SYS_PAGE_BLOCK_TABLE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sys_page_block_show_flg = models.SmallIntegerField(db_column='SYS_PAGE_BLOCK_SHOW_FLG', blank=True, null=True)  # Field name made lowercase.
    sys_page_block_sum_flg = models.SmallIntegerField(db_column='SYS_PAGE_BLOCK_SUM_FLG', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_page_block_rec'


class SysPageItem(models.Model):
    sys_page_item_id = models.BigIntegerField(db_column='SYS_PAGE_ITEM_ID', primary_key=True)  # Field name made lowercase.
    sys_page_item_page_block = models.ForeignKey(SysPageBlock, db_column='SYS_PAGE_ITEM_PAGE_BLOCK_ID', blank=True, null=True)  # Field name made lowercase.
    sys_page_item_seq = models.SmallIntegerField(db_column='SYS_PAGE_ITEM_SEQ', blank=True, null=True)  # Field name made lowercase.
    sys_page_item_field_code = models.CharField(db_column='SYS_PAGE_ITEM_FIELD_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_title = models.CharField(db_column='SYS_PAGE_ITEM_TITLE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_code = models.CharField(db_column='SYS_PAGE_ITEM_CODE', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_name = models.CharField(db_column='SYS_PAGE_ITEM_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_table = models.CharField(db_column='SYS_PAGE_ITEM_TABLE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_second_table = models.CharField(db_column='SYS_PAGE_ITEM_SECOND_TABLE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_type = models.CharField(db_column='SYS_PAGE_ITEM_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_wid = models.SmallIntegerField(db_column='SYS_PAGE_ITEM_WID', blank=True, null=True)  # Field name made lowercase.
    sys_page_item_dig = models.SmallIntegerField(db_column='SYS_PAGE_ITEM_DIG', blank=True, null=True)  # Field name made lowercase.
    sys_page_item_control = models.CharField(db_column='SYS_PAGE_ITEM_CONTROL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_val_flg = models.SmallIntegerField(db_column='SYS_PAGE_ITEM_VAL_FLG', blank=True, null=True)  # Field name made lowercase.
    sys_page_item_val_str = models.CharField(db_column='SYS_PAGE_ITEM_VAL_STR', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_is_sum = models.SmallIntegerField(db_column='SYS_PAGE_ITEM_IS_SUM', blank=True, null=True)  # Field name made lowercase.
    sys_page_item_is_edit = models.SmallIntegerField(db_column='SYS_PAGE_ITEM_IS_EDIT', blank=True, null=True)  # Field name made lowercase.
    sys_page_item_is_visible = models.SmallIntegerField(db_column='SYS_PAGE_ITEM_IS_VISIBLE', blank=True, null=True)  # Field name made lowercase.
    sys_page_item_tag = models.CharField(db_column='SYS_PAGE_ITEM_TAG', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sys_page_item_where_str = models.CharField(db_column='SYS_PAGE_ITEM_WHERE_STR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_page_item_rec'


class SysPage(models.Model):
    sys_page_id = models.BigIntegerField(db_column='SYS_PAGE_ID', primary_key=True)  # Field name made lowercase.
    sys_page_sys_menu_id = models.BigIntegerField(db_column='SYS_PAGE_SYS_MENU_ID', blank=True, null=True)  # Field name made lowercase.
    sys_page_sys_doct = models.ForeignKey(SysDoct, db_column='SYS_PAGE_SYS_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    sys_page_type = models.SmallIntegerField(db_column='SYS_PAGE_TYPE', blank=True, null=True)  # Field name made lowercase.
    sys_page_code = models.CharField(db_column='SYS_PAGE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_page_name = models.CharField(db_column='SYS_PAGE_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_page_remark = models.CharField(db_column='SYS_PAGE_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_page_create_user_id = models.BigIntegerField(db_column='SYS_PAGE_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_page_create_time = models.DateTimeField(db_column='SYS_PAGE_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_page_modify_user_id = models.BigIntegerField(db_column='SYS_PAGE_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_page_modify_time = models.DateTimeField(db_column='SYS_PAGE_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_page_rec'


class SysRoleMenu(models.Model):
    sys_role_menu_id = models.BigIntegerField(db_column='SYS_ROLE_MENU_ID', primary_key=True)  # Field name made lowercase.
    sys_role_menu_sys_role = models.ForeignKey('SysRole', db_column='SYS_ROLE_MENU_SYS_ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    sys_role_menu_sys_menu_id = models.BigIntegerField(db_column='SYS_ROLE_MENU_SYS_MENU_ID', blank=True, null=True)  # Field name made lowercase.
    sys_role_menu_doct_id = models.BigIntegerField(db_column='SYS_ROLE_MENU_DOCT_ID', blank=True, null=True)  # Field name made lowercase.
    sys_role_menu_sys_btn = models.ForeignKey(SysBtn, db_column='SYS_ROLE_MENU_SYS_BTN_ID', blank=True, null=True)  # Field name made lowercase.
    sys_role_menu_create_user_id = models.BigIntegerField(db_column='SYS_ROLE_MENU_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_role_menu_create_time = models.DateTimeField(db_column='SYS_ROLE_MENU_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_role_menu_modify_user_id = models.BigIntegerField(db_column='SYS_ROLE_MENU_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_role_menu_modify_time = models.DateTimeField(db_column='SYS_ROLE_MENU_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_role_menu_rec'


class SysRole(models.Model):
    sys_role_id = models.BigIntegerField(db_column='SYS_ROLE_ID', primary_key=True)  # Field name made lowercase.
    sys_role_code = models.CharField(db_column='SYS_ROLE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_role_name = models.CharField(db_column='SYS_ROLE_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sys_role_remark = models.CharField(db_column='SYS_ROLE_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sys_role_create_user_id = models.BigIntegerField(db_column='SYS_ROLE_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_role_create_time = models.DateTimeField(db_column='SYS_ROLE_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    sys_role_modify_user_id = models.BigIntegerField(db_column='SYS_ROLE_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    sys_role_modify_time = models.DateTimeField(db_column='SYS_ROLE_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'sys_role_rec'


class Tcode(models.Model):
    tcode_id = models.BigIntegerField(db_column='TCODE_ID', primary_key=True)  # Field name made lowercase.
    tcode_code = models.CharField(db_column='TCODE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tcode_name = models.CharField(db_column='TCODE_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tcode_role = models.ForeignKey(SysRole, db_column='TCODE_ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    tcode_create_user_id = models.BigIntegerField(db_column='TCODE_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    tcode_create_time = models.DateTimeField(db_column='TCODE_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    tcode_modify_user_id = models.BigIntegerField(db_column='TCODE_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    tcode_modify_time = models.DateTimeField(db_column='TCODE_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'tcode_rec'


class TmnIncomeDetail(models.Model):
    tmn_income_detail_id = models.AutoField(db_column='TMN_INCOME_DETAIL_ID', primary_key=True)  # Field name made lowercase.
    tmn_income_detail_tmn_id = models.IntegerField(db_column='TMN_INCOME_DETAIL_TMN_ID')  # Field name made lowercase.
    tmn_income_detail_member_id = models.IntegerField(db_column='TMN_INCOME_DETAIL_MEMBER_ID')  # Field name made lowercase.
    tmn_income_detail_sod_id = models.IntegerField(db_column='TMN_INCOME_DETAIL_SOD_ID')  # Field name made lowercase.
    tmn_income_detail_date = models.DateField(db_column='TMN_INCOME_DETAIL_DATE')  # Field name made lowercase.
    tmn_income_detail_iamt1 = models.DecimalField(db_column='TMN_INCOME_DETAIL_IAMT1', max_digits=12, decimal_places=2)  # Field name made lowercase.
    tmn_income_detail_iamt2 = models.DecimalField(db_column='TMN_INCOME_DETAIL_IAMT2', max_digits=12, decimal_places=2)  # Field name made lowercase.
    tmn_income_detail_iamt3 = models.DecimalField(db_column='TMN_INCOME_DETAIL_IAMT3', max_digits=12, decimal_places=2)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'tmn_income_detail_rec'


class TmnIncome(models.Model):
    tmn_income_id = models.BigIntegerField(db_column='TMN_INCOME_ID', primary_key=True)  # Field name made lowercase.
    tmn_income_date = models.DateField(db_column='TMN_INCOME_DATE')  # Field name made lowercase.
    tmn_income_member_id = models.BigIntegerField(db_column='TMN_INCOME_MEMBER_ID')  # Field name made lowercase.
    tmn_income_tmn_id = models.BigIntegerField(db_column='TMN_INCOME_TMN_ID')  # Field name made lowercase.
    tmn_income_type = models.IntegerField(db_column='TMN_INCOME_TYPE')  # Field name made lowercase.
    tmn_income_lamt = models.DecimalField(db_column='TMN_INCOME_LAMT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    tmn_income_iamt = models.DecimalField(db_column='TMN_INCOME_IAMT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    tmn_income_oamt = models.DecimalField(db_column='TMN_INCOME_OAMT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    tmn_income_amt = models.DecimalField(db_column='TMN_INCOME_AMT', max_digits=12, decimal_places=2)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'tmn_income_rec'


class Tmn(models.Model):
    tmn_id = models.BigIntegerField(db_column='TMN_ID', primary_key=True)  # Field name made lowercase.
    tmn_code = models.CharField(db_column='TMN_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmn_name = models.CharField(db_column='TMN_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tmn_member = models.ForeignKey(Member, db_column='TMN_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_first_member_id = models.BigIntegerField(db_column='TMN_FIRST_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_second_member = models.ForeignKey(Member, db_column='TMN_SECOND_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_store_id = models.BigIntegerField(db_column='TMN_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_type = models.SmallIntegerField(db_column='TMN_TYPE', blank=True, null=True)  # Field name made lowercase.
    tmn_url = models.CharField(db_column='TMN_URL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tmn_manager = models.CharField(db_column='TMN_MANAGER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmn_tel = models.CharField(db_column='TMN_TEL', max_length=120, blank=True, null=True)  # Field name made lowercase.
    tmn_address = models.CharField(db_column='TMN_ADDRESS', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tmn_stat = models.BigIntegerField(db_column='TMN_STAT', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'tmn_rec'


class Unit(models.Model):
    unit_id = models.BigIntegerField(db_column='UNIT_ID', primary_key=True)  # Field name made lowercase.
    unit_code = models.CharField(db_column='UNIT_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    unit_name = models.CharField(db_column='UNIT_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    unit_stat = models.SmallIntegerField(db_column='UNIT_STAT', blank=True, null=True)  # Field name made lowercase.
    unit_remark = models.CharField(db_column='UNIT_REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit_create_user_id = models.IntegerField(db_column='UNIT_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    unit_create_time = models.DateTimeField(db_column='UNIT_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    unit_modify_user_id = models.IntegerField(db_column='UNIT_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    unit_modify_time = models.DateTimeField(db_column='UNIT_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'unit_rec'


class User(models.Model):
    user_id = models.BigIntegerField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    user_code = models.CharField(db_column='USER_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    user_full_name = models.CharField(db_column='USER_FULL_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    user_password = models.CharField(db_column='USER_PASSWORD', max_length=128, blank=True, null=True)  # Field name made lowercase.
    user_phone = models.CharField(db_column='USER_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_type = models.SmallIntegerField(db_column='USER_TYPE', blank=True, null=True)  # Field name made lowercase.
    user_create_user_id = models.BigIntegerField(db_column='USER_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    user_create_time = models.DateTimeField(db_column='USER_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    user_modify_user_id = models.BigIntegerField(db_column='USER_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    user_modify_time = models.DateTimeField(db_column='USER_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.
    user_status = models.SmallIntegerField(db_column='USER_STATUS', blank=True, null=True)  # Field name made lowercase.
    user_department_id = models.BigIntegerField(db_column='USER_DEPARTMENT_ID', blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_remark = models.CharField(db_column='USER_REMARK', max_length=128, blank=True, null=True)  # Field name made lowercase.
    user_tel = models.CharField(db_column='USER_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_store_id = models.BigIntegerField(db_column='USER_STORE_ID', blank=True, null=True)  # Field name made lowercase.
    user_member_id = models.BigIntegerField(db_column='USER_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'user_rec'


class UserRole(models.Model):
    user_role_id = models.BigIntegerField(db_column='USER_ROLE_ID', primary_key=True)  # Field name made lowercase.
    user_role_user = models.BigIntegerField(User, db_column='USER_ROLE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    user_role_sys_role = models.BigIntegerField(SysRole, db_column='USER_ROLE_SYS_ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    user_role_create_user_id = models.BigIntegerField(db_column='USER_ROLE_CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    user_role_create_time = models.DateTimeField(db_column='USER_ROLE_CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    user_role_modify_user_id = models.BigIntegerField(db_column='USER_ROLE_MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    user_role_modify_time = models.DateTimeField(db_column='USER_ROLE_MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'user_role_rec'


class StoreReport(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='STORE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    member_id = models.BigIntegerField(db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_id = models.BigIntegerField(db_column='TMN_ID', blank=True, null=True)  # Field name made lowercase.
    tmn_type = models.IntegerField(db_column='TMN_TYPE', blank=True, null=True)  # Field name made lowercase.
    agent_id = models.BigIntegerField(db_column='AGENT_ID', blank=True, null=True)  # Field name made lowercase.
    agent_amt = models.DecimalField(db_column='AGENT_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales_amt = models.DecimalField(db_column='SALES_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    register_amt = models.DecimalField(db_column='REGISTER_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmn_amt = models.DecimalField(db_column='TMN_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    profit_amt = models.DecimalField(db_column='PROFIT_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    profit_amt_rate = models.CharField(db_column='PROFIT_AMT_RATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    member_count = models.BigIntegerField(db_column='MEMBER_COUNT', blank=True, null=True)  # Field name made lowercase.
    member_sod_count = models.BigIntegerField(db_column='MEMBER_SOD_COUNT', blank=True, null=True)  # Field name made lowercase.
    member_active_rate = models.CharField(db_column='MEMBER_ACTIVE_RATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sod_item_count = models.BigIntegerField(db_column='SOD_ITEM_COUNT', blank=True, null=True)  # Field name made lowercase.
    sod_count = models.BigIntegerField(db_column='SOD_COUNT', blank=True, null=True)  # Field name made lowercase.
    sod_avg_price = models.DecimalField(db_column='SOD_AVG_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sod_item_avg_price = models.DecimalField(db_column='SOD_ITEM_AVG_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    member_sod_avg_count = models.DecimalField(db_column='MEMBER_SOD_AVG_COUNT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refund_amt = models.DecimalField(db_column='REFUND_AMT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refund_sod_item_count = models.BigIntegerField(db_column='REFUND_SOD_ITEM_COUNT', blank=True, null=True)  # Field name made lowercase.
    refund_rate = models.CharField(db_column='REFUND_RATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    report_date = models.DateField(db_column='REPORT_DATE', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'dim_store_reports'


class Message(models.Model):
    id = models.BigIntegerField(db_column='id',primary_key=True)
    name = models.CharField(db_column='name', max_length=39, blank=True, null=True)
    title = models.CharField(db_column='title', max_length=120, blank=True, null=True)
    content = models.CharField(db_column='content', max_length=1200, blank=True, null=True)
    postingTime = models.DateTimeField(db_column='posting_time', max_length=38, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'ms_message'


class Replies(models.Model):
    id = models.BigIntegerField(db_column='id',primary_key=True)
    repliesContent = models.CharField(db_column='replies_content', max_length=1200, blank=True, null=True)
    thisTime = models.DateTimeField(db_column='this_time', blank=True, null=True)
    mId = models.BigIntegerField(Message,db_column='messageId')

    # class Meta:
    #     managed = False
    #     db_table = 'ms_replies'

class Resource(models.Model):
    id = models.BigIntegerField(db_column='id',primary_key=True)
    name = models.CharField(db_column='name',max_length=40,blank=True,null=True)
    url = models.CharField(db_column='url',max_length=130,blank=True,null=True)
    type = models.CharField(db_column='type',max_length=12,blank=True,null=True)
    create_time = models.DateTimeField('create_time',max_length=38,blank=True,null=True)
    parentId = models.BigIntegerField(db_column='parentId')
    imgPath = models.CharField(db_column='background_img_path',max_length=200,blank=True,null=True)
    # class Meta:
    #     db_table = 'resource'


class RoleResource(models.Model):
    id = models.BigIntegerField(db_column='id',primary_key=True)
    resource_id = models.BigIntegerField(db_column='resource_id',max_length=120,null=True)
    role_id = models.BigIntegerField(db_column='role_id')
    type = models.BigIntegerField(db_column='type')
    create_time = models.DateTimeField('create_time',max_length=38,blank=True,null=True)
    # class Meta:
    #     db_table = 'sys_role_resource'

class UserAgent(models.Model):
    id = models.BigIntegerField(db_column='ID',primary_key=True)
    user_id = models.BigIntegerField(db_column='USER_ID',max_length=6,null=True)
    user_code = models.BigIntegerField(db_column='USER_CODE',max_length=6,null=True)
    agent_id = models.CharField(db_column='AGENT_ID',max_length=36,null=True)
    create_time = models.DateTimeField('CREATE_TIME',max_length=38,blank=True,null=True)
    modify_time = models.DateTimeField('MODIFY_TIME',max_length=38,blank=True,null=True)

    # class Meta:
    #     db_table = 'user_agent_rec'

class Price(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    le_id = models.BigIntegerField(db_column='LE_ID')  # Field name made lowercase.
    purchase_id = models.BigIntegerField(db_column='PURCHASE_ID')  # Field name made lowercase.
    purchase_detail_id = models.BigIntegerField(db_column='PURCHASE_DETAIL_ID')  # Field name made lowercase.
    purchase_cost = models.DecimalField(db_column='PURCHASE_COST', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchase_bid_price = models.DecimalField(db_column='PURCHASE_BID_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sell_price = models.DecimalField(db_column='SELL_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    market_price = models.DecimalField(db_column='MARKET_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sell_bid_price = models.DecimalField(db_column='SELL_BID_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gen_gross_margin = models.DecimalField(db_column='GEN_GROSS_MARGIN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    agent_price = models.DecimalField(db_column='AGENT_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    agent_gross = models.DecimalField(db_column='AGENT_GROSS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    agent_gross_margin = models.DecimalField(db_column='AGENT_GROSS_MARGIN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ms_gross = models.DecimalField(db_column='MS_GROSS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ms_gross_margin = models.DecimalField(db_column='MS_GROSS_MARGIN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    target_gross_margin = models.DecimalField(db_column='TARGET_GROSS_MARGIN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ems = models.DecimalField(db_column='EMS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bc = models.DecimalField(db_column='BC', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.BigIntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    modify_user_id = models.BigIntegerField(db_column='MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ms_price'

class Supplier(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name_en = models.CharField(db_column='NAME_EN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country_code = models.CharField(db_column='COUNTRY_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    catalog = models.CharField(db_column='CATALOG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contacter = models.CharField(db_column='CONTACTER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weixin = models.CharField(db_column='WEIXIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qq = models.CharField(db_column='QQ', max_length=20, blank=True, null=True)  # Field name made lowercase.
    other_contact = models.CharField(db_column='OTHER_CONTACT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contacter2 = models.CharField(db_column='CONTACTER2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email2 = models.CharField(db_column='EMAIL2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel2 = models.CharField(db_column='TEL2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weixin2 = models.CharField(db_column='WEIXIN2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qq2 = models.CharField(db_column='QQ2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    other_contact2 = models.CharField(db_column='OTHER_CONTACT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='CURRENCY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='BANK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='ACCOUNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='LEVEL', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    principal = models.CharField(db_column='PRINCIPAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.BigIntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    swift_code = models.CharField(db_column='SWIFT_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ms_supplier'

class Purchase(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    purchase_no = models.CharField(db_column='PURCHASE_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_rate = models.CharField(db_column='PAY_RATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type = models.CharField(db_column='PAY_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='CURRENCY', max_length=20, blank=True, null=True)  # Field name made lowercase.SUPPLIER_ID
    supplier_code = models.CharField(db_column='SUPPLIER_CODE', max_length=20, blank=True, null=True)
    supplier = models.ForeignKey(Supplier,db_column='SUPPLIER_ID', max_length=20, blank=True, null=True)
    supplier_name = models.CharField(db_column='SUPPLIER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pay_account = models.CharField(db_column='PAY_ACCOUNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    first_amount = models.DecimalField(db_column='FIRST_AMOUNT', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rest_amount = models.DecimalField(db_column='REST_AMOUNT', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    shipping_mode = models.CharField(db_column='SHIPPING_MODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shipping_time = models.DateTimeField(db_column='SHIPPING_TIME', blank=True, null=True)  # Field name made lowercase.
    freight = models.DecimalField(db_column='FREIGHT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    est_arrival_time = models.DateTimeField(db_column='EST_ARRIVAL_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.BigIntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    confirm_user_id = models.CharField(db_column='CONFIRM_USER_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modify_user_id = models.BigIntegerField(db_column='MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    is_deleted = models.IntegerField(db_column='IS_DELETED', blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='BANK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    payee = models.CharField(db_column='PAYEE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    swift_code = models.CharField(db_column='SWIFT_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pay_mode = models.CharField(db_column='PAY_MODE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ms_purchase'


class PurchaseDetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    purchase = models.ForeignKey(Purchase,db_column='PURCHASE_ID', blank=True, null=True)  # Field name made lowercase.
    #purchase_id = models.BigIntegerField(db_column='PURCHASE_ID', blank=True, null=True)  # Field name made lowercase.
    le = models.ForeignKey(Le,db_column='LE_ID', blank=True, null=True)  # Field name made lowercase.
    package_spe = models.IntegerField(db_column='PACKAGE_SPE', blank=True, null=True)  # Field name made lowercase.
    package_qty = models.IntegerField(db_column='PACKAGE_QTY', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    #currency = models.CharField(db_column='CURRENCY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    foreign_price = models.DecimalField(db_column='FOREIGN_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    foreign_amt = models.DecimalField(db_column='FOREIGN_AMT', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rmb_price = models.DecimalField(db_column='RMB_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rmb_amt = models.DecimalField(db_column='RMB_AMT', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchase_cost = models.DecimalField(db_column='PURCHASE_COST', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sell_price = models.DecimalField(db_column='SELL_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    target_gross_margin = models.DecimalField(db_column='TARGET_GROSS_MARGIN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sell_bid_price = models.DecimalField(db_column='SELL_BID_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchase_bid_price = models.DecimalField(db_column='PURCHASE_BID_PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stock_qty = models.BigIntegerField(db_column='STOCK_QTY', blank=True, null=True)  # Field name made lowercase.
    stock_sell_rate = models.DecimalField(db_column='STOCK_SELL_RATE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    validity_date = models.DateTimeField(db_column='VALIDITY_DATE', blank=True, null=True)  # Field name made lowercase.
    purchase_type = models.IntegerField(db_column='PURCHASE_TYPE', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    department_id = models.SmallIntegerField(db_column='DEPARTMENT_ID', blank=True, null=True)  # Field name made lowercase.
    arrival_bar_code = models.CharField(db_column='ARRIVAL_BAR_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    article_number = models.CharField(db_column='ARTICLE_NUMBER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirm_spe = models.CharField(db_column='CONFIRM_SPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cif_cost = models.DecimalField(db_column='CIF_COST', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    confirm_qty = models.BigIntegerField(db_column='CONFIRM_QTY', blank=True, null=True)  # Field name made lowercase.
    check_qty = models.BigIntegerField(db_column='CHECK_QTY', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    modify_user_id = models.BigIntegerField(db_column='MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    le_barcode = models.CharField(db_column='LE_BARCODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arrival_qty = models.IntegerField(db_column='ARRIVAL_QTY', blank=True, null=True,default=0)  # Field name made lowercase.
    is_new = models.IntegerField(db_column='IS_NEW', blank=True, null=True)  # Field name made lowercase.
    le_code = models.CharField(db_column='LE_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ms_purchase_detail'

class inBound(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    purchaseDetailid = models.BigIntegerField(db_column='PURCHASE_DETAIL_ID', blank=True, null=True)  # Field name made lowercase.
    qty = models.BigIntegerField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.BigIntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CREATE_USER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BARCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ms_inbound'

class iMages(models.Model):
     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
     img_name = models.CharField(db_column='IMG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
     img = models.FileField(db_column='IMG_URL',upload_to='img', max_length=100, blank=True, null=True)  # Field name made lowercase.
     create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.

     # class Meta:
     #    managed = False
     #    db_table = 'ms_image_rec'

class ImgForm(ModelForm):
    class Meta:
        model = iMages
        fields = ('img',)

class purchaseLog(models.Model):
     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
     create_user_name = models.CharField(db_column='CREATE_USER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
     create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
     modify_user_id = models.BigIntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
     content = models.CharField(db_column='CONTENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
     business_name = models.CharField(db_column='BUSINESS_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.

     # class Meta:
     #    managed = False
     #    db_table = 'ms_purchase_log'

class ReportStockDay(models.Model):
     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
     stock_date = models.DateField(db_column='STOCK_DATE')  # Field name made lowercase.
     le = models.ForeignKey(Le,db_column='LE_ID', blank=True, null=True)  # Field name made lowercase.
     stock_qty = models.BigIntegerField(db_column='STOCK_QTY', blank=True, null=True)  # Field name made lowercase.
     sale_qty = models.BigIntegerField(db_column='SALE_QTY', blank=True, null=True)  # Field name made lowercase.
     return_qty = models.BigIntegerField(db_column='RETURN_QTY', blank=True, null=True)  # Field name made lowercase.
     create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
     sale_date = models.DateField(db_column='SALE_DATE')  # Field name made lowercase.

     # class Meta:
     #    managed = False
     #    db_table = 'report_stock_day'

class MsStock(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    le_id = models.BigIntegerField(db_column='LE_ID')  # Field name made lowercase.
    le_code = models.CharField(db_column='LE_CODE', max_length=30)  # Field name made lowercase.
    made_in = models.CharField(db_column='MADE_IN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfrs_cn = models.CharField(db_column='MFRS_CN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfrs_en = models.CharField(db_column='MFRS_EN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    product_name_cn = models.CharField(db_column='PRODUCT_NAME_CN', max_length=100)  # Field name made lowercase.
    carton = models.CharField(db_column='CARTON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ingredient = models.CharField(db_column='INGREDIENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    batch = models.CharField(db_column='BATCH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    buying_price = models.DecimalField(db_column='BUYING_PRICE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    buying_price_cif = models.DecimalField(db_column='BUYING_PRICE_CIF', max_digits=12, decimal_places=2)  # Field name made lowercase.
    employee_price = models.DecimalField(db_column='EMPLOYEE_PRICE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    cost_rv = models.DecimalField(db_column='COST_RV', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gross_rate_yc = models.DecimalField(db_column='GROSS_RATE_YC', max_digits=10, decimal_places=2)  # Field name made lowercase.
    gross_amt_yc = models.DecimalField(db_column='GROSS_AMT_YC', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gross_rate_dealer = models.DecimalField(db_column='GROSS_RATE_DEALER', max_digits=10, decimal_places=2)  # Field name made lowercase.
    gross_amt_dealer = models.DecimalField(db_column='GROSS_AMT_DEALER', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gross_amt_all = models.DecimalField(db_column='GROSS_AMT_ALL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    gross_rate_all = models.DecimalField(db_column='GROSS_RATE_ALL', max_digits=10, decimal_places=2)  # Field name made lowercase.
    sp_cost = models.DecimalField(db_column='SP_COST', max_digits=12, decimal_places=2)  # Field name made lowercase.
    sp_gross_rate_yc = models.DecimalField(db_column='SP_GROSS_RATE_YC', max_digits=10, decimal_places=2)  # Field name made lowercase.
    sp_gross_amt_yc = models.DecimalField(db_column='SP_GROSS_AMT_YC', max_digits=12, decimal_places=2)  # Field name made lowercase.
    sp_gross_rate_dealer = models.DecimalField(db_column='SP_GROSS_RATE_DEALER', max_digits=10, decimal_places=2)  # Field name made lowercase.
    sp_gross_amt_dealer = models.DecimalField(db_column='SP_GROSS_AMT_DEALER', max_digits=12, decimal_places=2)  # Field name made lowercase.
    yt_rrp = models.DecimalField(db_column='YT_RRP', max_digits=12, decimal_places=2)  # Field name made lowercase.
    yt_profit_amt_rd_100k = models.DecimalField(db_column='YT_PROFIT_AMT_RD_100K', max_digits=12, decimal_places=2)  # Field name made lowercase.
    yt_profit_rate_rd_100k = models.DecimalField(db_column='YT_PROFIT_RATE_RD_100K', max_digits=10, decimal_places=2)  # Field name made lowercase.
    yt_profit_amt_rd_cif = models.DecimalField(db_column='YT_PROFIT_AMT_RD_CIF', max_digits=12, decimal_places=2)  # Field name made lowercase.
    yt_profit_rate_rd_cif_mix = models.DecimalField(db_column='YT_PROFIT_RATE_RD_CIF_MIX', max_digits=10, decimal_places=2)  # Field name made lowercase.
    yt_rd_cost = models.DecimalField(db_column='YT_RD_COST', max_digits=12, decimal_places=2)  # Field name made lowercase.
    yt_rd_cost_30k = models.DecimalField(db_column='YT_RD_COST_30K', max_digits=12, decimal_places=2)  # Field name made lowercase.
    yt_rd_cost_100k = models.DecimalField(db_column='YT_RD_COST_100K', max_digits=12, decimal_places=2)  # Field name made lowercase.
    yt_rd_profit_rate_custom = models.DecimalField(db_column='YT_RD_PROFIT_RATE_CUSTOM', max_digits=10, decimal_places=2)  # Field name made lowercase.
    yt_cif_hk_price_mix_no_moq = models.DecimalField(db_column='YT_CIF_HK_PRICE_MIX_NO_MOQ', max_digits=12, decimal_places=2)  # Field name made lowercase.
    yt_cif_hk_price_mix_30k = models.DecimalField(db_column='YT_CIF_HK_PRICE_MIX_30K', max_digits=12, decimal_places=2)  # Field name made lowercase.
    yt_cif_hk_price_60k = models.DecimalField(db_column='YT_CIF_HK_PRICE_60K', max_digits=12, decimal_places=2)  # Field name made lowercase.
    goods_status = models.CharField(db_column='GOODS_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier_1 = models.CharField(db_column='SUPPLIER_1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier_2 = models.CharField(db_column='SUPPLIER_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier_3 = models.CharField(db_column='SUPPLIER_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier_4 = models.CharField(db_column='SUPPLIER_4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier_5 = models.CharField(db_column='SUPPLIER_5', max_length=50, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ms_stock'


class MsStockPara(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    para_name = models.CharField(db_column='PARA_NAME', unique=True, max_length=200)  # Field name made lowercase.
    para_value = models.DecimalField(db_column='PARA_VALUE', max_digits=14, decimal_places=4)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ms_stock_para'

class MsPurchaseAnalysis(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    le_id = models.BigIntegerField(db_column='LE_ID')  # Field name made lowercase.
    sales_qty_day = models.DecimalField(db_column='SALES_QTY_DAY', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sales_days = models.IntegerField(db_column='SALES_DAYS', blank=True, null=True)  # Field name made lowercase.
    stock_sales_ratio_day = models.DecimalField(db_column='STOCK_SALES_RATIO_DAY', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stock_sales_ratio_week = models.DecimalField(db_column='STOCK_SALES_RATIO_WEEK', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stock_sales_ratio_month = models.DecimalField(db_column='STOCK_SALES_RATIO_MONTH', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transit_qty = models.IntegerField(db_column='TRANSIT_QTY', blank=True, null=True)  # Field name made lowercase.
    arrive_days = models.IntegerField(db_column='ARRIVE_DAYS', blank=True, null=True)  # Field name made lowercase.
    virtual_qty = models.IntegerField(db_column='VIRTUAL_QTY', blank=True, null=True)  # Field name made lowercase.
    warning1 = models.CharField(db_column='WARNING1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    warning2 = models.CharField(db_column='WARNING2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    est_sales_days = models.IntegerField(db_column='EST_SALES_DAYS', blank=True, null=True)  # Field name made lowercase.
    normal_days = models.IntegerField(db_column='NORMAL_DAYS', blank=True, null=True)  # Field name made lowercase.
    common_days = models.IntegerField(db_column='COMMON_DAYS', blank=True, null=True)  # Field name made lowercase.
    total_days = models.IntegerField(db_column='TOTAL_DAYS', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.BigIntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    modify_user_id = models.BigIntegerField(db_column='MODIFY_USER_ID', blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ms_purchase_analysis'

class MsSubOrder(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sod_id = models.BigIntegerField(db_column='SOD_ID', blank=True, null=True)  # Field name made lowercase.
    sod_no = models.CharField(db_column='SOD_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sod_sub_no = models.CharField(db_column='SOD_SUB_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    order_amt = models.DecimalField(db_column='ORDER_AMT', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    order_qty = models.BigIntegerField(db_column='ORDER_QTY', blank=True, null=True)  # Field name made lowercase.
    member_id = models.BigIntegerField(db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    import_time = models.DateTimeField(db_column='IMPORT_TIME', blank=True, null=True)  # Field name made lowercase.
    is_success = models.IntegerField(db_column='IS_SUCCESS', blank=True, null=True)  # Field name made lowercase.
    is_pay_no_sync = models.IntegerField(db_column='IS_PAY_NO_SYNC')  # Field name made lowercase.
    create_member_id = models.BigIntegerField(db_column='CREATE_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    modify_member_id = models.BigIntegerField(db_column='MODIFY_MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    express_no = models.CharField(db_column='EXPRESS_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    express_com = models.CharField(db_column='EXPRESS_COM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    express_com_no = models.CharField(db_column='EXPRESS_COM_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_bc = models.IntegerField(db_column='IS_BC', blank=True, null=True)  # Field name made lowercase.
    order_state = models.IntegerField(db_column='ORDER_STATE', blank=True, null=True)  # Field name made lowercase.
    store_no = models.CharField(db_column='STORE_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'ms_sub_order'