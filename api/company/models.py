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
    type_of_issuer = models.CharField(max_length=128, help_text='issuerCat', null=True)
    issuer_country = models.CharField(max_length=128, help_text='invCountry', null=True)
    original_balance = models.FloatField(help_text='balance', null=True)
    total_value = models.FloatField(help_text='valUSD', null=True)
    lvt = models.FloatField(help_text='pctVal', null=True)
    maturity_date = models.DateField(help_text='maturityDt', null=True)
    coupon_rate = models.FloatField(help_text='annualizedRt', null=True)
    defaultStatus = models.BooleanField(help_text='idDefault', null=True)
    collateral = models.BooleanField(help_text='isCashCollateral', null=True)
    isNonCacheCollateral = models.BooleanField(help_text='isNonCashCollateral', null=True)
    isLoanByFund = models.BooleanField(help_text='isLoanByFund', null=True)

