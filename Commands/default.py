'''
discord.Client() - default.py
기본적인 봇을 구동하는 코드입니다.

- [ @ ] 데코레이터란?
  어떤 함수를 받아 명령을 추가한 뒤 이를 다시 함수의 형태로 반환하는 함수.
  어떤 함수의 내부를 수정하지 않고 기능에 변화를 주고 싶을 때 사용한다.
  말그대로 다른 함수를 꾸며주는 함수.

- [ f-string ] 포맷팅이란?
  f-string은 파이썬 3.6 이상 버전에서만 지원하며,
  어떠한 문자열 내에 변수값을 삽입해야 할 때 유용하게 사용됩니다.
  "{}".format(변수명) 식으로도 사용할 수 있지만,

  f-string 포맷팅이 지원됨으로서
  f"{변수명}" 식으로 더욱 더 간편하게 문자열 포맷팅을 사용할 수 있습니다.
'''

from discord.ext import commands    # discord.ext 에서 commands 라는 특정 기능만 불러옵니다.

bot = commands.Bot(command_prefix="!")  # 봇의 접두사를 설정합니다. 현재 봇의 접두사는 [ ! ] 입니다.
token = "봇 토큰"  # 봇 토큰은 양 옆 따옴표('')나 큰 따옴표("")로 감싸져, 문자열(string)형태여야 합니다.

@bot.command()  # @(골뱅이)는 데코레이터(decorator)라고 부릅니다. 위의 설명문을 참고하세요.
async def 안녕(ctx):  # [접두사]안녕 이라는 메시지가 보내졌을 때, 아래의 구문을 실행합니다.
    await ctx.send("안녕하세요.")    # 해당 텍스트 채널에 "안녕하세요." 라는 메시지를 출력합니다.

@bot.command(aliases=["하이", "방가"])    # aliases=[] 를 사용하여 "!반가워" 외에도, "!하이", "!방가" 의 메시지에도 같은 응답을 하게 할 수 있습니다.
async def 반가워(ctx):
    await ctx.send("반갑습니다.")

@bot.event
async def on_ready():   # on_ready() 이벤트(봇이 온라인으로 전환되었을때)이며, 디스코드 봇은 비동기로 작동하기 때문에 비동기 함수를 사용합니다.
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {bot.user.name}")   # 봇의 닉네임
    print(f"[!] 다음 : {bot.user.id}")     # 봇의 고유 id
    print(f"[!] 참가 중인 서버 : {len(bot.guilds)}개의 서버에 참여 중\n")  # 참여 중인 서버 개수

try:    # try - except 구문, try 아래 구문을 실행하다가 오류가 발생하면, except 아래의 구문을 실행하는 내용입니다.
    bot.run(token)   # 봇을 온라인으로 전환시키는 코드입니다.

except Exception as e:  # 어떠한 오류가 발생했을 때, 아래 구문을 실행합니다. 또한, 오류의 내용을 e 라고 통칭하여 저장합니다.
    print(f"[!] 봇을 구동하는 과정에서 오류가 발생했습니다.")
    print(f"[!] 토큰이 올바른지 다시 한번 확인해주세요.")
    print(f"[!] 오류 세부 사항 : {e}")    # f-string 포맷팅입니다. 자세한 사항은 위의 설명문을 참고하세요.