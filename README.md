# Stock Comparison Application

This application enables users to compare two stocks based on their analyst recommendations and fundamentals. The app leverages powerful tools and APIs to fetch stock data, process it, and present a concise summary of comparisons. Built with Gradio for an interactive user interface, the app provides a seamless experience for stock analysis.

---

## Features

1. **Stock Comparison**:
   - Fetch and compare stock analyst recommendations and fundamentals.
   - Displays concise summaries in table format for better clarity.

2. **Web Integration**:
   - Leverages DuckDuckGo for additional web searches if required.

3. **User-Friendly Interface**:
   - Built using Gradio with a visually appealing theme.
   - Simple input and output system for ease of use.

---

## Installation

### Prerequisites

- Python 3.8 or above.
- Ensure you have a `.env` file containing the `GROQ_API_KEY` for authenticating with the Groq model.

### Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:

- **Phidata**: For managing agents and Groq models.
- **Groq**: To utilize the Llama model for advanced AI capabilities.
- **yfinance**: For fetching stock data such as prices, fundamentals, and analyst recommendations.
- **duckduckgo-search**: To perform web searches directly.
- **Gradio**: For creating the user interface.

---

## How to Use

1. **Prepare Your Environment**:
   - Ensure the `.env` file with the `GROQ_API_KEY` is set up correctly.
   - Example `.env` file:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```

2. **Run the Application**:

   Execute the Python script:

   ```bash
   python app.py
   ```

3. **Interact with the App**:
   - Enter two stock symbols (e.g., `AAPL`, `MSFT`) in the provided textboxes.
   - View the generated stock comparison in the output section.

---

## Key Components

1. **Finance Agent**:
   - Fetches stock data and generates comparisons.
   - Utilizes YFinanceTools for detailed stock analysis.

2. **Web Agent**:
   - Performs web searches using DuckDuckGo for additional information.

3. **Agent Team**:
   - Combines the capabilities of the Finance Agent and Web Agent.
   - Processes and returns comprehensive responses.

4. **Gradio Interface**:
   - Provides an intuitive interface for user input and displays results.

---

## Error Handling

The application includes retry logic to handle rate limits when querying APIs. If a `RateLimitError` occurs, the system will wait for a specified duration before retrying.

---

## Customization

- Modify the theme by changing the `theme` parameter in the Gradio interface.
- Update the model or tools in the `Agent` definitions for enhanced capabilities.

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
