# Generated by Django 5.1.8 on 2025-05-05 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('method', models.CharField(choices=[('CASH', 'Cash'), ('CARD', 'Credit Card'), ('MOBILE', 'Mobile Payment'), ('OTHER', 'Other')], max_length=10)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed'), ('REFUNDED', 'Refunded')], default='PENDING', max_length=10)),
                ('transaction_id', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='orders.order')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
