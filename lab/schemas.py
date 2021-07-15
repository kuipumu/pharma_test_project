"""lab JSON schemas

Define any JSON schema rules using jsonschema rules to validate json fields on models.
    https://json-schema.org/understanding-json-schema/
Examples:
Function views
    1. Validate string array: {
        'type' : 'array',
        'items' : {
            'type' : 'object',
        },
        'minItems': 1
    }
"""

# Create your JSON schemas here.
string_schema = {
    'type' : 'string'
}

drugs_schema = {
    'type' : 'array',
    'items' : {
        'type' : 'object',
        'properties' : {
            'Generic' : {
                'type' : 'array',
                'items' : string_schema,
                'minItems': 1
            },
            'Trade' : {
                'type' : 'array',
                'items' : string_schema,
                'minItems': 1
            },
        },
        'minItems': 1,
        'required': [
            'Generic',
            'Trade',
        ]
    },
    'minItems': 1
}

theraputic_area_schema = {
    'type' : 'array',
    'items' : string_schema,
    'minItems': 1
}

gene_info_schema = {
    'type' : 'array',
    'items' : {
        'type' : 'object',
    },
    'minItems': 1
}

action_schema = {
    'type' : "array",
    'items' : string_schema,
    'minItems': 1
}

current_medications_schema = {
    'type' : 'array',
    'items' : {
        'type': 'object',
        'properties': {
            'Drugs': drugs_schema,
            'TheraputicArea': theraputic_area_schema,
            'GeneInfo': gene_info_schema,
            'GroupPhenotype': string_schema,
            'Action': action_schema,
            'Recommendation': string_schema,
        },
        'required': [
            'Drugs',
            'TheraputicArea',
            'GeneInfo',
            'GroupPhenotype',
            'Action',
            'Recommendation'
        ]
    },
}

sample_schema = {
    '$schema': f'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'SampleNumber': string_schema,
        'PipelineVersion': string_schema,
        'Sequencer': string_schema,
        'KnowledgebaseVersion': string_schema,
        'DateGenerated': string_schema,
        'CurrentMedications' : current_medications_schema
    },
    'required': [
        'SampleNumber',
        'PipelineVersion',
        'Sequencer',
        'KnowledgebaseVersion',
        'DateGenerated',
        'CurrentMedications'
    ]
}
