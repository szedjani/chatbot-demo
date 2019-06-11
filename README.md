This is a demo chatbot module. It tags short texts using the following tags:
1.	Lang: English
2.	Lang: German
3.	Company Structure: Ltd.
4.	Company Structure: plc
5.	Shareholder

The solution is unit-tested and the code style complies with PEP-8 standards.

# Requirements
* Python 3.6 (Tensorflow do not support 3.7 on Windows.)
* Tested only on Windows 10.

# Installation

The module can be installed using the following command:

`pip install git+https://github.com/szedjani/chatbot-demo.git`

# Usage

```python
import chatbot_demo
tagger = Tagger()
print(tagger.tag("Can I be shareholder of a limited company?"))
```

It would print `[1,3,5]`

# Development

First install the modules `Rasa` and `langdetect` (pip would install them automatically), then clone the project.

# Evaluation

The solution correctly tags all given test sentences (you can find them in `test.py`). However, further development would require more test data.