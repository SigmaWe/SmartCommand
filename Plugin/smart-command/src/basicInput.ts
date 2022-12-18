/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

import { window } from 'vscode';
import * as vscode from 'vscode';
//import fetch from 'node-fetch'; 
const fetch = require('node-fetch')

export async function SingleStepSearch() {
	let i = 0;
	//const allCommands = await vscode.commands.getCommands(true);
	const query = await vscode.window.showInputBox();
	const [id, response]:any|undefined = await main(query);

	const result: string | undefined = await window.showQuickPick(response, {
		placeHolder: 'Select a command.',
		//onDidSelectItem: item => window.showInformationMessage(`Focus ${++i} option: ${item}`)
	});
	/*
	const result2 = await window.showQuickPick(response, {
		placeHolder: 'Select a command for the second model.',
		//onDidSelectItem: item => window.showInformationMessage(`Focus ${++i} option: ${item}`)
	});
	*/
	vscode.commands.executeCommand(String(result));
	const selection_id = response.indexOf(result);
	const collection_flag = vscode.workspace.getConfiguration().get('conf.data.collection');
	//const selection_id2 = response2.indexOf(result2);
	if (typeof result == 'string' && collection_flag){
		const confirm = await fetch('https://querycollection-app.icymeadow-3b7ab52d.centralus.azurecontainerapps.io/updatequery/', {
			method: 'PUT', 
			body: JSON.stringify([{'id':id, 'selection': result}]),
			headers: {'accept': 'application/json', 'Content-Type': 'application/json'}
		  }).then((confirm: any) => confirm.json());
		if (confirm[id].status==1){
			window.showInformationMessage(`Finish uploading feedback. Thank you!`);
		}else{
			window.showInformationMessage(`The data collection failed. Please try again.`);
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
};

export async function main(query: any) {
  const myUrl = 'https://querycollection-app.icymeadow-3b7ab52d.centralus.azurecontainerapps.io/createquery/';
  const myData = {'query': query};
  //window.showInformationMessage(`Got query: ${query}`);
  window.showInformationMessage(`Searching your command. It takes seconds. Please wait and do not click anywhere.`);
  const response = await fetch(myUrl, {
    method: 'POST',
    body: JSON.stringify(myData),
	headers: {'accept': 'application/json', 'Content-Type': 'application/json'}
  }).then((response: any) => response.json());
  if (typeof response.BERTScore !== 'undefined')
  {
	return [response.BERTScore.id, response.BERTScore.predictions] as const;
  }
  else if (typeof response.sentenceBERT !== 'undefined')
  {
	return [response.sentenceBERT.id, response.sentenceBERT.predictions] as const;
  }
}
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