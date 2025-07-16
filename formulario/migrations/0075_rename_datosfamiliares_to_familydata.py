from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ("formulario", "0074_rename_recluta_to_personaldata"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DatosFamiliares",
            new_name="FamilyData",
        ),
    ]