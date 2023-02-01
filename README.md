# doc_summary_ai

Prototype of using GPT index to answer questions in technical documentation.

## Get Started

Create `.env` file and add OpenAI API key to it:

```sh
# .env
OPENAI_API_KEY=<sk-...>
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Run:

```sh
python main.py
```

## Add You Own Index

Right now the index just contains a couple of random documentation pages about [Atlas Functions](https://www.mongodb.com/docs/atlas/app-services/functions/).

You can find these pages in `gen_index.py` in the `urls` list.
If you want to change the pages indexed, you can just edit this list of links.

To regenerate the index, run:

```sh
python gen_index.py
```
