from enum import Enum, auto
from PyQt5 import QtGui

class State(Enum):
    intro = auto()
    stand = auto()
    dash = auto()
    jump = auto()
    shoot = auto()
    uppercut = auto()   

class FaceDir(Enum):
    left = auto()
    right = auto()

class Frame:
    def __init__(self, centerX, centerY, top, bottom, left, right, maxCounterVal, next, sprite, mask):
        self.centerX = centerX 
        self.centerY = centerY
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.maxCounterVal = maxCounterVal
        self.next = next
        self.sprite = sprite
        self.mask = mask
        self.frameWidth = self.right - self.left
        self.frameHeight = self.bottom - self.top

class FrameList:
    def __init__(self, character, amount):
        self.array = []
        self.spriteSheet = character.spriteSheet
        self.amount = amount

    def insert(self, centerX, centerY, top, bottom, left, right, maxCounterVal, next):
        tempSprite = self.spriteSheet.copy(left, top, right - left, bottom - top)
        
        tempMask = self.spriteSheet.copy(left, top, right - left, bottom - top)
        for x in range(right - left):
            for y in range(bottom - top):
                if tempMask.pixelColor(x, y) == QtGui.QColor(0, 0, 0, 255):
                    tempMask.setPixelColor(x, y, QtGui.QColor(255, 255, 255, 255))
                else:
                    tempMask.setPixelColor(x, y, QtGui.QColor(0, 0, 0, 255))
        self.array.append(Frame(centerX - left, centerY - top, top - top, bottom - top, left - left, right - left, maxCounterVal, next, tempSprite, tempMask))

class SpriteObject:
    def __init__(self, name, spriteUrl, faceDir):
        self.name = name
        self.spriteSheet = QtGui.QImage(spriteUrl)
        self.posX = 0
        self.posY = 0
        self.vX = 0
        self.vY = 0
        self.currentState = State.offscrean
        self.frameIndex = 0
        self.frameTimeCounter = 0
        self.faceDir = faceDir
        self.initFaceDir = faceDir

FlameStag = SpriteObject("Flame Stag", "flamestag.png", FaceDir.left)


FlameStagIntro = FrameList(FlameStag, 11)
FlameStagStand = FrameList(FlameStag, 1)
FlameStagDash = FrameList(FlameStag, 10)
FlameStagJump = FrameList(FlameStag, 5)
FlameStagDownAttack = FrameList(FlameStag, 10)
FlameStagUpAttack = FrameList(FlameStag, 6)
FlameStagCharge = FrameList(FlameStag, 2)
FlameStagDeath = FrameList(FlameStag, 2)
FlameStagGetHit = FrameList(FlameStag, 1)
FlameStagLanding = FrameList(FlameStag, 4)
FlameStagUppercut = FrameList(FlameStag, 4)
FlameStagSmackDown = FrameList(FlameStag, 1)

FlameStagJump.insert(37, 50, 7, 27, 69, 74,1,0)
FlameStagJump.insert(95, 43, 78, 13, 116, 74,1,1)
FlameStagJump.insert(149, 43, 125, 13, 176, 71,1,2)
FlameStagJump.insert(210, 45, 183, 16, 236, 72,1,3)
FlameStagJump.insert(284, 41, 252, 13, 304, 70,1,4)

FlameStagLanding.insert(32, 125, 13, 92, 51, 158,1,0)
FlameStagLanding.insert(73, 125, 56, 100, 93, 158,1,1)
FlameStagLanding.insert(124, 139, 98, 115, 147, 157,1,2)
FlameStagLanding.insert(178, 139, 152, 115, 199, 156,1,3)

FlameStagIntro.insert(34, 203, 8, 176, 58, 225,1,0)
FlameStagIntro.insert(95, 203, 71, 176, 120, 225,1,0)
FlameStagIntro.insert(157, 203, 131, 176, 187, 225,1,0)
FlameStagIntro.insert(215, 203, 192, 176, 239, 225,1,0)
FlameStagIntro.insert(273, 203, 245, 183, 300, 225,1,0)
FlameStagIntro.insert(339, 203, 306, 183, 370, 225,1,0)
FlameStagIntro.insert(402, 203, 374, 178, 428, 225,1,0)
FlameStagIntro.insert(461, 203, 431, 179, 484, 225,1,0)
FlameStagIntro.insert(516, 203, 492, 171, 541, 225,1,0)
FlameStagIntro.insert(571, 203, 549, 167, 597, 225,1,0)
FlameStagIntro.insert(622, 203, 606, 158, 645, 225,1,0)

FlameStagDownAttack.insert(32, 267, 9, 238, 56, 288,1,0)
FlameStagDownAttack.insert(92, 267, 69, 238, 117, 289,1,0)
FlameStagDownAttack.insert(151, 267, 126, 238, 180, 289,1,0)
FlameStagDownAttack.insert(213, 267, 188, 240, 243, 289,1,0)
FlameStagDownAttack.insert(277, 267, 255, 237, 302, 289,1,0)
FlameStagDownAttack.insert(346, 267, 316, 248, 376, 289,1,0)
FlameStagDownAttack.insert(415, 267, 381, 248, 446, 289,1,0)
FlameStagDownAttack.insert(493, 267, 455, 248, 523, 289,1,0)
FlameStagDownAttack.insert(577, 267, 529, 248, 607, 289,1,0)
FlameStagDownAttack.insert(672, 267, 616, 248, 703, 289,1,0)

FlameStagUpAttack.insert(41, 330, 12, 308, 66, 355,1,0)
FlameStagUpAttack.insert(107, 330, 77, 309, 129, 355,1,0)
FlameStagUpAttack.insert(174, 330, 143, 309, 196, 355,1,0)
FlameStagUpAttack.insert(242, 330, 211, 303, 264, 355,1,0)
FlameStagUpAttack.insert(315, 330, 279, 296, 341, 355,1,0)
FlameStagUpAttack.insert(374, 330, 350, 296, 399, 355,1,0)

FlameStagSmackDown.insert(227, 505, 212, 472, 244, 545,1,0)

FlameStagDash.insert(48, 399, 10, 362, 80, 428,1,0)
FlameStagDash.insert(134, 399, 96, 362, 165, 428,1,0)
FlameStagDash.insert(218, 399, 177, 362, 250, 428,1,0)
FlameStagDash.insert(307, 399, 258, 362, 341, 428,1,0)
FlameStagDash.insert(405, 399, 347, 362, 437, 428,1,0)
FlameStagDash.insert(509, 399, 443, 362, 540, 428,1,0)
FlameStagDash.insert(620, 399, 546, 360, 652, 428,1,0)
FlameStagDash.insert(739, 399, 657, 360, 770, 428,1,0)
FlameStagDash.insert(868, 399, 777, 360, 898, 428,1,0)
FlameStagDash.insert(1002, 399, 905, 360, 1034, 428,1,0)

FlameStagUppercut.insert(37, 510, 15, 479, 52, 544,1,0)
FlameStagUppercut.insert(72, 510, 58, 474, 87, 545,1,0)
FlameStagUppercut.insert(109, 510, 94, 471, 123, 545,1,0)
FlameStagUppercut.insert(163, 492, 132, 451, 193, 546,1,0)

FlameStagCharge.insert(827, 44, 801, 15, 852, 67,1,0)
FlameStagCharge.insert(880, 44, 857, 16, 906, 67,1,0)

FlameStagDeath.insert(828, 125, 801, 90, 844, 150,1,0)
FlameStagDeath.insert(883, 125, 855, 96, 901, 148,1,0)

FlameStagGetHit.insert(830, 201, 803, 171, 856, 224,1,0)


Megaman = SpriteObject("Megaman", "MegamanSprite", FaceDir.right)

MegamanStand = FrameList(Megaman, 3)
MegamanStagger = FrameList(Megaman, 4)

MegamanStand.insert(18, 26, 3, 43, 0, 34, 10, 1)
MegamanStand.insert(54, 25, 2, 42, 36, 70, 10, 2)
MegamanStand.insert(90, 25, 2, 42, 72, 106, 5, 0)

MegamanStagger.insert(126, 26, 3, 43, 108, 143, 1, 1)
MegamanStagger.insert(165, 23, 2, 43, 146, 181, 1, 2)
MegamanStagger.insert(202, 22, 0, 44, 184, 216, 1, 3)
MegamanStagger.insert(237, 22, 1, 44, 218, 257, 1, 0)

Fireball = SpriteObject("Fireball", "flamestag.png", FaceDir.left)

DownFireBall = FrameList(Fireball, 4)
UpFireBall = FrameList(Fireball, 4)

DownFireBall.insert(604, 483, 593, 473, 618, 493, 1, 1)
DownFireBall.insert(633, 483, 623, 473, 650, 491, 1, 1)
DownFireBall.insert(667, 483, 655, 472, 681, 493, 1, 1)
DownFireBall.insert(696, 483, 686, 471, 711, 490, 1, 1)

UpFireBall.insert(724, 527, 717, 517, 732, 545, 1, 1)
UpFireBall.insert(743, 527, 736, 517, 750, 545, 1, 1)
UpFireBall.insert(762, 527, 755, 517, 769, 545, 1, 1)
UpFireBall.insert(781, 527, 774, 517, 790, 545, 1, 1)


