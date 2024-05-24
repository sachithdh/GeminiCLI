# Gemini-For-Terminal

Using this tool you can use latest [gemini-1.5-pro-latest](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-pro-expandable) generative model in your terminal.

## Installation

**Generate API key**
If you don't already have Gemini API key create a key from [here](https://aistudio.google.com/app/apikey).

**Download the .deb File**
- Go to the [Releases](https://github.com/sacheex/Gemini-For-Terminal/releases) section of this repository.
- Find the desired version and download the .deb file
- Navigate to the directory where the .deb file is located
- Run the installation command:
  ```bash
  sudo dpkg -i gemini-for-terminal.deb
  ```
  Then follow the instructions.

## Usage
**text-only prompts**

```bash
gemini <prompt>
```
**Prompt that includes images.

```bash
gemini -i <path/to/image> <prompt>
```

Also you can find usage help using ```gemini --help``` command

```bash
$ gemini --help
usage: gemini [-h] [-i IMG] [words ...]

Gemini AI for terminal

positional arguments:
  words              prompt

options:
  -h, --help         show this help message and exit
  -i IMG, --img IMG  Path to an image
```

## Contributing
If you'd like to contribute to the Gemini Terminal Chatbot project, feel free make your changes, and submit a pull request. Contributions are always welcome and appreciated!
