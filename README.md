# LearnIt
Learn through generative AI video content. \
<img src="client/src/components/images/landingpage.png"  width="575" height="500"/>

## Setup / Installation

- [Install](https://nodejs.org/en/download) Node.js 18 or higher
- [Install](https://www.python.org/downloads/release/python-3110/) Python 3.11 or higher

In the `server` directory, you need the following yaml configuration file keys.yaml” to save the Google Gemini and Deepgram API keys:

```
gemini: "KEY"
deepgram: "KEY"
```

## Available Scripts

NOTE: Scripts are directory dependent. Certain scripts will not work in other directories.

### `npm start`
Runs the frontned client in the development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser. Make sure to run in the `client` directory.

### `npm install`

Installs all packages listed in the `package.json` file in the directory you are in. Make sure to run in the `client` directory.

### `npm run format`

Formats all code using Prettier. Make sure to run in the `client` directory to format all JavaScript files. \
In VS Code, you can install the plugin [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) to format code automatically when saving a file.

### ```fastapi dev main.py```
Runs the backend server. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view it in your browser. Make sure to run in the `server` directory.

### ```source env/bin/activate```
Starts Python virtual environment. Make sure to run in the `server` directory. 

### ```deactivate```
Deactivates Python virtual environment. Make sure to run in the `server` directory.

### `pip install -r requirements.txt`

Installs all required dependencies to run the Python scripts. Make sure to run in the `server` directory.