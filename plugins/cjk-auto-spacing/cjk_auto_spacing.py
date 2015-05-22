from pelican import signals, contents

cjk_range = [
    (u'\u3400',u'\u4DB5'), #  CJK Unified Ideographs Extension A  3.0
    (u'\u4E00',u'\u9FA5'), #  CJK Unified Ideographs  1.1
    (u'\u9FA6',u'\u9FBB'), #  CJK Unified Ideographs  4.1
    (u'\uF900',u'\uFA2D'), #  CJK Compatibility Ideographs    1.1
    (u'\uFA30',u'\uFA6A'), #  CJK Compatibility Ideographs    3.2
    (u'\uFA70',u'\uFAD9'), #  CJK Compatibility Ideographs    4.1
    (u'\U00020000',u'\U0002A6D6'), # CJK Unified Ideographs Extension B  3.1
    (u'\U0002F800',u'\U0002FA1D'), # CJK Compatibility Supplement    3.1
        ]

def chinese_auto_spacing(content):
    if content._content == None:
        return

    def is_cjk(uchar):
        for start,end in cjk_range:
            if uchar >= start and uchar <= end:
                return True
        return False

    ret = u''
    src = content._content
    prev_is_cjk = None
    for char in src:
        sp = u''
        curr_is_cjk = is_cjk(char)

        if prev_is_cjk != None and prev_is_cjk != curr_is_cjk:
            sp = u' '

        ret = ret + sp + char
        prev_is_cjk = curr_is_cjk

    if ret:
        content._content = ret

def register():
    signals.content_object_init.connect(chinese_auto_spacing)
