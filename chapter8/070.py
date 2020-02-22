import codecs
import random

positives = []
negatives = []

with codecs.open('data/rt-polarity.pos', 'r', 'cp1252') as fp:
  for line in fp:
    positives.append('+1 %s' % line)

with codecs.open('data/rt-polarity.neg', 'r', 'cp1252') as fp:
  for line in fp:
    negatives.append('-1 %s' % line)

print('n(positives)=%d' % len(positives))
print('n(negatives)=%d' % len(negatives))

results = positives + negatives
random.shuffle(results)

with open('chapter8/sentiment.txt', 'w') as fp:
  fp.writelines(results)
