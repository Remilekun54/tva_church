from django.test import TestCase
from .models import Category, Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Books", slug="books")
        self.product = Product.objects.create(
            category=self.category,
            title="Divine Assignment",
            sellar_price=5000.00,
            amazon_price=25.00,
            sellar_link="https://sellar.co/book",
            amazon_link="https://amazon.com/book"
        )

    def test_product_fields(self):
        self.assertEqual(self.product.sellar_price, 5000.00)
        self.assertEqual(self.product.amazon_price, 25.00)
        self.assertEqual(self.product.sellar_link, "https://sellar.co/book")
        self.assertEqual(self.product.amazon_link, "https://amazon.com/book")
