import { app, BrowserWindow, ipcMain } from 'electron';
import path from 'path';
import { fileURLToPath } from 'url';
import isDev from 'electron-is-dev';
import { spawn } from 'child_process';

// Get __dirname equivalent in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let mainWindow;

const registerIpcHandlers = () => {
    ipcMain.handle('run-python', async (event, prompt) => {
        console.log("IPC Handler called with prompt:", prompt);
        
        return new Promise((resolve, reject) => {
            try {
                // Go up two directories from public to reach server
                const scriptPath = path.join(__dirname, '..', '..', 'server', 'main.py');
                console.log("Executing Python script at:", scriptPath);
                
                const pythonProcess = spawn('python3', [scriptPath, prompt]);

                pythonProcess.stdout.on('data', (data) => {
                    console.log(`Python stdout: ${data}`);
                });

                pythonProcess.stderr.on('data', (data) => {
                    console.error(`Python stderr: ${data}`);
                });

                pythonProcess.on('close', (code) => {
                    console.log(`Python process exited with code ${code}`);
                    resolve(code);
                });

                pythonProcess.on('error', (err) => {
                    console.error('Failed to start Python process:', err);
                    reject(err);
                });
            } catch (error) {
                console.error('Error in IPC handler:', error);
                reject(error);
            }
        });
    });
};

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 850,
        height: 800,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            enableRemoteModule: true
        },
    });

    mainWindow.loadURL(
        isDev
            ? 'http://localhost:3000'
            : `file://${path.join(__dirname, '../build/index.html')}`
    );

    if (isDev) {
        mainWindow.webContents.openDevTools();
    }
}

app.whenReady().then(() => {
    registerIpcHandlers();
    createWindow();
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
}); 