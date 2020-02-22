import utilities
import re
import collections

raw_features = []
rare_words = []
features = []

with open('chapter8/sentiment.txt', 'r') as fp:
  for line in fp:
    match = re.match(r'[+-]1 (.+)', line.strip())
    words = match[1].split(' ')
    raw_features += words

# 空文字を削除
raw_features = [w for w in raw_features if len(w) > 0]

# 頻度が5以下の単語抽出
counter = collections.Counter(raw_features)
for w, i in counter.items():
  if i > 5: continue
  rare_words.append(w)

# 重複削除
raw_features = list(set(raw_features))

# ストップワードか低頻度の単語を取り除く
for feature in raw_features:
  # ストップワードを除く
  if utilities.is_stop_word(feature): continue
  # 低頻度を除く
  if feature in rare_words: continue
  # 数字と記号を除く
  if not re.match('^[a-zA-Z]+$', feature): continue
  features.append(feature)

print('features', features, len(features))

with open('chapter8/features.txt', 'w') as fp:
  fp.writelines('\n'.join(features))
