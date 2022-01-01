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
      '覆蓋面積為 #'
  ]
  WELCOME = __COMPUTER[0]
  UNDERSTAND = __COMPUTER[1]

  def content(self, index):
    return self.__COMPUTER[index]


class Dialog:
  def __init__(self) -> None:
    self.record = []
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

  def speak(self, text='', current=1):
    st = text_to_speech()
    if current == 1:
      ans = 'Computer> ' + text
      self.__speak(ans)
      st.speak(text)
    elif current == 0:
      ans = '%s %s <User' % (' '*(60 - self.width(text)), text)
      self.__speak(ans)
    self.record.append(ans)
    self.show()

  def listen(self):
    st = speech_to_text()
    while True:
      text = st.listen()
      self.speak(text, 0)
      if '沒' in text:
        return 'no'
      elif '有' in text:
        return 'yes'
      elif self.__isdigit(text):
        return self.__toInt(text)
      else:
        self.understand()

  def welcome(self):
    self.speak(_DialogContent().WELCOME, 1)

  def understand(self):
    self.speak(_DialogContent().UNDERSTAND, 1)

  def query(self, cnt: int, xy: int, lr: int):
    if lr == 0:
      self.speak(_DialogContent().content(2).replace(
          '#', '%d' % cnt).replace('%', "xy"[xy]), 1)
    elif lr == 1:
      self.speak(_DialogContent().content(3).replace(
          '#', '%d' % cnt).replace('%', "xy"[xy]), 1)
    while True:
      result = self.listen()
      try:
        if int(result) :
          return result
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

  def result(self, area):
    self.speak(_DialogContent().content(5).replace('#', '%d' % area), 1)
