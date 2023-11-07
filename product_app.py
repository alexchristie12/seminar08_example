"""
Product App
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

from product import Products


class ProductApp(App):
    """Main program - Product display app."""
    status_text = StringProperty()
    total_cost = 0
    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        self.products = [Products("Cheese", 12.50),
                         Products("Laptop", 12.95),
                         Products("Plant", 4.75)]

    def build(self):
        """Construct Kivy GUI"""
        self.title = "CP1404 Meetup"
        self.root = Builder.load_file('product.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from list of objects and add them to the GUI."""
        self.status_text = "Total Price: "
        for product in self.products:
            temp_button = Button(text=str(product))
            temp_button.bind(on_release=self.press_entry)
            # Store a reference to the product object in the button object
            temp_button.product = product
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing guitar buttons."""
        # Each button was given its own ".guitar" object reference, so we can get it directly
        product = instance.product
        total_cost += product.price
        # Update button text and label
        instance.text = str(product)
        self.status_text = f"Total Cost: {total_cost}"