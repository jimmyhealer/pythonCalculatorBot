import dialog
import calc
import show

speakBot = dialog.Dialog()

running = True
array = [[13, 20, 15, 25], [14, 11, 37, 50]]
cnt = 1
while running:
  results = [[0, 0], [0, 0]]
  for i in range(2):
    for j in range(2):
      results[i][j] = speakBot.query(cnt, j, i)
  array.append([results[0][0], results[0][1], results[1][0], results[1][1]])

  if speakBot.queryContinue():
    running = False
    break
  cnt += 1

ans = calc.calc(array, cnt)
show.GenerateGraph(array).showGraph()
speakBot.result(ans)
