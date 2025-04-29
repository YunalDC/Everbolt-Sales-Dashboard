from django import forms
from .models import Visit, UserProfile

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = [
            'visit_date',
            'sales_officer',
            'company',
            'visit_type',
            'visit_details',
            'remarks',
        ]

class BulkInvoiceUploadForm(forms.Form):
    dummy_field = forms.CharField(required=False)

class BulkExcelUploadForm(forms.Form):
    excel_file = forms.FileField(required=True)

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']

