# Generated by Django 2.1.4 on 2018-12-29 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buttons', '0002_auto_20181229_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('14L', '14L'), ('15L', '15L'), ('16L', '16L'), ('17L', '17L'), ('18L', '18L'), ('19L', '19L'), ('20L', '20L'), ('21L', '21L'), ('22L', '22L'), ('23L', '23L'), ('24L', '24L'), ('25L', '25L'), ('26L', '26L'), ('27L', '27L'), ('28L', '28L'), ('29L', '29L'), ('30L', '30L'), ('31L', '31L'), ('32L', '32L'), ('33L', '33L'), ('34L', '34L'), ('35L', '35L'), ('36L', '36L')], default='14L', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'sizes',
                'ordering': ['size'],
            },
        ),
        migrations.RemoveField(
            model_name='button',
            name='size',
        ),
        migrations.AddField(
            model_name='button',
            name='size',
            field=models.ManyToManyField(related_name='sizes', to='buttons.Sizes'),
        ),
    ]