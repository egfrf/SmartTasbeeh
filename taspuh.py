from kivy.config import Config
Config.set('graphics', 'width', '380')
Config.set('graphics', 'height', '600')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
import arabic_reshaper
from kivymd.uix.selectioncontrol import MDSwitch
from bidi.algorithm import get_display
from kivymd.icon_definitions import md_icons


Builder.load_string("""
<Main>:
    Screen:
         
        MDIconButton:
            icon: "white-balance-sunny"
            on_release: app.moon()
            pos_hint: {"x": 0.2,"y": 0.1}
        MDIconButton:
            icon: "weather-night"
            on_release: app.sun()
            pos_hint: {"x": 0.1,"y": 0.1}
   
         

        MDFloatLayout:
            pos_hint: {"y": -0.1}
            orientation: "horizontal"
            Image:
                id: image
                source: "suph.png"
                size_hint: None, None
                size: 303, 300
                pos_hint: {"x": 0.1,"y":0.3}
          
              
     
            MDRaisedButton:
                id: but_text
                text: "%d" %root.scare
                pos_hint: {"center_x": 0.5, "center_y": 0.66}
                size_hint: 0.44, 0.1
                elevation: 5
                md_bg_color: "#a0b773"
                font_size: 30
              
           
            MDIconButton:
                icon: "dots-circle"
                pos_hint: {"center_x": 0.5, "center_y": 0.43}
                md_bg_color: "#c28904"
                size_hint: 0.21, 0.13
                on_release: root.myscar()
                
            MDIconButton:
                icon: "restore"
                pos_hint: {"center_x": 0.66, "center_y": 0.52}
                md_bg_color: "#a24c42"
                icon_size: 17
                on_release: root.cleare()
    BoxLayout:
        orientation: "vertical"
        MDLabel:
            id: label
            text: root.arabic_text("اللهم صل على محمد وال محمد")
            pos_hint: {"x": 0.4, "y": 0.6}
            size_hint: 0.2, 0.2
            font_name: "arial"
            font_size: 30
            pos_hint: {"center_x": 0.6}
            size_hint_x: 1
            multiline: False
            
      
            

   
            
        
   


        MDSlider:
            id: slider
            min: 0
            max: 30
            value: 0
            elevation: 0
            size_hint: 0.5, 0.1
            pos_hint: {"x": 0.24}
            thumb_color: (0,1,1,1)
            disabled: True
        
        BoxLayout:
              
                 


""")
class Main(Screen):
    def arabic_text(self,text):
        reshp_text= arabic_reshaper.reshape(text)
        bidi_text= get_display(reshp_text)  
        
        return bidi_text
       

            


    scare=NumericProperty(0)
    def myscar(self):
        self.scare+=1
        self.ids.slider.value+=1
        if self.scare == 33:
            self.ids.label.text= get_display(arabic_reshaper.reshape("سبحان الله"))
            self.ids.label.multiline=False       
            self.ids.slider.value=0
            self.ids.label.pos_hint={'x':0.36}
            

            
        elif self.scare == 66:
            self.ids.label.text= get_display(arabic_reshaper.reshape("الله اكبر"))
            self.ids.label.multiline=False  
            self.ids.slider.value=0
            self.ids.label.pos_hint={'x':0.36}
            
            
        elif self.scare == 99:
            self.ids.label.text= get_display(arabic_reshaper.reshape("الحمد الله"))
            self.ids.label.multiline=False  
            self.ids.slider.value=0
            self.ids.label.pos_hint={'x':0.36}
           
            self.cleare()
            # غير مكمل عندمل يوصل قيمه الي 99 يرجه كلشي الي مكانها
            

    def cleare(self):
        self.scare=0
        self.ids.slider.value=0
        self.ids.label.multiline=False  
        self.ids.label.pos_hint={'x':0.1}
        self.ids.label.text= get_display(arabic_reshaper.reshape("اللهم صل على محمد وال محمد"))
        








class Name(MDApp):
    def build(self):
        self.title="App ali"
        scr=Screen()
        scr.add_widget(Main(name="Main"))
        return scr
    def moon(self):
        self.theme_cls.theme_style="Light"
        
    def sun(self):
        self.theme_cls.theme_style="Dark"
Name().run()