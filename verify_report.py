import pypdf

r = pypdf.PdfReader('TERRA_AI_PROJECT_REPORT.pdf')
print(f'Total pages in generated PDF: {len(r.pages)}')

full_text = ''
for i, page in enumerate(r.pages):
    txt = page.extract_text() or ''
    full_text += txt + '\n'

forbidden = ['TERRA·AI', 'TerraAI', 'TERRA AI', 'Autonomous Geotechnical & Environmental Intelligence Platform']
for word in forbidden:
    count = full_text.count(word)
    print(f'Count of "{word}": {count}')

print('\nCheck Official Title:')
print('CONSTRUCTION SITE VIABILITY count:', full_text.count('CONSTRUCTION SITE VIABILITY') + full_text.count('Construction Site Viability'))

print('\nCheck Team Members:')
for m in ['Vaira Selvi S', 'Vishali S', 'Mohana Priya K']:
    print(f'  {m}: {full_text.count(m)}')

print('\nCheck Institution:')
print('  Kamaraj College:', full_text.count('Kamaraj College'))

print('\nCheck End Sections:')
for s in ['References', 'Feedback and Conclusion', 'Sample API Request and Response', 'Glossary of Terms', 'Certificate of Completion', 'Project Photographs', 'GEOTAGGED PHOTOGRAPHS']:
    print(f'  {s}: {full_text.count(s)}')
