# Quick Start: Install Evangelion Theme in GoLand / IntelliJ

## For GoLand Users

### Option 1: Manual Installation (Recommended)

1. **Find your GoLand version and config directory:**
   ```bash
   # macOS
   ls ~/Library/Application\ Support/JetBrains/
   
   # Linux
   ls ~/.config/JetBrains/
   
   # Windows (PowerShell)
   dir $env:APPDATA\JetBrains\
   ```

2. **Copy theme files:**
   ```bash
   # macOS example (replace GoLand2023.2 with your version)
   cp intellij-themes/*.icls ~/Library/Application\ Support/JetBrains/GoLand2023.2/colors/
   
   # Linux example
   cp intellij-themes/*.icls ~/.config/JetBrains/GoLand2023.2/colors/
   
   # Windows (PowerShell)
   Copy-Item intellij-themes\*.icls $env:APPDATA\JetBrains\GoLand2023.2\colors\
   ```

3. **Restart GoLand**

4. **Apply theme:**
   - Press `⌘,` (macOS) or `Ctrl+Alt+S` (Windows/Linux)
   - Go to: **Editor → Color Scheme**
   - Select: **Eva 01 Theme**, **Eva 01 v2.0**, or **Eva 02 Theme**
   - Click **OK**

### Option 2: Import via Settings

1. Open GoLand
2. Go to **File → Manage IDE Settings → Import Settings...**
3. Browse to `intellij-themes/` directory
4. Select any `.icls` file
5. Check "Color schemes" and click **OK**
6. Restart when prompted

## Available Themes

| Theme | Description | Best For |
|-------|-------------|----------|
| **Eva 01 Theme** | Classic purple/green | General coding |
| **Eva 01 v2.0** | Neon purple/green | Dark environments |
| **Eva 02 Theme** | Red/orange | High contrast |

## Troubleshooting

### Can't find colors directory?
Create it manually:
```bash
# macOS
mkdir -p ~/Library/Application\ Support/JetBrains/GoLand2023.2/colors/

# Linux
mkdir -p ~/.config/JetBrains/GoLand2023.2/colors/
```

### Theme not appearing?
1. Make sure you restarted GoLand
2. Check that `.icls` files are in the correct directory
3. Try importing via Settings instead

### Colors look wrong?
1. Ensure you selected the theme from: **Settings → Editor → Color Scheme**
2. Try switching to a default theme and back
3. Restart GoLand

## Full Documentation

- Installation guide: [intellij-themes/README.md](intellij-themes/README.md)
- Conversion details: [CONVERSION.md](CONVERSION.md)
- Main README: [README.md](README.md)

## Support

For issues or questions:
- Check the repository's Issues page
- Review the full documentation in `intellij-themes/README.md`

---

**Enjoy your Evangelion-themed IDE!** 🤖💜💚
