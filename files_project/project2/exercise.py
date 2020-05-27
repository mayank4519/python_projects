questions = open('questions.txt', 'r')
qlines = [line.strip() for line in questions.readlines()]

questions.close()

n = 0
m = len(qlines)

for qline in qlines:
    q, a = qline.split('=')
    user_ans = input("{}=".format(q))
    if user_ans == a:
        n += 1

result = open('result.txt','w')
result.write(f"{n}/{m}")
result.close()