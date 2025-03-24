from PIL import Image
import base64
super_secret = Image.open(base64.b32decode(b'M5ZHKLTKOBTQ====').decode('utf-8'))
def encrypt(message,pad):
    cypher = ''
    x = pad[0][0]
    y = pad[0][1]
    it = pad[0][2]%150 #Ensure not one continuous block
    # REDACTED CODE HERE
        
    return cypher

width, height = super_secret.size
pad = [[sum(super_secret.getpixel((x, y))) for x in range(width)] for y in range(height)]
img = Image.open(decrypt('ʟʒʟ˓ʗʍ,',pad))



width, height = img.size
pad = [[sum(img.getpixel((x, y))) for x in range(width)] for y in range(height)]
plaintext = decrypt("śőĉƬǕǷɆǦǞǷǨǽŮǑâƢĠĞǶǞƥȟńƘǭƦòí",pad)