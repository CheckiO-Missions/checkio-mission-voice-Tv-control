init_code = """
if not "VoiceCommand" in USER_GLOBAL:
    raise NotImplementedError("Where is 'VoiceCommand'?")
VoiceCommand = USER_GLOBAL['VoiceCommand']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. First": [
        prepare_test(middle_code='''channels = ['BBC', 'Discovery', 'TV1000']
controller = VoiceCommand(channels)
controller.turn_channel(1)
controller.previous()''',
                     test="controller.current()",
                     answer="TV1000")
    ],
    "2. Second": [
        prepare_test(middle_code='''channels = ['BBC', 'Discovery', 'TV1000']
controller = VoiceCommand(channels)
controller.turn_channel(3)
controller.next()''',
                     test="controller.current()",
                     answer="BBC")
    ],
    "3. Third": [
        prepare_test(middle_code='''channels = ['BBC', 'Discovery', 'NickMusic', 'MTV']
controller = VoiceCommand(channels)
controller.next()
controller.next()
controller.next()''',
                     test="controller.current()",
                     answer="MTV")
    ],
    "4. Fourth": [
        prepare_test(middle_code='''channels = ['ZeeTV', 'Eurosport', 'TV1000', 'ABC News']
controller = VoiceCommand(channels)
controller.turn_channel(2)
controller.turn_channel(4)
controller.next()''',
                     test="controller.current()",
                     answer="ZeeTV")
    ],
    "5. Fifth": [
        prepare_test(middle_code='''channels = ['ZeeTV', 'Eurosport', 'TV1000', 'ABC News']
controller = VoiceCommand(channels)
controller.turn_channel(1)''',
                     test="controller.is_exist(6)",
                     answer="No")
    ],
    "6. Sixth": [
        prepare_test(middle_code='''channels = ['BBC', 'Discovery', 'NickMusic', 'MTV']
controller = VoiceCommand(channels)
controller.previous()
controller.previous()''',
                     test="controller.current()",
                     answer="NickMusic")
    ],
    "7. Seventh": [
        prepare_test(middle_code='''channels = ['BBC', 'Discovery', 'NickMusic', 'MTV']
controller = VoiceCommand(channels)
controller.first()
controller.next()
controller.next()''',
                     test="controller.current()",
                     answer="NickMusic")
    ],
    "8. Eighth": [
        prepare_test(middle_code='''channels = ['ZeeTV', 'Eurosport', 'TV1000', 'ABC News']
controller = VoiceCommand(channels)
controller.last()
controller.previous()''',
                     test="controller.current()",
                     answer="TV1000")
    ],
    "9. Ninth": [
        prepare_test(middle_code='''channels = ['Nickelodeon', 'BBC', 'Discovery', 'TV1000']
controller = VoiceCommand(channels)
controller.turn_channel(3)
controller.next()''',
                     test="controller.is_exist('BBC')",
                     answer="Yes")
    ],
    "10. Tenth": [
        prepare_test(middle_code='''channels = ['BBC', 'Nickelodeon', 'Discovery', 'TV1000']
controller = VoiceCommand(channels)
controller.turn_channel(3)
controller.next()''',
                     test="controller.current()",
                     answer="BBC")
    ]

}
