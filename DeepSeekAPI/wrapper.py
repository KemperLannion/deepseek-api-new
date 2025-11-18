from .DeepSeekChat import DeepSeekChat
from enum import Enum
import subprocess
import sys
import io
class IOMethods(Enum):
    PRINT=1
    RETURN=2
    STREAMDOWN=3
def DeepSeekChatExample(DS_SESSION_ID,AUTHORIZATION_TOKEN,message,mode,thinking_enabled=False,search_enabled=False):
    if mode==IOMethods.STREAMDOWN:
        proc=subprocess.Popen(
            [
                sys.executable,
                '-c',
                f"from DeepSeekAPI import DeepSeekChat; DeepSeekChat({repr(DS_SESSION_ID)},{repr(AUTHORIZATION_TOKEN)}).send_message({repr(message)},True,{thinking_enabled},{search_enabled})"
            ],
            stdout=subprocess.PIPE,
            text=False
        )
        from .streamdown import init,emit
        init()
        emit(proc.stdout)
        return
    else:
        ret=DeepSeekChat(DS_SESSION_ID,AUTHORIZATION_TOKEN).send_message(message,mode==IOMethods.PRINT,thinking_enabled,search_enabled)
        if mode==IOMethods.PRINT:
            return
        return ret
