# Locally-Built-RAG-Agent-using-Ollama-and-Langchain

<div align="center">![Pasted image 20240513123914.png](Pasted image 20240513123914.png)</div>




Large language models have limitations too, such as inaccurate information, and these limitations are referred to as LLM hallucinations. To mitigate such unwanted responses from LLMs, there are some techniques that have gained popularity. One of such techniques is Retrieval-Augmented Generation (RAG).

Ollama is a software tool designed to run a specific type of AI application entirely on your own computer system, rather than relying on cloud storage.

 Traditional RAG applications rely on powerful LLMs hosted in the cloud. Ollama allows you to download and run a locally available and more efficient version of an LLM directly on your computer.

# Ollama Installation

Download Ollama's setup file from its website ([ollama.ai](https://ollama.ai)).

# Locally Available Large Language Models

Ollama offers a few renowned models for use like:

**LLAMA3–7B**
**Mistral-7B**
**Phi3-Mini-4B**
**Open Hermes 2.5 — Mistral 7B**

# Model Installation

To install the model into the system, you need to pull the model into Ollama using command

```
ollama pull llama3
```

You can check that your model is installed using the command:

```
ollama list
```

# Ollama Embedding Models

We can also use embedding models through ollama. Some of the famous embedding models are: 

- Nomic-Embed-Text
- sentence-transformers
- mistral-text-embeddings
# Local Vector Databases

Local vector databases in Ollama serve as repositories of dense numerical representations (vectors) derived from textual data. Unlike traditional cloud-based solutions, local vector databases operate entirely on the user’s device, ensuring that sensitive data remains secure and private.

Some of the famous local databases available are:

- Chroma DB
- Lance DB
- FAISS

This RAG Agent uses Chroma DB for local vector storage.
