from xml.etree import ElementTree

tree = ElementTree.parse('./nlp.txt.xml')
root = tree.getroot()

for sentence in root.iter('sentence'):
  predicates = {} # {述語idx: 述語}
  subjects   = {} # {述語idx: 主語}
  objects    = {} # {述語idx: 目的語}

  for dep in sentence.iterfind('.//dependencies[@type="collapsed-dependencies"]/dep'):
    dep_type = dep.get('type')
    if not dep_type in ['nsubj', 'dobj']: continue
    governor      = dep.find('governor')
    dependent     = dep.find('dependent')
    governor_idx  = int(governor.get('idx'))
    dependent_idx = int(dependent.get('idx'))

    predicates[governor_idx] = governor.text # 述語登録

    if dep_type == 'nsubj': subjects[governor_idx] = dependent.text # 主語登録
    if dep_type == 'dobj':  objects[governor_idx]  = dependent.text # 目的語登録

  #print(predicates)
  #print(subjects)
  #print(objects)
  for index, predicate in predicates.items():
    if not index in subjects: continue
    if not index in objects:  continue
    subject = subjects[index]
    obje    = objects[index]
    print("%s\t%s\t%s" % (subject, predicate, obje))
