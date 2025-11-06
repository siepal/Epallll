MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
}
def morse_to_text(morse_code_message):
  translated_text = []
  words = morse_code_message.strip().split('   ')
  
  for word in words:
    characters = word.split(' ')
    for char_code in characters:
      if char_code in MORSE_CODE_DICT:
        translated_text.append(MORSE_CODE_DICT[char_code])
      else:
        translated_text.append('[UNKNOWN')
    translated_text.append(' ')
    
  return ''.join(translated_text).strip()
  

if __name__ == "__main__":
  user_input = input("Enter morse code (gunakan spasi untuk memisahkan karakter, 3 kali spasi untuk memisahkan huruf): ")
  result = morse_to_text(user_input)
  print("teks yang sudah di translate:", result)