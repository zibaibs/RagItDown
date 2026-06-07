# RagItDown — AI RAG Chatbot

Chatbot con interfaccia web che risponde a domande basandosi sui documenti forniti, usando Retrieval-Augmented Generation (RAG).

## Come funziona

1. I documenti in `raw_data/` (PDF, DOCX, XLSX, immagini, ecc.) vengono convertiti in Markdown strutturato da **MarkItDown**, che preserva la gerarchia dei titoli (`#`, `##`, `###`). Questa struttura viene usata per splittare il testo in chunk semanticamente coerenti, poi indicizzati come vettori in ChromaDB
2. Quando l'utente fa una domanda, il sistema cerca i 3 chunk più rilevanti per similarità semantica
3. I chunk vengono iniettati nel prompt e Mistral genera una risposta basata solo su quel contesto

## Stack

- **LangChain** — orchestrazione pipeline RAG
- **MarkItDown** — converte documenti in Markdown strutturato (PDF, DOCX, XLSX, immagini, HTML, e altro via `[all]`). La struttura dei titoli prodotta è la base del chunking semantico
- **MistralAI** — embeddings e generazione (mistral-medium-3.5)
- **ChromaDB** — vector store locale
- **Gradio** — interfaccia web chat

## Setup

```bash
# Clona il repo
git clone https://github.com/zibaibs/RagItDown
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
- Formati supportati: PDF, DOCX, XLSX, PPTX, immagini, HTML, CSV, ZIP (tramite `markitdown[all,pdf]`)
