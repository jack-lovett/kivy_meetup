from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label

from model import Product


class ShoppingApp(App):
    def __init__(self):
        super().__init__()
        self.products = [Product("Cheese", 12.5), Product("Laptop", 912.95), Product("Plant", 4.75)]

    def build(self):
        """Build the Kivy app and add buttons dynamically."""
        self.title = "Shopping"
        self.root = Builder.load_file("dynamic_labels.kv")
        for product in self.products:
            button = Button(text=product, font_size=24)
            button.bind(on_press=self.buy)
            self.root.ids.button_box.add_widget(button)
        return self.root

    def buy(self, instance):
        price = instance.price

        self.total_price += price


    def handle_reset(self):
        self.total_price = 0


if __name__ == "__main__":
    ShoppingApp().run()
