"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");
const search_1 = require("./search");
class myt {
    constructor(label, path) {
        this.description = '';
        this.label = label;
        this.filePath = path;
    }
}
let a = new myt('abc', 'def');
let b = new myt('abc', 'def');
class NLPSearch {
    constructor(context) {
        this.quickPick = vscode.window.createQuickPick();
        this.search = new search_1.default();
        this.quickPick.busy = false;
        this.quickPick.items = a;
        this.quickPick.placeholder = "Fuzzy search";
        this.quickPick.matchOnDescription = true;
        this.quickPick.sortByLabel = false;
        // this.quickPick.onDidChangeValue(this.onDidChangeValue);
        // this.quickPick.onDidAccept(this.onAccept);
        this.quickPick.show();
        this.find('123');
    }
    find(value) {
        this.quickPick.busy = true;
        const searchTerm = value.toString();
        this.search.search(searchTerm);
    }
}
exports.default = NLPSearch;
//# sourceMappingURL=NLP-search.js.map