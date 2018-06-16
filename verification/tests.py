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
        prepare_test(middle_code='''CHANNELS = ['BBC', 'Discovery', 'TV1000']
controller = VoiceCommand(CHANNELS)
controller.turn_channel(1)
controller.previous_channel()''',
                     test="controller.current_channel()",
                     answer="TV1000")
    ],
    "2. Second": [
        prepare_test(middle_code='''CHANNELS = ['BBC', 'Discovery', 'TV1000']
controller = VoiceCommand(CHANNELS)
controller.turn_channel(3)
controller.next_channel()''',
                     test="controller.current_channel()",
                     answer="BBC")
    ],
    "3. Third": [
        prepare_test(middle_code='''CHANNELS = ['BBC', 'Discovery', 'NickMusic', 'MTV']
controller = VoiceCommand(CHANNELS)
controller.next_channel()
controller.next_channel()
controller.next_channel()''',
                     test="controller.current_channel()",
                     answer="MTV")
    ],
    "4. Fourth": [
        prepare_test(middle_code='''CHANNELS = ['ZeeTV', 'Eurosport', 'TV1000', 'ABC News']
controller = VoiceCommand(CHANNELS)
controller.turn_channel(2)
controller.turn_channel(4)
controller.next_channel()''',
                     test="controller.current_channel()",
                     answer="ZeeTV")
    ],
    "5. Fifth": [
        prepare_test(middle_code='''CHANNELS = ['ZeeTV', 'Eurosport', 'TV1000', 'ABC News']
controller = VoiceCommand(CHANNELS)
controller.turn_channel(1)''',
                     test="controller.is_exist(6)",
                     answer="No")
    ],
    "6. Sixth": [
        prepare_test(middle_code='''CHANNELS = ['BBC', 'Discovery', 'NickMusic', 'MTV']
controller = VoiceCommand(CHANNELS)
controller.previous_channel()
controller.previous_channel()''',
                     test="controller.current_channel()",
                     answer="NickMusic")
    ],
    "7. Seventh": [
        prepare_test(middle_code='''CHANNELS = ['BBC', 'Discovery', 'NickMusic', 'MTV']
controller = VoiceCommand(CHANNELS)
controller.first_channel()
controller.next_channel()
controller.next_channel()''',
                     test="controller.current_channel()",
                     answer="NickMusic")
    ],
    "8. Eighth": [
        prepare_test(middle_code='''CHANNELS = ['ZeeTV', 'Eurosport', 'TV1000', 'ABC News']
controller = VoiceCommand(CHANNELS)
controller.last_channel()
controller.previous_channel()''',
                     test="controller.current_channel()",
                     answer="TV1000")
    ],
    "9. Ninth": [
        prepare_test(middle_code='''CHANNELS = ['Nickelodeon', 'BBC', 'Discovery', 'TV1000']
controller = VoiceCommand(CHANNELS)
controller.turn_channel(3)
controller.next_channel()''',
                     test="controller.is_exist('BBC')",
                     answer="Yes")
    ],
    "10. Tenth": [
        prepare_test(middle_code='''CHANNELS = ['BBC', 'Nickelodeon', 'Discovery', 'TV1000']
controller = VoiceCommand(CHANNELS)
controller.turn_channel(3)
controller.next_channel()''',
                     test="controller.current_channel()",
                     answer="TV1000")
    ]

}
