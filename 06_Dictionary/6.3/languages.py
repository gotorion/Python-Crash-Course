favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java'
}

for name in favorite_languages.keys():
    print(name.title())
# default to traversal keys, code below do the same thing
for name in favorite_languages:
    print(name.title())

for name in sorted(favorite_languages):
    print(name.title())
