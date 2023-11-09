# ！/usr/bin/env/python
"""
抽象工厂模式是一种创建型设计模式，它提供一个抽象类和抽象工厂类，用于创建一系列相关或相互依赖的对象，
而不需要指定它们具体的类

抽象工厂的主要目的是通过一组具有相似主题的工厂，使得客户端能以一种与产品类实现无关的方式创建一组相关的产品，
抽象工厂模式提供了一个抽象工厂类和一组抽象产品类，具体工厂和具体产品类由他们的子类实现。
"""

from abc import ABC, abstractclassmethod

# 定义抽象产品类，抽象工厂类
class Button(ABC):
    @abstractclassmethod
    def paint(self):
        pass


class TextButton(ABC):
    @abstractclassmethod
    def paint(self):
        pass


class CheckBox(ABC):
    @abstractclassmethod
    def paint(self):
        pass


class ButtonFactory(ABC):
    @abstractclassmethod
    def create_button(self):
        pass

    @abstractclassmethod
    def create_text_button(self):
        pass

    @abstractclassmethod
    def create_check_box(self):
        pass

# 定义具体工厂子类以及具体产品类
class WindowsButton(Button):
    def paint(self):
        print("Painting a Windows style button")


class WinodwsTextButton(TextButton):
    def paint(self):
        print("Painting a Windows WinodwsTextButton")


class WindowsCheckBox(CheckBox):
    def paint(self):
        print("Painting a Windows WindowsCheckBox")


class MacButton(Button):
    def paint(self):
        print("Painting a Mac style button")


class MacTextButton(TextButton):
    def paint(self):
        print("Painting a Mac MacTextButton")


class MacCheckBox(CheckBox):
    def paint(self):
        print("Painting a Mac MacCheckBox")


class WindowsFactory(ButtonFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_text_button(self) -> WinodwsTextButton:
        return WinodwsTextButton()

    def create_check_box(self) -> WindowsCheckBox:
        return WindowsCheckBox()


class MacFactory(ButtonFactory):
    def create_button(self) -> MacButton:
        return MacButton()

    def create_text_button(self) -> WinodwsTextButton:
        return WinodwsTextButton()

    def create_check_box(self) -> WindowsCheckBox:
        return WindowsCheckBox()


def create_gui(factory):
    button = factory.create_button()
    textbox = factory.create_text_button()
    chcekbox = factory.create_check_box()
    button.paint()
    textbox.paint()
    chcekbox.paint()
    return button, textbox, chcekbox


button, textbox, chcekbox = create_gui(WindowsFactory())
print(button, textbox, chcekbox)
