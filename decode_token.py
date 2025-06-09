import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o")
token_id = 63842

token_bytes = encoding.decode_single_token_bytes(token_id)
print("Bytes:", token_bytes)
print("Decoded text:", token_bytes.decode('utf-8', errors='ignore'))
