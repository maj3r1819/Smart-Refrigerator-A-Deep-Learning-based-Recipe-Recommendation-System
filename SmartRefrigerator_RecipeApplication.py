from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDIconButton, MDRaisedButton, MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.list import MDList, OneLineListItem, OneLineAvatarListItem,ThreeLineAvatarListItem, TwoLineAvatarListItem, TwoLineListItem, ImageLeftWidget, IconLeftWidget
from kivy.core.window import Window
from itertools import zip_longest
import re

Window.size = (307.894, 650)
screen_helper = """
ScreenManager:
    MenuScreen:
    DietRecipesScreen:
    IngredientsScreen:
    RecipesScreen:
    HealthyRecipesScreen:
<MenuScreen>:
    name: 'menu'
    BoxLayout:
        canvas.before:
            Rectangle:
                source: './imgs/screenbg/phonescreen1.jpg'
                size: self.width + 20, self.height + 20
                pos: self.x - 10, self.y - 10
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Smart Menu'
            md_bg_color: 20/255.0, 20/255.0, 20/255.0, 1
            specific_text_color: 255/255.0, 255/255.0, 255/255.0, 1
            elevation:5
        FloatLayout:
            MDCard:
                orientation: "vertical"
                padding: "16dp"
                size_hint: None, None
                size: "200dp", "150dp"
                elevation: 12
                md_bg_color: 246/255.0, 249/255.0, 253/255.0, 1
                pos_hint: {"center_x": 0.5, "center_y": 0.75}
                canvas:
                    Rectangle:
                        source: './imgs/screenbg/cardimg.jpg'
                        size: self.width + 20, self.height + 20
                        pos: self.x - 10, self.y - 10
                MDLabel:
                    text: ""
                    theme_text_color: 'Custom'
                    text_color: 20/255.0, 20/255.0, 20/255.0, 1
                    halign: 'center'
            MDRaisedButton:
                text: 'Ingredients Detected'
                text_color: 255/255.0, 255/255.0, 255/255.0, 1
                #md_bg_color: 107/255.0, 164/255.0, 49/255.0, 1
                md_bg_color: 33/255.0, 33/255.0, 33/255.0, 1
                pos_hint: {'center_x':0.5,'center_y':0.5}
                on_press:
                    root.manager.current = 'ingredients'
                    root.manager.transition.direction = "left"
            MDRaisedButton:
                text: 'Recipe List'
                text_color: 255/255.0, 255/255.0, 255/255.0, 1
                #md_bg_color: 107/255.0, 164/255.0, 49/255.0, 1
                md_bg_color: 33/255.0, 33/255.0, 33/255.0, 1
                pos_hint: {'center_x':0.5,'center_y':0.4}
                on_press:
                    root.manager.current = 'recipes'
                    root.manager.transition.direction = "left"
            MDRaisedButton:
                text: 'Diet Recipes List'
                text_color: 255/255.0, 255/255.0, 255/255.0, 1
                #md_bg_color: 107/255.0, 164/255.0, 49/255.0, 1
                md_bg_color: 33/255.0, 33/255.0, 33/255.0, 1
                pos_hint: {'center_x':0.5,'center_y':0.3}
                on_press:
                    root.manager.current = "healthyrecipes"
                    root.manager.transition.direction = "left"            
            #MDRaisedButton:
                #text: 'Find Recipes'
                #text_color: 255/255.0, 255/255.0, 255/255.0, 1
                #md_bg_color: 107/255.0, 164/255.0, 49/255.0, 1
                #pos_hint: {'center_x':0.5,'center_y':0.2}
                #on_press:
                    #root.manager.current = "dietrecipes"
                    #root.manager.transition.direction = "left"

<IngredientsScreen>:
    name: 'ingredients'
    canvas:
        Rectangle:
            source: './imgs/screenbg/bgphonescreen2.jpg'
            size: self.size
            pos: self.pos
    MDCard:
        orientation: "vertical"
        padding: "16dp"
        size_hint: None, None
        size: "350dp", "45dp"
        elevation: 10
        md_bg_color: 20/255.0, 20/255.0, 20/255.0, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.96}

        MDLabel:
            text: "Ingredients Detected"
            theme_text_color: 'Custom'
            text_color: 255/255.0, 255/255.0, 255/255.0, 1
            halign: 'center'
    ScrollView:
        pos_hint: {'center_x': 0.5, 'center_y': 0.44}
        MDList:
            id:container
    #MDRaisedButton:
        #text: 'Show Recipes'
        #text_color: 255/255.0, 255/255.0, 255/255.0, 1
        #md_bg_color: 107/255.0, 164/255.0, 49/255.0, 1
        #pos_hint: {'center_x':0.5,'center_y':0.075}
        #elevation: 8
        #on_press:
            #root.manager.current = 'recipes'
            #root.manager.transition.direction = "left"
    MDIconButton:
        icon: 'chevron-left'
        pos_hint: {'center_x':0.15,'center_y':0.035}
        on_press:
            root.manager.current = "menu"
            root.manager.transition.direction = "right"

<RecipesScreen>:
    name: 'recipes'
    canvas:
        Rectangle:
            source: './imgs/screenbg/bgphonescreen2.jpg'
            size: self.size
            pos: self.pos
    ScrollView:
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDList:
            id:recipelist
    MDIconButton:
        icon: 'chevron-left'
        pos_hint: {'center_x':0.15,'center_y':0.035}
        on_press:
            root.manager.current = "menu"
            root.manager.transition.direction = "right"

<HealthyRecipesScreen>:
    name: 'healthyrecipes'
    canvas:
        Rectangle:
            source: './imgs/screenbg/bgphonescreen2.jpg'
            size: self.size
            pos: self.pos
    ScrollView:
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDList:
            id:healthyrecipelist
    MDIconButton:
        icon: 'chevron-left'
        pos_hint: {'center_x':0.15,'center_y':0.035}
        on_press:
            root.manager.current = "menu"
            root.manager.transition.direction = "right"

<DietRecipesScreen>:
    name: 'dietrecipes'
    canvas:
        Rectangle:
            source: './imgs/screenbg/bgphonescreen2.jpg'
            size: self.size
            pos: self.pos
    MDLabel:
        text: 'Type of Diet'
        halign: 'left'
        pos_hint: {'center_x':0.59,'center_y':0.95}
    MDTextField:
        hint_text: 'non-veg is default'
        color_mode: 'custom'
        line_color_focus: 107/255.0, 164/255.0, 49/255.0, 1
        helper_text: "ex: vegetarian/vegan."
        helper_text_mode: "on_focus"
        pos_hint: {'center_x':0.5,'center_y':0.88}
        size_hint_x: None
        width: 250
    MDLabel:
        text: 'Cuisine'
        halign: 'left'
        pos_hint: {'center_x':0.59,'center_y':0.8}
    MDTextField:
        hint_text: 'ex: italian/indian/japanese/korean'
        color_mode: 'custom'
        line_color_focus: 107/255.0, 164/255.0, 49/255.0, 1
        helper_text: "or chinese/french/mexican/spanish/american."
        helper_text_mode: "on_focus"
        pos_hint: {'center_x':0.5,'center_y':0.73}
        size_hint_x: None
        width: 250
    MDLabel:
        text: 'Type of Dish'
        halign: 'left'
        pos_hint: {'center_x':0.59,'center_y':0.65}
    MDTextField:
        hint_text: 'ex: main course/dessert/salad'
        color_mode: 'custom'
        line_color_focus: 107/255.0, 164/255.0, 49/255.0, 1
        helper_text: "or bread/breakfast/soup/beverage/appetizer."
        helper_text_mode: "on_focus"
        pos_hint: {'center_x':0.5,'center_y':0.58}
        size_hint_x: None
        width: 250
    MDLabel:
        text: 'Intolerances'
        halign: 'left'
        pos_hint: {'center_x':0.59,'center_y':0.5}
    MDTextField:
        hint_text: 'ex: dairy/egg/gluten/peanut/soy'
        color_mode: 'custom'
        line_color_focus: 107/255.0, 164/255.0, 49/255.0, 1
        helper_text: "or sesame/seafood/shellfish/sulfite/wheat."
        helper_text_mode: "on_focus"
        pos_hint: {'center_x':0.5,'center_y':0.43}
        size_hint_x: None
        width: 250
    MDRaisedButton:
        text: 'Show Recipes'
        text_color: 255/255.0, 255/255.0, 255/255.0, 1
        md_bg_color: 107/255.0, 164/255.0, 49/255.0, 1
        pos_hint: {'center_x':0.5,'center_y':0.22}
        elevation: 8
        on_press:
            root.manager.current = 'recipes'
            root.manager.transition.direction = "left"
    MDIconButton:
        icon: 'chevron-left'
        pos_hint: {'center_x':0.15,'center_y':0.035}
        on_press:
            root.manager.current = "menu"
            root.manager.transition.direction = "right"
"""

class IngredientsScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class DietRecipesScreen(Screen):
    pass
class HealthyRecipesScreen(Screen):
    pass
class RecipesScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(IngredientsScreen(name='ingredients'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(DietRecipesScreen(name='dietrecipes'))
sm.add_widget(HealthyRecipesScreen(name='healthyrecipes'))
sm.add_widget(RecipesScreen(name='recipes'))

class SmartRefrigeratorApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.primary_hue = "800"
        screen = Screen()
        self.help_str = Builder.load_string(screen_helper)
        search = MDRectangleFlatButton(text='Save Options',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       md_bg_color=(107/255.0, 164/255.0, 49/255.0, 1))

        self.help_str.get_screen('dietrecipes').add_widget(search)
        screen.add_widget(self.help_str)
        return screen

    def on_start(self):
        #fh = open("ingredients.txt")
        #ingredients = []
        #for line in fh:
            #line = line.rstrip()
            #line = line.capitalize()
            #if line == 'Tomato':
                #line = 'Tomatoes'
            #ingredients.append(str(line))
        ingredients = ['Eggs','Apple', 'Cauliflower', 'Tomatoes','Milk','Banana','Eggplant']
        ingredients = sorted(ingredients)
        MainRecipelist = {}
        HealthyRecipelist = {}
        expiry = []
        for i in ingredients:
            if i == 'Apple': expiry.append('expiry: 3-5 days')
            elif i == 'Cauliflower': expiry.append('expiry: 3 days')
            elif i == 'Milk': expiry.append('expiry: 1 day')
            elif i == 'Eggs': expiry.append('expiry: 1 week')
            elif i == 'Banana': expiry.append('expiry: 3-5 days')
            elif i == 'Eggplant': expiry.append('expiry: 3 days')
            elif i == 'Tomatoes': expiry.append('expiry: 1 week')
        ingre = dict(zip(ingredients, expiry))
        #====================================Main-recipelist=======================================
        Allrecipes = list()
        Alltime = []
        fhandle = open('Recipes-Dataset.txt')
        for line in fhandle:
            if line[0:6] == "Recipe":
                y = re.findall(': (.+) R', line)
                Allrecipes = Allrecipes + y
            elif line[0:4] == "Time":
                z = re.findall(': (.+)', line)
                z = 'cooking time: ' + z[0]
                Alltime.append(z)
        Allrecipesdict = {}
        Allrecipesdict = dict(zip(Allrecipes, Alltime))
        from itertools import zip_longest
        chunks = [Allrecipesdict.items()] * 7
        g = (dict(filter(None, v)) for v in zip_longest(*chunks))
        g = list(g)
        for i in ingredients:
            if i == "Apple":
                for d in (g[0:8]): MainRecipelist.update(d)
            elif i == "Cauliflower":
                for d in (g[8:16]): MainRecipelist.update(d)
            elif i == "Banana":
                for d in (g[32:40]): MainRecipelist.update(d)
            elif i == "Eggs":
                for d in (g[16:24]): MainRecipelist.update(d)
            elif i == "Eggplant":
                for d in (g[40:48]): MainRecipelist.update(d)
            elif i == "Tomatoes":
                for d in (g[48:56]): MainRecipelist.update(d)
            elif i == "Milk":
                for d in (g[24:32]): MainRecipelist.update(d)
        # ====================================Main-recipelist=======================================
        # ====================================Healthy-recipelist=======================================
        Allrecipes2 = list()
        Alltime2 = []
        fhandle2 = open('Healthy-Recipes-Dataset.txt')
        for line in fhandle2:
            if line[0:6] == "Recipe":
                y2 = re.findall(': (.+) R', line)
                Allrecipes2 = Allrecipes2 + y2
            elif line[0:4] == "Time":
                z2 = re.findall(': (.+)', line)
                z2 = 'cooking time: ' + z2[0]
                Alltime2.append(z2)
        Allrecipesdict2 = {}
        Allrecipesdict2 = dict(zip(Allrecipes2, Alltime2))
        from itertools import zip_longest
        chunks2 = [Allrecipesdict2.items()] * 7
        g2 = (dict(filter(None, v2)) for v2 in zip_longest(*chunks2))
        g2 = list(g2)
        for i in ingredients:
            if i == "Apple":
                for d2 in (g2[0:8]): HealthyRecipelist.update(d2)
            elif i == "Cauliflower":
                for d2 in (g2[8:16]): HealthyRecipelist.update(d2)
            elif i == "Banana":
                 for d2 in (g2[32:40]): HealthyRecipelist.update(d2)
            elif i == "Eggs":
                for d2 in (g2[16:24]): HealthyRecipelist.update(d2)
            elif i == "Eggplant":
                for d2 in (g2[40:48]): HealthyRecipelist.update(d2)
            elif i == "Tomatoes":
                for d2 in (g2[48:56]): HealthyRecipelist.update(d2)
            elif i == "Milk":
                for d2 in (g2[24:32]): HealthyRecipelist.update(d2)
        # ====================================Healthy-recipelist=======================================
        for k, v in ingre.items():
            image = ImageLeftWidget(source= './imgs/ingredients/'+ k +'.png')
            inl = TwoLineAvatarListItem(text = f"{k}",
                                        secondary_text = f"{v}")
            inl.add_widget(image)
            self.help_str.get_screen('ingredients').ids.container.add_widget(inl)

        for m, l in MainRecipelist.items():
            mrimage = ImageLeftWidget(source='./imgs/recipephotos/'+ m + ".jpg")
            recipelist = TwoLineAvatarListItem(text = f"{m}",secondary_text = f"{l}")
            recipelist.add_widget(mrimage)
            self.help_str.get_screen('recipes').ids.recipelist.add_widget(recipelist)

        for p, q in HealthyRecipelist.items():
            hrimage = ImageLeftWidget(source='./imgs/healthyrecipephotos/'+ p + ".jpg")
            healthyrecipelist = TwoLineAvatarListItem(text = f"{p}",secondary_text = f"{q}")
            healthyrecipelist.add_widget(hrimage)
            self.help_str.get_screen('healthyrecipes').ids.healthyrecipelist.add_widget(healthyrecipelist)

SmartRefrigeratorApp().run()
