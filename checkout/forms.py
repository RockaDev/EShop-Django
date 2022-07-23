from shop.models import ShippingAddress
from django import forms

class CheckoutForm(forms.ModelForm):
    address = forms.CharField(max_length=9999)
    post_num = forms.CharField(max_length=9999)
    country = forms.CharField(max_length=9999)
    name = forms.CharField(max_length=9999)
    surname = forms.CharField(max_length=9999)
    tel_number = forms.IntegerField(label="Telefonne cislo")
    dic = forms.CharField(max_length=9999,required=False)
    email = forms.EmailField(max_length=9999)
    order_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    product = forms.CharField(widget = forms.HiddenInput(), required = False)
    transaction_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        model = ShippingAddress
        fields = "__all__"

    def save(self, commit=True):
        self.instance.address=self.cleaned_data['address']
        self.instance.post_num=self.cleaned_data['post_num']
        self.instance.country=self.cleaned_data['country']
        self.instance.name=self.cleaned_data['name']
        self.instance.surname=self.cleaned_data['surname']
        self.instance.tel_number=self.cleaned_data['tel_number']
        self.instance.dic=self.cleaned_data['dic']
        self.instance.email=self.cleaned_data['email']

        user = super(CheckoutForm, self).save(commit=False)

        if commit:
            user.save()
        return user





