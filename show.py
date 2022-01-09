import matplotlib.pyplot as plt
import matplotlib.patches as patches
import shapely.geometry as sg
import shapely.ops as ops
import geopandas as gpd

class GenerateGraph:
  def __init__(self, datas):
    self.__datas = datas

  def showGraph(self):
    xmin, ymin, xmax, ymax = tuple(self.__datas[0])
    polygons = []
    for data in self.__datas:
      polygons.append(sg.box(data[0], data[1], data[2], data[3], ))
      xmin = min(xmin, data[0], data[2])
      ymin = min(ymin, data[1], data[3])
      xmax = max(xmax, data[0], data[2])
      ymax = max(ymax, data[1], data[3])

    boundary = gpd.GeoSeries(ops.unary_union(polygons))
    boundary.plot(color = "aqua", edgecolor = "black")

    print("plt show")
    plt.show()

if __name__ == '__main__':
  data = [[0.5, 0.5, 20, 20], [15, 15, 30, 10]]
  graph = GenerateGraph(data)
  graph.showGraph()