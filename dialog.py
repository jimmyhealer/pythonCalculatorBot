from speech import text_to_speech, speech_to_text
import unicodedata
import os


class _DialogContent:
  __COMPUTER = [
      '歡迎來到聊天計算機',
      '我聽不懂您在說甚麼?',
      '第#個矩形的左下角%座標為?',
      '第#個矩形的右上角%座標為?',
      '還有矩形嗎?',
      '覆蓋總面積為 #',
      '第#個矩形的顏色為?',
      '#面積為 @ ，占比 & %',
  ]
  WELCOME = __COMPUTER[0]
  UNDERSTAND = __COMPUTER[1]

  def content(self, index):
    return self.__COMPUTER[index]


class Dialog:
  def __init__(self) -> None:
    self.record = []
    self.__color = ['紅色', '橙色', '黃色', '綠色', '藍色', '紫色', '黑色', '青色']
    super().__init__()
    self.welcome()

  def __speak(self, text=''):
    if type(text) == str:
      print(text)
    elif type(text) == list:
      for line in text:
        print(line)

  def show(self):
    os.system("cls")
    self.__speak(self.record)
    pass

  def __isdigit(self, text: str):
    if text == '':
      return False
    if text.isdigit():
      return True
    number = "一二三四五六七八九十"
    if text in number:
      return True
    return False

  def __toInt(self, text: str):
    if text.isdigit():
      return int(text)
    number = "一二三四五六七八九十"
    if text in number:
      return int(number.index(text)) + 1

  def width(self, string):
    return sum(1+(unicodedata.east_asian_width(c) in "WF")
               for c in string)

  def speak(self, text='', current=1, gogoro=0):
    st = text_to_speech()
    if current == 1:
      ans = 'Computer> ' + text
      self.__speak(ans)
      st.speak(text, gogoro=gogoro)
    elif current == 0:
      ans = '%s %s <User' % (' '*(60 - self.width(text)), text)
      self.__speak(ans)
    self.record.append(ans)
    self.show()

  def listen(self):
    st = speech_to_text()
    cnt = 0
    while True:
      text = st.listen()
      self.speak(text, 0)
      if '抽' in text and ('gogoro' in text or '狗狗肉' in text):
        self.speak('就說 沒有 要抽 gogoro 要問幾次!!', gogoro=1)
        exit()
      elif '沒' in text:
        return 'no'
      elif '有' in text:
        return 'yes'
      elif self.__isdigit(text):
        return self.__toInt(text)
      elif text in self.__color:
        return 'color', self.__color.index(text)
      else:
        cnt += 1
        if cnt >= 5:
          self.speak('要問不問的，滾啦')
          exit()
        self.understand()

  def welcome(self):
    self.speak(_DialogContent().WELCOME, 1)

  def understand(self):
    self.speak(_DialogContent().UNDERSTAND, 1)

  def queryCoordinate(self, cnt: int, xy: int, lr: int):
    if lr == 0:
      self.speak(_DialogContent().content(2).replace(
          '#', '%d' % cnt).replace('%', "xy"[xy]), 1)
    elif lr == 1:
      self.speak(_DialogContent().content(3).replace(
          '#', '%d' % cnt).replace('%', "xy"[xy]), 1)
    while True:
      result = self.listen()
      try:
        if int(result):
          return result
      except:
        self.understand()

  def queryColor(self, cnt: int):
    self.speak(_DialogContent().content(6).replace(
        '#', '%d' % cnt), 1)
    while True:
      try:
        type, result = self.listen()
        if type == 'color':
          return result
        else:
          self.understand()
      except:
        self.understand()

  def queryContinue(self):
    self.speak(_DialogContent().content(4), 1)
    while True:
      result = self.listen()
      if result == 'yes':
        return False
      elif result == 'no':
        return True
      self.understand()

  def result(self, area, colorArea):
    self.speak(_DialogContent().content(5).replace('#', '%d' % area), 1)
    for index, i in enumerate(colorArea):
      if i != 0:
        msg = _DialogContent().content(7).replace('#', self.__color[index]).replace(
            '@', '%d' % i).replace('&', '%.2f' % (i / area * 100))
        self.speak(msg, 1)
