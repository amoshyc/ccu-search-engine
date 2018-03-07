import json
import shutil
import pathlib

DOC_DIR = pathlib.Path('../data/ettoday/').resolve()
DOC_PATHS = sorted(DOC_DIR.glob('ettoday*.rec'))

JSON_DIR = pathlib.Path('../data/json/').resolve()
if JSON_DIR.exists():
    shutil.rmtree(str(JSON_DIR))
JSON_DIR.mkdir(exist_ok=True)

record_cnt = 0


def save_record(record):
    global record_cnt
    json_path = (JSON_DIR / f'{record_cnt:03d}.json')
    with json_path.open('w') as f:
        json.dump(record, f, ensure_ascii=False)
    record_cnt += 1


def extract_json(data):
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
            save_record(record)


for path in DOC_PATHS:
    with path.open('r') as f:
        data = f.readlines()
    print(path, end='...')
    extract_json(data)
    print('done')

print('#Records:', record_cnt)