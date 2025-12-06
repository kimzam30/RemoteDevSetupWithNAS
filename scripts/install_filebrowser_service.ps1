$nssmPath = "C:\Program Files\FileBrowser\nssm.exe"
& $nssmPath install FileBrowserService "C:\Program Files\FileBrowser\filebrowser.exe" -r "D:\Files' -a 0.0.0.0 -p 8080 '
Start-Service FileBrowserService
Write-Host "FileBrowser Service installed & started" -ForegroundColor Green