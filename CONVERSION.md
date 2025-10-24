# Converting VS Code Themes to IntelliJ IDEA Color Schemes

This document explains how the conversion from VS Code themes to IntelliJ IDEA color schemes works.

## Conversion Script

The `convert_to_intellij.py` script automates the conversion process. It:

1. **Reads VS Code theme JSON files** from the `themes/` directory
2. **Maps VS Code color settings** to IntelliJ color scheme attributes
3. **Converts syntax highlighting tokens** from TextMate scopes to IntelliJ attributes
4. **Generates .icls XML files** compatible with IntelliJ IDEA and all JetBrains IDEs

## Color Mappings

### Editor Colors

| VS Code Setting | IntelliJ Attribute |
|----------------|-------------------|
| `editor.background` | `GUTTER_BACKGROUND` |
| `editorCursor.foreground` | `CARET_COLOR` |
| `editor.selectionBackground` | `SELECTION_BACKGROUND` |
| `editorLineNumber.foreground` | `LINE_NUMBERS_COLOR` |
| `editorLineNumber.activeForeground` | `SELECTED_LINE_NUMBER_COLOR` |
| `terminal.background` | `CONSOLE_BACKGROUND_KEY` |
| `terminal.foreground` | `CONSOLE_FOREGROUND_KEY` |
| `tree.indentGuidesStroke` | `INDENT_GUIDE` |
| `focusBorder` | `SELECTED_INDENT_GUIDE` |

### Syntax Highlighting

| VS Code Scope | IntelliJ Attribute |
|--------------|-------------------|
| `comment` | `DEFAULT_COMMENT`, `COMMENT` |
| `keyword`, `storage.type` | `DEFAULT_KEYWORD`, `KEYWORD` |
| `string` | `DEFAULT_STRING`, `STRING` |
| `constant.numeric` | `DEFAULT_NUMBER`, `NUMBER` |
| `entity.name.function` | `DEFAULT_FUNCTION_DECLARATION`, `FUNCTION_DECLARATION` |
| `support.class`, `entity.name.class` | `DEFAULT_CLASS_NAME`, `CLASS_NAME` |
| `variable` | `DEFAULT_INSTANCE_FIELD`, `INSTANCE_FIELD` |
| `constant.language` | `DEFAULT_CONSTANT`, `CONSTANT` |
| `keyword.operator` | `OPERATOR_SIGN` |
| `entity.name.tag` | `TAG_NAME` |
| `entity.other.attribute-name` | `ATTRIBUTE_NAME` |

## Language-Specific Support

The conversion includes special handling for:
- **Go**: Builtin functions, types, keywords, exported functions
- **JavaScript/TypeScript**: Classes, methods, decorators
- **HTML/XML**: Tags and attributes
- **CSS**: Properties and selectors
- **Markdown**: Headers, links, emphasis
- **JSON**: Property names at different nesting levels

## Running the Conversion

To convert all themes:

```bash
python3 convert_to_intellij.py
```

The script will:
1. Read all `.json` files from the `themes/` directory
2. Generate `.icls` files in the `intellij-themes/` directory
3. Display progress and any errors encountered

## File Format

IntelliJ color schemes use XML format (.icls):

```xml
<scheme name="Theme Name" version="142" parent_scheme="Darcula">
  <colors>
    <option name="CARET_COLOR" value="15FF00"/>
    <!-- More color options -->
  </colors>
  <attributes>
    <option name="DEFAULT_KEYWORD">
      <value>
        <option name="FOREGROUND" value="FA04D3"/>
      </value>
    </option>
    <!-- More syntax highlighting attributes -->
  </attributes>
</scheme>
```

## Customization

To modify the conversion:

1. Edit `convert_to_intellij.py`
2. Update the `color_mappings` dictionary for editor colors
3. Update the `intellij_attributes` dictionary for syntax highlighting
4. Run the script again to regenerate the themes

## Testing

After conversion:
1. Install the theme in your JetBrains IDE
2. Open various file types (Go, JavaScript, HTML, etc.)
3. Verify colors match the VS Code theme
4. Adjust mappings if needed

## Limitations

Some VS Code theme features don't have direct IntelliJ equivalents:
- Activity bar colors (IntelliJ has different UI structure)
- Status bar customizations (limited in IntelliJ)
- Bracket pair colorization (handled differently)
- Git decorations (IntelliJ uses its own system)

The conversion focuses on:
- ✅ Editor background and foreground
- ✅ Syntax highlighting
- ✅ Line numbers and selection
- ✅ Console/terminal colors
- ✅ Caret and cursor colors

## Resources

- [IntelliJ Color Scheme Documentation](https://www.jetbrains.com/help/idea/configuring-colors-and-fonts.html)
- [JetBrains Plugin SDK - Themes](https://plugins.jetbrains.com/docs/intellij/themes.html)
- [TextMate Scopes](https://macromates.com/manual/en/language_grammars)
