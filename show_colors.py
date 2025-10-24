#!/usr/bin/env python3
"""
Quick demo to show the main colors in each Evangelion theme
"""

import json
from pathlib import Path

def show_theme_colors(theme_path):
    """Display the main colors from a VS Code theme"""
    with open(theme_path, 'r') as f:
        theme = json.load(f)
    
    name = theme.get('name', theme_path.stem)
    print(f"\n{'='*60}")
    print(f"Theme: {name}")
    print('='*60)
    
    colors = theme.get('colors', {})
    
    # Show key colors
    color_keys = [
        ('Editor Background', 'editor.background'),
        ('Cursor/Caret', 'editorCursor.foreground'),
        ('Selection', 'editor.selectionBackground'),
        ('Line Numbers', 'editorLineNumber.foreground'),
        ('Active Line Number', 'editorLineNumber.activeForeground'),
        ('Terminal Background', 'terminal.background'),
        ('Terminal Foreground', 'terminal.foreground'),
        ('Focus Border', 'focusBorder'),
    ]
    
    print("\nUI Colors:")
    for label, key in color_keys:
        value = colors.get(key, 'N/A')
        print(f"  {label:25} {value}")
    
    # Show syntax colors
    print("\nSyntax Highlighting:")
    token_colors = theme.get('tokenColors', [])
    
    important_scopes = {
        'Comments': 'comment',
        'Keywords': 'keyword',
        'Strings': 'string',
        'Numbers': 'constant.numeric',
        'Functions': 'entity.name.function',
        'Classes': 'support.class',
    }
    
    scope_map = {}
    for token in token_colors:
        scopes = token.get('scope', [])
        if isinstance(scopes, str):
            scopes = [scopes]
        foreground = token.get('settings', {}).get('foreground')
        for scope in scopes:
            scope_map[scope] = foreground
    
    for label, scope in important_scopes.items():
        color = scope_map.get(scope, 'N/A')
        print(f"  {label:25} {color}")

def main():
    themes_dir = Path(__file__).parent / 'themes'
    
    print("Evangelion Theme Color Reference")
    print("=" * 60)
    
    for theme_file in sorted(themes_dir.glob('*.json')):
        try:
            show_theme_colors(theme_file)
        except Exception as e:
            print(f"\nError reading {theme_file.name}: {e}")
    
    print("\n" + "="*60)
    print("IntelliJ themes available in: intellij-themes/")
    print("="*60)

if __name__ == '__main__':
    main()
