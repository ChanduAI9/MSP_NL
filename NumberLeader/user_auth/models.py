from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

#models Here       
class CustomUser(AbstractUser):
    startup_name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    introductory_video = models.URLField(blank=True)
    co_founder = models.CharField(max_length=255, blank=True)
    linkedin_profile = models.URLField(blank=True)
    introduction = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, default='profile_photos/default_profile_photo.png')
    phone_number = models.CharField(max_length=15, blank=True)

class FinancialDetails(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)
    sales = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    ebitda = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ebit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pat = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    shares_issued = models.PositiveIntegerField(blank=True, null=True)
    book_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    INDUSTRY_CHOICES = [
    ('Casual Dining restaurant Chain', 'Casual Dining restaurant Chain'),
    ('Contact Center Software Platform', 'Contact Center Software Platform'),
    ('Fashion Info Aggregator App', 'Fashion Info Aggregator App'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Nanotechnology', 'Nanotechnology'),
    ('Hospitality', 'Hospitality'),
    ('FinTech', 'FinTech'),
    ('EdTech', 'EdTech'),
    ('SaaS', 'SaaS'),
    ('Waste Management Service', 'Waste Management Service'),
    ('Agtech', 'Agtech'),
    ('Deep-Tech', 'Deep-Tech'),
    ('Energy', 'Energy'),
    ('Digital Media', 'Digital Media'),
    ('Professional Network for Women', 'Professional Network for Women'),
    ('Advertising', 'Advertising'),
    ('Utility Solutions Provider', 'Utility Solutions Provider'),
    ('LegalTech', 'LegalTech'),
    ('EduTech', 'EduTech'),
    ('Food Delivery', 'Food Delivery'),
    ('AgriTech', 'AgriTech'),
    ('Digital Reconciliation and Financial Services', 'Digital Reconciliation and Financial Services'),
    ('Food Production', 'Food Production'),
    ('Co-working Spaces', 'Co-working Spaces'),
    ('Intelligent Marketing Cloud', 'Intelligent Marketing Cloud'),
    ('Cafe', 'Cafe'),
    ('Information Technology and Services', 'Information Technology and Services'),
    ('Transportation', 'Transportation'),
    ('E-Tech', 'E-Tech'),
    ('Fashion and Apparel', 'Fashion and Apparel'),
    ('B2B-focused foodtech startup', 'B2B-focused foodtech startup'),
    ('Video', 'Video'),
    ('Aerospace', 'Aerospace'),
    ('B2B Marketing', 'B2B Marketing'),
    ('Last Mile Transportation', 'Last Mile Transportation'),
    ('Software', 'Software'),
    ('Video Games', 'Video Games'),
    ('Consumer Goods', 'Consumer Goods'),
    ('Customer Service', 'Customer Service'),
    ('Advertising, Marketing', 'Advertising, Marketing'),
    ('IoT', 'IoT'),
    ('Information Technology', 'Information Technology'),
    ('Consumer Technology', 'Consumer Technology'),
    ('Accounting', 'Accounting'),
    ('Automotive', 'Automotive'),
    ('Customer Service Platform', 'Customer Service Platform'),
    ('Retail', 'Retail'),
    ('Tech', 'Tech'),
    ('Luxury Label', 'Luxury Label'),
    ('Compliance', 'Compliance'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
]

    industry = models.CharField(max_length=50,choices=INDUSTRY_CHOICES, blank=True, null=True)
    is_past_year = models.BooleanField(default=False)

    def __str__(self):
        return f"FinancialDetails for {self.user.username}"

    def save(self, *args, **kwargs):
        self.pe_ratio = 15
        self.ebitda_margin = 0.25
        self.number_of_outstanding_shares = 1000000

        super().save(*args, **kwargs)

    def calculate_cmp_rs(self):
        return self.pat * self.pe_ratio

    def calculate_mar_cap_rs_cr(self):
        return self.calculate_cmp_rs() * self.number_of_outstanding_shares / 1000000

    def calculate_sales_rs_cr(self):
        return self.ebitda / self.ebitda_margin

class ForecastedFinancialDetails(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    forecasted_sales = models.DecimalField(max_digits=10, decimal_places=2)
    forecasted_ebitda = models.DecimalField(max_digits=10, decimal_places=2)
    forecasted_ebit = models.DecimalField(max_digits=10, decimal_places=2)
    forecasted_pat = models.DecimalField(max_digits=10, decimal_places=2)
    total_current_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_current_pat = models.DecimalField(max_digits=10, decimal_places=2)
    INDUSTRY_CHOICES = [
    ('Casual Dining restaurant Chain', 'Casual Dining restaurant Chain'),
    ('Contact Center Software Platform', 'Contact Center Software Platform'),
    ('Fashion Info Aggregator App', 'Fashion Info Aggregator App'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Nanotechnology', 'Nanotechnology'),
    ('Hospitality', 'Hospitality'),
    ('FinTech', 'FinTech'),
    ('EdTech', 'EdTech'),
    ('SaaS', 'SaaS'),
    ('Waste Management Service', 'Waste Management Service'),
    ('Agtech', 'Agtech'),
    ('Deep-Tech', 'Deep-Tech'),
    ('Energy', 'Energy'),
    ('Digital Media', 'Digital Media'),
    ('Professional Network for Women', 'Professional Network for Women'),
    ('Advertising', 'Advertising'),
    ('Utility Solutions Provider', 'Utility Solutions Provider'),
    ('LegalTech', 'LegalTech'),
    ('EduTech', 'EduTech'),
    ('Food Delivery', 'Food Delivery'),
    ('AgriTech', 'AgriTech'),
    ('Digital Reconciliation and Financial Services', 'Digital Reconciliation and Financial Services'),
    ('Food Production', 'Food Production'),
    ('Co-working Spaces', 'Co-working Spaces'),
    ('Intelligent Marketing Cloud', 'Intelligent Marketing Cloud'),
    ('Cafe', 'Cafe'),
    ('Information Technology and Services', 'Information Technology and Services'),
    ('Transportation', 'Transportation'),
    ('E-Tech', 'E-Tech'),
    ('Fashion and Apparel', 'Fashion and Apparel'),
    ('B2B-focused foodtech startup', 'B2B-focused foodtech startup'),
    ('Video', 'Video'),
    ('Aerospace', 'Aerospace'),
    ('B2B Marketing', 'B2B Marketing'),
    ('Last Mile Transportation', 'Last Mile Transportation'),
    ('Software', 'Software'),
    ('Video Games', 'Video Games'),
    ('Consumer Goods', 'Consumer Goods'),
    ('Customer Service', 'Customer Service'),
    ('Advertising, Marketing', 'Advertising, Marketing'),
    ('IoT', 'IoT'),
    ('Information Technology', 'Information Technology'),
    ('Consumer Technology', 'Consumer Technology'),
    ('Accounting', 'Accounting'),
    ('Automotive', 'Automotive'),
    ('Customer Service Platform', 'Customer Service Platform'),
    ('Retail', 'Retail'),
    ('Tech', 'Tech'),
    ('Luxury Label', 'Luxury Label'),
    ('Compliance', 'Compliance'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
]

    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.user)



class FinancialData(models.Model):
    name = models.CharField(max_length=255)
    cmp_rs = models.FloatField(null=True, blank=True,default=0.0)
    pe = models.FloatField(null=True, blank=True,default=0.0)
    mar_cap_rs = models.FloatField(null=True, blank=True,default=0.0)
    num_of_shares = models.FloatField(null=True, blank=True,default=0.0)
    np_qtr_rs = models.FloatField(null=True, blank=True,default=0.0)
    sales_qtr_rs = models.FloatField(null=True, blank=True,default=0.0)
    roce_percentage = models.FloatField(null=True, blank=True,default=0.0)
    sales_rs = models.FloatField(null=True, blank=True,default=0.0)
    sales_per_share = models.FloatField(null=True, blank=True,default=0.0)
    cmp_over_sales = models.FloatField(null=True, blank=True,default=0.0)
    cmp_over_bv = models.FloatField(null=True, blank=True,default=0.0)
    bv_in_cr = models.FloatField(null=True, blank=True,default=0.0)
    ind_pe = models.FloatField(null=True, blank=True,default=0.0)
    profit_growth_percentage = models.FloatField(null=True, blank=True,default=0.0)
    ev_rs = models.FloatField(null=True, blank=True,default=0.0)
    pat_12m_rs = models.FloatField(null=True, blank=True,default=0.0)
    debt_eq = models.FloatField(null=True, blank=True,default=0.0)
    cmp_over_ocf = models.FloatField(null=True, blank=True,default=0.0)
    ev_over_ebitda = models.FloatField(null=True, blank=True,default=0.0)
    industry = models.CharField(max_length=255)

    def __str__(self):
        return self.name



    


#v5

# class FormulaValue(models.Model):
#     revised_tag = models.CharField(max_length=255)
#     symbol = models.CharField(max_length=255)
#     audited = models.BooleanField()
#     standalone = models.BooleanField()
#     value = models.DecimalField(max_digits=15, decimal_places=2)  
#     period = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.symbol} - {self.revised_tag} - {self.period}"

     
    