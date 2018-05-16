# Generated by Django 2.0.5 on 2018-05-16 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calculator', '0042_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id_keyword', models.AutoField(primary_key=True, serialize=False)),
                ('keyword', models.CharField(blank=True, max_length=25)),
            ],
            options={
                'verbose_name': 'Keyword',
                'verbose_name_plural': 'keywords',
            },
        ),
        migrations.CreateModel(
            name='Warscroll',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nazwa')),
                ('army', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Army')),
                ('keywords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warscrolls.Keyword')),
            ],
            options={
                'verbose_name': 'Warscroll',
                'verbose_name_plural': 'Warscrolls',
            },
        ),
    ]
