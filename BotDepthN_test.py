from Board import Board
from BotDepthN import BotDepthN
from Utils import *
from TestUtils import *

def testBotDepthN_D1_PickBestCapture():
    challengePickBestCapture(BotDepthN(1))

def testBotDepthN_D1_MateInOne():
    challengeMateInOneAvoidDraw(BotDepthN(1))
    challengeMateInOneWithQueen(BotDepthN(1))
    challengeMateInOneWithBishop(BotDepthN(1))
    challengeMateInOneWithPawn(BotDepthN(1))
    challengeMateInOneWithKnight(BotDepthN(1))
    challengeMateInOneWithRook(BotDepthN(1))
    challengeMateInOneWithPromotion(BotDepthN(1))

def testBotDepthN_D2_MateInOne():
    challengeMateInOneAvoidDraw(BotDepthN(2))
    challengeMateInOneWithQueen(BotDepthN(2))
    challengeMateInOneWithBishop(BotDepthN(2))
    challengeMateInOneWithPawn(BotDepthN(2))
    challengeMateInOneWithKnight(BotDepthN(2))
    challengeMateInOneWithRook(BotDepthN(2))
    challengeMateInOneWithPromotion(BotDepthN(2))

def testBotDepthN_D2_MateInTwo():
    challengeMateInTwoWithRook(BotDepthN(2))
    challengeMateInTwoWithRookAndKing(BotDepthN(2))
    challengeMateInTwoWithBishopAndPawn(BotDepthN(2))
    challengeMateInTwoWithKnightAndKing(BotDepthN(2))
    # challengeMateInTwoWithQueenAndKing(BotDepthN(2))