
# File Upload Pandas Viewer

This is a Streamlit app that allows users to upload CSV, Excel, or JSON files and view their contents using pandas. It also provides the ability to run queries on the uploaded data using the OpenAI API.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Illia-the-coder/DataPulse.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Obtain an OpenAI API key:

   You need to obtain an API key from OpenAI to use the language processing capabilities. Refer to the OpenAI documentation for instructions on how to obtain the API key.

4. Set up the API key:

   Open the `app.py` file and replace `'Your-OpenAI-API-Key'` with your actual OpenAI API key.

## Usage
```

Remember to replace `'Your-OpenAI-API-Key'` with your actual OpenAI API key.

Feel free to customize this README file further to provide more specific information about your project, such as additional sections explaining the functionalities, providing examples, or including screenshots of the app.
```
1. Run the Streamlit app:

```

   streamlit run app.py
   ```

2. Access the app:

   Open your web browser and navigate to `http://localhost:8501`. You should see the File Upload Pandas Viewer app.

3. Upload a file:

   Click on the "Choose a file" button and select a CSV, Excel, or JSON file to upload. The file will be displayed in a pandas DataFrame format.

4. Run queries:

   Enter a query in the text input box provided and click "Enter" to submit the query. The app will use the OpenAI API to process the query on the uploaded data and display the result.

5. Explore the data:

   You can interact with the DataFrame by scrolling, sorting, filtering, or visualizing the data using the available pandas functionalities.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
