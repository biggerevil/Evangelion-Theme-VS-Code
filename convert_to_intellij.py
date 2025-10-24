#!/usr/bin/env python3
"""
Script to convert VS Code Evangelion themes to IntelliJ IDEA color schemes (.icls format)
"""

import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.dom import minidom


def hex_to_rgb(hex_color):
    """Convert hex color to RGB values"""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 8:  # RGBA format
        hex_color = hex_color[:6]  # Remove alpha channel
    return hex_color.upper()


def create_intellij_scheme(vscode_theme_path, output_path):
    """Convert a VS Code theme to IntelliJ color scheme"""
    
    # Load VS Code theme
    with open(vscode_theme_path, 'r', encoding='utf-8') as f:
        vscode_theme = json.load(f)
    
    # Get theme name
    theme_name = vscode_theme.get('name', 'Evangelion Theme')
    
    # Create root scheme element
    scheme = ET.Element('scheme', {
        'name': theme_name,
        'version': '142',
        'parent_scheme': 'Darcula'
    })
    
    # Add colors section
    colors_elem = ET.SubElement(scheme, 'colors')
    
    # Map VS Code colors to IntelliJ colors
    colors = vscode_theme.get('colors', {})
    
    # Comprehensive color mappings from VS Code to IntelliJ
    color_mappings = {
        # Editor background
        'editor.background': 'GUTTER_BACKGROUND',
        
        # Caret and selection
        'editorCursor.foreground': 'CARET_COLOR',
        'editor.selectionBackground': 'SELECTION_BACKGROUND',
        'editor.selectionForeground': 'SELECTION_FOREGROUND',
        
        # Line numbers
        'editorLineNumber.foreground': 'LINE_NUMBERS_COLOR',
        'editorLineNumber.activeForeground': 'SELECTED_LINE_NUMBER_COLOR',
        
        # Terminal/console
        'terminal.background': 'CONSOLE_BACKGROUND_KEY',
        'terminal.foreground': 'CONSOLE_FOREGROUND_KEY',
        
        # General foreground
        'foreground': 'CONSOLE_FOREGROUND_KEY',
        
        # Borders and guides
        'focusBorder': 'SELECTED_INDENT_GUIDE',
        'tree.indentGuidesStroke': 'INDENT_GUIDE',
        
        # Editor gutter
        'editorGutter.background': 'GUTTER_BACKGROUND',
        
        # Whitespace
        'editorWhitespace.foreground': 'WHITESPACES',
        
        # Current line
        'editor.lineHighlightBackground': 'CARET_ROW_COLOR',
        
        # Scrollbar
        'scrollbarSlider.background': 'SCROLLBAR_THUMB_COLOR',
        
        # Notifications
        'notifications.border': 'NOTIFICATION_BACKGROUND',
    }
    
    # Apply color mappings, avoiding duplicates
    added_colors = set()
    for vscode_key, intellij_key in color_mappings.items():
        if vscode_key in colors and intellij_key not in added_colors:
            ET.SubElement(colors_elem, 'option', {
                'name': intellij_key,
                'value': hex_to_rgb(colors[vscode_key])
            })
            added_colors.add(intellij_key)
    
    # Add attributes section for syntax highlighting
    attributes_elem = ET.SubElement(scheme, 'attributes')
    
    # Map VS Code token colors to IntelliJ attributes
    token_colors = vscode_theme.get('tokenColors', [])
    
    # Create a mapping of scopes to colors
    scope_colors = {}
    for token in token_colors:
        scopes = token.get('scope', [])
        if isinstance(scopes, str):
            scopes = [scopes]
        
        settings = token.get('settings', {})
        foreground = settings.get('foreground')
        font_style = settings.get('fontStyle', '')
        
        for scope in scopes:
            scope_colors[scope] = {
                'foreground': foreground,
                'fontStyle': font_style
            }
    
    # Map common scopes to IntelliJ attributes
    def add_attribute(name, scope_keys, default_fg=None):
        """Helper to add an attribute based on scope(s)"""
        if isinstance(scope_keys, str):
            scope_keys = [scope_keys]
        
        # Try each scope key in order
        for scope_key in scope_keys:
            color_info = scope_colors.get(scope_key)
            if color_info and color_info['foreground']:
                option = ET.SubElement(attributes_elem, 'option', {'name': name})
                value = ET.SubElement(option, 'value')
                ET.SubElement(value, 'option', {
                    'name': 'FOREGROUND',
                    'value': hex_to_rgb(color_info['foreground'])
                })
                
                # Add font style if specified
                font_style = color_info.get('fontStyle', '')
                if 'bold' in font_style.lower():
                    ET.SubElement(value, 'option', {
                        'name': 'FONT_TYPE',
                        'value': '1'
                    })
                elif 'italic' in font_style.lower():
                    ET.SubElement(value, 'option', {
                        'name': 'FONT_TYPE',
                        'value': '2'
                    })
                return  # Successfully added, stop trying other keys
    
    # Add common syntax highlighting attributes with fallbacks
    add_attribute('DEFAULT_COMMENT', ['comment', 'comment.line', 'comment.block'])
    add_attribute('DEFAULT_KEYWORD', ['keyword', 'storage.type', 'storage.modifier'])
    add_attribute('DEFAULT_STRING', ['string', 'string.quoted'])
    add_attribute('DEFAULT_NUMBER', ['constant.numeric', 'constant.language'])
    add_attribute('DEFAULT_FUNCTION_DECLARATION', ['entity.name.function', 'meta.function-call', 'support.function'])
    add_attribute('DEFAULT_CLASS_NAME', ['entity.name.class', 'entity.name.type', 'support.class'])
    add_attribute('DEFAULT_INSTANCE_FIELD', ['variable', 'variable.other'])
    add_attribute('DEFAULT_CONSTANT', ['constant.language', 'constant.character'])
    add_attribute('DEFAULT_IDENTIFIER', ['variable', 'entity.name'])
    
    # Additional language-specific attributes for better syntax highlighting
    intellij_attributes = {
        'KEYWORD': ['keyword', 'storage.type'],
        'COMMENT': ['comment'],
        'DOC_COMMENT': ['comment.block.documentation', 'comment.block'],
        'STRING': ['string'],
        'NUMBER': ['constant.numeric'],
        'FUNCTION_DECLARATION': ['entity.name.function'],
        'CLASS_NAME': ['support.class', 'entity.name.class'],
        'CONSTANT': ['constant.language', 'support.constant'],
        'INSTANCE_FIELD': ['variable.other.property', 'variable'],
        'STATIC_FIELD': ['variable.other.constant'],
        'OPERATOR_SIGN': ['keyword.operator', 'keyword.control'],
        'TAG_NAME': ['entity.name.tag'],
        'ATTRIBUTE_NAME': ['entity.other.attribute-name'],
        'INVALID_STRING_ESCAPE': ['invalid', 'invalid.illegal'],
        'METADATA': ['entity.name.tag', 'meta.tag'],
        'TYPE_PARAMETER_NAME': ['entity.name.type', 'support.type'],
        'GO_BUILTIN_FUNCTION': ['support.function'],
        'GO_BUILTIN_TYPE': ['support.type'],
        'GO_KEYWORD': ['keyword'],
        'GO_EXPORTED_FUNCTION': ['entity.name.function'],
    }
    
    for intellij_attr, vscode_scopes in intellij_attributes.items():
        add_attribute(intellij_attr, vscode_scopes)
    
    # Convert to pretty XML string
    xml_str = ET.tostring(scheme, encoding='unicode')
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent='  ')
    
    # Remove extra blank lines and XML declaration
    lines = pretty_xml.split('\n')
    lines = [line for line in lines if line.strip()]
    pretty_xml = '\n'.join(lines[1:])  # Skip XML declaration
    
    # Write to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f"✓ Converted {vscode_theme_path.name} -> {output_path.name}")
    return output_path


def main():
    """Main conversion function"""
    script_dir = Path(__file__).parent
    themes_dir = script_dir / 'themes'
    intellij_dir = script_dir / 'intellij-themes'
    
    # Create output directory
    intellij_dir.mkdir(exist_ok=True)
    
    # Get all theme files
    theme_files = list(themes_dir.glob('*.json'))
    
    if not theme_files:
        print("No theme files found in themes/ directory")
        sys.exit(1)
    
    print(f"Found {len(theme_files)} theme(s) to convert:\n")
    
    # Convert each theme
    for theme_file in theme_files:
        output_name = theme_file.stem + '.icls'
        output_path = intellij_dir / output_name
        
        try:
            create_intellij_scheme(theme_file, output_path)
        except Exception as e:
            print(f"✗ Error converting {theme_file.name}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n✓ Conversion complete! IntelliJ themes saved to: {intellij_dir}")
    print("\nTo install:")
    print("1. Copy .icls files to your IntelliJ config directory:")
    print("   - macOS: ~/Library/Application Support/JetBrains/<Product><Version>/colors/")
    print("   - Linux: ~/.config/JetBrains/<Product><Version>/colors/")
    print("   - Windows: %APPDATA%\\JetBrains\\<Product><Version>\\colors\\")
    print("2. Restart IntelliJ/GoLand")
    print("3. Go to Settings > Editor > Color Scheme")
    print("4. Select your Evangelion theme from the dropdown")


if __name__ == '__main__':
    main()
