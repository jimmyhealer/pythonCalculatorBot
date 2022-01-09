import matplotlib.pyplot as plt
import matplotlib.patches as patches

class GenerateGraph:
  def __init__(self, datas):
    self.__datas = datas

  def showGraph(self):
    fig, ax = plt.subplots()
    xmin, ymin, xmax, ymax = tuple(self.__datas[0])
    print("yaaa", xmin, ymin, xmax, ymax)
    for data in self.__datas:
      print("add", data)
      ax.add_patch(
        patches.Rectangle(
          (data[0], data[1]),
          data[2] - data[0],
          data[3] - data[1],
          edgecolor = 'black',
          facecolor = 'aqua',
          fill=True
        )
      )
      xmin = min(xmin, data[0], data[2])
      ymin = min(ymin, data[1], data[3])
      xmax = max(xmax, data[0], data[2])
      ymax = max(ymax, data[1], data[3])

    xmargin = (xmax - xmin) / 20
    ymargin = (ymax - ymin) / 20
    xmin -= xmargin
    ymin -= ymargin
    xmax += xmargin
    ymax += ymargin
    ax = plt.gca()
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    plt.show()

if __name__ == '__main__':
  data = [[0.5, 0.5, 20, 20], [15, 15, 30, 10]]
  graph = GenerateGraph(data)
  graph.showGraph()