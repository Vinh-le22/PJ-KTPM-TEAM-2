from django.db import migrations

def add_default_categories(apps, schema_editor):
    Category = apps.get_model('books', 'Category')
    categories = [
        'Tiểu thuyết',
        'Trinh thám',
        'Khoa học viễn tưởng',
        'Kinh dị',
        'Tâm lý - Kỹ năng sống',
        'Lịch sử',
        'Kinh tế',
        'Thiếu nhi',
        'Học thuật - Giáo trình',
        'Truyện tranh'
    ]
    for category_name in categories:
        Category.objects.get_or_create(name=category_name)

def remove_default_categories(apps, schema_editor):
    Category = apps.get_model('books', 'Category')
    categories = [
        'Tiểu thuyết',
        'Trinh thám',
        'Khoa học viễn tưởng',
        'Kinh dị',
        'Tâm lý - Kỹ năng sống',
        'Lịch sử',
        'Kinh tế',
        'Thiếu nhi',
        'Học thuật - Giáo trình',
        'Truyện tranh'
    ]
    Category.objects.filter(name__in=categories).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_categories, remove_default_categories),
    ] 