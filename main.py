import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    end_text = ""
    for l in text:
        if l in alphabet:
            index_start = alphabet.index(l)
            if direction == 'encode':
                end_text += alphabet[(index_start + shift) % len(alphabet)]
            if direction == 'decode':
                end_text += alphabet[(index_start - shift) % len(alphabet)]
        else:
            end_text += l

    return end_text


while True:
    print(art.logo)
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    end_text = caesar(text, shift, direction)
    print(f"The {direction} is: {end_text}")
    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart == 'no':
        print("See you next time")
        break
