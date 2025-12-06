# Allow taillscale SMB
New-NetFirewallRule -DisplayName "Tailscale SMB Allow" -Direction Inbound -Protocol TCP -LocalPort 445 -Action Allow -RemoteAddress 100.x.x.x/10 "

# Fix SMB Speed 
Set-SMBServerConfiguration -EnableMultiChannel $false -Force
Write-Host "Firewall and SMB Configured!" -ForegroundColor Green

