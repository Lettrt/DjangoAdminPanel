from django.contrib import admin
from .models import Header, FirstTopCard, SecondTopCard, ThirdTopCard, ScoreBoardMain, MentorTitle, MentorOne, MentorTwo, PriceTitile, PriceCardOne, PriceCardOneOption, PriceCardTwo, PriceCardTwoOption, PriceCardThree, PriceCardThreeOption, DarkBlock, HelpBlock, LinkTitleBlock, LinkOptionBlock
from django.core.exceptions import ValidationError
from django import forms

class HeaderForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and Header.objects.exists():
            raise ValidationError("Может быть создана только одна запись для Первая карточка топ блока")

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    form = HeaderForm
    list_display = ['subTitle', 'mainTitle', 'buttonOne', 'buttonTwo', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

class FirstTopCardForm(forms.ModelForm):
    class Meta:
        model = FirstTopCard
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and FirstTopCard.objects.exists():
            raise ValidationError("Может быть создана только одна запись для первой карточка топ блока")

@admin.register(FirstTopCard)
class FirstTopCardAdmin(admin.ModelAdmin):
    form = FirstTopCardForm
    list_display = ['title', 'description', 'button', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

class SecondTopCardForm(forms.ModelForm):
    class Meta:
        model = SecondTopCard
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and SecondTopCard.objects.exists():
            raise ValidationError("Может быть создана только одна запись для второй карточка топ блока")

@admin.register(SecondTopCard)
class SecondTopCardAdmin(admin.ModelAdmin):
    form = SecondTopCardForm
    list_display = ['title', 'description', 'button', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

class ThirdTopCardForm(forms.ModelForm):
    class Meta:
        model = ThirdTopCard
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and ThirdTopCard.objects.exists():
            raise ValidationError("Может быть создана только одна запись для третей карточка топ блока")

@admin.register(ThirdTopCard)
class ThirdTopCardAdmin(admin.ModelAdmin):
    form = ThirdTopCardForm
    list_display = ['title', 'description', 'button', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']


class ScoreBoardMainForm(forms.ModelForm):
    class Meta:
        model = ScoreBoardMain
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and ScoreBoardMain.objects.exists():
            raise ValidationError("Может быть создана только одна запись для панели с цифрами")
        
@admin.register(ScoreBoardMain)
class ScoreBoardMainAdmin(admin.ModelAdmin):
    form = ScoreBoardMainForm
    list_display = ['title', 'colOneNum', 'colOneText', 'colTwoNum', 'colTwoText', 'colThreeNum', 'colThreeText', 'colFourNum', 'colFourText', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

class MentorTitleForm(forms.ModelForm):
    class Meta:
        model = MentorTitle
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and MentorTitle.objects.exists():
            raise ValidationError("Может быть создана только одна запись для заголовка блока менторы")
        
@admin.register(MentorTitle)
class MentorTitleAdmin(admin.ModelAdmin):
    form = MentorTitleForm
    list_display = ['title', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

class MentorOneForm(forms.ModelForm):
    class Meta:
        model = MentorOne
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and MentorOne.objects.exists():
            raise ValidationError("Может быть создана только одна запись для ментора")
        
@admin.register(MentorOne)
class MentorOneAdmin(admin.ModelAdmin):
    form = MentorOneForm
    list_display = ['firstName', 'secondName', 'grade', 'exp', 'photo', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

class MentorTwoForm(forms.ModelForm):
    class Meta:
        model = MentorTwo
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and MentorTwo.objects.exists():
            raise ValidationError("Может быть создана только одна запись для ментора")
        
@admin.register(MentorTwo)
class MentorTwoAdmin(admin.ModelAdmin):
    form = MentorTwoForm
    list_display = ['firstName', 'secondName', 'grade', 'exp', 'photo', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

class PriceTitileForm(forms.ModelForm):
    class Meta:
        model = PriceTitile
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and PriceTitile.objects.exists():
            raise ValidationError("Может быть создана только одна запись для заголовка блока цены")
        
@admin.register(PriceTitile)
class PriceTitileAdmin(admin.ModelAdmin):
    form = PriceTitileForm
    list_display = ['title', 'subtitle', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

class PriceCardOneForm(forms.ModelForm):
    class Meta:
        model = PriceCardOne
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and PriceCardOne.objects.exists():
            raise ValidationError("Может быть создана только одна запись для первой карточки")
        
@admin.register(PriceCardOne)
class PriceCardOneAdmin(admin.ModelAdmin):
    form = PriceCardOneForm
    list_display = ['title', 'upperButton', 'price', 'description', 'button', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

@admin.register(PriceCardOneOption)
class PriceCardOneOptionAdmin(admin.ModelAdmin):
    list_display = ['option']
    readonly_fields = ('created',)
    search_fields = ['updated', 'option']

class PriceCardTwoForm(forms.ModelForm):
    class Meta:
        model = PriceCardTwo
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and PriceCardTwo.objects.exists():
            raise ValidationError("Может быть создана только одна запись для второй карточки")
        
@admin.register(PriceCardTwo)
class PriceCardTwoAdmin(admin.ModelAdmin):
    form = PriceCardTwoForm
    list_display = ['title', 'upperButton', 'price', 'description', 'button', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

@admin.register(PriceCardTwoOption)
class PriceCardTwoOptionAdmin(admin.ModelAdmin):
    list_display = ['option']
    readonly_fields = ('created',)
    search_fields = ['updated', 'option']

class PriceCardThreeForm(forms.ModelForm):
    class Meta:
        model = PriceCardThree
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and PriceCardThree.objects.exists():
            raise ValidationError("Может быть создана только одна запись для третей карточки")
        
@admin.register(PriceCardThree)
class PriceCardThreeAdmin(admin.ModelAdmin):
    form = PriceCardThreeForm
    list_display = ['title', 'price', 'description', 'button', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

@admin.register(PriceCardThreeOption)
class PriceCardThreeOptionAdmin(admin.ModelAdmin):
    list_display = ['option']
    readonly_fields = ('created',)
    search_fields = ['updated', 'option']

class DarkBlockForm(forms.ModelForm):
    class Meta:
        model = DarkBlock
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and DarkBlock.objects.exists():
            raise ValidationError("Может быть создана только одна запись для темного блока")
        
@admin.register(DarkBlock)
class DarkBlockAdmin(admin.ModelAdmin):
    form = DarkBlockForm
    list_display = ['title', 'subtitle', 'descrition', 'secondTitle', 'secondDescription', 'button', 'updated']
    readonly_fields = ('created',)
    search_fields = ['updated']

class HelpBlockForm(forms.ModelForm):
    class Meta:
        model = HelpBlock
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and HelpBlock.objects.exists():
            raise ValidationError("Может быть создана только одна запись для блока помощи")
        
@admin.register(HelpBlock)
class HelpBlockAdmin(admin.ModelAdmin):
    form = HelpBlockForm
    list_display = ['title', 'subtitle']
    readonly_fields = ('created',)
    search_fields = ['updated']

class LinkTitleBlockForm(forms.ModelForm):
    class Meta:
        model = LinkTitleBlock
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and LinkTitleBlock.objects.exists():
            raise ValidationError("Может быть создана только одна запись для блока заголовков ссылок")
        
@admin.register(LinkTitleBlock)
class LinkTitleBlockAdmin(admin.ModelAdmin):
    form = LinkTitleBlockForm
    list_display = ['titleOne', 'titleTwo', 'titleThree']
    readonly_fields = ('created',)
    search_fields = ['updated']

@admin.register(LinkOptionBlock)
class LinkOptionBlockAdmin(admin.ModelAdmin):
    list_display = ['optionOne', 'optionTwo', 'optionThree']
    readonly_fields = ('created',)
    search_fields = ['updated']