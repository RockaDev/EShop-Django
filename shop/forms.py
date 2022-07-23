from shop.models import ShopItems
from django import forms
import unidecode

class ShopForm(forms.ModelForm):
    product_item = forms.CharField(label="Názov Produktu",max_length=100)
    product_item_ascii = forms.CharField(max_length=100,required=False,widget = forms.HiddenInput())
    about_item = forms.CharField(label="Popis Produktu",max_length=9999,widget=forms.Textarea(attrs={'rows':'5', 'cols':'40'}))
    price = forms.IntegerField(label="Cena",widget=forms.NumberInput(attrs={'min':'1'}))
    image = forms.FileField(required=False)
    on_stock = forms.IntegerField(label="Na sklade")

    class Meta:
        model = ShopItems
        fields = "__all__"

    def save(self, commit=True):
        self.instance.product_item=self.cleaned_data['product_item']
        self.instance.product_item_ascii=unidecode.unidecode(self.cleaned_data['product_item'])
        self.instance.price=self.cleaned_data['price']
        self.instance.about_item=self.cleaned_data['about_item']
        self.instance.on_stock=self.cleaned_data['on_stock']

        file = self['image'].value()

        user = super(ShopForm, self).save(commit=False)

        if commit:
            user.save()
        return user





