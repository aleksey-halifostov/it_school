byte_text = b'r\xc3\xa9sum\xc3\xa9'
text = byte_text.decode()
print(text)
byte_text = text.encode("Latin1")
print(byte_text)
text = byte_text.decode("Latin1")
print(text)
