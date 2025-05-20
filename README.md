# learn-chat-ai

## Summary

A CLI tool for language learning chat powered by OpenAI.

Default settings support Japanese speakers learning English, but other language pairs are configurable.

## Features

- Interactive conversation practice via OpenAI
- Simple CLI interface
- Context-aware prompt history
- Easy installation with pipx

## Prerequisites

- Python 3.8 or later
- pipx installed ([installation guide](https://pipxproject.github.io/pipx/installation/))
- An OpenAI API key (set via the `OPENAI_API_KEY` environment variable)

## Language customization

The app is language-adaptive via two constants in the code:

- `LEARNER_LANGUAGE`: defines the target language to be practiced.
- `FEEDBACK_LANGUAGE`: defines the language used for feedback explanations.

You can modify these constants in the source code to switch between different language combinations.

Example: For French learners getting feedback in English
```python
LEARNER_LANGUAGE = "French"
FEEDBACK_LANGUAGE = "English"
```

## Installation

```bash
pipx install .
```

## How to use

```bash
learn-chat-ai
```

## Example

```terminal
> learn-chat-ai
--------
AI: What's your favorite food?
You: I like sushi.
--------
Feedback: 良い表現ですが "I love sushi" も自然です。
- I enjoy sushi.
- Sushi is my favorite.
--------
AI: What do you like about sushi?
You:
```

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

## Author

- [Kazuaki Oshiba](https://github.com/kazusanto)
