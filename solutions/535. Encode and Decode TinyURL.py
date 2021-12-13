# class Codec:
#     def __init__(self):
#         self.store = []
​
#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
#         self.store.append(longUrl)
#         return "http://tinyurl.com/" + str(len(self.store) - 1)
​
#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return self.store[int(shortUrl.split('/')[-1])]
        
​
# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(url))
​
​
# class Codec:
#     def __init__(self):
#         self.url2code = {}
#         self.code2url = {}
​
#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
        
#         # hash longUrl
#         code = hash(longUrl) 
#         self.url2code[longUrl] = code
#         self.code2url[code] = longUrl
#         return "http://tinyurl.com/" + str(code)
        
​
#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return self.code2url[int(shortUrl.split('/')[-1])]
    
class Codec:
    
    alphabet = string.ascii_letters + '0123456789'
    
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
​
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.url2code[longUrl] = code
                self.code2url[code] = longUrl
        
        return self.url2code[longUrl]
​
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code2url[shortUrl.split('/')[-1]]
    
    
​
