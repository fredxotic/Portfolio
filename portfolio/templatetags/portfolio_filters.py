import re
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def split(value, arg):
    """Split a string by the given delimiter."""
    return value.split(arg)


@register.filter(is_safe=True)
def richtext(value):
    """Convert structured plain text into semantic HTML.

    Handles:
      - Paragraphs separated by blank lines  →  <p>
      - Lines ending with ':'                 →  <h4> headings
      - Lines starting with '•' or '- '      →  <ul> lists
      - Lines starting with '1.' '2.' etc     →  <ol> lists
      - Everything else                       →  <p>
    """
    if not value:
        return ''

    value = escape(value)
    blocks = re.split(r'\n\s*\n', value.strip())
    output = []

    for block in blocks:
        lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
        if not lines:
            continue

        i = 0
        while i < len(lines):
            line = lines[i]

            # Heading: short line ending with ':'
            if line.endswith(':') and len(line) < 80:
                output.append(f'<h4 class="fk-rich-heading">{line[:-1]}</h4>')
                i += 1
                continue

            # Unordered list: lines starting with • or -
            if line.startswith('•') or line.startswith('- '):
                items = []
                while i < len(lines) and (lines[i].startswith('•') or lines[i].startswith('- ')):
                    items.append(re.sub(r'^[•\-]\s*', '', lines[i]))
                    i += 1
                output.append(
                    '<ul class="fk-rich-list">'
                    + ''.join(f'<li>{item}</li>' for item in items)
                    + '</ul>'
                )
                continue

            # Ordered list: lines starting with 1. 2. etc
            if re.match(r'^\d+[\.\)]\s', line):
                items = []
                while i < len(lines) and re.match(r'^\d+[\.\)]\s', lines[i]):
                    items.append(re.sub(r'^\d+[\.\)]\s*', '', lines[i]))
                    i += 1
                output.append(
                    '<ol class="fk-rich-list">'
                    + ''.join(f'<li>{item}</li>' for item in items)
                    + '</ol>'
                )
                continue

            # Regular paragraph
            output.append(f'<p>{line}</p>')
            i += 1

    return mark_safe('\n'.join(output))