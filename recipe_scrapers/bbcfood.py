from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class BBCFood(AbstractScraper):

    @classmethod
    def host(self, domain='com'):
        return 'bbc.{}'.format(domain)

    def title(self):
        return normalize_string(self.soup.find('h1').get_text())

    def total_time(self):
        return sum([
            get_minutes(self.soup.find(
                'p',
                {'class': 'recipe-metadata__prep-time'})
            ),

            get_minutes(self.soup.find(
                'p',
                {'class': 'recipe-metadata__cook-time'})
            )
        ])

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "recipe-ingredients__list-item"}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'p',
            {'class': 'recipe-method__list-item-text'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
