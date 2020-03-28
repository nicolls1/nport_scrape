from django.db import models


class Fund(models.Model):
    series_lei = models.CharField(max_length=128, help_text='seriesLei', null=True)
    name = models.CharField(max_length=256, help_text='regName', null=True)
    series_name = models.CharField(max_length=256, help_text='seriesName', null=True)
    total_assets = models.FloatField(help_text='totAssets', null=True)
    total_liabilities = models.FloatField(help_text='totLiabs', null=True)
    net_assets = models.FloatField(help_text='netAssets', null=True)


class FundHolding(models.Model):
    type = models.CharField(max_length=64, help_text='assetCat', null=True)
    coupon = models.CharField(max_length=64, help_text='couponKind', null=True)
    issuer = models.CharField(max_length=512, help_text='name', null=True)
    name = models.CharField(max_length=512, help_text='title', null=True)
    type_of_issuer = models.CharField(max_length=128, help_text='issuerCat')
    issuer_country = models.CharField(max_length=128, help_text='invCountry')
    original_balance = models.FloatField(help_text='balance')
    total_value = models.FloatField(help_text='valUSD')
    lvt = models.FloatField(help_text='pctVal')
    maturity_date = models.DateField(help_text='maturityDt')
    coupon_rate = models.FloatField(help_text='annualizedRt')
    defaultStatus = models.BooleanField(help_text='idDefault')
    collateral = models.BooleanField(help_text='isCashCollateral')
    isNonCacheCollateral = models.BooleanField(help_text='isNonCashCollateral')
    isLoanByFund = models.BooleanField(help_text='isLoanByFund')

