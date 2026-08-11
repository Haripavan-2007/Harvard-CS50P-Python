def convert(message):
    if ":)" in message:#converting :) into smile emoji
        message=message.replace(":)","🙂")
    if ":(" in message:#converting :( into sad emoji
        message=message.replace(":(","🙁")
    return message
def main():
    sentence=input()
    print(convert(sentence))
main()


