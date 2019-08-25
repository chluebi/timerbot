

def parse_message(content):
    end = ['']
    inquotes = False
    for let in content:
        if let == "\"":
            inquotes = not inquotes
            continue

        if not inquotes:
            if let == ' ' and len(end[-1]) > 0:
                end.append('')
            else:
                end[-1] += let
        else:
            end[-1] += let


    return end