# Generated by Django 2.2.7 on 2019-12-12 11:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_type', models.CharField(choices=[('1', 'Patient'), ('2', 'Therapist')], max_length=10)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('1', 'M'), ('2', 'F'), ('3', 'Transgender')], max_length=15)),
                ('phone', models.CharField(blank=True, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be valid', regex='^\\+?1?\\d{9,10}$')])),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GuestContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_data', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_photo')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('1', 'Stress'), ('2', 'Depression'), ('3', 'Anxiety'), ('4', 'OCD'), ('5', 'Eating Disorders'), ('6', 'Relationships'), ('7', 'Work Stress'), ('8', 'Self Doubt'), ('9', 'Addiction and Substance Abuse'), ('10', 'Suicidal Tendency')], max_length=20)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('subtitle', models.CharField(max_length=75, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField(unique=True)),
                ('therapist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]