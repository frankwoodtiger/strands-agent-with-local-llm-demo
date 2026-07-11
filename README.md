# Strands Agent with Local LLM Demo

This project demonstrates a simple Strands agent that runs against a locally hosted LLM through Ollama.

## Prerequisites

Make sure you have Ollama installed and a model pulled locally.

Example:

```bash
ollama run qwen3.5:2b
```

Replace `qwen3.5:2b` with your preferred local model ID if needed.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the demo

Start the agent:

```bash
python -u agent.py
```

## Notes

The example expects Ollama to be running locally and reachable at:

```text
http://localhost:11434/v1
```
