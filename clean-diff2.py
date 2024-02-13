import sys

def remove_difadd_wrappers(content):
    while '\\DIFadd{' in content:
        start = content.find('\\DIFadd{')
        end = content.find('}', start)
        content = content[:start] + content[start+8:end] + content[end+1:]
    return content

def replace_author_line(line):
    if line.startswith('\\author{Caleb '):
        return '\\author{Caleb C. Chan}\n'
    return line

def fix_bibliography(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Split the content into lines
    lines = content.split('\n')

    # Replace the author line
    for i, line in enumerate(lines):
        lines[i] = replace_author_line(line)

    # Join the lines back into content
    content = '\n'.join(lines)

    # Find the start and end positions of the bibliography section
    start_index = content.find('\\begin{thebibliography}')
    end_index = content.find('\\end{thebibliography}')

    if start_index == -1 or end_index == -1:
        print('Bibliography section not found in the file.')
        return

    # Extract the bibliography section content
    bibliography_content = content[start_index:end_index]

    # Remove \DIFadd{} wrappers from the bibliography content
    bibliography_content = remove_difadd_wrappers(bibliography_content)

    # Replace the bibliography section content in the original content
    content = content[:start_index] + bibliography_content + content[end_index:]

    with open(filename, 'w') as file:
        file.write(content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python fix_bibliography.py <filename>')
    else:
        filename = sys.argv[1]
        fix_bibliography(filename)