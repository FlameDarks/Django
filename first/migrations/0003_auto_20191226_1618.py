# Generated by Django 3.0.1 on 2019-12-26 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20191225_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='书籍类别')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='cataId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='first.Catalog'),
        ),
    ]