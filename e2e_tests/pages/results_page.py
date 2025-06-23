# pages/results_page.py

from .base_page import BasePage

class ResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.card_selector = '[itemprop="itemListElement"]'
        self.price_selector = '[data-testid="price"]'
        self.rating_selector = '[aria-label*="Rating"]'
        self.title_selector = '._9xiloll'

    def extract_result_data(self):
        cards = self.page.locator(self.card_selector)
        results = []
        count = cards.count()
        for i in range(count):
            card = cards.nth(i)
            try:
                title = card.locator(self.title_selector).inner_text()
                price_text = card.locator(self.price_selector).inner_text()
                rating_text = card.locator(self.rating_selector).inner_text()

                price = int(''.join(filter(str.isdigit, price_text)))
                rating = float(rating_text.split()[0])
                results.append({
                    "title": title,
                    "price": price,
                    "rating": rating,
                })
            except:
                continue
        return results

    def get_cheapest_high_rated(self, results):
        high_rated = [r for r in results if r['rating'] >= 4.5]
        if not high_rated:
            return None
        return min(high_rated, key=lambda x: x["price"])
