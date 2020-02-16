from xml.etree import ElementTree
import pprint

tree = ElementTree.parse('./nlp.txt.xml')
root = tree.getroot()

# 共参照の辞書作成
coreferences = {} # {(sentend_id, token_id): Dict}
for coreference in root.iterfind('.//coreference/coreference'):
  repr = None
  for mention in coreference.iterfind('mention'):
    # 代表参照表現
    if mention.get('representative') == 'true':
      repr = mention.find('text').text
      continue
    # 参照表現
    sentence_id = int(mention.find('sentence').text)
    start = int(mention.find('start').text)
    end = int(mention.find('end').text)
    text = mention.find('text').text
    coreferences[(sentence_id, start)] = {
      'end': end,
      'original_text': text,
      'repr_text': repr,
    }

# 共参照辞書を用いて参照表現を代表参照表現に置き換えたセンテンスを作成
for sentence in root.iter('sentence'):
  if not sentence.get('id'): continue

  sentence_id = int(sentence.get('id'))
  coreference = None

  for token in sentence.iter('token'):
    token_id = int(token.get('id'))
    new_token_text = None

    if (sentence_id, token_id) in coreferences: # 辞書にある
      coreference = coreferences[(sentence_id, token_id)]
      new_token_text = '「%s（%s）」' % (coreference['repr_text'], coreference['original_text'])
    elif coreference == None: # 参照表現の中でない
      new_token_text = token.find('word').text
    elif token_id < coreference['end']: # 参照表現のトークン
      continue
    elif token_id >= coreference['end']: # 参照表現の終わり
      coreference = None
      new_token_text = token.find('word').text

    print('%s ' % new_token_text, end='')
  print('')
