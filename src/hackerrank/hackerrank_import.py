# {
#   "contest": "Master",
#   "challenge": "Palindrome Index",
#   "code": "...",
#   "score": 1,
#   "language": "cpp"
# }

# python hackerrank/hackerrank_import.py /Users/abnerjcorreajr/Downloads/abnercorreajr_data.json /usr/local/development/Code/c/ml-ai/algorithms/src/hackerrank

import json
import os
import sys

if __name__ == '__main__':
    assert len(sys.argv) == 3, 'Usage:\nhackerrank_import.py <export_path> <output_dir>'

    with open(sys.argv[1]) as f:
        profile = json.load(f)

    challenges = [s for s in profile['submissions'] if s['score'] == 1.0]

    output_dir = sys.argv[2]

    for challenge in challenges:
        ext = 'py' if challenge['language'].startswith('python') else challenge['language']
        file_name = challenge['challenge'].replace(' ', '').replace('!', '').replace(':', '').replace('\'', '').replace(',', '') + '.' + ext
        file_path = os.path.join(output_dir, file_name)
        code = challenge['code']
        with open(file_path, 'w') as f:
            f.write(code)
