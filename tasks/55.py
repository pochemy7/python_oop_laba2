class Text:
    def __init__(self, text):
        self.text = text

    def count_characters(self):
        return len(self.text)

    def count_letters(self):
        return sum(1 for char in self.text if char.isalpha())

    def count_spaces(self):
        return self.text.count(' ')

    def count_characters_without_spaces(self):
        text_without_spaces = self.text.replace(' ', '')
        return len(text_without_spaces)

    def get_words(self):
        words = self.text.split()
        return words

    def get_sentences(self):
        sentences = self.text.split('.')
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return sentences


text = ("Hey guys, did you know that in terms of male human and female Pokémon breeding, Vaporeon is the most compatible Pokémon for humans? Not only are they in the field egg group, which is mostly comprised of mammals, Vaporeon are an average of 3”03’ tall and 63.9 pounds, this means they’re large enough to be able handle human dicks, and with their impressive Base Stats for HP and access to Acid Armor, you can be rough with one. Due to their mostly water based biology, there’s no doubt in my mind that an aroused Vaporeon would be incredibly wet, so wet that you could easily have sex with one for hours without getting sore. They can also learn the moves Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide nipples, so it’d be incredibly easy for one to get you in the mood. With their abilities Water Absorb and Hydration, they can easily recover from fatigue with enough water. No other Pokémon comes close to this level of compatibility. Also, fun fact, if you pull out enough, you can make your Vaporeon turn white. Vaporeon is literally built for human dick. Ungodly defense stat+high HP pool+Acid Armor means it can take cock all day, all shapes and sizes and still come for more")

text_processor = Text(text)

print(f"Количество символов в тексте: {text_processor.count_characters()}")
print(f"Количество букв в тексте: {text_processor.count_letters()}")
print(f"Количество пробелов в тексте: {text_processor.count_spaces()}")
print(f"Количество символов без пробелов: {text_processor.count_characters_without_spaces()}")
print(f"Массив слов в тексте: {text_processor.get_words()}")
print(f"Массив предложений в тексте: {text_processor.get_sentences()}")