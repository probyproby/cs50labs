'''
import emoji

emos = {['face_with_head-bandage', 'face_screaming_in_fear', 'Zimbabwe',
         '1st_place_medal', 'globe_showing_Americas', 'globe_showing_Asia-Australia',
         'thumbs_up','thumbs_down']}

def convert_emojis(n):
    if 'face_with_head-bandage' in emos:
        emoji.emojize(":face_with_head-bandage:")
        emoji.demojize("🤕")
    elif 'face_screaming_in_fear' in emos:
        emoji.emojize(":face_screaming_in_fear:")
        emoji.demojize("😱")
    elif 'Zimbabwe' in emos:
        emoji.emojize(":Zimbabwe:")
        emoji.demojize("🇿🇼")
    elif '1st_place_medal' in emos:
        emoji.emojize(":1st_place_medal:")
        emoji.demojize("🥇")
    elif 'globe_showing_Americas' in emos:
        emoji.emojize(":globe_showing_Americas:")
        emoji.demojize("🌎")
    elif 'globe_showing_Asia-Australia' in emos:
        emoji.emojize(":globe_showing_Asia-Australia:")
        emoji.demojize("🌏")
    elif 'globe_showing_Europe-Africa' in emos:
        emoji.emojize(":globe_showing_Europe-Africa:")
        emoji.demojize("🌍")
    elif 'thumbs_up' in emos:
        emoji.emojize(":thumbs_up:")
        emoji.demojize("👍")
    elif 'thumbs_down' in emos:
        emoji.emojize(":thumbs_down:")
        emoji.demojize("👎")

'''
#tried
'''
import emoji

emos = ['face_with_head-bandage', 'face_screaming_in_fear', 'Zimbabwe',
        '1st_place_medal', 'globe_showing_Americas', 'globe_showing_Asia-Australia',
        'globe_showing_Europe-Africa', 'thumbs_up', 'thumbs_down']

def convert_emojis(n):
    if n == 'face_with_head-bandage':
        return emoji.demojize("🤕")
    elif n == 'face_screaming_in_fear':
        return emoji.demojize("😱")
    elif n == 'Zimbabwe':
        return emoji.demojize("🇿🇼")
    elif n == '1st_place_medal':
        return emoji.demojize("🥇")
    elif n == 'globe_showing_Americas':
        return emoji.demojize("🌎")
    elif n == 'globe_showing_Asia-Australia':
        return emoji.demojize("🌏")
    elif n == 'globe_showing_Europe-Africa':
        return emoji.demojize("🌍")
    elif n == 'thumbs_up':
        return emoji.demojize("👍")
    elif n == 'thumbs_down':
        return emoji.demojize("👎")
    else:
        return n

def main():
    text = input("Enter Text Version: ")
    emojized_text = ' '.join([convert_emojis(word) for word in text.split()])
    print("Emoji:", emojized_text)

if __name__ == "__main__":

    main()
''

import emoji

def main():
    text = input("Enter Text Version: ")
    emojized_text = emoji.emojize(text)
    print("Emoji:", emojized_text)

if __name__ == "__main__":
    main()
''
import emoji


emos = ['face_with_head-bandage', 'face_screaming_in_fear', 'Zimbabwe',
        '1st_place_medal', 'globe_showing_Americas', 'globe_showing_Asia-Australia',
        'globe_showing_Europe-Africa', 'thumbs_up', 'thumbs_down', 'money_bag', 'candy',]


def main():
    text = input("Input: ")
    emojized_text = convert_emojis(text, use_aliases=True)
    print("Output:", emojized_text)

def convert_emojis(n):
    if n == 'face_with_head-bandage':
        return emoji.emojize(":face_with_head-bandage:")
    elif n == 'face_screaming_in_fear':
        return emoji.emojize(":face_screaming_in_fear:")
    elif n == ':Zimbabwe:':
        return emoji.emojize(":Zimbabwe:")
    elif n == '1st_place_medal':
        return emoji.emojize(":1st_place_medal:")
    elif n == ':globe_showing_Americas:':
        return emoji.emojize(":globe_showing_Americas:")
    elif n == 'globe_showing_Asia-Australia':
        return emoji.emojize(":globe_showing_Asia-Australia:")
    elif n == 'globe_showing_Europe-Africa':
        return emoji.emojize(":globe_showing_Europe-Africa:")
    elif n == 'thumbs_up':
        return emoji.emojize(":thumbs_up:")
    elif n == 'thumbs_down':
        return emoji.emojize(":thumbs_down:")
    elif ':money_bag:' == n:
        return emoji.emojize(":money_bag:")
    elif ':candy:' == n:
        return emoji.emojize(":candy:")
    else:
        return n


if __name__ == "__main__":
    main()


import emoji

def main():
    text = input("Input: ")
    emojized_text = emoji.emojize(text)
    print("Output:", emojized_text)

if __name__ == "__main__":
    main()
'''

import emoji

emos = {
    ':face_with_head-bandage:': "🤕",
    ':face_screaming_in_fear:': "😱",
    ':Zimbabwe:': "🇿🇼",
    ':1st_place_medal:': "🥇",
    ':globe_showing_Americas:': "🌎",
    ':globe_showing_Asia-Australia:': "🌏",
    ':globe_showing_Europe-Africa:': "🌍",
    ':thumbs_up:': "👍",
    ':thumbs_down:': "👎",
    ':money_bag:': "💰",
    ':candy:': "🍬"
}

def convert_emojis(n):
    if n in emos:
        return emos[n]
    return n

def main():
    text = input("Input: ")
    emojized_text = ' '.join([convert_emojis(word) for word in text.split()])
    print("Output:", emojized_text)

if __name__ == "__main__":
    main()