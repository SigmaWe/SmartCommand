/*
// The module 'vscode' contains the VS Code extensibility API
*/

import { window, commands, ExtensionContext } from 'vscode';
import { SingleStepSearch} from './basicInput';

export function activate(context: ExtensionContext) {
	context.subscriptions.push(commands.registerCommand('text2command.NLPSearch', async () => {
		/*
		const options: { [key: string]: (context: ExtensionContext) => Promise<void> } = {
			SingleStepSearch,
		};
		const quickPick = window.createQuickPick();
		quickPick.items = Object.keys(options).map(label => ({ label }));
		quickPick.onDidChangeSelection(selection => {
			if (selection[0]) {
				options[selection[0].label](context)
					.catch(console.error);
			}
		});
		quickPick.onDidHide(() => quickPick.dispose());
		quickPick.show();*/
		SingleStepSearch();
	}));
}
