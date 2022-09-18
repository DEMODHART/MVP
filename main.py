# напиши тут свою програму
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *
from kivy.core.window import Window

Window.size = (1300, 500)

age = ""
name = 0
pulse_first = 0
pulse1 = 0
pulse2 = 0

class Screen_Button(Button):
    def __init__(self, screen_in, screen_to, direction, **kwargs):
        super().__init__(**kwargs)
        self.screen_in = screen_in
        self.screen_to = screen_to
        self.direction = direction

    def on_press(self):
        self.screen_in.manager.transition.direction = self.direction
        self.screen_in.manager.current = self.screen_to
class Screen_Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global name
        global age

        instruction = Label(text = txt_instruction)

        label_name = Label(text = "Введить им'я:", size_hint = (0.75, None), height = 68, pos_hint = {"center_x" : 0.5})
        name_input = TextInput(multiline = False, size_hint = (0.75, None), height = 68, pos_hint = {"center_x" : 0.5})
        name = name_input.text
        
        label_age = Label(text = "Введить вік:", size_hint = (0.75, None), height = 68, pos_hint = {"center_x" : 0.5})
        age_input = TextInput(multiline = False, size_hint = (0.75, None), height = 68, pos_hint = {"center_x" : 0.5})
        age = age_input.text
        
        layout_name = BoxLayout(padding = 20, spacing = 20)
        layout_name.add_widget(label_name)
        layout_name.add_widget(name_input)
        
        layout_age = BoxLayout(padding = 20, spacing = 20)
        layout_age.add_widget(label_age)
        layout_age.add_widget(age_input)
        
        button = Screen_Button(self, "Screen Check", "up", text = "Почати")

        main_layout = BoxLayout(orientation = "vertical", padding = 20, spacing = 20)
        main_layout.add_widget(instruction)
        main_layout.add_widget(layout_name)
        main_layout.add_widget(layout_age)
        main_layout.add_widget(button)
        
        self.add_widget(main_layout)
        
class Check_Screen(Screen):  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global pulse_first

        instruction = Label(text = txt_test1)
        
        pulse_label = Label(text = "Ваші результати:", size_hint = (0.75, None), height = 68, pos_hint = {"center_x" : 0.5})
        pulse_input = TextInput(multiline = False, size_hint = (0.75, None), height = 68, pos_hint = {"center_x" : 0.5})
        pulse_layout = BoxLayout(padding = 20, spacing = 20)
        pulse_layout.add_widget(pulse_label)
        pulse_layout.add_widget(pulse_input)
        pulse_first = pulse_input.text
        
        button = Screen_Button(self, "Screen Instruction", "up", text = "Продовжити")
        
        main_layout = BoxLayout(orientation = "vertical", padding = 20, spacing = 20)
        main_layout.add_widget(instruction)
        main_layout.add_widget(pulse_layout)
        main_layout.add_widget(button)

        self.add_widget(main_layout)

class Instruction_Screen(Screen):  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instruction = Label(text = txt_sits)
        
        button = Screen_Button(self, "Screen Pulse", "up", text = "Продовжити")
        
        main_layout = BoxLayout(orientation = "vertical", padding = 20, spacing = 20)
        main_layout.add_widget(instruction)
        main_layout.add_widget(button)

        self.add_widget(main_layout)

class Pulse_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global pulse1
        global pulse1

        instruction = Label(text = txt_test3)

        label_pulse1 = Label(text = "Результат:")
        pulse1_input = TextInput(multiline = False, size_hint = (0.75, None), height = 68, pos_hint = {"center_x" : 0.5})
        pulse1 = pulse1_input.text
        
        label_pulse2 = Label(text = "результат після відпочинку:")
        pulse2_input = TextInput(multiline = False, size_hint = (0.75, None), height = 68, pos_hint = {"center_x" : 0.5})
        pulse2 = pulse2_input.text
        
        layout_pulse1 = BoxLayout(padding = 20, spacing = 20)
        layout_pulse1.add_widget(label_pulse1)
        layout_pulse1.add_widget(pulse1_input)
        
        layout_pulse2 = BoxLayout(padding = 20, spacing = 20)
        layout_pulse2.add_widget(label_pulse2)
        layout_pulse2.add_widget(pulse2_input)
        
        button = Screen_Button(self, "Screen Result", "up", text = "Завершити")

        main_layout = BoxLayout(orientation = "vertical", padding = 20, spacing = 20)
        main_layout.add_widget(instruction)
        main_layout.add_widget(layout_pulse1)
        main_layout.add_widget(layout_pulse2)
        main_layout.add_widget(button)
        
        self.add_widget(main_layout)

class Result_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global name
        global age
        global pulse_first
        global pulse1
        global pulse2
        
        print(name, age, pulse_first, pulse1, pulse2)
        '''print(pulse_first)
        print(pulse1)
        print(pulse2)
        print(age)'''
        
        text1 = ("Ваш индекс Руф'є:", ruffier(hertbeats_count(pulse_first, pulse1, pulse1)))
        text2 = ("Працесдатнисть сердця:", main_ruffier(pulse_first, pulse1, pulse2, age))

        name_label = Label(text = name, size_hint = (0.75, None), height = 208, pos_hint = {"center_x" : 0.5})
        rufier_result = Label(text = text1, size_hint = (0.75, None), height = 208, pos_hint = {"center_x" : 0.5})
        heart_result = Label(text = text2, size_hint = (0.75, None), height = 208, pos_hint = {"center_x" : 0.5})

        main_layout = BoxLayout(orientation = "vertical")
        main_layout.add_widget(name_label)
        main_layout.add_widget(rufier_result)
        main_layout.add_widget(heart_result)

        self.add_widget(main_layout)

class MyApp(App):
    def build(self):
        sc = ScreenManager()
        sc.add_widget(Screen_Main(name = "Main Screen"))
        sc.add_widget(Check_Screen(name = "Screen Check"))
        sc.add_widget(Instruction_Screen(name = "Screen Instruction"))
        sc.add_widget(Pulse_Screen(name = "Screen Pulse"))
        sc.add_widget(Result_Screen(name = "Screen Result"))

        return sc
app = MyApp()
app.run()
