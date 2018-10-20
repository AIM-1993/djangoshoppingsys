from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(max_length=254)
    address = forms.CharField(label="Address", max_length=128)
    city = forms.CharField(label="City", max_length=50)
    country = forms.CharField(label="Country", max_length=50)
    zipcode = forms.IntegerField(label="邮编")
    tele = forms.IntegerField(label="电话号码")
    created_count = forms.BooleanField(required=False)
    ship_address = forms.BooleanField(required=False)
    order_notes = forms.CharField(label="Order Notes", max_length=300)
    read = forms.BooleanField(required=False)
