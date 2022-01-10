import matplotlib.pyplot as plt
import matplotlib.patches as patches
import shapely.geometry as sg
import shapely.ops as ops
import geopandas as gpd
import descartes

class GenerateGraph:
  def __init__(self, datas):
    self.__datas = datas

  def showGraph(self):
    xmin, ymin, xmax, ymax = tuple(self.__datas[0])
    polygons = []
    for data in self.__datas:
      polygons.insert(0, sg.box(data[0], data[1], data[2], data[3], ))
      xmin = min(xmin, data[0], data[2])
      ymin = min(ymin, data[1], data[3])
      xmax = max(xmax, data[0], data[2])
      ymax = max(ymax, data[1], data[3])

    # boundary = gpd.GeoSeries(ops.unary_union(polygons))
    polygons.insert(0, ops.unary_union(polygons))
    gdf = gpd.GeoDataFrame(dict(geometry=polygons))
    fcs = [(0,1,1,1)] + [(0,0,0,0) for i in range(len(self.__datas))]
    lss = ['-'] + ['--' for i in range(len(self.__datas))]
    gdf.plot(linestyle=lss, linewidth=2, facecolor=fcs, edgecolor='black')
    # ax = boundary.plot(color = "aqua", edgecolor = "black")
    # for polygon in polygons:
    #   ax.add_patch(descartes.PolygonPatch(polygon, alpha=0))

    plt.show()

if __name__ == '__main__':
  data = [[0.5, 0.5, 20, 20], [15, 15, 30, 10]]
  graph = GenerateGraph(data)
  graph.showGraph()