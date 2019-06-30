import unittest
from src import homer

class TestWords(unittest.TestCase):

    def test_nouns(self):
        nouns = ['London', 'Chair', 'Computer', 'mobile']
        for noun in nouns:
            word = homer.Word(noun)
            self.assertTrue(word.is_noun)


    def test_adjective(self):
        adjectives = ['big', 'small', 'adorable']
        for adjective in adjectives:
            word = homer.Word(adjective)
            self.assertTrue(word.is_adjective, word)

    def test_compsulsive_hedgers(self):
        compulsive_hedgers = ['apparently', 'almost', 'fairly', 'nearly', 'partially', 'predominantly', 'presumably',
                              'rather', 'relative', 'seemingly']
        for compulsive_hedger in compulsive_hedgers:
            word = homer.Word(compulsive_hedger)
            self.assertTrue(word.is_compulsive_hedger)

    def test_intesifiers(self):
        intensifiers = ['very', 'highly', 'extremely']
        for intensifier in intensifiers:
            word = homer.Word(intensifier)
            self.assertTrue(word.is_intensifier)

    def test_meta_concepts(self):
        meta_words = ["issues", 'contexts', 'frameworks', 'perspectives']
        for meta_w in meta_words:
            word = homer.Word(meta_w)
            self.assertTrue(word.is_meta_concept)

    def test_abstract_nouns(self):
        abs_nouns = ["approach", 'assumption', 'concept', 'condition', 'context', 'framework', 'issue', 'model',
                     'process', 'range', 'role', 'strategy', 'tendency', 'variable']
        for abs_noun in abs_nouns:
            word = homer.Word(abs_noun)
            self.assertTrue(word.is_abstract_noun)

    def test_zombie_nouns(self):
        zombies = ['ance', 'ment', 'ments', 'ation', 'ations', 'ing', 'ty']
        zombies = ['thinking', 'eating']
        for zombie in zombies:
            word = homer.Word(zombie)
            self.assertTrue(word.is_zombie_noun, zombie)

    def test_ands(self):
        ands = ['and', 'And']
        for _and in ands:
            word = homer.Word(_and)
            self.assertTrue(word.is_and)

if __name__ == "__main__":
    unittest.main()
