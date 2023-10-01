from django.test import TestCase
from .models import Header, FirstTopCard, SecondTopCard, ThirdTopCard, ScoreBoardMain, MentorTitle
from django.urls import reverse

class AllModelsViewsTestCase(TestCase):
    def setUp(self):
        self.header = Header.objects.create(
            subTitle="Test Subtitle",
            mainTitle="Test Main Title",
            buttonOne="Button One",
            buttonTwo="Button Two"
        )
        self.firsttopcard = FirstTopCard.objects.create(
            title="Test Title",
            description="Test Description",
            button="Test Button"
        )
        self.secondtopcard = SecondTopCard.objects.create(
            title="Test Title",
            description="Test Description",
            button="Test Button"
        )
        self.thirdtopcard = ThirdTopCard.objects.create(
            title="Test Title",
            description="Test Description",
            button="Test Button"
        )
        self.scoreboardmain = ScoreBoardMain.objects.create(
            subtitle="Test Subtitle",
            title="Test Title",
            colOneNum="1",
            colOneText="col OneText",
            colTwoNum = '2',
            colTwoText = 'col TwoText',
            colThreeNum = '3',
            colThreeText = 'col ThreeText',
            colFourNum = '4',
            colFourText = 'colFourText'
        )
        self.mentortitle = MentorTitle.objects.create(
            title="Mentor Title",
        )

    def test_header_model(self):
        self.assertEqual(str(self.header), self.header.mainTitle)
    
    def test_firsttopcard_model(self):
        self.assertEqual(str(self.firsttopcard), self.firsttopcard.title)

    def test_secondtopcard_model(self):
        self.assertEqual(str(self.secondtopcard), self.secondtopcard.title)

    def test_thirdtopcard_model(self):
        self.assertEqual(str(self.thirdtopcard), self.thirdtopcard.title)

    def test_scoreboardmain_model(self):
        self.assertEqual(str(self.scoreboardmain), self.scoreboardmain.title)

    def test_mentortitle_model(self):
        self.assertEqual(str(self.mentortitle), self.mentortitle.title)

    
    def test_header_list_view(self):
        response = self.client.get(reverse('allmodelsviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.header.mainTitle)
    
    def test_firsttopcard_list_view(self):
        response = self.client.get(reverse('allmodelsviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.firsttopcard.title)

    def test_secondtopcard_list_view(self):
        response = self.client.get(reverse('allmodelsviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.secondtopcard.title)
    
    def test_thirdtopcard_list_view(self):
        response = self.client.get(reverse('allmodelsviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.thirdtopcard.title)

    def test_scoreboardmain_list_view(self):
        response = self.client.get(reverse('allmodelsviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.scoreboardmain.title)

    def test_mentortitle_list_view(self):
        response = self.client.get(reverse('allmodelsviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.mentortitle.title)

 