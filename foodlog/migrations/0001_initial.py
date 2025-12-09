# Generated initial migration for Food model (simplified)
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
