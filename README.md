# Streamlit desktop app with Streamlit + Pyodide + Electron

## Rrquires
- Python 3.11
- Node v22.13.0 (LTS)
- package.json : See [@stlite/desktop - npm](https://www.npmjs.com/package/@stlite/desktop)

## Instructions
0. Python VirtualEnv
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

1. Install Node packages
   ```sh
   npm install
   ```

2. Dump packages
   ```sh
   npm run dump hello-world -- -r requirements.txt
   ```

3. Run Serve
   ```sh
   npm run serve
   ```

4. (Optional) Create distoributions
   ```sh
   # npm run app:dist -- --win
   npm run app:dist -- --mac
   open dist/mac/hello-desktop.app
   ```

## for Dev
```sh
streamlit run app.py
```
