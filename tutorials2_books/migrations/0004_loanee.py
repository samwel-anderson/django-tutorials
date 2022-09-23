# Generated by Django 4.1.1 on 2022-09-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials2_books', '0003_alter_books_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loanee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanee_id', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated time')),
            ],
            options={
                'verbose_name': 'Loanee',
                'verbose_name_plural': 'Loanee',
                'permissions': (('can_apply_loan', 'Can Apply Loan'), ('can_repay_loan', 'Can Repay Loan'), ('can_cancel_application', 'Can Cancel Application')),
            },
        ),
    ]
