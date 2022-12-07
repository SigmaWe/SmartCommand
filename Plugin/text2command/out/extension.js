"use strict";
/*
// The module 'vscode' contains the VS Code extensibility API
*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = void 0;
const vscode_1 = require("vscode");
const basicInput_1 = require("./basicInput");
function activate(context) {
    context.subscriptions.push(vscode_1.commands.registerCommand('text2command.NLPSearch', async () => {
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
        (0, basicInput_1.SingleStepSearch)();
    }));
}
exports.activate = activate;
//# sourceMappingURL=extension.js.map