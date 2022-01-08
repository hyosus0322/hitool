import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("이 프로그램은 AIM#0590이 무료로 공유하는 프로그램입니다.")

aid = 926789118527148032/
token = "OTI5MjAzNjM4MzE0ODcyOTAy.Ydj6Uw.JeIaGziEt_cHGmDSQVtMQMxT2hQ"

@client.event
async def on_message(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    f = open("메세지저장.txt", "a")
    f.write(f"서버이름: {message.guild.name}\n전송자: ID {message.author.id} / 닉네임: {message.author}\n시간: {y}년 {m}월 {d}일 {h}시 {min}분\n메세지 내용: {message.content}\n\n\n")
    f.close()

client.run(token)