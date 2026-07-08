#Name:
#Mini-Project - Build Your Own Game!
'''
This is YOUR game. You are the designer. There are only two requirements:

  1. Your game must use USER INPUT — typed answers, key strokes, mouse clicks, etc.
  2. Your game must keep track of and DISPLAY A SCORE.

You have everything you need from Modules 1-6: variables, input(), if/elif/else,
while loops, for loops, lists, random, and turtle graphics.

======================= NEED AN IDEA? PICK ONE OF THESE =======================

  TERMINAL GAMES (use input(), great with while loops + random):
    - Number guessing: score points for guessing in fewer tries, play 5 rounds
    - Math quiz: random questions, +1 per right answer, show the final score
    - Rock, paper, scissors: first to 3 wins, show the running score
    - Trivia: store questions and answers in lists, loop through them

  TURTLE GAMES (use the mouse or keyboard, see the reminder below):
    - Click the turtle: it jumps to a random spot every time you click it
    - Turtle race: press a key to make your turtle dash to the finish line
    - Falling catch: move a paddle with the arrow keys to catch a falling dot

  ...or invent something completely new. Weird ideas are welcome.

============================ HELPFUL SNIPPETS ================================

  Typed input:
      guess = int(input("Your guess: "))

  Turtle keyboard input:
      screen = turtle.Screen()
      screen.onkey(move_left, "Left")     # calls move_left() on the left arrow
      screen.listen()

  Turtle mouse input:
      screen.onclick(jump)                # calls jump(x, y) on every click
      my_turtle.onclick(caught)           # only when the turtle itself is clicked

  Keeping and showing a score:
      score = 0
      score = score + 1                   # when the player earns a point
      print("Score:", score)              # terminal
      pen.write("Score: " + str(score))   # turtle (use a separate pen turtle)

  REMINDER for turtle games — to see your game in Codespaces: run it, open the
  PORTS tab, click port 6080 ("Turtle Desktop"), Connect, password: vscode

========================== LEVEL-UP IDEAS (optional) ==========================

  - Add lives: the game ends after 3 misses
  - Add difficulty: harder questions or a faster game as the score goes up
  - Add a high score: remember the best score across rounds with a variable
  - Add sound-off flair: ASCII art title screens, victory messages, emoji

==============================================================================
Build your game below. Delete this line and start coding!
'''

# Pong

import random
import sys
import time
import pygame

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

Pwidth, Pheight = 15, 100
Bsize = 15

player1 = pygame.Rect(30, height//2 - Pheight//2, Pwidth, Pheight)
player2 = pygame.Rect(width - 30 - Pwidth, height//2 - Pheight//2, Pwidth, Pheight)
ball = pygame.Rect(width//2 - Bsize//2, height//2 - Bsize//2, Bsize, Bsize)

Pspeed = 7
Bspeedx = 5 * random.choice((1, -1))
Bspeedy = 5 * random.choice((1, -1))

scoreP1 = 0
scoreP2 = 0
win = 5
font = pygame.font.Font(None, 74)

def reset_ball():
    global Bspeedx, Bspeedy
    ball.center = (width//2, height//2)
    Bspeedx = 5 * random.choice((1,-1))
    Bspeedy = 5 * random.choice((1, -1))

while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w] and player1.top > 0:
     player1.y -= Pspeed
  if keys[pygame.K_s] and player1.bottom < height:
     player1.y += Pspeed
  if keys[pygame.K_i] and player2.top > 0:
     player2.y -= Pspeed
  if keys[pygame.K_k] and player2.bottom < height:
     player2.y += Pspeed

  ball.y += Bspeedy
  ball.x += Bspeedx

  if ball.top <= 0 or ball.bottom >= height:
     Bspeedy *= -1
  if ball.colliderect(player1) and Bspeedx < 0:
     Bspeedx *= -1.1
  if ball.colliderect(player2) and Bspeedx > 0:
     Bspeedx *= -1.1
  
  if ball.left <= 0:
     scoreP2 += 1
     reset_ball()
  if ball.right >= width:
     scoreP1 += 1
     reset_ball()
  

  screen.fill(black)

  pygame.draw.line(screen, white, (width//2, 0), (width//2, height), 2)

  pygame.draw.rect(screen, white, player1)
  pygame.draw.rect(screen, white, player2)
  pygame.draw.ellipse(screen, white, ball)

  p1text = font.render(str(scoreP1), True, white)
  p2text = font.render(str(scoreP2), True, white)

  screen.blit(p1text, (width//4, 20))
  screen.blit(p2text, (width * 3//4 - p2text.get_width(), 20))
  pygame.display.flip()

  if scoreP1 == win:
     wintext = font.render(str("Player 1 wins!"), True, white)
     screen.blit(wintext, (width//4, height//3))
     pygame.display.flip()
     time.sleep(2)
     scoreP1, scoreP2 = 0, 0
     reset_ball()

  elif scoreP2 == win:
     wintext = font.render(str("Player 2 wins!"), True, white)
     screen.blit(wintext, (width//4, height//3))
     pygame.display.flip()
     time.sleep(2)
     scoreP1, scoreP2 = 0, 0
     reset_ball()

  clock.tick(60)

