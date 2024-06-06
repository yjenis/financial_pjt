from django.db import models

# Create your models here.
#예금---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)  # 금융 상품 코드
    kor_co_nm = models.TextField()  # 금융회사명
    fin_prdt_nm = models.TextField()  # 금융 상품명
    mtrt_int = models.TextField(blank=True, null=True)
    etc_note = models.TextField()  # 금융 상품 설명 
    join_deny = models.IntegerField()  # 가입 제한
    join_member = models.TextField()  # 가입대상
    join_way = models.TextField()  # 가입 방법
    spcl_cnd = models.TextField()  # 우대조건
    max_limit = models.IntegerField(blank=True, null=True)

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE) 
    fin_prdt_cd = models.TextField()  # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)  # 저축금리 유형명
    intr_rate = models.FloatField(blank=True, null=True, default=0)  # 저축금리
    intr_rate2 = models.FloatField(blank=True, null=True, default=0)  # 최고 우대금리
    save_trm = models.IntegerField()  # 저축 기간 (단위: 개월)

#적금---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)  # 금융 상품 코드
    kor_co_nm = models.TextField()  # 금융회사명
    fin_prdt_nm = models.TextField()  # 금융 상품명
    mtrt_int = models.TextField(blank=True, null=True)
    etc_note = models.TextField()  # 금융 상품 설명 
    join_deny = models.IntegerField()  # 가입 제한
    join_member = models.TextField()  # 가입대상
    join_way = models.TextField()  # 가입 방법
    spcl_cnd = models.TextField()  # 우대조건
    max_limit = models.IntegerField(blank=True, null=True)

class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE) 
    fin_prdt_cd = models.TextField()  # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)  # 저축금리 유형명
    intr_rate = models.FloatField(blank=True, null=True, default=0)  # 저축금리
    intr_rate2 = models.FloatField(blank=True, null=True, default=0)  # 최고 우대금리
    save_trm = models.IntegerField()  # 저축 기간 (단위: 개월)
    rsrv_type_nm = models.TextField()
    rsrv_type = models.TextField()
