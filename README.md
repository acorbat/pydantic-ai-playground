# Pydantic AI Playground

Small playground for trying examples from different sources:

- Real Python: `hello_agent.py`, `db_handling.py`
- ArjanCodes: `triage.py`
- Pydantic AI docs/examples: `data_analyst.py`

The project uses `pixi.toml` to manage dependencies such as `pydantic-ai`, `requests`, `datasets`, and `duckdb`.

## Files

| File | What happens | What was learned |
| --- | --- | --- |
| `hello_agent.py` | Creates a minimal Pydantic AI agent, loads environment variables with `python-dotenv`, sends one prompt, and prints a one-sentence answer. | The smallest useful Pydantic AI setup is just a model, instructions, and `run_sync(...)`. |
| `db_handling.py` | Defines a small database wrapper around the JSONPlaceholder API, exposes it to the agent through dependencies and a tool, and returns a validated `UserSummary` Pydantic model. | Agents can call external systems through tools, and `output_type` makes the final response structured and validated instead of free-form text. |
| `triage.py` | Builds an async medical triage agent with dependency injection, a dynamic system prompt that adds the patient name, and a tool that fetches the latest vitals before producing a typed triage result. | Pydantic AI supports async workflows, context-aware system prompts, and structured decision outputs like escalation flags and urgency scores. |
| `data_analyst.py` | Creates a data analyst agent that loads Hugging Face datasets into pandas, stores intermediate DataFrames as references like `Out[1]`, queries them with DuckDB SQL, and displays previews. | Agents can orchestrate multi-step data workflows, keep intermediate state in dependencies, and use `ModelRetry` to steer the model back to valid references when it makes a mistake. |

## Overall Takeaways

- Pydantic AI scales from simple prompt/response scripts to agents with tools, dependencies, and typed outputs.
- Dependency injection keeps external state and services separate from the prompt itself.
- Pydantic models are useful guardrails for getting reliable, machine-readable results.
- Tools let the model work with real data sources, APIs, and local analysis steps instead of only generating text.