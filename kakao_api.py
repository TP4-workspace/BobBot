#-*- coding: utf-8 -*-

from kakao_keyboard import Keyboard
from operator import eq
import menu

class Message:

    baseKeyboard = {
        "type": "buttons",
        "buttons": Keyboard.buttons,
    }

    baseMessage = {
        "message": {
            "text": "",
        },
        "keyboard": baseKeyboard
    }


    def __init__(self):
        self.returnedMessage = None

    def homeKeyboard(self):
        self.returnedMessage = self.baseKeyboard
        self.returnedMessage["buttons"] = Keyboard.todayButtons
        return self.returnedMessage

    def updateMessage(self, message):
        self.returnedMessage["message"]["text"] = message

    def updateKeyboard(self, argKeyboard):
        keyboard = Message.baseKeyboard
        keyboard["buttons"] = argKeyboard
        self.returnedMessage["keyboard"] = keyboard

    def initMessage(self):
        self.returnedMessage = self.baseMessage

    def process(self, data=None):
        user_key = data["user_key"]
        request_type = data["type"]
        content = data["content"]
        self.initMessage()

        step1 = [u"아침", u"점심", u"저녁", u"다른 요일"]
        if content in step1:
            if eq(content.encode('utf-8'), '아침'):
                self.updateMessage(menu.get_today_a_menu(0))
            elif eq(content.encode('utf-8'), '점심'):
                self.updateMessage(menu.get_today_a_menu(1))
            elif eq(content.encode('utf-8'), '저녁'):
                self.updateMessage(menu.get_today_a_menu(2))
            elif eq(content.encode('utf-8'), '다른 요일'):
                self.updateMessage(u"요일을 선택하세요")
                self.updateKeyboard(Keyboard.wdayButtons)
            return self.returnedMessage

        step2 = [u"월요일",u"화요일",u"수요일",u"목요일",u"금요일",u"취소"]
        if content in step2:
            if eq(content.encode('utf-8'), '월요일'):
                self.updateMessage(menu.get_someday_all_menu(0))
            elif eq(content.encode('utf-8'), '화요일'):
                self.updateMessage(menu.get_someday_all_menu(1))
            elif eq(content.encode('utf-8'), '수요일'):
                self.updateMessage(menu.get_someday_all_menu(2))
            elif eq(content.encode('utf-8'), '목요일'):
                self.updateMessage(menu.get_someday_all_menu(3))
            elif eq(content.encode('utf-8'), '금요일'):
                self.updateMessage(menu.get_someday_all_menu(4))
            else:
                self.updateMessage("오늘의 메뉴는?")
                self.updateKeyboard(Keyboard.todayButtons)
            return self.returnedMessage

Message = Message()