# Generated by Django 4.0.4 on 2022-06-01 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie'),
        ),
    ]
