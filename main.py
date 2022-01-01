import dialog
import calc

speakBot = dialog.Dialog()

running = True
array = []
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
speakBot.result(ans)
