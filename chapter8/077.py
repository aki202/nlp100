TP = 0
TN = 0
FP = 0
FN = 0

with open('outputs/sentiment_result.txt', 'r') as fp:
  for line in fp:
    predict, label, probability = line.strip().split('\t')
    if predict == label:
      if predict == '+1':
        TP += 1
      else:
        TN += 1
    else:
      if predict == '+1':
        FP += 1
      else:
        FN += 1

print('TP={}, TN={}, FP={}, FN={}'.format(TP, TN, FP, FN))

accuracy = (TP + TN) / (TP + TN + FP + FN) # 正解率
precision = TP / (TP + FP) # 適合率、予測の中に正解がどれだけ含まれているか
recall = TP / (TP + FN) # 再現率、正解全体がどれだけ予測されているか
f1 = (2 * accuracy * precision) / (accuracy + recall)

print('accuracy\t{}'.format(accuracy))
print('precision\t{}'.format(precision))
print('recall\t{}'.format(recall))
print('f1\t{}'.format(f1))
