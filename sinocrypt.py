import random

codex = {
        'a': ["一", "乙", "乚", "乚", "亅"],
        'b': ["了", "人", "力", "十", "又", "二", "九", "八", "七", "厂"],
        'c': ["个", "上", "大", "也", "子", "下", "之", "么", "小", "已"],
        'd': ["不", "中", "为", "以", "方", "天", "分", "心", "开", "从"],
        'e': ["他", "们", "出", "可", "对", "生", "发", "用", "去", "只"],
        'f': ["在", "有", "地", "会", "而", "那", "自", "年", "过", "后"],
        'g': ["我", "这", "来", "时", "你", "作", "里", "没", "还", "进"],
        'h': ["的", "和", "国", "到", "所", "事", "经", "法", "学", "现"],
        'i': ["是", "说", "要"],
        'j': ["能", "家", "都"],
        'k': ["得", "着", "理"],
        'l': ["就", "道", "然"],
        'm': ["想", "意", "新"],
        'n': ["管", "算", "需", "精", "察", "境", "愿", "模", "疑", "演"],
        'o': ["题", "德", "影"],
        'p': ["整", "器", "激"],
        'q': ["藏", "戴", "翼"],
        'r': ["翻", "覆", "鹰", "藤", "鞭", "藩", "鳍", "蹦", "襟", "戳"],
        's': ["警", "爆", "颤", "疆", "攀", "蹲", "藻", "簿", "瓣", "孽"],
        't': ["魔", "籍", "耀", "灌", "嚷", "壤", "譬", "躁", "馨", "嚼"],
        'u': ["露", "霸", "蠢"],
        'v': ["囊", "懿", "镶"],
        'w': ["罐", "麟", "攫"],
        'x': ["矗", "鑫", "衢"],
        'y': ["囔", "馕", "鬣"],
        'z': ["蠼", "鱲", "鱵"]}

# Function that will replace a single english character with the appropriately coded chinese character
def encrypt(letter):

    # Choose a random character replacement from the appropriate array
    rand = random.randint(0, len(codex[letter]) - 1)

    # Return the encrypted character
    return(codex[letter][rand])

def decrypt(letter):
    
    for e, c in codex.items():
        if letter in c:
            return e

    return ''


if __name__ == "__main__":
    mode = input("Press E for encode, D for decode")
    if mode == 'E':
        plaintext = input("Enter message to encrypt: ")
        encryptedMessage = ""

        # Loop through the plaintext string to build the encrypted message
        for i in plaintext:
            #drop punctuation, spaces, special characters
            if i.isalpha():
                encryptedMessage += encrypt(i)
    
        # Print the encrypted message to the screen
        print(encryptedMessage)
    else:
        plaintext = ""
        encryptedMessage = input("Enter message to decrypt: ")

        for i in encryptedMessage:
            plaintext += decrypt(i)
        
        print(plaintext)