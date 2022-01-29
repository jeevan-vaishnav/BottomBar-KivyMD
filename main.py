from kivymd.app import MDApp
from kivy.lang import Builder


class BottomBar(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')

    def presser(self):
        self.root.ids.my_label.text = f"You Pressed it "

#  ['Red', 'Pink', 'Purple',
#  'DeepPurple', 'Indigo', 'Blue', 'LightBlue',
#  'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime',
#   'Yellow', 'Amber', 'Orange', 'DeepOrange',
#    'Brown', 'Gray', 'BlueGray']


if __name__ == "__main__":
    BottomBar().run()
