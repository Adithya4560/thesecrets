from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'encrypter/index.html')

def process(request):
    text = request.GET.get('text', '')
    action = request.GET.get('action', 'encrypt')
    shift = int(request.GET.get('shift', 0))
    
    if action == 'encrypt':
        processed_text = encrypt(text, shift)
        return JsonResponse({'processed_text': processed_text})
    elif action == 'decrypt':
        possible_decryptions = {i: decrypt(text, i) for i in range(26)}
        return JsonResponse({'possible_decryptions': possible_decryptions})

def encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)
