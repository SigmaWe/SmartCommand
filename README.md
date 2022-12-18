# text2command

The VSCode extension is available at the VSCode Market named `smart command`. After installation from the VSCode market place, simply type `NLPSearch` in the command palette or use the key binding `ctrl+alt+q` (`shift+cmd+q` on Mac) to call our function. Then type in the description of your desired command. The extension will show a list of candidate commands after a few seconds. We also porive an option in the setting to enable/disable the data collection, which is disabled by default. The user data is only used for model improvement.

## Instruction on the building scaffolding package locally

### Prepare required software and files

Folliwing the official vscode extension tutorial [here](https://code.visualstudio.com/api/get-started/your-first-extension)
Make sure you have Node.js and Git installed, then install Yeoman and VS Code Extension Generator with:

`npm install -g yo generator-code`

### Create new extension

run `yo code` to create a new extension. THen it will ask your choice on some initial options. Choose the Typescript to create the new extension and name it as `smart command`. It is fine to just use the default for other options.
After creating the new extension, you need to install the `node-fetch` by running 
```
cd smart-command
npm install node-fetch@2
```
Then copy the folder `plugin/smart-command` to the new extension and replace the files.

### Run the plugin locally

Open the folder Plugin/text2command in VSCode locally. Use F5 to run the plugin and it will open a new VSCode window. Open command palette in that new VSCode window and search NLPSearch command. Check the plugin Readme file for extension usage guides.

### Notice

If it shows error after press F5 to run the plugin, one can choose debug anyway to temporaily ignore it and continue.

## QueryCollection API
This folder means to collect queries for VSCode smart/fuzzy command search plugin

### How to develop locally?

The query collection server and the plug-in can and should be developed separately,
so this README file will focus on how to set up and develop the query collection server locally.

1. Download and install the latest docker desktop from [the docker website](https://www.docker.com/products/docker-desktop/)

2. Start the docker desktop, in this folder, run `docker compose up`

3. After the server is up, go to http://127.0.0.1:8000/docs to test the API. If you need more details about the API,
please refer to [FastAPI](https://fastapi.tiangolo.com/) in general and `API_doc.docx` for this specific project.

4. To access the database, open your favorite DB managment system and connect to the `Postgres SQL` using the following info:

```
HOST: localhost
DB: database
USERNAME: service
PASSWORD: password
PORT: 54320
```

P.S. You don't need the plugin to test the API. But if you want
to test whether the plugin works correctly or not locally, you need to change the API address in the plugin as follows:

Replace the Micrsoft Azure [createURL](https://github.com/SigmaWe/text2command/blob/f71fc51bc3b4105fbb02c3abb7ba5de2e6ac98f7/Plugin/text2command/src/basicInput.ts#L83) with the localhost one `http://127.0.0.1:8000/createquery/`

Replace the Micrsoft Azure [updateURL](https://github.com/SigmaWe/text2command/blob/main/Plugin/text2command/src/basicInput.ts#L32) with the localhost one `http://127.0.0.1:8000/updatequery/`

For how those two URL works, please refer to the `API_doc.docx` for more details.
