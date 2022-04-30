# Generated by Django 4.0.4 on 2022-04-29 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='menu',
            field=models.ForeignKey(blank=True, choices=[('image', 'Image'), ('links', 'Links'), ('video', 'Video')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.menu'),
        ),
    ]