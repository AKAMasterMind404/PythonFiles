import json

def toJSON(text):
    return json.loads("{" + text + "}")


def solve(text, Q, queries):
    jsonText = toJSON(text)
    prop = queries[0]
    return jsonText.prop

text = input()
Q = int(input())
queries = []
for _ in range(Q):
    queries.append(input())

out_ = solve(text, Q, queries)
for i_out_ in out_:
    print(i_out_)
