# KaitoMCPServer

## Environment Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and Python environment management.

### Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Installation

1. **Install uv** (if not already installed):

   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Or using Homebrew on macOS
   brew install uv
   ```

2. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd KaitoMCPServer
   ```

3. **Install dependencies**:

   ```bash
   uv sync
   ```

   This will:
   - Create a virtual environment automatically
   - Install all project dependencies as specified in `pyproject.toml`
   - Lock the dependencies in `uv.lock`

### Running the Project

To run the MCP server:

```bash
uv run python main.py
```

### Development

To activate the virtual environment for development:

```bash
uv shell
```

To add new dependencies:

```bash
uv add <package-name>
```

To add development dependencies:

```bash
uv add --dev <package-name>
```
