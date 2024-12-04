from Board import Board
from BotDepth1 import BotDepth1
from Utils import *
from TestUtils import *

def testBotDepth1PickBestCapture():
    challengePickBestCapture(BotDepth1())

def testBotDepth1MateInOne():
    challengeMateInOneAvoidDraw(BotDepth1())
    challengeMateInOneWithQueen(BotDepth1())
    challengeMateInOneWithBishop(BotDepth1())
    challengeMateInOneWithPawn(BotDepth1())
    challengeMateInOneWithKnight(BotDepth1())
    challengeMateInOneWithRook(BotDepth1())
    challengeMateInOneWithPromotion(BotDepth1())

