# Evangelion Themes for IntelliJ IDEA / GoLand

This directory contains IntelliJ IDEA color schemes converted from the Evangelion VS Code themes.

## Available Themes

- **Eva 01 Theme** (`Eva 01 Theme-color-theme.icls`) - Classic Eva 01 color palette with purple, green, and yellow
- **Eva 01 v2.0** (`Eva 01 v2.0.icls`) - Neon version of Eva 01 with enhanced syntax highlighting
- **Eva 02 Theme** (`EVA 02.icls`) - Based on Eva 02 color palette with red and orange tones

## Installation Instructions

### For GoLand, IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs:

1. **Locate your IDE's colors directory:**
   
   - **macOS**: `~/Library/Application Support/JetBrains/<Product><Version>/colors/`
     - Example: `~/Library/Application Support/JetBrains/GoLand2023.2/colors/`
   
   - **Linux**: `~/.config/JetBrains/<Product><Version>/colors/`
     - Example: `~/.config/JetBrains/GoLand2023.2/colors/`
   
   - **Windows**: `%APPDATA%\JetBrains\<Product><Version>\colors\`
     - Example: `C:\Users\YourName\AppData\Roaming\JetBrains\GoLand2023.2\colors\`

2. **Create the colors directory if it doesn't exist:**
   ```bash
   # macOS/Linux
   mkdir -p ~/Library/Application\ Support/JetBrains/GoLand2023.2/colors/
   
   # Or on Linux
   mkdir -p ~/.config/JetBrains/GoLand2023.2/colors/
   ```

3. **Copy the .icls files to the colors directory:**
   ```bash
   # Copy all themes
   cp *.icls ~/Library/Application\ Support/JetBrains/GoLand2023.2/colors/
   
   # Or copy just one theme
   cp "Eva 01 v2.0.icls" ~/Library/Application\ Support/JetBrains/GoLand2023.2/colors/
   ```

4. **Restart your JetBrains IDE** (GoLand, IntelliJ IDEA, etc.)

5. **Apply the theme:**
   - Go to **Settings/Preferences** (⌘, on macOS or Ctrl+Alt+S on Windows/Linux)
   - Navigate to **Editor → Color Scheme**
   - Select your Evangelion theme from the dropdown (e.g., "Eva 01 Theme")
   - Click **OK** to apply

## Alternative Installation Method (Import)

You can also import the theme files directly through the IDE:

1. Open your JetBrains IDE
2. Go to **File → Manage IDE Settings → Import Settings...**
3. Select the `.icls` file you want to import
4. Check "Color schemes" in the import dialog
5. Click **OK** and restart the IDE if prompted

## Theme Preview

The themes include customized colors for:
- Syntax highlighting (keywords, strings, comments, functions, etc.)
- Editor background and foreground
- Line numbers and current line
- Selection colors
- Console/terminal colors
- Caret and cursor colors
- And more!

## Customization

After installing a theme, you can further customize it:
1. Go to **Settings → Editor → Color Scheme**
2. Select your Evangelion theme
3. Click the gear icon ⚙️ next to the theme dropdown
4. Choose **Duplicate** to create a copy you can modify
5. Customize individual colors as needed

## Support

If you encounter any issues or want to customize the themes further:
- Check the main repository for updates
- Report issues on the GitHub repository
- Customize the .icls files directly (they're XML files)

## Credits

These themes are converted from the original Evangelion VS Code themes.
Original themes created for Visual Studio Code, now available for JetBrains IDEs!

**Enjoy coding with Evangelion!** 🤖💜💚
