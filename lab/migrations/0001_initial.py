# Generated by Django 3.2.5 on 2021-07-15 11:01

from django.db import migrations, models
import django_json_field_schema_validator.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('properties', models.JSONField(validators=[django_json_field_schema_validator.validators.JSONFieldSchemaValidator({'$schema': 'http://json-schema.org/draft-07/schema#', 'properties': {'CurrentMedications': {'items': {'properties': {'Action': {'items': {'type': 'string'}, 'minItems': 1, 'type': 'array'}, 'Drugs': {'items': {'minItems': 1, 'properties': {'Generic': {'items': {'type': 'string'}, 'minItems': 1, 'type': 'array'}, 'Trade': {'items': {'type': 'string'}, 'minItems': 1, 'type': 'array'}}, 'required': ['Generic', 'Trade'], 'type': 'object'}, 'minItems': 1, 'type': 'array'}, 'GeneInfo': {'items': {'type': 'object'}, 'minItems': 1, 'type': 'array'}, 'GroupPhenotype': {'type': 'string'}, 'Recommendation': {'type': 'string'}, 'TheraputicArea': {'items': {'type': 'string'}, 'minItems': 1, 'type': 'array'}}, 'required': ['Drugs', 'TheraputicArea', 'GeneInfo', 'GroupPhenotype', 'Action', 'Recommendation'], 'type': 'object'}, 'type': 'array'}, 'DateGenerated': {'type': 'string'}, 'KnowledgebaseVersion': {'type': 'string'}, 'PipelineVersion': {'type': 'string'}, 'SampleNumber': {'type': 'string'}, 'Sequencer': {'type': 'string'}}, 'required': ['SampleNumber', 'PipelineVersion', 'Sequencer', 'KnowledgebaseVersion', 'DateGenerated', 'CurrentMedications'], 'type': 'object'})])),
            ],
        ),
    ]
