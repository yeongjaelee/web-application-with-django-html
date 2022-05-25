# Generated by Django 4.0.4 on 2022-05-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='blog classification', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_image', models.ImageField(blank=True, upload_to='')),
                ('content', models.TextField()),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(help_text="post's classification", to='blog.category')),
            ],
        ),
    ]