import datetime
from unittest import skip
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Type, Transaction, RepeatableTransaction, UserCategory
from .utils.date_generator import DateCalculator
from .forms import AddSingleTransactionForm, AddRepeatableTransactionForm, AddCategoryForm
# Create your tests here.

class TestDateCalculator(TestCase):
    def setUp(self):
        self.start_date = datetime.date(2022, 1, 1)
        self.end_date = datetime.date(2022, 3, 31)
        self.dc = DateCalculator(self.start_date, self.end_date)

    def test_generate_daily_dates(self):
        dates = self.dc._generate_daily_dates()
        self.assertEqual(len(dates), (self.end_date - self.start_date).days + 1)

    def test_generate_weekly_dates(self):
        recurrence_value = 0 # Monday
        dates = self.dc._generate_weekly_dates(recurrence_value)
        for date in dates:
            self.assertEqual(date.weekday(), recurrence_value)

    def test_generate_monthly_dates(self):
        recurrence_value = 15 # 15th day of the month
        dates = self.dc._generate_monthly_dates(recurrence_value)
        self.assertEqual(len(dates), 3) # should generate 3 dates
        self.assertEqual(dates[0], self.start_date.replace(day=recurrence_value)) # first date should be the start date with the day replaced by the recurrence value
        for i in range(1, len(dates)):
            self.assertEqual(dates[i].day, recurrence_value) # all other dates should have the recurrence value as the day
               
    def test_generate_monthly_dates_next_year(self):
        start_date = datetime.date(2022, 1, 1)
        end_date = datetime.date(2023, 1, 31)
        target = [
            datetime.date(2022, 1, 15),
            datetime.date(2022, 2, 15),
            datetime.date(2022, 3, 15),
            datetime.date(2022, 4, 15),
            datetime.date(2022, 5, 15),
            datetime.date(2022, 6, 15),
            datetime.date(2022, 7, 15),
            datetime.date(2022, 8, 15),
            datetime.date(2022, 9, 15),
            datetime.date(2022, 10, 15),
            datetime.date(2022, 11, 15),
            datetime.date(2022, 12, 15),
            datetime.date(2023, 1, 15),
        ]
        dc = DateCalculator(start_date, end_date)
        recurrence_value = 15 # 15th day of the month
        dates = dc._generate_monthly_dates(recurrence_value)
        self.assertEqual(len(dates), 13) # should generate 3 dates
        self.assertEqual(dates[0], start_date.replace(day=recurrence_value)) # first date should be the start date with the day replaced by the recurrence value
        for i in range(1, len(dates)):
            self.assertEqual(dates[i], target[i]) # all other dates should have the recurrence value as the day

    def test_generate_quaterly_dates(self):
        # TODO add test for quarterly dates
        pass

    def test_get_dates_daily(self):
        dates = self.dc.get_dates('daily')
        self.assertEqual(len(dates), (self.end_date - self.start_date).days + 1)

    def test_get_dates_weekly(self):
        recurrence_value = 0 # Monday
        dates = self.dc.get_dates('weekly', recurrence_value)
        for date in dates:
            self.assertEqual(date.weekday(), recurrence_value)

    def test_get_dates_monthly(self):
        recurrence_value = 15 # 15th day of the month
        dates = self.dc.get_dates('monthly', recurrence_value)
        self.assertEqual(len(dates), 3) # should generate 3 dates
        self.assertEqual(dates[0], self.start_date.replace(day=recurrence_value)) # first date should be the start date with the day replaced by the recurrence value
        for i in range(1, len(dates)):
            self.assertEqual(dates[i].day, recurrence_value) # all other dates should have the recurrence value as the day

    def test_get_dates_quaterly(self):
        # TODO add test for quarterly dates
        pass
    
    
@skip("In progress")
class DeleteCategoriesTest(TestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        # create a type
        self.type = Type.objects.create(
            type_name='Type 1')
        # create some categories
        self.category1 = Category.objects.create(
            category_name='Category 1',
            type=self.type)
        self.category1.users.add(self.user)
        self.category2 = Category.objects.create(
            category_name='Category 2',
            type=self.type)
        self.category2.users.add(self.user)

    def test_delete_categories(self):
        # login as the user
        self.client.login(username='testuser', password='testpass')
        # send a POST request to delete the categories
        url = reverse('delete_categories')
        response = self.client.post(url, {'ids[]': [self.category1.id, self.category2.id]})
        # check that the categories have been deleted
        self.assertFalse(Category.objects.filter(id=self.category1.id).exists())
        self.assertFalse(Category.objects.filter(id=self.category2.id).exists())
        # check that the response is successful
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'success': True})

    def test_invalid_request_method(self):
        # send a GET request instead of a POST request
        url = reverse('delete_categories')
        response = self.client.get(url)
        # check that the response indicates an invalid request method
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'success': False, 'message': 'Invalid request method'})
    



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        
        self.type = Type.objects.create(
            type_name="wydatki"
        )
        
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.category = Category.objects.create(
            category_name="Test Category",
            type=self.type,
        )
        self.user_category = UserCategory.objects.create(
            user=self.user,
            category=self.category,
        )
        

    def test_dashboard_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('planner:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    @skip("in progress")
    def test_add_single_transaction_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('planner:add_single'), {
            'type': self.type.pk,
            'amount': 100,
            'category': self.category.pk,
            'budget': '',
            'execution_date': '2022-04-11',
            'is_executed': True,
            'description': 'Test transaction'
        })
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/planner/dashboard/', 200)
        self.assertTrue(Transaction.objects.filter(
            user=self.user,
            type=self.type.pk,
            amount=100,
            category=self.category,
            execution_date='2022-04-11',
            is_executed=True,
            description='Test transaction'
        ).exists())

    @skip("in progress")
    def test_add_repeatable_transaction_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('planner:add_repeatable'), {
            'type': self.type.pk,
            'base_amout': 100,
            'start_date': '2022-04-11',
            'end_date': '',
            'recurrence_type': 'daily',
            'recurrence_value': 1,
            'category': self.category.pk,
            'budget': '',
            'description': 'Test repeatable transaction'
        })
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/planner/dashboard/', 200)
        self.assertTrue(RepeatableTransaction.objects.filter(
            user=self.user,
            type=self.type.pk,
            base_amout=100,
            start_date='2022-04-11',
            end_date=None,
            recurrence_type='daily',
            recurrence_value=1,
            category=self.category,
            description='Test repeatable transaction'
        ).exists())

    def test_add_category_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('planner:add_category'), {
            'category_name': 'New Category',
            'type': self.type.pk,
            'back_url': '/planner/dashboard/',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/planner/dashboard/')
        self.assertTrue(Category.objects.filter(
            category_name='New Category',
            type=self.type.pk,
        ).exists())
        self.assertTrue(UserCategory.objects.filter(
            user=self.user,
            category=Category.objects.get(category_name='New Category'),
        ).exists())
