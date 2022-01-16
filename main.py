import dialog
import calc
import show

speakBot = dialog.Dialog()

# test data
running = False
array = [[1,1,4,4,0], [2,2,5,5,1], [3,3,6,6,2], [4,4,7,7,3], [5,5,8,8,4], [6,6,9,9,5], [7,7,10,10,6], [8,8,11,11,7], [9,9,12,12,0]]
cnt = len(array)

# running = True
# array = []
# cnt = 1

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
show.GenerateGraph(array).showGraph()
