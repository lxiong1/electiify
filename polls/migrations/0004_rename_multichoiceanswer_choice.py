# Generated by Django 4.0.3 on 2022-04-09 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_rename_multi_choice_question_multichoiceanswer_question"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MultiChoiceAnswer",
            new_name="Choice",
        ),
    ]
