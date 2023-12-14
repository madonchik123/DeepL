import requests

def translate_text(text, outputlang, inputlang=None):
  
  params = {
    'method': 'LMT_handle_jobs',
  }
  
  json_data = {
    'jsonrpc': '2.0',
    'method': 'LMT_handle_jobs',
    'params': {
      'jobs': [
        {
          'kind': 'default',
          'sentences': [
            {
              'text': text,
              'id': 1,
              'prefix': '',
            },
          ],
          'raw_en_context_before': [],
          'raw_en_context_after': [],
          'preferred_num_beams': 4,
          'quality': 'fast',
        },
      ],
      'lang': {
        'target_lang': outputlang,
        'preference': {
          'weight': {
            'DE': 0.32942,
            'EN': 15.19922,
            'ES': 0.09817,
            'FR': 0.12459,
            'IT': 0.08959,
            'JA': 0.20261,
            'NL': 0.10217,
            'PL': 0.08653,
            'PT': 0.07999,
            'RU': 5.51509,
            'ZH': 0.7037,
            'BG': 1.21299,
            'CS': 0.0781,
            'DA': 0.07693,
            'EL': 0.04041,
            'ET': 0.10027,
            'FI': 0.05621,
            'HU': 0.05333,
            'ID': 0.06897,
            'LV': 0.05432,
            'LT': 0.0551,
            'RO': 0.09596,
            'SK': 0.06615,
            'SL': 0.08456,
            'SV': 0.09236,
            'TR': 0.43058,
            'UK': 1.65217,
            'KO': 0.03963,
            'NB': 0.08007,
          },
          'default': 'default',
        },
        'source_lang_user_selected': inputlang if inputlang else 'auto',
      },
      'priority': -1,
      'commonJobParams': {
        'mode': 'translate',
        'textType': 'plaintext',
        'browserType': 10241,
      },
      'timestamp': 1702557217443,
    },
    'id': 56510017,
  }
  
  response = requests.post('https://www2.deepl.com/jsonrpc', params=params, json=json_data)
  
  first_result = response.json()['result']['translations'][0]['beams'][0]['sentences'][0]['text']
  print(first_result)
  return first_result