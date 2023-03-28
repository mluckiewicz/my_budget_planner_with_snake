# Generated by Django 4.1.7 on 2023-03-27 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planner", "0007_rename_budgets_budget_rename_categories_category_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="budget",
            options={"verbose_name": "Budget", "verbose_name_plural": "Budgets"},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="repeatabletransaction",
            options={
                "verbose_name": "RepeatableTransaction",
                "verbose_name_plural": "RepeatableTransactions",
            },
        ),
        migrations.AlterModelOptions(
            name="transaction",
            options={
                "verbose_name": "Transaction",
                "verbose_name_plural": "Transactions",
            },
        ),
        migrations.AlterModelOptions(
            name="type",
            options={"verbose_name": "Type", "verbose_name_plural": "Types"},
        ),
        migrations.AlterField(
            model_name="repeatabletransaction",
            name="description",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="description",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="execution_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 3, 27, 21, 50, 14, 254045, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]