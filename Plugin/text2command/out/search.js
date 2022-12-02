"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const { spawn } = require('child_process');
const vscode = require("vscode");
function getOsPath() {
    const extensionPath = vscode.extensions.getExtension('tatosjb.fuzzy-search')?.extensionPath;
    switch (process.platform) {
        case 'darwin':
            return `${extensionPath}/binaries/darwin`;
        case 'win32':
            return `${extensionPath}/binaries/windows`;
        case 'linux':
            return `${extensionPath}/binaries/linux`;
        default:
            return `${extensionPath}/binaries/linux`;
    }
}
;
function getFdPath() {
    return process.platform === 'win32' ? `${getOsPath()}/fd.exe` : `${getOsPath()}/fd`;
}
;
function getFzfPath() {
    return process.platform === 'win32' ? `${getOsPath()}/fzf.exe` : `${getOsPath()}/fzf`;
}
;
function buildSearch(fd, fzf, text) {
    const path = vscode.workspace.workspaceFolders && vscode.workspace.workspaceFolders[0].uri.path;
    return text ? `${fd} -H --exclude '.git' --type f . '${path || ''}' | ${fzf} --tiebreak=end -m -f '${text}'\n` : '';
}
class Search {
    constructor() {
        this.sh = spawn('sh', []);
        this.fzfPath = getFzfPath();
        this.fdPath = getFdPath();
        this.onDataListeners = [];
        this.fileNames = [];
        this.onResultData = this.onResultData.bind(this);
        this.sh.stdout.on('data', this.onResultData);
    }
    async onResultData(data) {
        this.fileNames = this.fileNames
            .concat(data.toString()
            .split('\n')
            .filter(filePath => filePath.trim() !== '')).slice(0, 10);
        this.onDataListeners.forEach(listener => listener(this.fileNames));
    }
    search(text) {
        this.fileNames = [];
        if (text.length > 0) {
            const command = buildSearch(this.fdPath, this.fzfPath, text.replace(/::/g, '').toLowerCase());
            this.sh.stdin.write(Buffer.from(command));
        }
        else {
            this.onResultData('');
        }
    }
    onData(callback) {
        this.onDataListeners.push(callback);
    }
}
exports.default = Search;
//# sourceMappingURL=search.js.map