"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.main = exports.SingleStepSearch = void 0;
const vscode_1 = require("vscode");
const vscode = require("vscode");
//import fetch from 'node-fetch'; 
const fetch = require('node-fetch');
async function SingleStepSearch() {
    let i = 0;
    //const allCommands = await vscode.commands.getCommands(true);
    const query = await vscode.window.showInputBox();
    const [id, response] = await main(query);
    const result = await vscode_1.window.showQuickPick(response, {
        placeHolder: 'Select a command.',
        //onDidSelectItem: item => window.showInformationMessage(`Focus ${++i} option: ${item}`)
    });
    /*
    const result2 = await window.showQuickPick(response, {
        placeHolder: 'Select a command for the second model.',
        //onDidSelectItem: item => window.showInformationMessage(`Focus ${++i} option: ${item}`)
    });
    */
    vscode.commands.executeCommand(result);
    const selection_id = response.indexOf(result);
    const collection_flag = vscode.workspace.getConfiguration().get('conf.data.collection');
    //const selection_id2 = response2.indexOf(result2);
    if (typeof result == 'string' && collection_flag) {
        const confirm = await fetch('https://querycollection-app.icymeadow-3b7ab52d.centralus.azurecontainerapps.io/updatequery/', {
            method: 'PUT',
            body: JSON.stringify([{ 'id': id, 'selection': result }]),
            headers: { 'accept': 'application/json', 'Content-Type': 'application/json' }
        }).then((confirm) => confirm.json());
        if (confirm[id].status == 1) {
            vscode_1.window.showInformationMessage(`Finish uploading feedback. Thank you!`);
        }
        else {
            vscode_1.window.showInformationMessage(`The data collection failed. Please try again.`);
        }
    }
    /*
    const decision = await vscode.window.showInformationMessage(`Do you want to execute function ${response}?`, ...['YES', 'CANCEL']).then(selection => {
        if (selection === 'YES')
        {
            vscode.commands.executeCommand(response);
            return 1 as const;
        }else
        {
            return 0 as const;
        }
    });
    if (collection_flag){
    if (decision){
    const selection = await vscode.window.showInformationMessage(`Is this what you want?`, ...['YES', 'NO']).then(selection => {
        if (selection === 'YES')
        {
            return 0 as const;
        }
        else
        {
            return 1 as const;
        }
    });
    const confirm = await fetch('https://querycollection-app.icymeadow-3b7ab52d.centralus.azurecontainerapps.io/updatequery/', {
        method: 'PUT',
        body: JSON.stringify([{'id':id, 'selection': selection}]),
        headers: {'accept': 'application/json', 'Content-Type': 'application/json'}
      }).then((confirm: any) => confirm.json());
    if (confirm[id].status==1){
        window.showInformationMessage(`Finish uploading feedback. Thank you!`);
    }else{
        window.showInformationMessage(`The data collection failed. Please try again.`);
    };
    }
    };
    */
}
exports.SingleStepSearch = SingleStepSearch;
;
async function main(query) {
    const myUrl = 'https://querycollection-app.icymeadow-3b7ab52d.centralus.azurecontainerapps.io/createquery/';
    const myData = { 'query': query };
    //window.showInformationMessage(`Got query: ${query}`);
    vscode_1.window.showInformationMessage(`Searching your command. It takes seconds. Please wait and do not click anywhere.`);
    const response = await fetch(myUrl, {
        method: 'POST',
        body: JSON.stringify(myData),
        headers: { 'accept': 'application/json', 'Content-Type': 'application/json' }
    }).then((response) => response.json());
    if (typeof response.BERTScore !== 'undefined') {
        return [response.BERTScore.id, response.BERTScore.predictions];
    }
    else if (typeof response.sentenceBERT !== 'undefined') {
        return [response.sentenceBERT.id, response.sentenceBERT.predictions];
    }
}
exports.main = main;
/*
 * Shows an input box using window.showInputBox().
export async function showInputBox() {
    const result = await window.showInputBox({
        value: 'abcdef',
        valueSelection: [2, 4],
        placeHolder: 'For example: fedcba. But not: 123',
        validateInput: text => {
            window.showInformationMessage(`Validating: ${text}`);
            return text === '123' ? 'Not 123!' : null;
        }
    });
    window.showInformationMessage(`Got: ${result}`);
}
*/ 
//# sourceMappingURL=basicInput.js.map