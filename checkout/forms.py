from shop.models import ShippingAddress
from django import forms

class CheckoutForm(forms.ModelForm):
    address = forms.CharField(max_length=9999,label="Adresa")
    post_num = forms.CharField(max_length=9999,label="PSČ")
    country = forms.CharField(max_length=9999,label="Krajina")
    name = forms.CharField(max_length=9999,label="Meno")
    surname = forms.CharField(max_length=9999,label="Priezvisko")
    tel_number = forms.IntegerField(label="Telefónne číslo")
    dic = forms.CharField(max_length=9999,required=False,label="DIČ")
    email = forms.EmailField(max_length=9999,label="Email")
    order_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    product = forms.CharField(widget = forms.HiddenInput(), required = False)
    transaction_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        model = ShippingAddress
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'placeholder':'Vaša Adresa'})
        self.fields['post_num'].widget.attrs['placeholder'] = 'Poštové smerovacie číslo'
        self.fields['country'].widget.attrs['placeholder'] = 'Krajina'
        self.fields['name'].widget.attrs['placeholder'] = 'Krstné Meno'
        self.fields['surname'].widget.attrs['placeholder'] = 'Priezvisko'
        self.fields['tel_number'].widget.attrs['placeholder'] = 'Telefónne číslo'
        self.fields['dic'].widget.attrs['placeholder'] = 'DIČ | nepovinné'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Adresa'

        

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





