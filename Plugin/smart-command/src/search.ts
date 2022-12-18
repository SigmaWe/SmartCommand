import { QuickPickItem } from './types';
const { spawn } = require('child_process');
import * as path from 'path';
import * as vscode from 'vscode';
import { Uri } from 'vscode';

interface DataResultCallback {
  (filePaths: string[]): void;
}

function getOsPath(): String {
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
};

function getFdPath(): string {
  return process.platform === 'win32' ? `${getOsPath()}/fd.exe` : `${getOsPath()}/fd`;
};

function getFzfPath(): string {
  return process.platform === 'win32' ? `${getOsPath()}/fzf.exe` : `${getOsPath()}/fzf`;
};

function buildSearch(fd: string, fzf: string, text: string): string {
  const path = vscode.workspace.workspaceFolders && vscode.workspace.workspaceFolders[0].uri.path;

  return text ? `${fd} -H --exclude '.git' --type f . '${path || ''}' | ${fzf} --tiebreak=end -m -f '${text}'\n` : '';
}

export default class Search {
  private sh = spawn('sh', []);
  private fzfPath = getFzfPath();
  private fdPath = getFdPath();
  private onDataListeners: DataResultCallback[];
  private fileNames: string[];

  constructor(){
    this.onDataListeners = [];
    this.fileNames = [];

    this.onResultData = this.onResultData.bind(this);

    this.sh.stdout.on('data', this.onResultData);
  }

  private async onResultData(data: string) {
    this.fileNames = this.fileNames
      .concat(
        data.toString()
          .split('\n')
          .filter(filePath => filePath.trim() !== '')
      ).slice(0, 10);

    this.onDataListeners.forEach(listener => listener(this.fileNames));
  }

  search(text: string): void {
    this.fileNames = [];
    if(text.length > 0){
      const command = buildSearch(this.fdPath, this.fzfPath, text.replace(/::/g, '').toLowerCase());

      this.sh.stdin.write(Buffer.from(command));
    } else {
      this.onResultData('');
    }
  }

  onData(callback: DataResultCallback){
    this.onDataListeners.push(callback);
  }
}