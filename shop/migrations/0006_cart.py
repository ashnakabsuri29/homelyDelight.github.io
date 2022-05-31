# Generated by Django 4.0.3 on 2022-03-30 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_cook_pword_remove_cook_uname_cook_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.cook')),
                ('items', models.ManyToManyField(to='shop.dish')),
            ],
        ),
    ]
