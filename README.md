# RagItDown — AI RAG Chatbot

Chatbot con interfaccia web che risponde a domande basandosi sui documenti forniti, usando Retrieval-Augmented Generation (RAG).

## Come funziona

1. I documenti in `raw_data/` vengono convertiti in md tramite MarkItDown, splittati per sezione e indicizzati come vettori in ChromaDB
2. Quando l'utente fa una domanda, il sistema cerca i 3 chunk più rilevanti per similarità semantica
3. I chunk vengono iniettati nel prompt e Mistral genera una risposta basata solo su quel contesto

## Stack

- **LangChain** — orchestrazione pipeline RAG
- **MarkItDown** — conversione documenti (PDF, DOCX, ecc.) in Markdown
- **MistralAI** — embeddings e generazione (mistral-medium-3.5)
- **ChromaDB** — vector store locale
- **Gradio** — interfaccia web chat

## Setup

```bash
# Clona il repo
git clone <url-repo>
cd ragitdown

# Installa dipendenze (con uv)
uv sync

# Configura API key
echo "MISTRAL_API_KEY=la-tua-chiave" > .env

# Avvia
uv run python main.py
```

L'interfaccia si apre su `http://localhost:7860`.

## Struttura

```
main.py        — orchestratore, avvia Gradio
indexer.py     — converte documenti → chunk → embeddings → ChromaDB
retriever.py   — cerca chunk simili alla query
generator.py   — costruisce prompt con contesto e genera risposta
raw_data/      — documenti sorgente (PDF, DOCX, ecc.)
```

## Note

- L'indice viene ricostruito da zero ad ogni avvio
- Servono le API key di Mistral nel file `.env`
