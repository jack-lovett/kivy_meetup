from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.button import Button

from model import Product

class ShoppingApp(App):
    total_price = NumericProperty(0)  # Make total_price an observable property

    def __init__(self):
        super().__init__()
        self.products = [Product("Cheese", 12.5), Product("Laptop", 912.95), Product("Plant", 4.75)]

    def build(self):
        """Build the Kivy app and add buttons dynamically."""
        self.title = "Shopping"
        self.root = Builder.load_file("view.kv")
        for product in self.products:
            button = Button(text=product.name, font_size=24)  # use product name as text
            button.price = product.price  # store product price in button
            button.bind(on_press=self.buy)
            self.root.ids.button_box.add_widget(button)
        return self.root

    def buy(self, instance):
        price = instance.price
        self.total_price += price  # total_price updates dynamically

    def handle_reset(self):
        self.total_price = 0  # Reset the total price to zero


if __name__ == "__main__":
    ShoppingApp().run()
