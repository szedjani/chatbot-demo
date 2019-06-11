import unittest

from tagger import Tagger


class TestTaqgger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tagger = Tagger(["en", "de"])

    def test_english_detection(self):
        self.assertEqual(TestTaqgger.tagger.tag("Hello"), {1})

    def test_german_detection(self):
        self.assertEqual(TestTaqgger.tagger.tag("Hallo"), {2})

    def test_sentences(self):

        sentences = [
            {
                "text": "Can I be shareholder of a limited company?",
                "tags": {1,3,5}
            },
            {
                "text": "I want to become shareholder of a limited company.",
                "tags": {1,3,5}
            },
            {
                "text": "Can I be shareholder of a limited public corporate?",
                "tags": {1,4,5}
            },
            {
                "text": "Can my company be shareholder of a limited company?",
                "tags": {1,3,5}
            },
            {
                "text": "Can my company be shareholder of a public corporate?",
                "tags": {1,4,5}
            },
            {
                "text": "Kann ich Gesellschafter einer GmbH sein?",
                "tags": {2,3,5}
            },
            {
                "text": "Wer kann Gesellschafter einer AG sein?",
                "tags": {2,4,5}
            },
            {
                "text": "Kann ich mit meiner GmbH Mehrheitseigner einer AG sein?",
                "tags": {2,3,4,5}
            },
        ]

        for sentence in sentences:
            self.assertEqual(self.tagger.tag(sentence["text"]), sentence["tags"])

if __name__ == '__main__':
    unittest.main()