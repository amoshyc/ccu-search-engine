import pathlib
from tqdm import tqdm
from elasticsearch import Elasticsearch
from elasticsearch import helpers

DOC_DIR = pathlib.Path('../data/ettoday/').resolve()
DOC_PATHS = sorted(DOC_DIR.glob('et*.rec'))
BATCH_SIZE = 1000

es = Elasticsearch()
# curl -XDELETE 'localhost:9200/ettoday?pretty'
es.indices.delete(index='ettoday', ignore_unavailable=True)


def extract_record(data):
    for line in data:
        line = line.strip()
        if line.startswith('@GAISRec:'):
            record = dict()
        elif line.startswith('@U:'):
            record['url'] = line[3:]
        elif line.startswith('@T:'):
            record['title'] = line[3:]
        elif line.startswith('@B:'):
            pass
        else:
            record['body'] = line
            yield record


cnt = 0
for path in DOC_PATHS:
    print(path, end='...')
    with path.open('r') as f:
        data = f.readlines()

    actions = []
    for record in extract_record(data):
        actions.append({
            '_index': 'ettoday',
            '_type': 'news',
            '_id': cnt,
            '_source': record,
        })
        cnt += 1
        if len(actions) == BATCH_SIZE:
            helpers.bulk(es, actions)
            actions = []

    if len(actions) > 0:
        helpers.bulk(es, actions)

    print('done')

print('#Record:', cnt)
