from gpt_index import GPTSimpleVectorIndex
from gpt_index.readers import SimpleWebPageReader
from dotenv import load_dotenv

load_dotenv()
urls = [
  'https://www.mongodb.com/docs/atlas/app-services/functions/javascript-support/',
  'https://www.mongodb.com/docs/atlas/app-services/functions/',
  'https://www.mongodb.com/docs/atlas/app-services/functions/mongodb/',
  'https://www.mongodb.com/docs/atlas/app-services/functions/mongodb/read/',
  'https://www.mongodb.com/docs/atlas/app-services/functions/mongodb/write/',
  'https://www.mongodb.com/docs/atlas/app-services/functions/mongodb/aggregate/',
  ]

reader = SimpleWebPageReader(html_to_text=True)
docs = reader.load_data(urls)

index = GPTSimpleVectorIndex(docs)

index.save_to_disk('index.json')
