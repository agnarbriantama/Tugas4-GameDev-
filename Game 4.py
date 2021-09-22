# PART E
#improt library terlebih dahulu
import pygame, sys
from pygame import rect
from pygame.locals import *
import time

#mendenifisikan lebar dan panjang layar
#pemberian nama/judul output saat di running
WIDTH, HEIGHT = 720,640
TITLE = "Smooth Movement"

pygame.init() #menginisialisasi semua modul yang diperlukan untuk PyGame
#varible win untuk menampilkan output dengan ukuran jendela yg diinginkan
win = pygame.display.set_mode((WIDTH,HEIGHT)) #nilai HIGHT dan WIDHT tadi = 400, tinggal memanggil saja
pygame.display.set_caption(TITLE) #set title output saat di run
clock = pygame.time.Clock() #mengetahui waktu yang diperlukan untuk benda bergerak

# set RGB Colors
MedBlue = (100, 149, 237)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# PART D
#Di sini kita buat sebuah metode bernama __init__. Metode yang dipanggil saat 
#membuat sebuah objek. Di setiap metode class harus selalu ada self sebagai 
#parameter pertamanya.
#Variabel self merujuk kepada objek dari class tersebut
class Player: 
    def __init__(self, x, y): 
        self.x = int(x) 
        self.y = int(y) 
        self.rect = pygame.Rect(self.x , self.y, 32, 32) 
        self.color = (250, 120, 60) 
        self.velX = 0 
        self.velY = 0 
        self.left_pressed = False 
        self.right_pressed = False 
        self.up_pressed = False 
        self.down_pressed = False 
        self.speed = 4 

    #pada bagian F dan A terdapat Pada def update
    #juga terdapat variable self yang diikuti parameter
    # PART F
    def draw(self, win): 
        pygame.draw.rect(win, self.color, self.rect)

    # PART A
    def update(self): #mengupdate properti-properti pada object
        self.velX = 0 #memberikan arah gerak pada object di sumbu X, dimulai dari titik 0
        self.velY = 0 #memberikan arah gerak pada object di sumbu Y, dimulai dari titik 0
        if self.left_pressed and not self.right_pressed: #jika yang ditekan adalah tombol kiri dan bukan tombol kanan maka arah gerak menuju arah kiri (koordinat x negatif)
            if self.x >0: #memberikan batas agar objek tidak bergerak melewati batas display window (secara horizontal)
                self.velX = -self.speed
        if self.right_pressed and not self.left_pressed: #jika yang ditekan adalah tombol kanan dan bukan tombol kiri maka arah gerak menuju arah kanan (koordinat x positif)
            if self.x < 720 -32: #memberikan batas agar objek tidak bergerak melewati batas display window (secara horizontal)
                self.velX = self.speed
        if self.up_pressed and not self.down_pressed: #jika yang ditekan adalah tombol atas dan bukan tombol bawah maka arah gerak menuju arah atas (koordinat y positif)
            if self.y > 0: #memberikan batas agar objek tidak bergerak melewati batas display window (secara vertical)
                self.velY = -self.speed
        if self.down_pressed and not self.up_pressed: #jika yang ditekan adalah tombol bawah dan bukan tombol atas maka arah gerak menuju arah bawah (koordinat y negatif)
            if self.y < 640 - 32: #memberikan batas agar objek tidak bergerak melewati batas display window (secara vertical)
                self.velY = self.speed

        self.x += self.velX 
        self.y += self.velY 

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)


# PART B
# variable palyer untuk mengatur ukuran dari benda/player
# Mengatur player dengan HEIGHT dan WIDTH yang sudah didefiniskan lalu dibagi 2
player = Player(WIDTH/2, HEIGHT/2)

# Membuat Teks Pada Layar
#Digunakan font color untuk warna pada font
font_color = (255,0,127)
#font_obj akan mendenifisikan dari jenis font yang akan digunakan dan ukurannya
font_obj = pygame.font.Font("Bomb Da Gone.OTF",25)
#tulisan yang akan muncul pada layar
text = "Agnar Briantama Ridhwanullah"
#variable image mendenifisikan tulisan/teks dan warna yang nanti akan ditampilkan
img = font_obj.render(text, True, (BLACK))
#variable rect untuk mengambil variable img tadi
rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))

#perulangan while
#pada perulangan ini terdapat kode yang dimana saat player/shape sesuai kursor
#akan dijalankan sesuai dengan inputan yang diterima dari kyeboard. 
#Inputan berupa key up, key down, key left, dan key right
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

# PART C
    #warna background
    win.fill ((100, 149, 237))
    #warna player
    pygame.draw.rect(win, (WHITE), player)

    #blit/kelap kelip pada cursor 
    win.blit(img,rect)
    
    #perulangan untuk blit
    #warna blit saya samarkan biar tidak terlihat
    if time.time() % 1 > 0.5: 
        pygame.draw.rect(win, MedBlue, cursor)
    pygame.display.update()
    

    player.update()
     #menampilkan hasil
    pygame.display.flip()
    
    clock.tick(120)
