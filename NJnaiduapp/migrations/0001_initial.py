# Generated by Django 2.2.10 on 2020-03-05 06:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure_name', models.CharField(blank=True, max_length=200, null=True)),
                ('procedure_description', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='procedure')),
                ('meta_tag', models.CharField(blank=True, max_length=30, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_1', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_ip_address', models.CharField(blank=True, max_length=50, null=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_c_user', to='NJnaiduapp.User')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_m_user', to='NJnaiduapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('icon', models.CharField(blank=True, max_length=200, null=True)),
                ('iconcolour', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whyus_c_user', to='NJnaiduapp.User')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whyus_m_user', to='NJnaiduapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Specialities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality_name', models.CharField(blank=True, max_length=200, null=True)),
                ('speciality_description', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='specialities')),
                ('meta_tag', models.CharField(blank=True, max_length=30, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('Procedure', models.ManyToManyField(blank=True, null=True, to='NJnaiduapp.Procedure')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialities_c_user', to='NJnaiduapp.User')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialities_m_user', to='NJnaiduapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Section2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('section2_image', models.ImageField(blank=True, null=True, upload_to='section2')),
                ('section2background_image', models.ImageField(blank=True, null=True, upload_to='section2back')),
                ('happy_patients', models.IntegerField(blank=True, default='0', null=True)),
                ('surgeries', models.IntegerField(blank=True, default='0', null=True)),
                ('doctors', models.IntegerField(blank=True, default='0', null=True)),
                ('clinics', models.IntegerField(blank=True, default='0', null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section2_c_user', to='NJnaiduapp.User')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section2_m_user', to='NJnaiduapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Section1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('section_image', models.ImageField(blank=True, null=True, upload_to='section1')),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section1_c_user', to='NJnaiduapp.User')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section1_m_user', to='NJnaiduapp.User')),
            ],
        ),
        migrations.AddField(
            model_name='procedure',
            name='created_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='procedure_c_user', to='NJnaiduapp.User'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='modified_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='procedure_m_user', to='NJnaiduapp.User'),
        ),
        migrations.CreateModel(
            name='Ourteam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_image', models.ImageField(upload_to='ourteam')),
                ('doctor_name', models.CharField(blank=True, max_length=50, null=True)),
                ('doctor_designation', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ourteam_c_user', to='NJnaiduapp.User')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ourteam_m_user', to='NJnaiduapp.User')),
                ('specialities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NJnaiduapp.Specialities')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='itemimage')),
                ('meta_tag', models.CharField(blank=True, max_length=30, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_c_user', to='NJnaiduapp.User')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_m_user', to='NJnaiduapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images_c_user', to='NJnaiduapp.User')),
                ('events', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NJnaiduapp.Event')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images_m_user', to='NJnaiduapp.User')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='created_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_c_user', to='NJnaiduapp.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='modified_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_m_user', to='NJnaiduapp.User'),
        ),
        migrations.CreateModel(
            name='ContactUsForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contactusform_c_user', to='NJnaiduapp.User')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contactusform_m_user', to='NJnaiduapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('category_description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('active_from', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('active_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_c_user', to='NJnaiduapp.User')),
                ('item', models.ManyToManyField(blank=True, null=True, to='NJnaiduapp.Item')),
                ('modified_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_m_user', to='NJnaiduapp.User')),
            ],
        ),
    ]