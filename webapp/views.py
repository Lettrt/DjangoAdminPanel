from django.shortcuts import render
from django.views.generic import ListView
from .models import Header, FirstTopCard, SecondTopCard, ThirdTopCard, ScoreBoardMain, MentorTitle, MentorOne, MentorTwo, PriceTitile, PriceCardOne, PriceCardOneOption, PriceCardTwo, PriceCardTwoOption, PriceCardThree, PriceCardThreeOption, DarkBlock, HelpBlock, LinkTitleBlock, LinkOptionBlock

class AllModelsViews(ListView):
    template_name = 'main.html'
    model = Header

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['firsttopcard'] = FirstTopCard.objects.all()
        context['secondtopcard'] = SecondTopCard.objects.all()
        context['thirdtopcard'] = ThirdTopCard.objects.all()
        context['scoreboardmain'] = ScoreBoardMain.objects.all()
        context['mentortitle'] = MentorTitle.objects.all()
        context['mentorone'] = MentorOne.objects.all()
        context['mentortwo'] = MentorTwo.objects.all()
        context['pricetitile'] = PriceTitile.objects.all()
        context['pricecardone'] = PriceCardOne.objects.all()
        context['pricecardoneoption'] = PriceCardOneOption.objects.all()
        context['pricecardtwo'] = PriceCardTwo.objects.all()
        context['pricecardtwooption'] = PriceCardTwoOption.objects.all()
        context['pricecardthree'] = PriceCardThree.objects.all()
        context['pricecardthreeoption'] = PriceCardThreeOption.objects.all()
        context['darkblock'] = DarkBlock.objects.all()
        context['helpblock'] = HelpBlock.objects.all()
        context['linktitleblock'] = LinkTitleBlock.objects.all()
        context['linkoptionblock'] = LinkOptionBlock.objects.all()
        return context