# Generated by Django 3.2.8 on 2021-10-30 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mcq_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_exam', to='mcq_test.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_student', to='mcq_test.student')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_right', models.BooleanField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_answer', to='mcq_test.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_question', to='mcq_test.question')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_score', to='score.score')),
            ],
        ),
    ]
