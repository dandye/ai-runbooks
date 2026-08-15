# Malware Triage Runbook Evaluation

This directory contains the evaluation set for the Malware Triage runbook.

## Prerequisites

To run the evaluation, you need:

1.  The `google-adk` package installed with the `eval` extra:
    ```bash
    pip install "google-adk[eval]"
    ```
2.  The `uv` package installed.
3.  Access to Google SecOps, Google Threat Intelligence, and Vertex AI.

## Environment Setup

The agent requires a `.env` file in `mcp-security/run-with-google-adk/google-mcp-security-agent/`.
You can copy `mcp-security/run-with-google-adk/google-mcp-security-agent/sample.env` to `.env` and fill in the required values:

```bash
cp mcp-security/run-with-google-adk/google-mcp-security-agent/sample.env mcp-security/run-with-google-adk/google-mcp-security-agent/.env
```

Set the following variables in the `.env` file:
- `GOOGLE_API_KEY`: Your Gemini/Vertex AI API key.
- `CHRONICLE_PROJECT_ID`: Google Cloud Project ID for Chronicle.
- `CHRONICLE_CUSTOMER_ID`: Chronicle Customer ID.
- `CHRONICLE_REGION`: Chronicle Region.
- `VT_APIKEY`: VirusTotal API Key.
- `SOAR_URL`: SecOps SOAR URL.
- `SOAR_APP_KEY`: SecOps SOAR App Key.
- `GOOGLE_CLOUD_PROJECT`: Google Cloud Project ID.
- `GOOGLE_CLOUD_LOCATION`: Google Cloud Location (e.g., `us-central1`).

## Running the Evaluation

To run the evaluation, use the `adk eval` command:

```bash
adk eval mcp-security/run-with-google-adk/google-mcp-security-agent evals/malware_triage_eval.evalset.json
```

This will execute the agent defined in `mcp-security/run-with-google-adk/google-mcp-security-agent` against the `malware_triage_eval.evalset.json` file.

**Note:** The evaluation requires live access to the services defined in the runbook. Ensure your environment is configured correctly.
